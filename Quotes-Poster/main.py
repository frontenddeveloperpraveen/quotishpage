try:
    import os
    import shutil
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from time import sleep
    from csv import DictReader
    import datetime

    #All dir mentioned is my personal DIR
    
    directory_path = 'C:\\Python\\Quotes-Poster\\Output\\Images\\'

    files = os.listdir(directory_path)
    if files:
        img = files[0]
        print(f"The first file in the directory is: {img}")
    else:
        print("The directory is empty.")

    image_path = os.path.join(directory_path, img)

    print(image_path)

    DIR = 'C:\\Python\\Quotes-Poster\\Output\\Images\\'
    full_path = DIR+img
    print(full_path)

    #logic Start

    def get_cookies_val(file):
        with open(file,encoding='utf-8-sig') as f:
            dict_reader = DictReader(f)
            list_of_dict = list(dict_reader)
        return list_of_dict
    # For no GUI 
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome('C:\Python\Quotes-Poster\chromedriver.exe',options=chrome_options) #ADD option if dont want gui 
    driver.maximize_window()
    driver.get("https://www.instagram.com/")
    #Load Manually
    # username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

    # username_field.send_keys(os.environ.get("USERNAME"))

    # password_field =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

    # password_field.send_keys(os.environ.get("PASSWORD"))

    # button_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')))

    # button_field.click()

    #Load with cookies

    cookies = get_cookies_val("C:/Python/Quotes-Poster/cookie.csv")
    for i in cookies:
        print(i)
        driver.add_cookie(i)
    driver.refresh()
    sleep(10)

    #logic
    driver.get("https://www.instagram.com/quotishpage")
    sleep(7)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@aria-label="New post"]')))

    driver.find_element(By.XPATH,'//*[@aria-label="New post"]').click()
    sleep(2)

    button_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/button')))

    sleep(3)

    num = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/form/input')))
    num.send_keys(full_path)

    sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div').click()

    driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div').click()

    driver.implicitly_wait(5)

    msg = '''Caption Message'''

    driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div').send_keys(msg)
    button = driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div')
    if button.is_displayed:
        button.click()

    print("Post Uploaded successfully")
    sleep(10)
    driver.quit()



    #logic ends


    new_file_path = os.path.join(directory_path, img)
    destination_directory = "C:\\Python\\Quotes-Poster\\Output\\Post\\"

    shutil.move(new_file_path, os.path.join(destination_directory, img + os.path.splitext(img)[1]))

    print("ALL DONE")


    file = open("C:/Python/Quotes-Poster/task.txt",'a')
    file.write(f'{datetime.datetime.now()} - The script ran \n')

except Exception as e:
    print(e)
    file = open("C:/Python/Quotes-Poster/task.txt",'a')
    file.write(f'{datetime.datetime.now()} - Exception Occured\n')
    file.write("    Details\n")
    error = '   '+ str(e) + '\n'
    file.write(error)
    print("Error Logged")