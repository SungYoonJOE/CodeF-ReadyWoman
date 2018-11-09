#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
url1 = 'https://www.seoulwomanup.or.kr/womanup/edu/selectProgramPageListAll.do?currentPage='
url2 = '&organPgName=&schOrganCode=&schCourseCode=&schDomainCode=&schGroupCode=&schEduSt=&schDayOfWeek=&schEduFee=&schLecturerName=&schClassName='

for i in range(1,3):
    req = Request(url1+str(i)+url2)
    res = urlopen(req)
    html = res.read()
    bs = BeautifulSoup(html, 'html.parser')

    for j in range(1,10):
        #강좌명
        cname_tag = bs.select('#sub > section > section > div > ul > li:nth-of-type('+str(j)+') > div > dl > dt')[0]
        cname = cname_tag.text
        cname = cname.replace("\t","")
        cname = cname.replace("\r","")
        cname = cname.replace("\n","")

        #초,중,고급, 자격, 관계없음 삭제
        if (cname[len(cname)-1]=="음"):
            cname=cname[0:len(cname)-4]
        else:
            cname=cname[0:len(cname)-2]

        #교육기간
        cterm_tag = bs.select('#sub > section > section > div > ul > li:nth-of-type('+str(j)+') > div > dl > dd:nth-of-type(5) > em')[0]
        cterm = cterm_tag.text
        cterm = cterm.replace("\t","")
        cterm = cterm.replace("\r","")
        cterm = cterm.replace("\n","")

        #교육시간
        ctime_tag = bs.select('#sub > section > section > div > ul > li:nth-of-type('+str(j)+') > div > dl > dd:nth-of-type(6) > em')[0]
        ctime = ctime_tag.text

        #수강료
        cprice_tag = bs.select('#sub > section > section > div > ul > li:nth-of-type('+str(j)+') > div > dl > dd.line_bottom > em')[0]
        cprice = cprice_tag.text

        #정원
        cstatus_tag = bs.select('#sub > section > section > div > ul > li:nth-of-type('+str(j)+') > div > dl > dd:nth-of-type(3) > em')[0]
        cstatus = cstatus_tag.text

        #센터명
        center_tag = bs.select('#sub > section > section > div > ul > li:nth-of-type('+str(j)+') > div > h2')[0]
        center = center_tag.text

        #유형 ex)국비지원 등 -> 교육과정인가?
        ctype_tag = bs.select('#sub > section > section > div > ul > li:nth-of-type('+str(j)+') > div > dl > dd:nth-of-type(1) > em')[0]
        ctype = ctype_tag.text

        #신청/모집중
        cstep_tag = bs.select('#sub > section > section > div > ul > li:nth-of-type('+str(j)+') > div > h4')[0]
        cstep = cstep_tag.text

        #detailsURL
        url_tag = bs.select('#sub > section > section > div > ul > li:nth-of-type('+str(j)+') > div > a')[0]
        if (url_tag.get('onclick')):
            url_tag = url_tag.get('onclick')
            url_tag = url_tag.replace("application('","")
            parts = url_tag.split("','")
            part1 = parts[0]
            part2 = parts[1]
            detailsURL = part1 + "?class_code=" + part2
        
        print(cname)
        print(cterm)
        print(ctime)
        print(cprice)
        print(cstatus)
        print(center)
        print(ctype)
        print(cstep)
        print(detailsURL+"\n")
        

