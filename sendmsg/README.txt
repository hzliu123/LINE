How to use this:

1. Install LINE underground api from https://github.com/hzliu123/LINE
   git clone https://github.com/hzliu123/LINE
   pip install --user rsa curve thrift
   modify user credientials in LINE/sendmsg/sendmsg.py

2. Command syntax:
   sendmsg.sh friend_name text "Hello world!" image image.jpg

   Since this is only for demo, target user is fixed. Change it 
   from the source code if needed.
