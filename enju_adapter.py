# coding: utf-8
import requests
import settings
import json


class EnjuAdapter:
    def __init__(self, server_url, cert):
        print('init')
        self.server_url = server_url
        self.cert = cert

    def checkin(self, item_identifier):
        print "checkin: item_identifier={}".format(item_identifier)
        payload = {'event': 'checkin',
                   'item_identifier': unicode(item_identifier),
                   'cert': self.cert}
        r = requests.post(self.server_url, data=payload)
        return r

    def checkout(self, user_number, item_identifier):
        print "checkout: user_number={} item_identifier={}".format(user_number, item_identifier)

        payload = {'event': 'checkout',
                   'user_number': unicode(user_number),
                   'item_identifier': unicode(item_identifier),
                   'cert': self.cert}
        r = requests.post(self.server_url, data=payload)
        return r

    def cardid2userid(self, tag_id):
        print "cardid2userid: tag_id={}".format(tag_id)

        payload = {'event': 'cardid2userid', 'tag': tag_id, 'cert': self.cert}
        r = requests.post(self.server_url, data=payload)
        return r

    def get_item(self, item_identifer):
        print "item_identifier: identifier={}".format(item_identifer)

        payload = {'event': 'getitem', 'item_identifer': item_identifer, 'cert': self.cert}
        r = requests.post(self.server_url, data=payload)
        return r

