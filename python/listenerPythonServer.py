#!/usr/bin/env python
"""A Python server that listens for specific requests made from the `chatListener` HTML's scripts, then acts on them.
"""

import time
from http.server import BaseHTTPRequestHandler
from urllib import parse
from pynput.keyboard import Key, Controller
import threading

# This will be called when something makes an HTTP GET request to `http://localhost:8088/?customRewardAction01`
# In this example, the keyboard combination `LEFT ALT + RIGHT ALT + E` will be pressed and then released.
def customRewardAction01():
    print('Performing Custom Reward Action 01!')
    keyboard = Controller()
    keyboard.press(Key.alt_l)
    keyboard.press(Key.alt_r)
    keyboard.press('e')
    # Make sure to sleep here, or else some applications might not recognize the keypress.
    time.sleep(0.3)
    keyboard.release('e')
    keyboard.release(Key.alt_r)
    keyboard.release(Key.alt_l)

# This will be called when something makes an HTTP GET request to `http://localhost:8088/?customRewardAction02`
# In this example, the keyboard combination `LEFT ALT + RIGHT SHIFT + E` will be pressed and then released.
def customRewardAction02():
    print('Performing Custom Reward Action 02!')
    keyboard = Controller()
    keyboard.press(Key.alt_l)
    keyboard.press(Key.shift_r)
    keyboard.press('e')
    # Make sure to sleep here, or else some applications might not recognize the keypress.
    keyboard.release('e')
    keyboard.release(Key.shift_r)
    keyboard.release(Key.alt_l)
    
class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the GET request URL
        parsed_path = parse.urlparse(self.path)
        # Print out the query associated with the GET request URL
        print(f'Query: {parsed_path.query}')
        
        query = parsed_path.query
        
        # Start logic for handling different queries.
        if query == 'customRewardAction01':
            print('Calling `customRewardAction01()`...')
            customRewardAction01()
        elif query == 'customRewardAction02':
            # As an example, we show what code looks like if we want to defer an action for five seconds.
            print('Calling `customRewardAction02()` in 5.0 seconds...')
            timer = threading.Timer(5.0, customRewardAction02)
            timer.start()
        else:
            print(f'A GET request was made with query {query}. That query is not handled in `listenerPythonServer.py`.')
                
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8088), GetHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
