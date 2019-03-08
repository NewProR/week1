import requests
from lxml import etree
import re
import json

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}

lists = []

def get_information():
    html = requests.get('https://news.sina.com.cn/world/', headers=headers)
    html.encoding = 'utf-8'
    count = 0
    selector = etree.HTML(html.text)
    infos = selector.xpath('//div[contains(@class,"news-item")]')
    list = []
    for info in infos:

        if len(info) > 0:
            try:
                news = info.xpath('h2/a/text()')[0]
                url = info.xpath('h2/a/@href')[0]
                count = count + 1
                res = requests.get(url, headers=headers)
                res.encoding = 'utf-8'
                search = etree.HTML(res.text)
                regex_str = '原标题(.*?)'
                panduan = search.xpath('//div[contains(@class,"article")]/p/text()')[0]
                panduans = ''.join(panduan).replace('\u3000', '')
                if re.match(regex_str,panduans):
                    content = search.xpath('//div[contains(@class,"article")]/p/text()')[1:]
                    contents = ''.join(content).replace('\u3000', '')
                    print('标题:' + news + '\n' + '链接:' + url + '\n' + '内容:' + contents)
                    ccc = {'title':news, 'urls':url,'contents':contents}
                    print('-----------------------------------')
                    list.append(ccc)
                else:
                    content = search.xpath('//div[contains(@class,"article")]/p/text()')
                    contents = ''.join(content).replace('\u3000','')
                    print('标题:' + news + '\n' + '链接:' + url + '\n' + '内容:' + contents)
                    ccc = {'title': news, 'urls': url, 'contents': contents}
                    print('-----------------------------------')
                    list.append(ccc)

            except:
                pass
    print(list)
    lists.append(list)
    return list

if __name__ == '__main__':
    get_information()
    f = open('./json文件/'+ 'news.json', 'a')
    f.write(json.dumps(lists))
    f.close()





