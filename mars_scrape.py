import pandas as pd
import requests
from flask import Flask, render_template
import time
import numpy as np
import json
from selenium import webdriver
from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
    # splinter
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    # Mars News Titles
    Browser = init_browser()
    mars_collection = {}


# NASA Mars News

def marsNews():
    url = "https://mars.nasa.gov/news/"
    Browser.visit(url)

    html = browser.html
    rover = BeautifulSoup(html,"html.parser")

    news_title = rover.find('div', class_='content_title').text
    news_p = rover.find('div', class_='article_teaser_body').text

    print(f"In the latest news {news_title}.")
    print()
    print(news_p)

def Mars_Feature_Image():

    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)
    base_url = "https://www.jpl.nasa.gov"
    #get image url using BeautifulSoup
    html_image = browser.html
    soup = BeautifulSoup(html_image, "html.parser")

    img_url = soup.find('article', class_='carousel_item')['style'].split("'")[1]

    featured_image_url = base_url+ img_url
    return featured_image_url

def Mars_Weather():
    twiturl = "https://twitter.com/marswxreport?lang=en"
    browser.visit(twiturl)
    twit = browser.html
    twitter = BeautifulSoup(twit,"html.parser")
    mars_weather = twitter.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
    return mars_weather

def Mars_Facts():
    url3 = 'https://space-facts.com/mars/'
    tables = pd.read_html(url3)
    df = tables[0]
    df.columns = ['Description', 'Value']
    html_table = df.to_html()
    html_table.replace('\n', '')
    return html_table

def Mars_Hemispheres():
    url4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    base = "https://astrogeology.usgs.gov"

    # launch browser
    browser.visit(url4)
    
    # create beautifulsoup object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemisphere_image_urls = []

    hemi = soup.find("div", class_ = "result-list" )
    results = hemi.find_all("div", class_="item")

    for result in results:
        #print(img_title)
        img_title = result.find("h3").text
        #print(link_to_img)
        image = result.find("a")["href"]
        image_url = base + image    
        browser.visit(image_url)
        html = browser.html
        soup=BeautifulSoup(html, "html.parser")
        gumbo = soup.find("div", class_="downloads")
        image_url = gumbo.find("a")["href"]
        hemisphere_image_urls.append({"Title": img_title, "Image_Url": image_url})

        return hemisphere_image_urls

