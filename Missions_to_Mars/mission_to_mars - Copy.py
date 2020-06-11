{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "import re\n",
    "import pandas as pd\n",
    "from splinter.exceptions import ElementDoesNotExist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for x in range(20):\n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html, 'html.parser')\n",
    "    main = soup.find_all('div', class_='list_text')\n",
    "    \n",
    "    for  main in main:\n",
    "        news_title = main.find('div', class_='content_title').text\n",
    "        news_p = main.find('div',class_= 'article_teaser_body').text\n",
    "        print('-----------')\n",
    "        print(news_title)\n",
    "        print(news_p)\n",
    "        \n",
    "    try:\n",
    "        browser.click_link_by_partial_text('more')\n",
    "          \n",
    "    except:\n",
    "        print(\"Scraping Complete\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "url_img = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(url_img)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "    \n",
    "main = soup.find('article', attrs={'class':'carousel_item'})\n",
    "    \n",
    "featured_image_url  = main['style']\n",
    "featured_image_url  = re.findall(r\"'(.*?)'\",featured_image_url )\n",
    "featured_image_url  ='https://www.jpl.nasa.gov'+ featured_image_url [0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "url_w = 'https://twitter.com/marswxreport?lang=en'\n",
    "browser.visit(url_w)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "mars_weather = soup.find_all('div', attrs={'class':'css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0'})\n",
    "\n",
    "weather = []\n",
    "\n",
    "for mars_weather in mars_weather:\n",
    "    url = mars_weather.find('span', class_ = 'css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0').text\n",
    "    weather.append(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_weather  = weather[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "url_facts = 'https://space-facts.com/mars/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tables = pd.read_html(url_facts)\n",
    "tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "type(tables)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = tables[2]\n",
    "df.columns = ['description', 'value']\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_html('table.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "url_image = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url_image)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "url_list= []\n",
    "url_full_img = \"https://astrogeology.usgs.gov\"\n",
    "titles = []\n",
    "\n",
    "for x in range (4):\n",
    "            url_images = soup.find('div', class_=\"collapsible results\").find_all('a')[x]['href']\n",
    "            title = soup.find('div', class_=\"collapsible results\").find_all('h3')[x].text\n",
    "            full_url = url_full_img + url_images\n",
    "            url_list.append(full_url)\n",
    "            titles.append(title)\n",
    "        \n",
    "# dic = {\"Title\": titles , \"Image_URL\": url_final_image}\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced',\n",
       " 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced',\n",
       " 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced',\n",
       " 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced']"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "url_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Cerberus Hemisphere Enhanced',\n",
       " 'Schiaparelli Hemisphere Enhanced',\n",
       " 'Syrtis Major Hemisphere Enhanced',\n",
       " 'Valles Marineris Hemisphere Enhanced']"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [],
   "source": [
    "img_url =[]\n",
    "main_link = 'https://astrogeology.usgs.gov/'\n",
    "\n",
    "for url in url_list:\n",
    "    browser.visit(url)\n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html, 'html.parser')\n",
    "    image_link = soup.find('div', class_ ='container').find_all('img')[x]['src']\n",
    "    full_image_url = main_link + image_link\n",
    "    img_url.append(full_image_url)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    " dic = {\"Title\": titles ,\n",
    "          \"Image_URL\": img_url}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "img_url.append(dic)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Title': ['Cerberus Hemisphere Enhanced',\n",
       "  'Schiaparelli Hemisphere Enhanced',\n",
       "  'Syrtis Major Hemisphere Enhanced',\n",
       "  'Valles Marineris Hemisphere Enhanced'],\n",
       " 'Image_URL': ['https://astrogeology.usgs.gov//cache/images/f789a481f60deaf01996343999491211_valles_marineris_unenhanced.tif_thumb.png',\n",
       "  'https://astrogeology.usgs.gov//cache/images/f789a481f60deaf01996343999491211_valles_marineris_unenhanced.tif_thumb.png',\n",
       "  'https://astrogeology.usgs.gov//cache/images/f789a481f60deaf01996343999491211_valles_marineris_unenhanced.tif_thumb.png',\n",
       "  'https://astrogeology.usgs.gov//cache/images/f789a481f60deaf01996343999491211_valles_marineris_unenhanced.tif_thumb.png',\n",
       "  {...}]}"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
