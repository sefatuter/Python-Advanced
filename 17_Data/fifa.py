from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

class Fifa:
    def __init__(self):
        self.browser = webdriver.Chrome()
    
    def getPlayer(self):        
        self.browser.get("https://www.transfermarkt.com/premier-league/torschuetzenliste/wettbewerb/GB1/saison_id/2023")
        time.sleep(4)
        for i in range(1,26):
            players = self.browser.find_element(By.XPATH, f'//*[@id="yw1"]/table/tbody/tr[{i}]/td[2]/table/tbody/tr[1]/td[2]/a')
            country = self.browser.find_element(By.XPATH, f'//*[@id="yw1"]/table/tbody/tr[{i}]/td[3]/img').get_attribute("title")
            score = self.browser.find_element(By.XPATH, f'//*[@id="yw1"]/table/tbody/tr[{i}]/td[7]/a')
            game = self.browser.find_element(By.XPATH, f'//*[@id="yw1"]/table/tbody/tr[{i}]/td[6]/a')
            
            print(f'{i}.Player: ' + players.text)
            print('Score: ' + score.text)
            print('Game: ' + game.text)
            print(country)
           

fifa = Fifa()

fifa.getPlayer()