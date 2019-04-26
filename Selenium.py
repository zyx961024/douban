from selenium import webdriver
from lxml import etree
def get_html(url):
    browser=webdriver.Chrome()

    try:
        browser.get(url)
        #print(browser.page_source)

        return browser.page_source
    finally:
        browser.quit()
def parse_html(html):
    html=etree.HTML(html)
    print(html)
    li_tags=html.xpath('//ol[@class="commentlist"]/li[@id]')
    print(li_tags)
    print(len(li_tags))

    for li_tag in li_tags:
        name=li_tag.xpath('./div/div/div[1]/strong/text()')
        imgurl=li_tag.xpath('.//div[@class ="text"]//img/@src')
        print(name,imgurl)

def main():
   url='http://jiandan.net/ooxx'

   html=get_html(url)
   imgurls=parse_html(html)

if __name__ == "__main__":
    main()
