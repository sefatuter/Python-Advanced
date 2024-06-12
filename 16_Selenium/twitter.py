from twitterUserInfo import username, password
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time



class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.FirefoxOptions()
        opt = self.browserProfile.set_preference('prefs', {'intl.accept_languages':'en,en_US'}) # Sadece ingilizce olarak profil oluşturduk
        self.browser = webdriver.Firefox(options=opt)
        self.username = username
        self.password = password
        
        
    def signIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(2)
        usernameInput = self.browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(self.username)
        time.sleep(2)
        buttonSubmit = self.browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        buttonSubmit.click()
        time.sleep(2)
        passwordInput = self.browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(self.password)
        time.sleep(2)
        buttonSubmit = self.browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        buttonSubmit.click()
        time.sleep(15)
        
    def search(self, hashtag):
        searchInput = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
        searchInput.send_keys(hashtag)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)
        
        result = []
        
        liste = self.browser.find_elements(By.XPATH, "//div[@data-testid = 'tweetText']")
        time.sleep(2)
        print('Count: ' + str(len(liste)))
        
        for i in liste:
            result.append(i.text)
        
        
        # using scroll (JS)        
        loopCounter = 0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopCounter > 4:
                break
            self.browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loopCounter += 1
            
            liste2 = self.browser.find_elements(By.XPATH, "//div[@data-testid = 'tweetText']")
            time.sleep(2)
            print('Count: ' + str(len(liste2)))
            
            for i in liste2:
                result.append(i.text)
            
        count = 1      
        for item in result:
            print(f"{count}-{item}")
            count +=1
            print("-----------------")

        count = 1
        with open("tweets.txt", "w", encoding= "UTF-8") as file:
            for item in result:
                file.write(f"{count}- {item} \n")
                count += 1

twitter = Twitter(username, password)
twitter.signIn()
twitter.search("python")