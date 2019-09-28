
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import csv
import re

#first setup the driver;
#chromedriver="/Users/apple/Downloads/chromedriver"
chrome_options= webdriver.ChromeOptions()

#no need to open the chrome
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver =webdriver.Chrome(chrome_options=chrome_options)
movie_driver =webdriver.Chrome(chrome_options=chrome_options)
#initiate writer
file = open('task2_continued.csv','a')
csv_writer = csv.writer(file)
csv_writer.writerow(['names','locations','directors','writer','reviews','official_sites','languages'])

#first page; place outside the loop
driver.get("https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&sort=user_rating,desc&start=1194&ref_=adv_nxt")
for i in range(0,26):
    movie_list_total = driver.find_elements_by_xpath("//h3[@class ='lister-item-header']")
    
    movie_html_list=[]
    for movie_name in movie_list_total:
        a_attribute= movie_name.find_element_by_tag_name("a")
        #get partial html
        movie_html = a_attribute.get_attribute("href")
        movie_html_list.append(movie_html)



    for each_html in movie_html_list:
        movie_driver.get(each_html)
        try:
            movie_list = movie_driver.find_elements_by_xpath("//div[@class ='title_wrapper']")
            names = [name.find_element_by_tag_name("h1").text for name in movie_list]
        except:
            names = ['NA']
        try:
            movie_location = movie_driver.find_elements_by_xpath("//div[@class ='subtext']")
            location_finder = re.compile(r'[(](.*?)[)]', re.S)
            locations = [re.findall(location_finder,location.text)[0] for location in movie_location]
        except:
            locations = ['NA']
        try:
            movie_director=movie_driver.find_elements_by_css_selector("a[href*='tt_ov_dr']")
            directors = [director.text for director in movie_director if director.text != '']
        except:
            directors =  ['NA']
        try:
            movie_writer = movie_driver.find_elements_by_css_selector("a[href*='tt_ov_wr']")
            writer = [writer.text for writer in movie_writer if writer.text != '']
        except:
            writer =  ['NA']
        try:
            movie_reviewers=movie_driver.find_elements_by_css_selector("a[href ='reviews?ref_=tt_ov_rt']")
            reviews = [review.text for review in movie_reviewers if review.text != '']
        except:
            reviews =  ['NA']
        try:
            movie_tagline=movie_driver.find_elements_by_xpath("//div[@id='titleStoryLine']")
            taglines = [tagline.find_element_by_xpath("//div[@class ='txt-block']").text.split(":")[1] for tagline in movie_tagline]
        except:
            taglines =  ['NA']
        try:
            movie_official_site = movie_driver.find_elements_by_css_selector("a[href*='ofs_offsite']")
            official_sites = [site.text for site in movie_official_site if site.text != '']
        except:
            official_sites =  ['NA']
        try:
            movie_country = movie_driver.find_elements_by_css_selector("a[href*='country_of_origin']")
            countries = [country.text for country in movie_country if country.text != '']
        except:
            countries =  ['NA']
        try:
            movie_language = movie_driver.find_elements_by_css_selector("a[href*='primary_language']")
            languages = [language.text for language in movie_language if language.text != '']
        except:
            languages =  ['NA']

        csv_writer.writerow(
                            [names, locations, directors,writer, reviews, taglines, official_sites, countries,languages])
print("Page ",str(i)," is writing ",[names, locations, directors,writer]," and etc..")
next_page = driver.find_element_by_link_text("Next »")
next_page.click()
current_page = driver.current_window_handle

driver.close()
movie_driver.close()




## how to scrape details;


## how to get multiple value data;
