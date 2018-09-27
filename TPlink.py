from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlrd


def main():
    data = xlrd.open_workbook("data.xls")
    sheet = data.sheet_by_index(0)
    x = 6
    y = 1
    i = 0
    name = []
    mac = []
    while True:
        try:
            name.append(sheet.cell(y, x))
            temp = sheet.cell(y, x+1)
            mac.append(temp.value.split("\n"))
            y+=1
        except IndexError:
            break
    print("complected")
    global browser
    browser = webdriver.Chrome()
    browser.get("http://tplogin.cn/webpages/login.html")
    input("Login please~")
    browser.get("http://tplogin.cn/webpages/index.html")
    browser.

    input()
    add = browser.find_element_by_class_name("btn-add")
    macinput = browser.find_element_by_id("add_rule_mac")
    describe = browser.find_element_by_id("add_rule_describe")
    summit = browser.find_element_by_id("btn-submit")
    i = 0
    while i < name.__len__():
        add.click()
        j=0
        while j < mac[i].__len__():
            macinput.send_keys(mac[i][j])
            describe.send_keys(name[i]+j)
            summit.click()


if __name__ == '__main__':
    main()
