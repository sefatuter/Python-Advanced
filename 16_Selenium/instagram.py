from instagramUserInfo import username, password
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

class Instagram:
    
    def __init__(self):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome(options=self.browserProfile)
        self.username = username
        self.password = password
        
    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(2)
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        time.sleep(1)
        
        self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
        time.sleep(5)

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}/followers/")
        time.sleep(2)
        dialog = self.browser.find_element(By.CSS_SELECTOR, "div[role=dialog]").find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div')
        followerCount = len(dialog.find_elements(By.CLASS_NAME, 'x1dm5mii'))
        
        print(f"First count: {followerCount}")
        
        
        action = webdriver.ActionChains(self.browser)    
        action.send_keys(Keys.TAB).perform()
        time.sleep(2)
        action.send_keys(Keys.TAB).perform()
        time.sleep(2)
        action.send_keys(Keys.TAB).perform()
        time.sleep(2)
        while True:
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)
            
            newCount = len(dialog.find_elements(By.CLASS_NAME, 'x1dm5mii'))
            
            if followerCount != newCount:
                followerCount = newCount
                print(f'Updated count: {newCount}')
                time.sleep(3)
            else:
                break    
        
        followers = dialog.find_elements(By.CLASS_NAME, 'x1dm5mii')
        time.sleep(2)
        
        followerList = []
        for user in followers:
            link = user.find_element(By.CSS_SELECTOR, 'a').get_attribute("href")
            followerList.append(link)
        
        with open("followers.txt", "w", encoding='UTF-8') as file:
            for item in followerList:
                file.write(item + '\n')
        
    def followUser(self, username):
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)
        followButton = self.browser.find_element(By.TAG_NAME, "button")
        # print(followButton.text) # Hangi butonu aldığının kontrolü
        if followButton.text != "Following":
            followButton.click()
            time.sleep(2)
        else:
            print('Already Following.')
            time.sleep(1)
            
    def unfollowUser(self, username):
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)
        followButton = self.browser.find_element(By.TAG_NAME, "button")
        if followButton.text == "Following":
            followButton.click()
            time.sleep(2)
            self.browser.find_element(By.XPATH, '//button[text()="Unfollow"]').click()
        else:
            print('You are already not Following.')
            time.sleep(1)
        
     
insta = Instagram()

insta.signIn()
insta.getFollowers()
#insta.followUser("patika.dev")
#insta.unfollowUser("patika.dev")