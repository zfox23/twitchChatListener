#!/usr/bin/env python
"""A Python server that listens for specific requests made from the `chatListener` HTML's scripts.

"""

from http.server import BaseHTTPRequestHandler
from urllib import parse
from pynput.keyboard import Key, Controller
import threading

def doBoost():
    print('BOOSTING BITCH')
    keyboard = Controller()
    keyboard.press(Key.alt_l)
    keyboard.press(Key.alt_r)
    keyboard.press('e')
    keyboard.release('e')
    keyboard.release(Key.alt_r)
    keyboard.release(Key.alt_l)

def doFaToggle():
    print("you're on your own now bucko - maybe")
    keyboard.press(Key.alt_l)
    keyboard.press(Key.shift_r)
    keyboard.press('e')
    keyboard.release('e')
    keyboard.release(Key.shift_r)
    keyboard.release(Key.alt_l)
    

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = parse.urlparse(self.path)
        
        print(f'Path: {self.path}')
        print(f'Parsed Path: {parsed_path.path}')
        print(f'Query: {parsed_path.query}')
        
        query = parsed_path.query
        
        if query == 'boost':
            print('Boosting in 5 seconds')
            timer = threading.Timer(5.0, doBoost)
            timer.start()
        elif query == 'fatoggle':
            print('toggling FA in 5 seconds')
            timer = threading.Timer(5.0, doFaToggle)
            timer.start()
                
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8088), GetHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
