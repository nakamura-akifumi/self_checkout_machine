# coding: utf-8
import requests
import settings
import json
from logging import getLogger
import settings

logger = getLogger(__name__)

class EnjuAdapter:
    def __init__(self, server_url, cert):
        self.server_url = server_url
        self.cert = cert

    def checkin(self, item_identifier):
        logger.debug("checkin: item_identifier={}".format(item_identifier))
        payload = {'event': 'checkin',
                   'item_identifier': unicode(item_identifier),
                   'cert': self.cert}
        r = requests.post(self.server_url, data=payload)
        return r

    def checkout(self, user_number, item_identifier):
        logger.debug("checkout: user_number={} item_identifier={}".format(user_number, item_identifier))

        payload = {'event': 'checkout',
                   'user_number': unicode(user_number),
                   'item_identifier': unicode(item_identifier),
                   'cert': self.cert}
        r = requests.post(self.server_url, data=payload)
        return r

    def cardid2userid(self, tag_id):
        logger.debug("cardid2userid: cardid2userid={}".format(tag_id))

        payload = {'event': 'cardid2userid', 'tag': tag_id, 'cert': self.cert}
        r = requests.post(self.server_url, data=payload)
        print r
        # TODO: r.status_code == 500 -> throw exception
        return r

    def get_item(self, item_identifer):
        logger.debug("item_identifier: identifier={}".format(item_identifer))

        payload = {'event': 'getitem', 'item_identifer': item_identifer, 'cert': self.cert}
        r = requests.post(self.server_url, data=payload)
        return r

