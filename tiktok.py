import os
import sys
fisrt_start = sys.argv[1]
os.system('sudo apt update -y')
os.system('sudo apt install python3-pip -y')
os.system('sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
os.system('sudo apt install ./google-chrome-stable_current_amd64.deb -y')
os.system('pip install selenium')
import subprocess
import sys
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta
import pickle
import requests
from github import Github
def open_browser():
    global driver
    options = Options()
    #options.add_argument('--user-data-dir=sesion')
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)         
    driver.maximize_window()
con = 0
errrrroo = 0
def like3like_login_first():
    for cookies_totel in os.listdir(os.getcwd()):
        cookies_totel_1 = cookies_totel.split('_cookies')[0]
        if cookies_totel_1=='like':
            driver.get("https://www.like4like.org/#social-media-platform-list")
            cookies = pickle.load(open('{}'.format(cookies_totel), "rb"))
            for cookie in cookies:
                try:
                    driver.add_cookie(cookie)
                except Exception as ss:
                    print(ss)
                    continue
            driver.get("https://www.like4like.org/user/")
            time.sleep(10)
            current_url = driver.current_url
            if current_url=='https://www.like4like.org/user/':
                print('login_cookies')
                print('https://www.like4like.org/user/')
            else:
                print('false_cookies')
                email = cookies_totel.split('like_cookies_')[-1].split('.pkl')[0]
                print(email)
                password = '1234thelove'
                driver.get("https://www.like4like.org/login/")
                time.sleep(2)
                driver.get("https://www.like4like.org/login/")
                time.sleep(2)
                page_height = driver.execute_script("return document.body.scrollHeight;")
                driver.set_window_size(1920, page_height)
                time.sleep(2)
                driver.find_element(By.ID, 'username').send_keys(email)
                time.sleep(2)
                driver.find_element(By.ID, 'password').send_keys(password)
                time.sleep(2)
                driver.find_element(By.ID, 'password').send_keys(Keys.ENTER)
                time.sleep(1)
                driver.get("https://www.like4like.org/user/")
                time.sleep(10)
                current_url = driver.current_url
                if current_url=='https://www.like4like.org/user/':
                    print(current_url)
                    driver.get("https://www.like4like.org/#social-media-platform-list")
                    time.sleep(1)
                    cookies_add = "like_cookies_{}.pkl".format(email)
                    pickle.dump(driver.get_cookies(), open("like_cookies_{}.pkl".format(email), "wb"))
                else:
                    print('false_login')
                    print('false_login')
                    print('false_login')
                    break



def check_driver_open():
    try:
        all_windows = driver.window_handles
        if len(all_windows) > 1:
            for window in all_windows[1:]:
                driver.switch_to.window(window)
                driver.close()
            driver.switch_to.window(driver.window_handles[0])
    except Exception as ddfrs:
        print('check_driver_open: ' , ddfrs)
def failed_success_minutes():
    global driver
    try:
        erro_minutes=driver.find_element(By.ID, 'error-text').text
        You_have_failed  = erro_minutes.split(' success rate validation')[0]
        current_url = driver.current_url
        if current_url == 'https://www.like4like.org/user/bonus-page.php' or  current_url == 'https://www.like4like.org/user/bonus-page.php/':
            print('erro_https://www.like4like.org/user/bonus-page.php')
            print('erro_https://www.like4like.org/user/bonus-page.php')
            print('erro_https://www.like4like.org/user/bonus-page.php')
            print('erro_https://www.like4like.org/user/bonus-page.php')
            ##result > div > a:nth-child(8)
            ##result > div > a:nth-child(6)
            
            for a in range(8):
                rand = random.randrange(2,8)
                print(a)
                try:
                    driver.find_element(By.CSS_SELECTOR, "#result > div > a:nth-child({})".format(rand)).click()
                    break
                except:
                    print('errobonus-page.php')
        if You_have_failed == str('You have failed our'):
            print('You have failed our')
            minutes_to_add =  erro_minutes.split('next ')[-1].split(' minutes.')[0]
            print(minutes_to_add)
            current_time = datetime.utcnow()
            time_delta = timedelta(minutes=int(minutes_to_add))
            new_time = current_time + time_delta
            new_date = new_time.date()
            formatted_time = new_time.strftime('%H:%M')
            failed_success= "date:" + str(new_date) + "time:"+ str(formatted_time)
            print(failed_success)
            print('You have failed our')
            print('You have failed our')
            print('You have failed our')          
        if erro_minutes == 'No tasks are currently available, please try again later...':
            print('No tasks are currently available')
    except NoSuchWindowException:
        print('failed_success_minutes')	
    except NoSuchElementException:
        print('NoSuchElementException_failed_success_minutes')
    except Exception as ssssd2:
        print('failed_success_minutes:  ',ssssd2)
