# AristaPortFinder - Introduction
This Web App is Port Finder for Leaf Switch that is Arista Networks, inc.

Warn : This Project is for Test, not for ur job.

# Version

v0.2

# Setting
1. check packages : jsonrpclib-0.1.3-py2.7<br>
    [ ~/]$ python 
    Python 2.7.5 (default, May 19 2013, 13:26:46) 
    [GCC 4.2.1 Compatible Apple Clang 4.1 ((tags/Apple/clang-421.11.66))] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import jsonrpclib

2. check permission 
    ls -als {downloadPath}/www/cgi-bin/
    • if not : chmod +x {downloadPath}/www/cgi-bin/ -R

3. Change Switch setting in {downloadPath}/www/main.html
    ex)
        leafs={
          "leaf1":{"ip":"10.10.1.1","name":"PocAL1"},
          "leaf2":{"ip":"10.10.1.2","name":"PocAL2"},
          "leaf3":{"ip":"10.10.1.3","name":"PocAL3"},
          "leaf4":{"ip":"10.10.1.4","name":"PocAL4"},
          "leaf5":{"ip":"10.10.1.5","name":"PocAL5"}      
        }; 
        leafSwitchs={
          "leafSwitch1":{"ip":"10.10.10.1","name":"EdgeLeaf1"},
          "leafSwitch2":{"ip":"10.10.10.2","name":"EdgeLeaf1"}
        };
4. Check switch password : {downloadPath}/www/cgi-bin/eosClientRequest.py (default password is 'admin')
    Warn : Password repository support will be support. All Switch's password must be same.



# usage 
1. $ python webSrv.py 
2. connect to http://FQDN_or_ip:1234/

# example
-

# CF        

This is Demo Project for Arista Networks,

# BUGS

Please report bugs to nowage[at]icloud.com.

# todo

Password repository support

# CONTRIBUTING

The github repository is at https://github.com/Finfra/AristaPortFinder.git

# SEE ALSO

Some other stuff.

# AUTHOR

NamJungGu, <nowage[at]icloud.com>

# COPYRIGHT AND LICENSE

(c) Copyright 2005-2014 by finfra.com

This library is free software; you can redistribute it and/or modify
it under the same terms as Python itself.
