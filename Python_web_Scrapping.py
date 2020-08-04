import requests
from bs4 import BeautifulSoup as BS
import pandas as pd
import re

def raw(url):
  header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
  page=requests.get(url,headers=header)
  if page.status_code==200:
    return page.content
  else:
    print('error')

url='https://www.amazon.in/gp/product/B07V3CMQH3/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1'
soup=BS(raw(url))
review_link='https://www.amazon.in'+soup.findAll('a',attrs={'data-hook':'see-all-reviews-link-foot'})[0]['href']
i=0
reviews=[]
while i<1:
  s=BS(raw(('{}').format(review_link)))
  print(review_link)
  for j in s.findAll('span',attrs={'class':'a-size-base review-text review-text-content'}):
    reviews.append(j.text)
  try:
    review_link='https://www.amazon.in'+s.find('li',attrs={'class':'a-last'}).find('a').get('href')
  except AttributeError:
    break
review_data=pd.DataFrame()
review_data['Reviews']=reviews
print(review_data.head())
