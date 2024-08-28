#!python3
#下载漫画
import requests,os,bs4

url = 'https://xkcd.com'
os.makedirs('d:\\code\\pythonlearn\\xkcd', exist_ok=True) #创建xkcd文件夹
while not url.endswith('#'):

    #下载页面
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    #找到id为comic的img标签
    comicelem=soup.select('#comic img')
    if comicelem==[]:
        print('Could not find comic image.')
    else:
        comicurl='https:'+comicelem[0].get('src')#获取comicurl
        #下载图片
        print('Downloading image %s...' % comicurl)
        res = requests.get(comicurl)
        res.raise_for_status()
        

        #保存图片
        imagefile = open(os.path.join('d:\\code\\pythonlearn\\xkcd', os.path.basename(comicurl)), 'wb')
        for chunk in res.iter_content(100000):
            imagefile.write(chunk)
        imagefile.close()
    prevlink=soup.select('a[rel="prev"]')[0]#获取上一页url,select返回列表，list用[0]获取第一个元素
    url = 'https://xkcd.com' + prevlink.get('href')#获取上一页url

    '''#查找下一页
    nextlink = soup.select('a[rel="next"]')
    if nextlink:
        url = 'https://xkcd.com' + nextlink[0].get('href')#获取下一页url
    else:
        print('No more comics.')
        break'''