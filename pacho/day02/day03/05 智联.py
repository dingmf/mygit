import requests
import re
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

def getJobInfo(url):
    '''
    获取岗位详细信息
    :param url:
    :return:
    '''

    response = requests.get(url, headers=headers).content.decode('gbk')
    soup = BeautifulSoup(response, 'lxml')

    jobResponsibilityLsit = soup.select('div.bmsg.job_msg.inbox > p')
    jobResponsibility = ''
    for jobRes in jobResponsibilityLsit:
        jobResponsibility +=jobRes.text
    print(jobResponsibility)

    return jobResponsibility

def getJob(url):
    response = requests.get(url, headers=headers).content.decode('gbk')

    soup = BeautifulSoup(response, 'lxml')

    jobList = soup.select("#resultList > div.el")
    # #resultList > div:nth-child(4) > span.t2 > a
    for job in jobList[1:]:
        jobName = job.select('span:nth-of-type(1) > a')[0]['title']
        joburl = job.select('span:nth-of-type(1) > a')[0].attrs['href']
        jobInfo = getJobInfo(joburl)
        company = job.select('span.t2 > a')[0]['title']
        jobAddr = job.select('span.t3')[0].text
        # 薪资
        money = job.select('span.t4')[0].text
        # 发布时间
        time = job.select('span.t5')[0].text
        print(jobName, joburl, company, jobAddr, money, time, jobInfo)

def getPageNun(url):
    '''
    获取岗位页数
    :param url:
    :return:
    '''
    response = requests.get(url, headers=headers).content.decode('gbk')
    # print(response)
    soup = BeautifulSoup(response, 'lxml')
    pageNum = soup.select('div.p_in > .td')[0].text[1:3]
    return int(pageNum)


if __name__ == '__main__':

    starUrl = 'https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,3.html'
    pagenum = getPageNun(starUrl)
    for num in range(1, pagenum + 1):
        newurl = 'https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,%d.html' % num
        getJob(newurl)