def follow_tiktok():
    my_list_like = []
    try:
        with open('unfollowing_tiktok.txt', 'r') as file:
            flowws = file.readlines()
        for addfw in flowws:    
            my_list_like.append(addfw.strip())
    except:
        print('add_list')
    driver.get("https://www.like4like.org/user/earn-tiktok-follow.php")
    page_height = driver.execute_script("return document.body.scrollHeight;")
    driver.set_window_size(1920, page_height)
    con = 0

    for s in range(202):
        try:
            element_control_click = driver.find_element(By.CSS_SELECTOR,"a[class^='cursor earn_pages_button profile_view_img']")
            onclick_value = element_control_click.get_attribute("onclick").split('tiktok.com/')[-1].split("'")[0]
            print(onclick_value)
            if onclick_value in my_list_like:
                driver.find_element(By.CSS_SELECTOR, "a.cursor").click()
                print("skip")
                driver.get("https://www.like4like.org/user/earn-tiktok-follow.php")
                page_height = driver.execute_script("return document.body.scrollHeight;")
                driver.set_window_size(1920, page_height)

            else:
                
                    
                    driver.find_element(By.CSS_SELECTOR, "a[class^='cursor earn_pages_button profile_view_img']").click()
                    my_list_like.append(onclick_value)
                    with open('unfollowing.txt', 'a', encoding='utf-8') as result:
                        result.write("\n")
                        result.write(onclick_value)
                    driver.switch_to.window(driver.window_handles[1])
                    
                    username = onclick_value.split('@')[-1]
                    database_url = 'https://ahmed-3cacf-default-rtdb.firebaseio.com/'
                    users_endpoint = fisrt_start
                    new_user_data = {"name": "mohamed", "email": username}
                    response_put = requests.put(f'{database_url}/{users_endpoint}', json=new_user_data)
                    while True:
                        try:
                            time.sleep(1)
                            response_get = requests.get(f'{database_url}/{users_endpoint}')
                            
                            user_data = response_get.json()
                            email = user_data['email']
                            print(email)
                            if email == 'stop':
                                print('stop')
                                break
                        except:
                            pass
                    time.sleep(4)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(4)
                    driver.find_element(By.CSS_SELECTOR, '[alt="Click On The Button To Confirm Interaction!"]').click()
                    con +=1
                    if int(con) ==int(50):
                        try:
                            con = 0
                            for cookies_totel in os.listdir(os.getcwd()):
                                cookies_totel_1 = cookies_totel.split('_cookies')[0]
                                if cookies_totel_1=='like':
                                    email_mail = cookies_totel.split('like_cookies_')[-1].split('.pkl')[0]
                                    
                                    totel_mail = email_mail.split('_')[-1]
                                    totel_mail_new = int(700)+int(totel_mail) 
                                    print(totel_mail_new)
                                    # Set your GitHub access token
                                    access_token = "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"

                                    # Set the repository name
                                    repository_name = "you{}".format(totel_mail_new)

                                    # Set the local file path (assuming the files are text files)
                                    local_file_path = "unfollowing_tiktok.txt"
                                    #print("Local File Path:", local_file_path)

                                    # Create a connection to the GitHub repository using your access token
                                    g = Github(access_token)

                                    # Find the repository using the username and repository name
                                    repo = g.get_user().get_repo(repository_name)

                                    # Get the current file if it exists
                                    file_path = totel_email
                                    branch = "main"
                                    try:
                                        file = repo.get_contents(file_path, ref=branch)
                                        # Get the current SHA of the file
                                        sha = file.sha
                                    except Exception as e:
                                        # If the file doesn't exist in the repository, set an empty SHA
                                        sha = ""
                                        print("File not found:", e)

                                    # Upload the file to the repository
                                    with open(local_file_path, "rb") as file:
                                        content = file.read()
                                        message = "commit message"
                                        try:
                                            response = repo.update_file(file_path, message, content, sha, branch=branch)
                                            print("Upload Successful:")#, response)
                                        except Exception as ex:
                                            print("Error during upload:", ex)
                                    #print("Repository Name:", repository_name)

                                    #print(email,paswoc)
                                    print('finsh_unfollows')
                                                    
                        except Exception as ex:
                                print("Error:", ex)

                                                                
        except Exception as s:
            print(s)
            failed_success_minutes()
            check_driver_open()
            driver.get("https://www.like4like.org/user/earn-tiktok-follow.php")
            page_height = driver.execute_script("return document.body.scrollHeight;")
            driver.set_window_size(1920, page_height)

open_browser()
like3like_login_first()
follow_tiktok()
