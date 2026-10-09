#!/usr/bin/env python3
"""Threaded preview server for this landing page.

Python 3.9's `python3 -m http.server` is single-threaded. A page with 150+
images can stall or look like the server died. This process binds
127.0.0.1:8080, serves WebP with the correct MIME type, and stays up under
parallel browser requests.
"""
import mimetypes
import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
os.chdir(ROOT)
mimetypes.add_type('image/webp', '.webp')
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('application/javascript', '.js')

HOST, PORT = '127.0.0.1', 8080


class Handler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        '.webp': 'image/webp',
        '.css': 'text/css',
        '.js': 'application/javascript',
        '.html': 'text/html',
        '.svg': 'image/svg+xml',
        '.json': 'application/json',
    }

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        SimpleHTTPRequestHandler.end_headers(self)

    def log_message(self, fmt, *args):
        sys.stderr.write('[%s] %s\n' % (self.log_date_time_string(), fmt % args))


if __name__ == '__main__':
    httpd = ThreadingHTTPServer((HOST, PORT), Handler)
    httpd.daemon_threads = True
    print('Serving %s at http://%s:%s/' % (ROOT, HOST, PORT), flush=True)
    try:
        httpd.serve_forever(poll_interval=0.5)
    except KeyboardInterrupt:
        print('\nStopped.', flush=True)
