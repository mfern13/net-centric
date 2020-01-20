# Code taken from official Python documentation:
# https://docs.python.org/3/library/http.server.html
#
#GitHub repo: https://github.com/mfern13/net-centric.git

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
