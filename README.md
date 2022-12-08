## Setup & Installation

* Install ngrok: https://dashboard.ngrok.com/get-started/setup
* Run
```
ngrok http 3000
```
This exposes your local flask server using a randomly assigned URL that you get from the command. This will be of the form
https://<xxx>.ngrok.io. Note this URL will change everytime you restart ngrok.

* Create a new Slack App: https://api.slack.com/apps?new_app=1
  * Click "Create New App", choose "From scratch" option
  * Provide an App Name, Select a workspace
  * Add Features & Functionality
    * Slash Commands: 
      * Command: /chatgpt
      * Request URL: provide the ngrok URL you got above followed by the slack command: https://<xxx>.ngrok.io/chatgpt
      * Short Description: GPT chatbot for slack
      * Usage Hint: "<text prompt>"
    * OAuth & Permissions
      * The Bot User OAuth Token you see here is the slack token you will use in your code
      * Scopes: Enable the following bot token scopes: `channels:join`, `chat:write`, `chat:write_customize`, `chat:write.public`, `commands`, `incoming-webhook` 
    * Activate Incoming Webhooks
      * Select a channel for the bot to post to
      * The webhook URL you see here is what is provided as the response URL in the code. 
      * Install your app to your workspace


## Run flask server

* Create a conda environment: 
```commandline
conda create -n "chatgpt" python=3.8
pip3 install flask revChatGPT 
```

* Run flask server to serve generated images to slack workspace
```commandline
python chatgpt_slackbot.py
```

### Run on Google Cloud
* Create a basic f1-micro (~$5/month) instance
* Installation
```
# Get ngrok & other tools
curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip -o ngrok-stable-linux-amd64.zip
sudo apt-get install unzip tmux git
unzip ngrok-stable-linux-amd64.zip
```
* Run ngrok in a tmux session
```
tmux
./ngrok authtoken <token>
```
* Run flask server in a separate tmux session
```
tmux
git clone https://github.com/sanzgiri/chatgpt_slackbot.git
pip3 install flask revChatGPT packaging
cd chatgpt_slackbot
python3 chatgpt_slackbot.py
```
