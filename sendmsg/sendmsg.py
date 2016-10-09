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

import sys
import os
from line import LineClient, LineGroup, LineContact

arglen = len(sys.argv)
if arglen < 3:
    print("usage: sendmsg.py friend_name [text 'message'| image img.jpg]+")
    sys.exit(1)

AUTHFILE = '.auth'
PASSWDFILE = '.login'
loginfail = True
count = 0

# read id and password from .login
if os.path.isfile(PASSWDFILE):
    with open(PASSWDFILE, 'r') as f:
        LOGIN_ID, LOGIN_PASSWORD = f.read().splitlines()
else:
    print(".login file doesn't exist!")
    sys.exit(4)

# try to login 3 times, save authentication token for reuse
while loginfail and count < 3:
    count += 1
    if os.path.isfile(AUTHFILE):
        with open(AUTHFILE, 'r') as f:
            token=f.readline()
        try:
            client = LineClient(authToken=token)
            loginfail = False
        except:
            os.remove(AUTHFILE)
            print("login failed with token. Previous token removed.")
    else:
        try:
            client = LineClient(LOGIN_ID, LOGIN_PASSWORD)
            with open(AUTHFILE, 'w') as f:
               f.write(client.authToken)
            loginfail = False
        except:
            print("login failed with id and password")

if loginfail:
    sys.exit(2)

# find friend_name in contact list
friend_name = sys.argv[1]
friend_contact = None
for i in xrange(1, len(client.contacts)):
    if client.contacts[i].name == friend_name:
        friend_contact = client.contacts[i]
        break

if friend_contact == None:
    print("friend_name %s not found!" % friend_name)
    sys.exit(5)

# send message
for i in xrange(2, arglen, 2):
    msgtype = sys.argv[i]
    if msgtype == 'text':
        friend_contact.sendMessage(sys.argv[i+1])
    elif msgtype == 'image':
        friend_contact.sendImage(sys.argv[i+1])
    else:
        print("error argument!")
        sys.exit(3)

# flush outgoing message (and clear incoming message)
friend_contact.getRecentMessages(count=10)
