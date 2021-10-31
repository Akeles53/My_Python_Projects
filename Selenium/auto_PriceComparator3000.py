from selenium import webdriver
import time

def Hepsiburada(keywords):
    browser.get("https://www.hepsiburada.com/")
    time.sleep(1)

    search_hb = browser.find_element_by_xpath("//*[@id='SearchBoxOld']/div/div/div[1]/div[2]/input")
    search_hb.send_keys(keywords)

    search_button_hb = browser.find_element_by_xpath("//*[@id='SearchBoxOld']/div/div/div[2]")
    search_button_hb.click()

    titles_text = []
    prices_text = []
    flag = 0
    while flag <3:
        titles_hb = browser.find_elements_by_css_selector(".product-title.title")
        time.sleep(1)
        titles_text.append(titles_hb[flag].text)
        titles_hb = browser.find_elements_by_css_selector(".product-title.title")
        titles_hb[int(flag)].click()
        price_hb = browser.find_element_by_xpath("//*[@id='offering-price']/span[1]")
        prices_text.append(price_hb.text)
        print("{} = {} TL".format(titles_text[flag],price_hb.text))

        time.sleep(1)
        browser.back()
        flag +=1

    return titles_text,prices_text

def Trendyol(keywords):
    browser.get("https://www.trendyol.com/")
    time.sleep(1)
    try:
        close_ty = browser.find_element_by_xpath("/html/body/div[1]/div[5]/div/div/div/div/div[1]")
        close_ty.click()
    except:
        print("\n")

    search_ty = browser.find_element_by_xpath("//*[@id='auto-complete-app']/div/div/input")
    search_ty.send_keys(keywords)
    time.sleep(1)
    search_button_ty = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/i")
    search_button_ty.click()
    time.sleep(1)
    try:
        overlay_ty = browser.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div/div[1]/div[2]/div[2]/div/div[1]/div/a/div[1]/div[2]/div[3]/div[1]")
        overlay_ty.click()
    except:
        z= 3
    time.sleep(1)
    prices_text = []
    titles_text = []
    flag =0
    while flag <4:

        titles_ty = browser.find_elements_by_css_selector(".prdct-desc-cntnr-name.hasRatings")
        titles_text.append(titles_ty[flag].text)
        titles_ty[flag].click()
        time.sleep(1)
        browser.switch_to.window(browser.window_handles[1])
        prices_ty = browser.find_element_by_css_selector(".product-price-container")
        prices_text.append(prices_ty.text)
        browser.close()
        browser.switch_to.window(browser.window_handles[0])

        flag +=1
    for i in range(0,3):
        print("{} = {}".format(titles_text[i],prices_text[i]))
        print("\n")

keywords = str(input("Lütfen aramak istediğiniz ürünü yazınız :"))
browser = webdriver.Firefox()

Hepsiburada(keywords)
Trendyol(keywords)

time.sleep(2)



