import schedule
import time
import requests
from lxml import html
from datetime import datetime  


def run_scraper():
  URL = f'https://pib.gov.in/AllRelease.aspx'
  HEADERS = ({'User-Agent':
              'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'                                                                                                                                            ,\
              'Accept-Language': 'en-US, en;q=0.5'})

  webpage = requests.get(URL, headers=HEADERS)

  print(webpage)

  tree = html.fromstring(webpage.content)

  for i in range(10):
    anchor_tags = tree.xpath(
        f'//form/section[2]/div/div[6]/div/div/ul/li[{i}]/a')
    for tag in anchor_tags:
      data = {
          "title": tag.text_content(),
          "url": f"https://pib.gov.in/{tag.get('href')}",
          "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  

      }
      print(data)


# schedule.every().hour.do(run_scraper)
schedule.every(1).minutes.do(run_scraper)

while True:
  schedule.run_pending()
  time.sleep(1)
