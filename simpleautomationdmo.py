#ip vm check ports --->input&argv
#get hostname
#ports number range
#connect vm check port socket

import socket
import sys

hostnam=sys.argv[1]
port=sys.argv[2]
tagret= socket.gethostbyname(hostnam)
try:
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    res= s.connect_ex((tagret,int(port)))
    if(res==0):
        print('ip is up and port ',port,' open')
    else:
        print('ip is up and port ',port,' closed')
    s.close()
except socket.gaierror :
    print('hostname cannt be resolved')
except socket.error:
    print('server not responding!!!')

