from urllib import request
import requests
import re
import json
import os
count = 1


class paJs:

    def __init__(self):
        

        self.url = "http://www.imomoe.io/playdata/2/7426.js?1393.1"

        self.list = []
        self.text = ''


    def start(self):

        self.r = requests.get(self.url)

        txt = ''+self.r.text
        self.text = txt
        arr = txt.split('\'')
        count =0
        for index,val in enumerate(arr):
            ans = re.match('.u.*flv$',val)

            if ans!=None:
                count = count +1
                # print(index)
                # print(val)
                arr1 = val.split('$')
                #print(arr1[0])
                s = ''.join(arr1[0])
                #print(s)
                s=s.encode('utf-8')
                s = s.decode('unicode_escape')
                self.list.append([s,arr1[1]])

        # print(self.list)
        # print(count)

if __name__ == "__main__":

    p = paJs()
    p.start()
