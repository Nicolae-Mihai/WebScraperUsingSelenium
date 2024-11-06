# This is the script file
from selenium import webdriver
import time
import re
import random
import csv
'''
    All this variables go together in order to create the search link and then
the URL is reused to search for the titles.
    The variables go together like this: 
     URL + searchPrefix + userInput + searchSufix
    or like this:
     URL + searchResultLinks[i]
'''
URL="https://www.imdb.com/"
SEARCH_PREFIX="find/?q="
USER_INPUT=None
SEARCH_SUFIX="&ref_=nv_sr_sm"
WEBSITE_LIST_CLASS="ipc-metadata-list-summary-item__t"
cleanedReviews=[]

def randomSleep() -> float:
    return random.uniform(2.0,5.0)

def showSpoilers():
    spoilers=driver.find_elements("class name","review-spoiler-button")

    for spoiler in spoilers:
        driver.execute_script("arguments[0].scrollIntoView(true);", spoiler)
        time.sleep(randomSleep())
        spoiler.click()
    
def getReviews():
    reviews=driver.find_elements("class name","user-review-item")
    
    for review in reviews:
        tempElem=[]
        driver.execute_script("arguments[0].scrollIntoView(true);", review)
        try:
            tempElem.append(review.find_element("class name","review-rating").text)
            tempElem.append(review.find_element("class name","ipc-html-content-inner-div").text)
            cleanedReviews.append(cleanElements(tempElem))
        except:
            pass
        time.sleep(randomSleep())

def cleanElements(elements):
    cleans = []
    score = elements[0].rsplit()
    cleans.append(score[0])
    cleans.append(re.sub('[^A-Za-z0-9.!? ]+','',elements[1]))
    return cleans

def writeToCVS():
    with open("reviews/reviews.cvs","+a",encoding="UTF8") as file:
        writer=csv.write(file)
        for row in cleanedReviews:
            writer.writerow(row)
    file.close()

moreMovies="/html/body/div[2]/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/div/span/button"
declineCookieButton="/html/body/div[2]/div/div/div[2]/div/button[1]"
reviewsButton="/html/body/div[2]/main/div/section[1]/div/section/div/div[1]/section[8]/div/div/a/h3"
showAllReviewsButton="/html/body/div[2]/main/div/section/div/section/div/div[1]/section[1]/div[3]/div/span[2]/button"
driver=webdriver.Firefox()

# Array in which the list elements are stored
# searchResultLinks=[]

# USER_INPUT=input("\nWhat would you want to scrape today from " + URL+SEARCH_PREFIX)
# print('\n Commencing search for "' + USER_INPUT + '".')

# site=URL+SEARCH_PREFIX+USER_INPUT+SEARCH_SUFIX
site="https://www.imdb.com/title/tt11315808/?ref_=fn_al_tt_1"
driver.get(site)
time.sleep(randomSleep())


# this part of the code gets all the movies shown on the front page after 
# clicking more movies button it also declines cookies

driver.find_element("xpath", declineCookieButton).click()
time.sleep(randomSleep())

# driver.find_element("xpath", moreMovies).click()

# titlesXPath="/html/body/div[2]/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/ul"

# time.sleep(randomSleep())
# movieTable = driver.find_elements("class name","find-title-result")

# for movie in movieTable:
#     searchResultLinks.append(URL + movie.find_element("class name","ipc-metadata-list-summary-item__t").get_dom_attribute("href"))
# driver.execute_script('window.scrollTo(0,driver.find_element("xpath",reviewsButton) .offsetTop)')
reviews = driver.find_element("xpath",reviewsButton)
driver.execute_script("arguments[0].scrollIntoView(true);", reviews)
time.sleep(randomSleep())
reviews.click()

allReviewsButton = driver.find_element("xpath",showAllReviewsButton)
driver.execute_script("arguments[0].scrollIntoView(true);", allReviewsButton)
time.sleep(5)

allReviewsButton.click()
# time.sleep(120)

showSpoilers()

getReviews()
print("")
# time.sleep(randomSleep())


# driver.get(searchResultLinks[0])
# driver.quit()
