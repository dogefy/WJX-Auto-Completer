import time
import pyautogui
from random import *
from selenium import webdriver
from selenium.webdriver import EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def one_run():
    q1 = random()
    if 0 <= q1 <= 0.2:
        driver.find_element(By.XPATH, "//a[@rel='q1_1']").click()
    elif 0.2 < q1 <= 0.7:
        driver.find_element(By.XPATH, "//a[@rel='q1_2']").click()
    else:
        driver.find_element(By.XPATH, "//a[@rel='q1_3']").click()
    time.sleep(0.5)

    q2 = random()
    if 0 <= q2 <= 0.20:
        driver.find_element(By.XPATH, "//a[@rel='q2_1']").click()
        driver.find_element(By.XPATH, "//a[@rel='q2_2']").click()
        driver.find_element(By.XPATH, "//a[@rel='q2_3']").click()
        driver.find_element(By.XPATH, "//a[@rel='q2_4']").click()
    elif 0.20 < q2 <= 0.40:
        driver.find_element(By.XPATH, "//a[@rel='q2_1']").click()
        driver.find_element(By.XPATH, "//a[@rel='q2_2']").click()
        driver.find_element(By.XPATH, "//a[@rel='q2_3']").click()
        driver.find_element(By.XPATH, "//a[@rel='q2_5']").click()
    elif 0.20 < q2 <= 0.40:
        driver.find_element(By.XPATH, "//a[@rel='q2_1']").click()
        driver.find_element(By.XPATH, "//a[@rel='q2_2']").click()
        driver.find_element(By.XPATH, "//a[@rel='q2_4']").click()
        driver.find_element(By.XPATH, "//a[@rel='q2_5']").click()
    elif 0.20 < q2 <= 0.40:
        driver.find_element(By.XPATH, "//a[@rel='q2_1']").click()
        driver.find_element(By.XPATH, "//a[@rel='q2_3']").click()
        driver.find_element(By.XPATH, "//a[@rel='q2_4']").click()
        driver.find_element(By.XPATH, "//a[@rel='q2_5']").click()
    else:
        driver.find_element(By.XPATH, "//a[@rel='q2_1']").click()
        driver.find_element(By.XPATH, "//a[@rel='q2_2']").click()
        driver.find_element(By.XPATH, "//a[@rel='q2_3']").click()
        driver.find_element(By.XPATH, "//a[@rel='q2_4']").click()
        driver.find_element(By.XPATH, "//a[@rel='q2_5']").click()

    q3 = random()
    if 0 <= q3 <= 0.20:
        driver.find_element(By.XPATH, "//a[@rel='q3_1']").click()
        driver.find_element(By.XPATH, "//a[@rel='q3_2']").click()
        driver.find_element(By.XPATH, "//a[@rel='q3_3']").click()
        driver.find_element(By.XPATH, "//a[@rel='q3_4']").click()
    elif 0.20 < q3 <= 0.40:
        driver.find_element(By.XPATH, "//a[@rel='q3_1']").click()
        driver.find_element(By.XPATH, "//a[@rel='q3_2']").click()
        driver.find_element(By.XPATH, "//a[@rel='q3_3']").click()
        driver.find_element(By.XPATH, "//a[@rel='q3_5']").click()
    elif 0.20 < q3 <= 0.40:
        driver.find_element(By.XPATH, "//a[@rel='q3_1']").click()
        driver.find_element(By.XPATH, "//a[@rel='q3_2']").click()
        driver.find_element(By.XPATH, "//a[@rel='q3_4']").click()
        driver.find_element(By.XPATH, "//a[@rel='q3_5']").click()
    elif 0.20 < q3 <= 0.40:
        driver.find_element(By.XPATH, "//a[@rel='q3_1']").click()
        driver.find_element(By.XPATH, "//a[@rel='q3_3']").click()
        driver.find_element(By.XPATH, "//a[@rel='q3_4']").click()
        driver.find_element(By.XPATH, "//a[@rel='q3_5']").click()
    else:
        driver.find_element(By.XPATH, "//a[@rel='q3_1']").click()
        driver.find_element(By.XPATH, "//a[@rel='q3_2']").click()
        driver.find_element(By.XPATH, "//a[@rel='q3_3']").click()
        driver.find_element(By.XPATH, "//a[@rel='q3_4']").click()
        driver.find_element(By.XPATH, "//a[@rel='q3_5']").click()

    q4 = random()
    if 0 <= q4 <= 0.4:
        driver.find_element(By.XPATH, "//a[@rel='q4_1']").click()
    else:
        driver.find_element(By.XPATH, "//a[@rel='q4_2']").click()
    time.sleep(0.5)

    q5 = random()
    if 0 <= q5 <= 0.20:
        driver.find_element(By.XPATH, "//a[@rel='q5_1']").click()
        driver.find_element(By.XPATH, "//a[@rel='q5_3']").click()
    elif 0.20 < q5 <= 0.40:
        driver.find_element(By.XPATH, "//a[@rel='q5_5']").click()
    elif 0.20 < q5 <= 0.40:
        pass
    elif 0.40 < q5 <= 0.60:
        driver.find_element(By.XPATH, "//a[@rel='q5_2']").click()
    elif 0.60 < q5 <= 0.80:
        driver.find_element(By.XPATH, "//a[@rel='q5_4']").click()

    q6 = random()
    if 0 <= q6 <= 0.4:
        driver.find_element(By.XPATH, "//a[@rel='q6_1']").click()
    else:
        driver.find_element(By.XPATH, "//a[@rel='q6_2']").click()
    time.sleep(0.5)

    q7 = random()
    if 0 <= q7 <= 0.50:
        driver.find_element(By.XPATH, "//a[@rel='q7_1']").click()
    elif 0.50 < q7 <= 0.90:
        driver.find_element(By.XPATH, "//a[@rel='q7_2']").click()
    else:
        driver.find_element(By.XPATH, "//a[@rel='q7_3']").click()
    time.sleep(0.5)

    driver.find_element(By.XPATH, "//input[@value='提交']").click()
    time.sleep(0.5)

    try:
        driver.find_element(By.XPATH, "//button[text()='确认']").click()
        driver.find_element(By.XPATH, "//div[@id='captcha']").click()
    except:
        pass
    time.sleep(2)
    # 滑块条形码需重新设置
    pyautogui.moveTo(805, 1005, duration=1)
    time.sleep(0.5)
    pyautogui.dragRel(370, 0, duration=0.8)
    time.sleep(5)


if __name__ == '__main__':
    print('开始')
    options = EdgeOptions()
    # options.add_argument(('--proxy-server=http://112.80.248.73:80')) #代理设置
    url_survey = 'https://www.wjx.cn/vj/******.aspx'  # 问卷URL
    s = Service(executable_path=r'')  # msedgedriver.exe位置
    driver = webdriver.Edge(service=s, options=options)
    #绕过智能检测
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                           {
                               'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
    driver.maximize_window()  # 最大化窗口以拖动滑块
    for i in range(1000):
        driver.get(url_survey)
        time.sleep(2)
        one_run()
        print("完成" + str(i))
