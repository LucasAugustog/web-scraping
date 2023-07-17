import sys
import os
from distutils.command.clean import clean
import time
import datetime
from bs4 import BeautifulSoup, element
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from urllib.request import urlopen


data=datetime.datetime.now()

html_content = "https://www.espn.com.br/nba/classificacao"

option = Options()
option.headless = True
driver = webdriver.Firefox() 

driver.get(html_content)
time.sleep(1)

act = ActionChains(driver)
p = 1
l = 0

while l <= p:
    act.send_keys(Keys.PAGE_UP).perform()
    time.sleep(0.1)
    act.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(0.1)
    act.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(0.1)
    l += 1


time.sleep(1)
element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div[3]/div/div[1]/section/div/section/div[2]/div/section/div[1]/div")

html_content = element.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')

driver.quit()


#Name Table
name = soup.find_all('div', class_='Table__Title')

name_str = str(name)
name_clean = name_str.replace('[<div class="Table__Title">','')
name_clean = name_clean.replace('</div>]','')

 

#Name Teams
teams_all = soup.find_all('span', class_='hide-mobile')
teams_str = str(teams_all)

teams_clean = teams_str.replace('<span class="hide-mobile"><a class="AnchorLink" data-clubhouse-uid="s:40~l:46~t:', '')
teams_clean = teams_clean.replace('tabindex="0">', '')
teams_clean = teams_clean.replace('" href="', ' href="')
teams_clean = teams_clean.replace('href="/nba/time/_/nome/', '')
teams_clean = teams_clean.replace('</a></span>, ', '()')
teams_clean = teams_clean.replace('" ', '()')
teams_clean = teams_clean.replace('</a></span>', '')
teams_clean = teams_clean.replace('[', '')
teams_clean = teams_clean.replace(']', '')
teams = teams_clean.split('()')

teams_count = (len(teams))
team_list = []

for x in range(teams_count):
    if(x%2 != 0):
        inserir = teams[x]
        correct_order = len(team_list)
        team_list.insert(correct_order, inserir)
    

#Date
date_all = soup.find_all('span', class_='stat-cell')
date_str = str(date_all)

date_clean = date_str.replace('<span class="stat-cell">', '')
date_clean = date_clean.replace('</span>,', '()')
date_clean = date_clean.replace('</span>', '')
date_clean = date_clean.replace('[', '')
date_clean = date_clean.replace(']', '') 
date_clean = date_clean.replace('<span class="stat-cell clr-positive">', '')
date_clean = date_clean.replace('<span class="stat-cell clr-negative">', '')
date_clean = date_clean.replace(' ', '')
date = date_clean.split('()')

date_count = len(date)

victory_result = []
defeat_result = []
winning_percentage_result = []
games_ago_result = []
game_home_result = []
game_visit_result = []
division_record_result = []
conference_mark_result = []
pts_avg_favor_result = []
pts_avg_against_result = []
pts_balance_result = []
current_seq_result = []
last10_games_campaign = []

y = 0

for y in range(15):

    order = len(victory_result)

    victory_result.insert(order, date[0 + (13 * y)])
    
    defeat_result.insert(order, date[1 + (13 * y)])
    
    winning_percentage_result.insert(order, date[2 + (13 * y)])
    
    games_ago_result.insert(order, date[3 + (13 * y)])
    
    game_home_result.insert(order, date[4 + (13 * y)])
    
    game_visit_result.insert(order, date[5 + (13 * y)])
    
    division_record_result.insert(order, date[6 + (13 * y)])
    
    conference_mark_result.insert(order, date[7 + (13 * y)])
    
    pts_avg_favor_result.insert(order, date[8 + (13 * y)])
    
    pts_avg_against_result.insert(order, date[9 + (13 * y)])
    
    pts_balance_result.insert(order, date[10 + (13 * y)])
    
    current_seq_result.insert(order, date[11 + (13 * y)])

    last10_games_campaign.insert(order, date[12 + (13 * y)])
    


print(name_clean)
print('teams: ', team_list)
print('V: ', victory_result)
print('D: ', defeat_result)
print('% VIT:',winning_percentage_result)
print('GA: ', games_ago_result)
print('HOME: ', game_home_result)
print('VISIT: ', game_visit_result)
print('DIV: ', division_record_result)
print('CONF: ', conference_mark_result)
print('PTS: ', pts_avg_favor_result)
print('PTS AGAINST: ', pts_avg_against_result)
print('DIF: ', pts_balance_result)
print('STRK: ', current_seq_result)
print('U10: ', last10_games_campaign)



