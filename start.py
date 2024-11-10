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
    They are made as "final" for ease of access in case modifications are 
needed in the future.
'''

URL = "https://www.imdb.com"
SEARCH_PREFIX = "/find/?q="
USER_INPUT = None
SEARCH_SUFIX = "&ref_=nv_sr_sm"
WEBSITE_LIST_CLASS = "ipc-metadata-list-summary-item__t"
DRIVER = webdriver.Firefox()

'''
    In this array the movie links are stored for future use after being scaped 
from the initial search page
'''
searchResultLinks = []

'''
    Here are stored the reviews and the binary values assigned to each one of 
them deppending on the score the user gave them.
    The reviews are stored after being cleaned, ready to insert in the csv file.
'''
cleanedReviews = []

'''
    This is the value that the script will try to match when it comes to review
count.
    The underscore in between the zeros is there to make the numbers more 
ledgeble, python will ignore it when executing.
'''
maxReviews = 10_000

'''
    This method generates a random float and returns it.
    It's used for the time.sleep() command so the page does not detect the same
    sleep time every time.
'''
def randomSleep() -> float:
    return random.uniform(2.0,5.0)
    
'''
    This method is the start of the program, asks the user for an input and then
generates the URL using the "final" URL variables and the user input, after that
it will tell the driver to open the webpage and start the process.
    First it declines the cookies.
    Second it scrapes the movies that match the searched term.
    Third it will iterate trough the movies list links. 
'''
def goToPage():
    userInput = input("\nWhat would you want to scrape today from " + URL + "/")
    print('\n Commencing search for "' + userInput + '".')
    
    site = URL + SEARCH_PREFIX + userInput + SEARCH_SUFIX
    DRIVER.get(site)
    time.sleep(randomSleep())
    declineCookies()
    getAllMovies()
    goToMovies()

'''
    This method locates the decline cookies button, clicks on it and then sleeps
so the page has time to load.
'''
def declineCookies():
    declineCookieButton = "/html/body/div[2]/div/div/div[2]/div/button[1]"
    DRIVER.find_element("xpath", declineCookieButton).click()
    time.sleep(randomSleep())
    
'''
    This method locates the "more movies button" and clicks on it, after that 
it sleeps so the page has time to load the movies. Once that is done it takes 
the movies and combines the movie link with the URL variable, because the page 
doesn't provide a full URL, and it stores them in the searchRelultLinks list.
'''
def getAllMovies():
    moreMovies = "/html/body/div[2]/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/div/span/button"
    moreMoviesButton = DRIVER.find_element("xpath", moreMovies)
    
    DRIVER.execute_script("arguments[0].scrollIntoView(true);", moreMoviesButton)
    time.sleep(randomSleep())
    moreMoviesButton.click()

    time.sleep(randomSleep())
    movieTable = DRIVER.find_elements("class name","find-title-result")

    for movie in movieTable:
        searchResultLinks.append(URL + movie.find_element("class name","ipc-metadata-list-summary-item__t").get_dom_attribute("href"))

'''
    This method iterates trough the list of scraped movie links and opens them
one by one, after that calls the "goToReviews" function to go to the revies 
page.
    If the end of the list or the desited amount of reviews is reached the loop 
breaks.
'''
def goToMovies():
    for link in searchResultLinks:
        if cleanedReviews.__len__() < maxReviews:
            DRIVER.get(link)
            goToReviews()        
        else:
            break

'''
    This method locates and clicks the button that opens the reviews page, if
the button is not in view, mostly do to the page loading elements and shifting 
the button it scrolls back to the button and clicks on it.
    Due to some pages not having enough reviews to warrant a "show all reviews"
button code for locating and clicking said button is encased in a try-except 
block. Inside this block there is also a 4 minute time.sleep() to allow the page
to load all the comments.
    After all reviews are loaded on the screen the showSpoilers() method is 
called.
'''
def goToReviews():
    button = "ipc-title__text"
    showAllReviewsButton = "/html/body/div[2]/main/div/section/div/section/div/div[1]/section[1]/div[3]/div/span[2]/button"
    
    buttons = DRIVER.find_elements("tag name","h3")
    time.sleep(randomSleep())
    
    for button in buttons:
        text=button.text.split("\n")

        if text[0] == "User reviews":
            DRIVER.execute_script("arguments[0].scrollIntoView(true);", button)
            time.sleep(randomSleep())
            
            if button.is_displayed():
                button.click()
                time.sleep(5)

            else:
                DRIVER.execute_script("arguments[0].scrollIntoView(true);", button)
                button.click()
                time.sleep(5)
            
            try:    
                allReviewsButton = DRIVER.find_element("xpath",showAllReviewsButton)
                DRIVER.execute_script("arguments[0].scrollIntoView(true);", allReviewsButton)
                time.sleep(5)
                allReviewsButton.click()
                time.sleep(120)

            except:
                print("All reviews option not available.")
            
            showSpoilers()
            break

'''
    This method locates and clicks on the reviews that contain spoilers in order
to show them, due to the page not loading them otherwise, then calls the method
"getReviews()"
'''
def showSpoilers():
    spoilers = DRIVER.find_elements("class name","review-spoiler-button")

    for spoiler in spoilers:
        DRIVER.execute_script("arguments[0].scrollIntoView(true);", spoiler)
        time.sleep(randomSleep())
        spoiler.click()

    getReviews()
    
'''
    This method locates all the reviews and cleans them using the 
"cleanElements()" method before appending them to the cleaned reviews list.
    Some reviews have no score, due to that the code is placed inside a 
try-except block.
'''
def getReviews():
    
    reviews = DRIVER.find_elements("class name","user-review-item")
    
    for review in reviews:
        tempElem = []
        
        try:
            tempElem.append(review.find_element("class name","review-rating").text)
            tempElem.append(review.find_element("class name","ipc-html-content-inner-div").text)
            cleanedReviews.append(cleanElements(tempElem))
            
            if cleanedReviews:
                print("got " + str(cleanedReviews.__len__()) + " reviews")
        
        except:
            print("review could not be pulled")
        
'''
    This method cleand the text of the reviews, assings binary values to the 
scores and adds quotation marks to the strings. 
'''
def cleanElements(elements):
    cleans = []
    score = elements[0].rsplit()
    text = re.sub("[^A-Za-z0-9' ]+",'',elements[1])
    cleans.append('"' + text + '"')
    
    
    if int(score[0])>5:
        cleans.append('"'+ str(1) +'"')
    
    else:
        cleans.append('"'+ str(0) +'"')    
    
    return cleans

'''
    This method creates a csv file and then appends the reviews with their 
respective binary values to the file.
'''
def writeToCVS():
    with open("reviews/reviews.csv","a+",newline="") as file:
        writer = csv.writer(file)
    
        for row in cleanedReviews:
            writer.writerow(row)
    
    file.close()
    
goToPage()
writeToCVS()
print("The program has pulled " + str(cleanedReviews.__len__()) + " reviews.")
DRIVER.quit()
