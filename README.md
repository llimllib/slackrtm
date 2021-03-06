```
     _            _         _
    | |          | |       | |
 ___| | __ _  ___| | ___ __| |_ _ __ ___
/ __| |/ _` |/ __| |/ / '__| __| '_ ` _ \
\__ \ | (_| | (__|   <| |  | |_| | | | | |
|___/_|\__,_|\___|_|\_\_|   \__|_| |_| |_|
```
================
A basic client for Slack.com, which can optionally connect to the Slack Real Time Messaging (RTM) API.

![](https://travis-ci.org/llimllib/slackrtm.svg?branch=master)

Overview
---------
This plugin is a light wrapper around the [Slack API](https://api.slack.com/). In its basic form, it can be used to call any API method and be expected to return a dict of the JSON reply.

The optional RTM connection allows you to create a persistent websocket connection, from which you can read events just like an official Slack client. This allows you to respond to events in real time without polling and send messages without making a full HTTPS request.

See [limbo](https://github.com/llimllib/limbo/) for an active project utilizing this library.

Installation
----------

#### Automatic w/ PyPI ([virtualenv](http://virtualenv.readthedocs.org/en/latest/) is recommended.)

    pip install slackrtm

#### Manual

    git clone https://github.com/llimllib/slackrtm.git
    pip install -r requirements.txt
    python setupy.py install

Usage
-----
See examples in [doc/examples](doc/examples/)

_Note:_ You must obtain a token for the user/bot. You can find or generate these at the [Slack API](https://api.slack.com/web) page.

###Basic API methods

```python
import time
from slackrtm import SlackClient

token = "xoxp-28192348123947234198234"      # found at https://api.slack.com/#auth)
sc = SlackClient(token)
print sc.api_call("api.test")
print sc.api_call("channels.info", channel="1234567890")
```

### Real Time Messaging
---------
```python
import time
from slackrtm import SlackClient

token = "xoxp-28192348123947234198234"# found at https://api.slack.com/#auth)
sc = SlackClient(token)
if sc.rtm_connect():
    while True:
        print sc.rtm_read()
        time.sleep(1)
else:
    print "Connection Failed, invalid token?"
```

####Objects
-----------

[SlackClient.**server**]
Server object owns the websocket and all nested channel information.

[SlackClient.server.**channels**]
A searchable list of all known channels within the parent server. Call `print (sc instance)` to see the entire list.

####Methods
-----------

SlackClient.**rtm_connect()**
Connect to a Slack RTM websocket. This is a persistent connection from which you can read events.

SlackClient.**rtm_read()**
Read all data from the RTM websocket. Multiple events may be returned, always returns a list [], which is empty if there are no incoming messages.

SlackClient.**rtm_send_message([channel, message])**
Sends the text in [message] to [channel], which can be a name or identifier i.e. "#general" or "C182391"

SlackClient.**api_call([method, params])**
Call the Slack method [method] with the a dict of params in [params]

SlackClient.server.**send_to_websocket([data])**
Send a JSON message directly to the websocket. See RTM documentation for allowed types.

SlackClient.server.**channnels[int].send_message([text])**
Send message [text] to [int] channel in the channels list.


####Contributors
-----------

[@TetraEtc](https://github.com/TetraEtc)
