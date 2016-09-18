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

if len(sys.argv) < 2:
    print("usage: sendmsg.py <message>")
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
x.sendMessage(sys.argv[1])
x.getRecentMessages(count=10)
