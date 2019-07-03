# -*- coding: utf-8 -*-

import urllib2
import re

class BDTB:
    baseUrl = 'http://book.zongheng.com/chapter/800460/45458947.html'
    #获取源代码
    def getPage(self,pageNum):
        try:
            url = self.baseUrl + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request).read()
            #print (response)
            return response
        except Exception :
            print(e)
    #匹配内容
    def Title(self,pageNum):
        html = self.getPage(pageNum)
        reg = re.compile(r'title="这(.*?)"')
        items = re.findall(reg,html)
        print(items[0])
        for item in items:
            f = open('text1.txt','w')
            f.write('标题'+'\t'+item)
            f.close()
        return items
    def Text(self,pageNum):
        html = self.getPage(pageNum)
        reg = re.compile(r'class="d_post_content j_d_post_content ">            (.*?)</div><br> ',re.S)
        req = re.findall(reg,html)
        #print req[0]
        for i in req:
            removeAddr = re.compile('<a.*?>|</a>')
            removeaddr = re.compile('<img.*?>')
            removeadd = re.compile('http.*?.html')
            i = re.sub(removeAddr,'',i)
            i = re.sub(removeaddr,'',i)
            i = re.sub(removeadd,'',i)
            i = i.replace('<br>','')
            print(i)
            f = open('text1.txt','a')
            f.write('\n\n'+i)
            f.close()



bdtb = BDTB()
print('爬虫正在启动。。。。')
try:
    for i in range(1,4):
        print('正在爬取第%s小说' %(i))
        bdtb.Title(1)
        bdtb.Text(1)
except Exception :
    print(e)