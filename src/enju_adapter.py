# coding: utf-8
import requests
from logging import getLogger

logger = getLogger(__name__)


class EnjuAdapter:
    def __init__(self, server_url, cert):
        self.server_url = server_url
        self.cert = cert
        self.request_timeout = 5

    def checkin(self, item_identifier):
        logger.debug("checkin: item_identifier={}".format(item_identifier))
        payload = {'event': 'checkin',
                   'item_identifier': unicode(item_identifier),
                   'cert': self.cert}
        r = requests.post(self.server_url, data=payload, timeout=self.request_timeout)
        return r

    def add_checkout_item(self, session_value, basket_id, item_identifier):
        logger.debug("add_checkout_item: basket_id={} item_identifier={}".format(basket_id, item_identifier))
        logger.debug("add_checkout_item: session_value={}".format(session_value))
        payload = {'event': 'add_checkout_item',
                   'basket_id': unicode(basket_id),
                   'item_identifier': unicode(item_identifier),
                   'session_value': unicode(session_value),
                   'cert': self.cert}
        r = requests.post(self.server_url, data=payload, timeout=self.request_timeout)
        return r

    def checkout(self, session_value, basket_id):
        logger.debug("checkout: basket_id={} session_value={}".format(basket_id, session_value))

        payload = {'event': 'checkout',
                   'basket_id': unicode(basket_id),
                   'session_value': unicode(session_value),
                   'cert': self.cert}
        r = requests.post(self.server_url, data=payload, timeout=self.request_timeout)
        return r

    def cardid2user_with_basket(self, tag_id):
        logger.debug("cardid2user_with_basket: cardid2user_with_basket={}".format(tag_id))

        payload = {'event': 'cardid2userbascket', 'tag': unicode(tag_id), 'cert': self.cert}
        r = requests.post(self.server_url, data=payload, timeout=self.request_timeout)
        print r
        print r.text
        # TODO: r.status_code == 500 -> throw exception
        return r


    def cardid2userid(self, tag_id):
        logger.debug("cardid2userid: cardid2userid={}".format(tag_id))

        payload = {'event': 'cardid2userid', 'tag': tag_id, 'cert': self.cert}
        r = requests.post(self.server_url, data=payload, timeout=self.request_timeout)
        print r
        # TODO: r.status_code == 500 -> throw exception
        return r

    def get_item(self, item_identifer):
        logger.debug("item_identifier: identifier={}".format(item_identifer))

        payload = {'event': 'getitem', 'item_identifer': item_identifer, 'cert': self.cert}
        r = requests.post(self.server_url, data=payload, timeout=self.request_timeout)
        return r

