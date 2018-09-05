import requests
import lxml
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

cityUrl = 'http://jobs.51job.com/'

def getCity(url):
    response = requests.get(url, headers=headers)
    html = response.content.decode('gbk')
    mytree = lxml.etree.HTML(html)

    cityList = mytree.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/a')
    for city in cityList:
        cityName = city.xpath('./text()')[0]
        cityHref = city.xpath('./@href')[0]
        print(cityName, cityHref)
        
if __name__ == '__main__':
    getCity(cityUrl)