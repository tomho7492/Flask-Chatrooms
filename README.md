# Flask-Chatrooms
 online messaging service using Flask, similar in spirit to Slack. Users are able to sign into the site with a display name, create channels (i.e. chatrooms) to communicate in, as well as see and join existing channels. Once a channel is selected, users will be able to send and receive messages with one another in real time. 

# Features
- Display Name: When a user visits your web application for the first time, they should be prompted to type in a display name that will eventually be associated with every message the user sends. If a user closes the page and returns to your app later, the display name should still be remembered.

- Channel Creation: Any user should be able to create a new channel, so long as its name doesn’t conflict with the name of an existing channel.

- Channel List: Users should be able to see a list of all current channels, and selecting one should allow the user to view the channel. 

- Messages View: Once a channel is selected, the user should see any messages that have already been sent in that channel, up to a maximum of 100 messages. 

- Sending Messages: Once in a channel, users should be able to send text messages to others the channel. When a user sends a message, their display name and the timestamp of the message should be associated with the message. All users in the channel should then see the new message (with display name and timestamp) appear on their channel page. Sending and receiving messages does NOT require reloading the page.

- Remembering the Channel: If a user is on a channel page, closes the web browser window, and goes back to your web application, your application should remember what channel the user was on previously and take the user back to that channel.
