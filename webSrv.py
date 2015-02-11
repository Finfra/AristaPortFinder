# httpd.py
from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler
import os

os.chdir("./www")
serv = HTTPServer(("", 1234), CGIHTTPRequestHandler)
serv.serve_forever()

