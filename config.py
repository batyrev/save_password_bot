import os

from utils import args_parser

token = os.getenv('TOKEN')
if token:
    TOKEN = token
else:
    args = args_parser()
    TOKEN = args.token

message_lifetime = os.getenv('MESSAGE_LIFETIME')
if token:
    MESSAGE_LIFETIME = int(message_lifetime)
else:
    args = args_parser()
    MESSAGE_LIFETIME = args.deltime
