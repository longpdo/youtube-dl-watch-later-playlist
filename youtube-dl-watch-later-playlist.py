from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from termcolor import colored
import getpass
import subprocess

# CREDITS: https://gist.github.com/ikegami-yukino/51b247080976cb41fe93#gistcomment-3181443
download_folder = '~/Downloads/'


def get_google_username():
    return input('ᕙ(⇀‸↼‶)ᕗ Enter your google username: ')


def get_google_password():
    return getpass.getpass('ᕙ(⇀‸↼‶)ᕗ Enter your google password: ')


def start_browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-plugins-discovery")
    chrome_options.add_argument("--incognito")
    return webdriver.Chrome(options=chrome_options)


def login_to_google(driver, username, password):
    driver.get("https://stackoverflow.com/users/signup")
    driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()

    verify_username(username)
    verify_password(password)

    # Waits until redirect to stackoverflow.com occurs
    wait = WebDriverWait(driver, 60)
    wait.until(EC.url_contains("stackoverflow.com"))
    print(colored('Login successful.', 'green'))


def verify_username(username):
    login_field = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, 'identifierId'))
    )
    while True:
        # Enters username and clicks next button
        login_field.send_keys(username)
        driver.find_element_by_id('identifierNext').click()

        try:
            # Checks for invalid username warning
            warning = WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[2]/div[2]'))
            )
            if warning:
                print(colored('Warning! Google Account not found.', 'red'))
                username = get_google_username()
                login_field.clear()
                continue
        except(TimeoutException):
            print(colored('Username verified.', 'green'))
            break


def verify_password(password):
    password_field = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="password"]'))
    )
    while True:
        # Enters password and clicks next button
        password_field.send_keys(password)
        driver.find_element_by_id('passwordNext').click()

        try:
            # Checks for invalid password warning
            warning = WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[2]'))
            )
            if warning:
                print(colored('Warning! Wrong password.', 'red'))
                password = get_google_password()
                continue
        except(TimeoutException):
            print(colored('Password verified.', 'green'))
            break


def scrape_watch_later_playlist(driver):
    driver.get("https://www.youtube.com/playlist?list=WL")
    videos = WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="content"]/a'))
    )
    urls = []

    for video in videos:
        url = video.get_attribute('href')
        url = url.split('&list=WL&index=')
        url = url[0]
        urls.append(url)
    return urls


def run_terminal_cmd(cmd):
    process = subprocess.run(cmd, shell=True)
    if process.returncode != 0:
        print(colored('Error running cmd!', 'red'))
        return
    else:
        return process.stdout


if __name__ == '__main__':
    print('ᕙ(⇀‸↼‶)ᕗ starting download script for youtube watch later playlist.')
    username = get_google_username()
    password = get_google_password()

    driver = start_browser()
    login_to_google(driver, username, password)
    videos = scrape_watch_later_playlist(driver)

    for video in videos:
        prefix = "youtube-dl -i -c "
        output = "-o '" + download_folder + "%(title)s.%(ext)s' "
        quality = "-f 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]' "
        cmd = prefix + output + quality + video
        run_terminal_cmd(cmd)
