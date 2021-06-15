import requests
import os
import urllib.request
import wget


#name = input("please enter name for config:  ")
#print(name)
#print(str(name))
#url = "https://github.com/risecore/test/blob/main/{}.txt".format(str(name))
#req = requests.get(url)
#print('downloading...')
#filename = os.getcwd() + '/{}.txt'.format(str(name))
#fo = open(filename,'w')
#fo.write(req.text)
#print('configuration...')
#print('complate..')

url = 'https://github.com/risecore/test/blob/main/test.txt'


wget.download(url)
