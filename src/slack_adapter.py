# coding: utf-8
import requests
import settings
import json
from slackclient import SlackClient
import time
import datetime
from logging import basicConfig, getLogger, DEBUG

# Slack Real Time Messaging API 利用してサーバとやり取りをする。
# https://api.slack.com/rtm
# https://api.slack.com/apps
# https://get.slack.help/hc/ja/articles/215770388-API-%E3%83%88%E3%83%BC%E3%82%AF%E3%83%B3%E3%81%AE%E7%94%9F%E6%88%90%E3%81%A8%E5%86%8D%E7%94%9F%E6%88%90

logger = getLogger(__name__)

class SlackAdapter:
    def __init__(self, slack_token, channel):
        print('init')
        self.slack_token = slack_token
        self.channel = channel

    def find_channel_id_by_name(self, sc, name):
        channel_id = ''
        r = sc.api_call("channels.list", exclude_archived=1)
        channels = r['channels']
        for c in channels:
            print c['name']
            if c['name'] == name or '#' + c['name'] == name:
                channel_id = c['id']
                break

        return channel_id

    def checkin(self, item_identifier):
        print "checkin: send_to={} item_identifier={}".format(self.channel, item_identifier)
        sc = SlackClient(self.slack_token)

        channel_id = self.find_channel_id_by_name(sc, self.channel)
        if channel_id == '':
            print "error!"

        print "channel_id={}".format(channel_id)
        if sc.rtm_connect():
            print 'connected'
            while True:
                res = sc.rtm_read()
                if res and ('type' in res[0]):
                    if res[0]['type'] == 'hello':
                        x = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                        sc.rtm_send_message(channel_id, "Hello! RTM x={}".format(x))
                    if res[0]['type'] == 'message':
                        print "response:"
                        print res[0]['text']
                        break
        else:
            print(u'slack への接続に失敗しました.')


if __name__ == '__main__':
    settings.init()
    token = settings.app['slack']['token']
    channel = settings.app['slack']['channel']
    machinename = settings.app['slack']['machinename']

    print "token={}".format(token)
    print "channel={}".format(channel)
    print "machinename={}".format(machinename)

    s = SlackAdapter(token, channel)
    s.checkin('R0003')
