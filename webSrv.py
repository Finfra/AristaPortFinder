# httpd.py
from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler
import os

os.chdir("/Users/jgnam73/_git/__gitHub/AristaPortFinder/www/")
serv = HTTPServer(("localhost", 1234), CGIHTTPRequestHandler)
serv.serve_forever()

