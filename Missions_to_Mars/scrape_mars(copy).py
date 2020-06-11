#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup
import re
import pandas as pd
from splinter.exceptions import ElementDoesNotExist


# In[15]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[ ]:


for x in range(20):
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    main = soup.find_all('div', class_='list_text')
    
    for  main in main:
        news_title = main.find('div', class_='content_title').text
        news_p = main.find('div',class_= 'article_teaser_body').text
        print('-----------')
        print(news_title)
        print(news_p)
        
    try:
        browser.click_link_by_partial_text('more')
          
    except:
        print("Scraping Complete")


# In[ ]:


url_img = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url_img)


# In[ ]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')
    
main = soup.find('article', attrs={'class':'carousel_item'})
    
featured_image_url  = main['style']
featured_image_url  = re.findall(r"'(.*?)'",featured_image_url )
featured_image_url  ='https://www.jpl.nasa.gov'+ featured_image_url [0]


# In[ ]:




# In[ ]:


url_w = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url_w)


# In[ ]:



html = browser.html
soup = BeautifulSoup(html, 'html.parser')

mars_weather = soup.find_all('div', attrs={'class':'css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0'})

weather = []

for mars_weather in mars_weather:
    url = mars_weather.find('span', class_ = 'css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0').text
    weather.append(url)


# In[ ]:


mars_weather  = weather[0]


# In[ ]:


mars_weather


# In[ ]:


url_facts = 'https://space-facts.com/mars/'


# In[ ]:


tables = pd.read_html(url_facts)
tables


# In[ ]:


type(tables)


# In[ ]:


df = tables[2]
df.columns = ['description', 'value']
df.head()


# In[ ]:


df.to_html('table.html')


# In[3]:


url_image = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url_image)


# In[4]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')

url_list= []
url_full_img = "https://astrogeology.usgs.gov"
titles = []

for x in range (4):
            url_images = soup.find('div', class_="collapsible results").find_all('a')[x]['href']
            title = soup.find('div', class_="collapsible results").find_all('h3')[x].text
            full_url = url_full_img + url_images
            url_list.append(full_url)
            titles.append(title)
        
# dic = {"Title": titles , "Image_URL": url_final_image}
    


# In[ ]:





# In[5]:


url_list


# In[6]:


titles


# In[53]:


img_url =[]
main_link = 'https://astrogeology.usgs.gov/'

for url in url_list:
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image_link = soup.find('div', class_ ='container').find_all('img')[x]['src']
    full_image_url = main_link + image_link
    img_url.append(full_image_url)


# In[61]:


dic = {"Title": titles ,
         "Image_URL": img_url}


# In[62]:


img_url.append(dic)


# In[63]:


dic

