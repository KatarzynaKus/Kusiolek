import xmlrpc.client
import base64
import os

class LimeSurveyRPC:
    def __init__(self, url, login, password):
        self.RPCHandle = xmlrpc.client.ServerProxy(url)
        self.login = login
        self.password = password
    def get_skey(self):
        return self.RPCHandle.get_session_key(self.login, self.password)

    skey = property(get_skey)

    def get_survey(self, lang, sid, dest):
        s = self.RPCHandle.export_responses(self.skey, sid, 'csv', lang, 'complete', 'code')
        s = base64.b64decode(s).decode('utf-8')
        try:
            os.mkdir(dest)
        except:
            pass
        with open('{dest}/{sid}.csv'.format(dest = dest, sid = sid), 'w') as f:
            f.write(s)
        print('Ankieta pobrana pomyślnie!')
