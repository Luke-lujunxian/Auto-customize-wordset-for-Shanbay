from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main():
    fl = open("570.txt")
    browser = webdriver.Chrome()
    browser.get("https://www.shanbay.com")
    print("完成登录后按回车")
    input()
    words = fl.readlines()
    # alert = browser.find_element_by_class_name("alert alert-error")
    wordInput = browser.find_element_by_id("to_add_vocabulary")
    lptr = 0
    lmptr = int((len(words)-1)/2)
    rmptr = int((len(words)-1)/2)
    rptr = len(words)-1
    total = 0
    times = 0
    while lptr != lmptr or rmptr != rptr:
        # total += times
        if total > 200:
            print("请新建单词本")
            input()
            wordInput = browser.find_element_by_id("to_add_vocabulary")
            total = 0
        times = 0
        while times <= 5 and lptr != lmptr:
            wordInput.send_keys(words[lptr])
            lptr += 1
            wordInput.send_keys(Keys.ENTER)
            time.sleep(1)
            i = 0
            while i < 20 and lptr != lmptr:
                wordInput.send_keys(Keys.BACK_SPACE)
                i += 1
            times += 1
            total += 1
        while times <= 10:
            wordInput.send_keys(words[lmptr])
            lmptr -= 1
            wordInput.send_keys(Keys.ENTER)
            time.sleep(1)
            i = 0
            while i < 20:
                wordInput.send_keys(Keys.BACK_SPACE)
                i += 1
            times += 1
            total += 1

        while times <= 15 and rmptr != rptr:
            wordInput.send_keys(words[rmptr])
            rmptr += 1
            wordInput.send_keys(Keys.ENTER)
            time.sleep(1)
            i = 0
            while i < 20:
                wordInput.send_keys(Keys.BACK_SPACE)
                i += 1
            times += 1
            total += 1
        while times <= 20 and rmptr != rptr:
            wordInput.send_keys(words[rptr])
            rptr -= 1
            wordInput.send_keys(Keys.ENTER)
            time.sleep(1)
            i = 0
            while i < 20:
                wordInput.send_keys(Keys.BACK_SPACE)
                i += 1
            times += 1
            total += 1


if __name__ == '__main__':
    main()
