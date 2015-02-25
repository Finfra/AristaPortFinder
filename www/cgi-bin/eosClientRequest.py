#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi, cgitb ,re,sys
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
import logging
# Create instance of FieldStorage 
print "Content-type:text/html\r\n\r\n"

form = cgi.FieldStorage() 
# print form
#print  """{"%s": "vEOS"}"""%(form.keys())
#print """{"%s": "%s"}"""%(form.keys(),form[0] )
#sys.exit() 
cmd=""
ip=""
frmt=""
isCmdIsList= form.has_key('cmd[]') 
if form.length>-1:
    logging.warning("\n".join(form.keys() ))
    logging.warning("\n"+ 't' if isCmdIsList else 'f' ) 
    logging.warning("\n".join(form.getlist('cmd[]')))

    if isCmdIsList:
        cmd=form.getlist('cmd[]')
    else:        
        cmd=form.getlist('cmd')
    ip=form.getlist('ip')[0]
    f=form.getlist('format')
    frmt="text" if len(f)!=0 else "json"
    logging.warning("\n format="+frmt)
    # print """{"parameter": "%s"}"""%cmd
else:
    print  """{"parameter": "no"}"""
    sys.exit() 


from jsonrpclib import Server

# print  """{"parameter": "%s"}"""%("https://admin:admin@"+str(ip[0])+"/command-api")
# sys.exit() 
# eapi = Server("https://admin:admin@172.16.130.100/command-api")
eapi = Server("https://admin:admin@"+str(ip)+"/command-api")


#j=eapi.runCmds(1, ["show version"],'json')
#j=eapi.runCmds(1, ["show interfaces status"],'json')
logging.warning("\n cmd="+cmd[0])
j=eapi.runCmds(1, cmd,frmt)

data=""
if isCmdIsList:
    for ss in j:
        data+=str(ss)+","
    data="["+data[:-1]+"]"
else:
    data=str(j[0])

p = re.compile("(u')")
data=p.sub("\"", data)
p = re.compile("(',)")
data=p.sub("\",", data)
p = re.compile("(':)")
data=p.sub("\":", data)
p = re.compile("('\})")
data=p.sub("\"}", data)
p = re.compile("( True,)")
data=p.sub(" true,", data)
p = re.compile("( False,)")
data=p.sub(" false,", data)
print data
# print """
# {"modelName": "vEOS"}
# """


logging.warning("\n"+data)


        









