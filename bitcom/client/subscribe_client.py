import ssl
import threading
import time

import websocket  # pip3 install websocket_client

websocket.enableTrace(True)


def on_wss_msg(evt):
    print(evt)


class SubscribeClient(websocket.WebSocketApp):
    def __init__(self, url, on_wss_open, on_wss_msg):
        self.url = url
        self.reconnect_intv_sec = 60

        super().__init__(url=url,
                         on_open=on_wss_open,
                         on_message=on_wss_msg,
                         on_error=self.on_wss_error,
                         on_close=self.on_wss_close)

    def on_wss_open(self):
        print(self.__class__.__name__ + ': on_wss_open')

    def on_wss_cont_message(self, msg, cont):
        print(self.__class__.__name__ + ': on_wss_cont_message')

    def on_wss_error(self, evt):
        print(self.__class__.__name__ + ': on_wss_error: msg = ' + str(evt))
        print(evt)

    def on_wss_close(self):
        print(self.__class__.__name__ + ': on_wss_close')

    def do_start(self):
        try:
            while True:
                print('Starting SubscribeClient url = ' + self.url)
                self.run_forever(ping_timeout=30, sslopt={"cert_reqs": ssl.CERT_NONE})

                print(f'Sleep {self.reconnect_intv_sec} seconds and connect again....')
                time.sleep(self.reconnect_intv_sec)

        except Exception as e:
            print('SubscribeClient: run_forever exception ' + str(e))

    def start(self):
        threading.Thread(target=self.do_start).start()
