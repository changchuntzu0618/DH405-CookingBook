import requests
from lxml import etree

def GetInfo(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    page = requests.get(url=url, headers=headers).text
    datas = ParseInfo(page)
    return datas

def ParseInfo(page):
    tree = etree.HTML(page.encode('utf-8'))
    tr_list = tree.xpath('//table[@style="width: 100%;"]/tr')
    # print([''.join(i.xpath("//text()")) for i in tr_list])

    fp = open('JuanDiErShiLiaoZhuBing.txt', 'w', encoding='utf-8')
    for tr in tr_list:
        text_list = tr.xpath('./td[2]//text()')
        # materials lists into oneline
        text = " ".join(text_list)
        print(text)
        fp.write(text + '\n')


if __name__ == "__main__":
    url = 'https://ctext.org/wiki.pl?if=gb&chapter=406913&remap=gb'  # 聚珍异馔01 JuanDiYiJvZhenYiZhuan_1
    # url = 'https://ctext.org/wiki.pl?if=gb&chapter=511418&remap=gb'  # 聚珍异馔02 JuanDiYiJvZhenYiZhuan_2
    # url = 'https://ctext.org/wiki.pl?if=gb&chapter=88013&remap=gb'  # 聚珍异馔03 JuanDiYiJvZhenYiZhuan_3
    # url = 'https://ctext.org/wiki.pl?if=gb&chapter=800802&remap=gb'  # 诸般汤煎 JuanDiErZhuBanTangJian
    # url = 'https://ctext.org/wiki.pl?if=gb&chapter=159049&remap=gb'  # 神仙服食 JuanDiErShenXianFuShi
    # url = 'https://ctext.org/wiki.pl?if=gb&chapter=470874&remap=gb'  # 食疗诸病 JuanDiErShiLiaoZhuBing

    datas = GetInfo(url)