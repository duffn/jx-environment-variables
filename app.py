#!/usr/bin/python

import os

from http.server import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8080

class MyHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    """Handler for GET requests"""
    self.send_response(200)
    self.send_header('Content-type','text/plain')
    self.end_headers()

    branch_name = os.environ.get('BRANCH_NAME', 'NOBRANCH')
    self.wfile.write(branch_name.encode())

try:
  server = HTTPServer(('', PORT_NUMBER), MyHandler)
  print('Started httpserver on port', PORT_NUMBER)
  server.serve_forever()

except KeyboardInterrupt:
  server.server_close()
  print('Stopping server')
