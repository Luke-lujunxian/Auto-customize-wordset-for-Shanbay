from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass
import datetime


def add_words(word):
    wordInput = browser.find_element_by_id("to_add_vocabulary")
    wordInput.send_keys(word)
    wordInput.send_keys(Keys.ENTER)
    time.sleep(1)
    for i in range(len(word)):
        wordInput.send_keys(Keys.BACKSPACE)



def login():
    browser.get("https://www.shanbay.com/web/account/login/")
    input("请完成登录后按回车")
    browser.get("https://www.shanbay.com/wordbook/create/basicinfo/")
    input_title = browser.find_element_by_id("id_title")
    global bookName
    bookName = "temp"+datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    input_title.send_keys(bookName)
    input_category = browser.find_element_by_id("id_category")
    input_category.send_keys("S")
    input_category.send_keys(Keys.ENTER)
    input_description = browser.find_element_by_id("id_description")
    for i in range(20):
        input_description.send_keys("temp")
        i += 1
    browser.find_element_by_class_name("wordbook-basicinfo-submit-btn").click()
    browser.get("https://www.shanbay.com/wordbook/books/mine/")
    browser.find_element_by_link_text(bookName).click()


def create_Word_Set(lengs):
    browser.get(browser.current_url)
    for i in range(int(lengs/200 + 1)):
        browser.find_element_by_class_name("btn-add-new-unit").click()
        browser.find_element_by_id("id_name").send_keys("Unit ", i)
        browser.find_element_by_class_name("btn-submit-unit-creation").click()
        browser.get(browser.current_url)


def main():
    global browser
    browser = webdriver.Chrome()
    fl = open("Words.txt")
    #global words
    sorted_words = []
    ptrs = []
    words = fl.readlines()
    for i in range(26):
        sorted_words.append([])
        ptrs.append(0)
    for word in words:
        word.lower()
        sorted_words[ord(word[0])-97].append(word)
    login()
    book_page = browser.current_url
    browser.get(book_page)
    create_Word_Set(len(words))
    while len(sorted_words) != 0:
        for i in range(int(len(words)/200 + 1)):
            browser.get(book_page)
            browser.find_element_by_link_text("Unit " + i.__str__()).click()
            browser.get(browser.current_url)
            inputed = 0
            while inputed < 200:
                for j in range(len(sorted_words)-1):
                    for k in range(10):
                        if sorted_words[j].__len__() == 0:
                            sorted_words.remove(sorted_words[j])
                            break
                        add_words(sorted_words[j].pop(0))
                        inputed = int(browser.find_element_by_id("wordlist-num-vocab").text)
                        #inputed += 1
                        k += 1
                    if j >= len(sorted_words)-1 or inputed >= 200:
                        break
                if inputed >= 200:
                    break


if __name__ == '__main__':
    main()

'''
 lptr = 0
    lmptr = int((len(words) - 1) / 2)
    rmptr = int((len(words) - 1) / 2)
    rptr = len(words) - 1
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
'''