# Simple chat app with flask and react via socket io

In this repo, I’m going to show you how to build a real-time simple chat app using react, flask and socket.Io libraries. React is JavaScript Library and Flask is python Library. I use React as my client-side and flask as my server-side. And I used socket.Io to make my app Real-Time.

### Server Part

First I’m Going To Build Server-Side part using flask.
First, you need to install python 3 on your computer or if you did not click here and download and install the latest version of python 3. 
After that, you need to install flask and virtualenv son your computer. 
You can do that by opening your terminal or cmd (windows) and types 

`pip install flask virtualenv`

Then go to your project folder and create virtualenv. 

For windows, 
`python -m venv venv`
For linux, 
`virtualenv venv`

It will create a venv folder and it is your environment for this application.
Now Open this folder your favourite text editor I’m Using vs-code and create a folder src. Inside src folder create app.py file. This app.py file is the main file in our application.
Then we need to activate our virtualenv to do that open terminal in your project folder and type 

For windows,
`.\venv\scripts\activate`
for linux,
`source ./venv/scripts/activate`

And Lastly, Move to the src folder present in the server folder, then we need to install flask_socketio and the required packages by the following command.
`pip install -r requirements.txt`

Now Environment setup is done in server-side. In app.py file first, we need to import flask and flask_socketio staff to build a server app.
```
from flask import Flask, jsonify;
from flask_socketio import SocketIO, send
from flask_cors import CORS
import logging
logging.getLogger('requests').setLevel(logging.ERROR)
logging.basicConfig(level=logging.ERROR)

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'mysecret'

socketIo = SocketIO(app, cors_allowed_origins="*", logger=False, engineio_logger=False)

app.debug = True
app.host = 'localhost'

@socketIo.on("message")
def handleMessage(msg):
    print(msg)
    msg = input("Enter your message: ")
    send(msg, broadcast=True)
    return None

if __name__ == '__main__':
    socketIo.run(app)
```

Now Server-side is done and we need to run our server. Open terminal in our project src Folder and type 
`python app.py`

It will give a message like this. So in my case, my app will run port 5000. you can find your server port by terminal details like the above image. Now We need to work with a client-side.

### Client Part

Start with client-side with react first we need to install nodejs and download and install nodejs on your computer. After that, we need to create react app using create-react-app. install it globally type 

`npm i -g create-react-app`

After install go to your project folder and open terminal and type 

`create-react-app client`

After app created open client folder in a text editor and inside HomePage.js file paste bellow code ( Code explains in comments )

```
import React, { Component } from "react";
import io from "socket.io-client";

let endPoint = "http://localhost:5000";
let socket = io.connect(`${endPoint}`);

class HomePage extends Component {
  state = {
    messages: ["Hello and Welcome"],
    message: ""
  };

  componentDidMount = () => {
    socket.on("message", msg => {
      this.setState({
        messages: [...this.state.messages, msg]
      });
    });
  };

  onChange = e => {
    this.setState({
      [e.target.name]: e.target.value
    });
  };

  onClick = () => {
    const { message } = this.state;
    if (message !== "") {
      this.setState({
        message: ""
      });
      socket.emit("message", message);
    } else {
      alert("Please Add A Message");
    }
  };

  render() {
    const { messages, message } = this.state;
    return (
      <div>
        {messages.length > 0 &&
          messages.map(msg => (
            <div>
              <p>{msg}</p>
            </div>
          ))}
        <input
          value={message}
          name="message"
          onChange={e => this.onChange(e)}
        />
        <button onClick={() => this.onClick()}>Send Message</button>
      </div>
    );
  }
}
export default HomePage;
```

Now the server and client-side done.
Now `npm start` in client folder and test your app.