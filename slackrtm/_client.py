#!/usr/bin/python
# mostly a proxy object to abstract how some of this works

import json

from ._server import Server

class SlackClient(object):
    def __init__(self, token):
        self.token = token
        self.server = Server(self.token, False)

    def rtm_connect(self):
        try:
            self.server.rtm_connect()
            return True
        except:
            return False

    def api_call(self, method, **kwargs):
        return self.server.api_call(method, **kwargs)

    def rtm_read(self):
        # in the future, this should handle some events internally i.e. channel
        # creation
        if self.server:
            json_data = self.server.websocket_safe_read()
            data = []
            if json_data != '':
                for d in json_data.split('\n'):
                    data.append(json.loads(d))
            for item in data:
                self.process_changes(item)
            return data
        else:
            raise SlackNotConnected

    def rtm_send_message(self, channel_id, message):
        return self.server.channels[channel_id].send_message(message)

    def process_changes(self, data):
        if "type" in data.keys():
            if data["type"] in ['channel_created', 'im_created']:
                channel = data["channel"]
                self.server.attach_channel(channel["name"], channel["id"], [])


class SlackNotConnected(Exception):
    pass