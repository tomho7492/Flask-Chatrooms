import os


from flask import Flask, request, render_template, session, redirect, url_for
from flask_socketio import SocketIO, emit, join_room, leave_room
from datetime import datetime

channelsDict = {"channelName":[]}
channelMessages = dict()



app = Flask(__name__)
app.config["SECRET_KEY"] = 'admin'
socketio = SocketIO(app)

def auth():
    return 'displayName' in session

@app.route("/")
def index():

    if auth() is False:
        return render_template("index.html")
    return redirect(url_for('home'))

@app.route("/login", methods=["POST"])
def login():
    displayName = request.form.get("displayname")
    session['displayName'] = str(displayName)
    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route("/home")
def home():

    if auth() is False:
        return redirect(url_for('index'))

    channelList = channelsDict["channelName"]
    return render_template("home.html", channels=channelList)

@app.route("/channels")
def channels():
    return channelsDict


@socketio.on("create channel")
def createchannel(data):
    channel = data["channelName"]
    channelsList = channelsDict["channelName"]
    if channel in channelsList:
        return "error channel already exists"
    channelsList.append(channel)
    emit("channelcreation", {"channelName": channel}, broadcast=True)

@app.route("/channels/<channelName>")
def channel(channelName):
    session.pop('current_channel', None)
    session['current_channel'] = str(channelName)
    if channelName not in channelMessages:
        #set key = empty list
        channelMessages[channelName] = []
    messages = channelMessages[channelName]
    return render_template("channel.html", messages=messages, channelName=channelName)

@socketio.on("message receive")
def messagereceive(data):
    channel = session['current_channel']
    message = data["message"]
    user = session['displayName']
    time = datetime.now().strftime('%I:%M:%S')
    if len(channelMessages[channel]) > 100:
        channelMessages[channel].pop(0)
    channelMessages[channel].append(f"[{time}] {user}: {message}")
    emit("message sent", {"message": data, "user": user}, room=channel)


@socketio.on("joined")
def joined():
    room = session['current_channel']
    join_room(room)
    emit('status', {
        'userJoined': session.get('displayName'),
        'channel': room,
        'msg': session.get('displayName') + ' has entered the channel'},
         room=room)

@socketio.on("disconnect")
def disconnect():
    room = session['current_channel']
    leave_room(room)
    emit('status', {
        'userJoined': session.get('displayName'),
        'channel': room,
        'msg': session.get('displayName') + ' has left the channel'},
         room=room)