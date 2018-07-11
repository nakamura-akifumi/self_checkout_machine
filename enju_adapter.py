import requests
import settings


class EnjuAdapter:
    def __init__(self, server_url, cert):
        print('init')
        self.server_url = server_url
        self.cert = cert


    def checkin(self, item_identifier):
        print "checkin: item_identifier={}".format(item_identifier)
        payload = {'send_event': 'checkin', 'item_identifier': item_identifier, 'cert': self.cert}
        r = requests.post(self.server_url, params = payload)
        return r


    def checkout(self, user_number, item_identifier):
        print "checkout: user_number={} item_identifier={}".format(user_number, item_identifier)

        payload = {'send_event': 'checkout', 'user_number': user_number, 'item_identifier': item_identifier, 'cert': self.cert}
        r = requests.post(self.server_url, params = payload)
        return r

    def cardid2userid(self, tag_id):
        print "cardid2userid: tag_id={}".format(tag_id)

        payload = {'send_event': 'cardid2userid', 'tag': tag_id, 'cert': self.cert}
        r = requests.post(self.server_url, params = payload)
        return r
