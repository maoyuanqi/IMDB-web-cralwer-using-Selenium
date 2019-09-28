
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import csv

#first setup the driver;
chromedriver="/Users/apple/Downloads/chromedriver"
chrome_options= webdriver.ChromeOptions()

chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver =webdriver.Chrome(executable_path=chromedriver,chrome_options=chrome_options)
movie_detail_driver = webdriver.Chrome(executable_path=chromedriver,chrome_options=chrome_options)
driver.get("https://www.imdb.com/search/title/?genres=action&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=037ZPKFCRZAQE2S82WZC&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_1")


movie_list_total = driver.find_elements_by_xpath("//h3[@class ='lister-item-header']")
movie_html_list=[]
final_list=[]


for movie_name in movie_list_total:
    a_attribute= movie_name.find_element_by_tag_name("a")
    movie_html = a_attribute.get_attribute("href")
    movie_html_list.append(movie_html)

reviewer_html_list=[]

for movie in movie_html_list:
    info_list = []
    movie_detail_driver.get(movie)
    movie_info = movie_detail_driver.find_element_by_xpath("//div[@class ='title_wrapper']").find_element_by_tag_name("h1").text
    info_list.append(movie_info)
    
    movie_reviewer=movie_detail_driver.find_element_by_css_selector("a[href*='tt_ov_rt']")
    html=movie_reviewer.get_attribute('href')
    ##get id;
    
    movie_detail_driver.get(html)
    specific_rate_number = []
    review_table2 = movie_detail_driver.find_elements_by_xpath("//div[@class ='smallcell']")
    for detail2 in review_table2:
        detail2_text = detail2.text
        specific_rate_number.append(detail2_text)
    
    info_list.extend(specific_rate_number)
    final_list.append(info_list)
with open("test.csv",'a') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(
                        ['title', 'All_All_Age', 'All_<18', 'All_18-29', 'All_30-44', 'All_45+', 'Males_All_Age', 'Males_<18',
                         'Males_18-29', 'Males_30-44', 'Males_45+','Females_All_Age', 'Females_<18', 'Females_18-29', 'Females_30-44', 'Females_45+','Top_1000_Voters','US_Users','Non_US_Users'])
    csv_writer.writerows(final_list)


for i in range(0,26):
    next_page=driver.find_element_by_link_text("Next »")
    next_page.click()
    current_page=driver.current_window_handle
    
    movie_list_total = driver.find_elements_by_xpath("//h3[@class ='lister-item-header']")
    movie_html_list = []
    final_list = []
    for movie_name in movie_list_total:
        a_attribute = movie_name.find_element_by_tag_name("a")
        movie_html = a_attribute.get_attribute("href")
        movie_html_list.append(movie_html)

    #reviewer_html_list = []

    for movie in movie_html_list:
        info_list = []
        movie_detail_driver.get(movie)
        movie_info = movie_detail_driver.find_element_by_xpath("//div[@class ='title_wrapper']").find_element_by_tag_name("h1").text
        info_list.append(movie_info)
        
        movie_reviewer = movie_detail_driver.find_element_by_css_selector("a[href*='tt_ov_rt']")
        html = movie_reviewer.get_attribute('href')
        ##get id;
        
        movie_detail_driver.get(html)
        specific_rate_number = []
        review_table2 = movie_detail_driver.find_elements_by_xpath("//div[@class ='smallcell']")
        for detail2 in review_table2:
            detail2_text = detail2.text
            specific_rate_number.append(detail2_text)
        
        info_list.extend(specific_rate_number)
        final_list.append(info_list)
with open("test.csv", 'a') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(final_list)

driver.close()
movie_detail_driver.close()


