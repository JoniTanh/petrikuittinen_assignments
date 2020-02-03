#!/usr/bin/python3

import http.server
import socketserver

handler = http.server.CGIHTTPRequestHandler
PORT = 8000
server_address = ("", PORT)
#handler.cgi_directories = ["cgi-bin/"]
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("HTTP serving at port", PORT)
    httpd.server_name = "test"
    httpd.server_port = PORT
    httpd.serve_forever()

