#
# Unofficial way to send LINE messages
#
# Initial version: 2016/9/18  joseph@dt42.io
# 
# Based on hack information from https://github.com/carpedm20/LINE
# 
# LINE Corp. started providing LINE Business Center this year, but it requires
# us to host bots on a public server with CA certificate for communicating with
# LINE servers. That's is too much work for our GTC demo.
#

import IPython
import sys
import os
from line import LineClient, LineGroup, LineContact

arglen = len(sys.argv)
if arglen < 3:
    print("usage: sendmsg.py [text 'message'| image img.jpg]+")
    sys.exit(1)

AUTHFILE = '.auth'
loginfail = True
count = 0
LOGIN_ID='line_id@gmail.com'
LOGIN_PASSWORD='PaSSW0rD'

while count < 3:
    count += 1
    if os.path.isfile(AUTHFILE):
        with open(AUTHFILE, 'r') as f:
            token=f.readline()
        try:
            client = LineClient(authToken=token)
            loginfail = False
            break
        except:
            os.remove(AUTHFILE)
            print("login failed with token. Previous token removed.")
    else:
        try:
            client = LineClient(LOGIN_ID, LOGIN_PASSWORD)
            with open(AUTHFILE, 'w') as f:
               f.write(client.authToken)
            loginfail = False
            break
        except:
            print("login failed with id and password")

if loginfail:
    sys.exit(2)

x=client.contacts[1]

for i in xrange(1, arglen, 2):
    msgtype = sys.argv[i]
    if msgtype == 'text':
        x.sendMessage(sys.argv[i+1])
    elif msgtype == 'image':
        x.sendImage(sys.argv[i+1])
    else:
        print("error argument!")
        sys.exit(3)

x.getRecentMessages(count=10)
