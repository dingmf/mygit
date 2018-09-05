import lxml
from lxml import etree

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<div>
    <ul class="ul">
        <li class="li">1</li>
        <li id="li2">2</li>
        <li class="li">3</li>
        <li class="li">1</li>
        <li id="li5">2</li>
        <li class="li">3</li>
    </ul>
</div>

<ul class="ul">
        <li class="li">1</li>
        <li id="li2">2</li>
        <li class="li">4</li>
</ul>

<p class="ul"></p>
</body>
</html>
'''
# 解析HTML
mytree = lxml.etree.HTML(html)
print(mytree)

# # /从根开始
# print(mytree.xpath('/html/head/title/text()'))
#
#
# print(mytree.xpath('/html/body/div/ul'))
# # //所有
# print(mytree.xpath('//ul'))
#
# #  . 当前
# ul = mytree.xpath('//ul')[0]
# li = ul.xpath('./li')
# print(li)

# 谓语
# li2 = mytree.xpath('//li[@id="li2"]')
# for l in li2:
#     print(l.text)
#     print(l.xpath('./text()'))

# li3 = mytree.xpath('//ul//li[3]/text()')
# print(li3)

# last()  first()
# last 倒数第一的数
# li3 = mytree.xpath('//div//li[last()]/text()')
# print(li3)

# position() 定位 < > = <= !=
print(mytree.xpath('//div//li[position() != 2]/text()'))

# 所有class=ul | 或
print(mytree.xpath('//ul[@class="ul"] | //p[@class="ul"]'))

print(mytree.xpath('//*[@class="ul"]'))

