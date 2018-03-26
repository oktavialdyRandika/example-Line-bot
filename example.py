import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time
import timeit
import random
import sys
import ast
import re
import os
import io
import json
import subprocess
import threading
import string
import codecs
import requests
import tweepy
import ctypes
import urllib
import urllib2
import wikipedia
import goslate
from bs4 import BeautifulSoup
from time import sleep
from urllib import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

import six

if (six.PY2):
    import urllib2
    import urllib
else:
    import urllib.request
    import urllib.parse

cl = LINETCR.LINE()
cl.login(token="ErGwQGZZTVcHtsc6rnk6.y+tyM7YcxOpgnp7/jgp39G.oNnP0q2/YJlgsqou6kL7wWT3CCUKdXSG5uvZEZpOKaw=")
cl.loginResult()

print "BOT MAIN"
reload(sys)
sys.setdefaultencoding('utf-8')

helpmsg = """♬♬♬♬♬♬♬♬	
♬    Okta Bots     ♬	
♬♬♬♬♬♬♬♬
Thanks Sam'sBot
For special commands.

Commands:
-------------------
 ⌬. 「media」
 ⌬. 「protective」
 ⌬. 「memegen」
 ⌬. 「quranlist」
 ⌬. 「group」
 ⌬. 「myhelp」
 
Service:
-------------
 ⌬.「botproblem
 ⌬.「payment
 ⌬.「sendmessage
 
Promote/Demote:
----------------
 ⌬.「staff:add
 ⌬.「expelstaff
 ⌬.「bot:add
 ⌬.「expelbot
 ⌬.「stafflist
 ⌬.「bot:room
 ⌬.「abort
 
Image:
 --------------
 ⌬.「pap
 ⌬.「imagetext
 ⌬.「papcontact
 """