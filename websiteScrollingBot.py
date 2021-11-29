import pyautogui, time, PIL
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def scrolling():
    pyautogui.scroll(-200)
    pyautogui.scroll(-200)
    time.sleep(3)

    pyautogui.scroll(-200)
    pyautogui.scroll(-200)
    pyautogui.scroll(-200)
    pyautogui.scroll(-150)
    time.sleep(17)

    pyautogui.scroll(-200)
    pyautogui.scroll(-200)
    time.sleep(13)

    if pyautogui.locateCenterOnScreen(r"share.png"):
        time.sleep(2)
        return
    else:
        pyautogui.scroll(-200)
        pyautogui.scroll(-200)
        time.sleep(7)
        return


def desh():
    c, d = pyautogui.locateCenterOnScreen(r"desh.png")
    pyautogui.doubleClick(c, d)
    time.sleep(3)

# scroll down multiple clicks & click on 1st news that appears in Desh Category
    pyautogui.scroll(-200)
    pyautogui.scroll(-200)
    if not pyautogui.locateCenterOnScreen(r"read-more.png"):
        time.sleep(2)
        pyautogui.scroll(-200)
    else:
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)

    pyautogui.press('esc')
    time.sleep(2)
    return


def videsh():
    pyautogui.hotkey('alt', 'left')
    time.sleep(2)

    # Scroll up multiple clicks  &  click on videsh category
    pyautogui.scroll(300)
    pyautogui.scroll(300)
    pyautogui.scroll(200)
    time.sleep(1)

    a, b = pyautogui.locateCenterOnScreen(r"videsh.png")
    pyautogui.doubleClick(a, b)
    time.sleep(3)

    # Now, scroll down & click 1st news that appears in videsh Category
    pyautogui.scroll(-300)
    if not pyautogui.locateCenterOnScreen(r"read-more.png"):
        time.sleep(2)
        pyautogui.scroll(-200)
    else:
        pass
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)
    return


def karobaar():
    pyautogui.hotkey('alt', 'left')
    time.sleep(2)

    # Scroll up multiple clicks  &  click on karobaar category
    pyautogui.scroll(300)
    pyautogui.scroll(300)
    pyautogui.scroll(200)
    time.sleep(1)

    a, b = pyautogui.locateCenterOnScreen(r"karobaar.png")
    pyautogui.doubleClick(a, b)
    time.sleep(3)

    # Now, scroll down & click 1st news that appears in karobaar Category
    pyautogui.scroll(-300)
    if not pyautogui.locateCenterOnScreen(r"read-more.png"):
        time.sleep(2)
        pyautogui.scroll(-200)
    else:
        pass
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)
    return


def khel():
    pyautogui.hotkey('alt', 'left')
    time.sleep(2)

    # Scroll up multiple clicks  &  click on khel category
    pyautogui.scroll(300)
    pyautogui.scroll(300)
    pyautogui.scroll(250)
    time.sleep(1)

    a, b = pyautogui.locateCenterOnScreen(r"khel.png")
    pyautogui.doubleClick(a, b)
    time.sleep(3)

    # Now, scroll down & click 1st news that appears in khel Category
    pyautogui.scroll(-300)
    if not pyautogui.locateCenterOnScreen(r"read-more.png"):
        time.sleep(2)
        pyautogui.scroll(-200)
    else:
        pass
    time.sleep(1)
    c, d = pyautogui.locateCenterOnScreen(r"read-more.png")
    time.sleep(1)
    pyautogui.click(c, d)
    time.sleep(2)
    return


def manoranjan():
    pyautogui.hotkey('alt', 'left')
    time.sleep(2)

    # Scroll up multiple clicks  &  click on manoranjan category
    pyautogui.scroll(300)
    pyautogui.scroll(300)
    pyautogui.scroll(250)
    time.sleep(1)

    a, b = pyautogui.locateCenterOnScreen(r"manoranjan.png")
    pyautogui.doubleClick(a, b)
    time.sleep(3)

    # Now, scroll down & click 1st news that appears in manoranjan Category
    pyautogui.scroll(-300)
    if not pyautogui.locateCenterOnScreen(r"read-more.png"):
        time.sleep(2)
        pyautogui.scroll(-200)
    else:
        pass
    time.sleep(1)
    c, d = pyautogui.locateCenterOnScreen(r"read-more.png")
    time.sleep(1)
    pyautogui.click(c, d)
    time.sleep(2)
    return


def sahitya():
    pyautogui.hotkey('alt', 'left')
    time.sleep(2)

    # Scroll up multiple clicks  &  click on sahitya category
    pyautogui.scroll(300)
    pyautogui.scroll(300)
    pyautogui.scroll(250)
    time.sleep(1)

    a, b = pyautogui.locateCenterOnScreen(r"sahitya.png")
    pyautogui.doubleClick(a, b)
    time.sleep(3)

    # Now, scroll down & click 1st news that appears in sahitya Category
    pyautogui.scroll(-300)
    if not pyautogui.locateCenterOnScreen(r"read-more.png"):
        time.sleep(2)
        pyautogui.scroll(-200)
    else:
        pass
    time.sleep(1)
    c, d = pyautogui.locateCenterOnScreen(r"read-more.png")
    time.sleep(1)
    pyautogui.click(c, d)
    time.sleep(2)
    return


def nirogi():
    pyautogui.hotkey('alt', 'left')
    time.sleep(2)

    # Scroll up multiple clicks  &  click on nirogi category
    pyautogui.scroll(300)
    pyautogui.scroll(300)
    pyautogui.scroll(250)
    time.sleep(1)

    a, b = pyautogui.locateCenterOnScreen(r"nirogi.png")
    pyautogui.doubleClick(a, b)
    time.sleep(3)

    # Now, scroll down & click 1st news that appears in nirogi Category
    pyautogui.scroll(-300)
    if not pyautogui.locateCenterOnScreen(r"read-more.png"):
        time.sleep(2)
        pyautogui.scroll(-200)
    else:
        pass
    time.sleep(1)
    c, d = pyautogui.locateCenterOnScreen(r"read-more.png")
    time.sleep(1)
    pyautogui.click(c, d)
    time.sleep(2)
    return


def dharm():
    pyautogui.hotkey('alt', 'left')
    time.sleep(2)

    # Scroll up multiple clicks  &  click on dharm category
    pyautogui.scroll(300)
    pyautogui.scroll(300)
    pyautogui.scroll(250)
    time.sleep(1)

    a, b = pyautogui.locateCenterOnScreen(r"dharm.png")
    pyautogui.doubleClick(a, b)
    time.sleep(3)

    # Now, scroll down & click 1st news that appears in dharm Category
    pyautogui.scroll(-300)
    if not pyautogui.locateCenterOnScreen(r"read-more.png"):
        time.sleep(2)
        pyautogui.scroll(-200)
    else:
        pass
    time.sleep(1)
    c, d = pyautogui.locateCenterOnScreen(r"read-more.png")
    time.sleep(1)
    pyautogui.click(c, d)
    time.sleep(2)
    return


def rashiphal():
    pyautogui.hotkey('alt', 'left')
    time.sleep(2)

    # Scroll up multiple clicks  &  click on rashiphal category
    pyautogui.scroll(300)
    pyautogui.scroll(300)
    pyautogui.scroll(250)
    time.sleep(1)

    a, b = pyautogui.locateCenterOnScreen(r"rashiphal.png")
    pyautogui.doubleClick(a, b)
    time.sleep(3)

    # Now, scroll down & click 1st news that appears in rashiphal Category
    pyautogui.scroll(-300)
    if not pyautogui.locateCenterOnScreen(r"read-more.png"):
        time.sleep(2)
        pyautogui.scroll(-200)
    else:
        pass
    time.sleep(1)
    c, d = pyautogui.locateCenterOnScreen(r"read-more.png")
    time.sleep(1)
    pyautogui.click(c, d)
    time.sleep(2)
    return


def xtra_scroll():
    pyautogui.scroll(-200)
    pyautogui.scroll(-200)
    pyautogui.scroll(-200)
    time.sleep(4)

    pyautogui.scroll(-200)
    pyautogui.scroll(-200)
    pyautogui.scroll(-200)
    time.sleep(4)
    if pyautogui.locateCenterOnScreen(r"share.png"):
        time.sleep(2)
        return
    else:
        pyautogui.scroll(-200)
        pyautogui.scroll(-200)
        time.sleep(4)

        pyautogui.scroll(-200)
        pyautogui.scroll(-200)
        time.sleep(4)
        return
    return


pyautogui.PAUSE=1
pyautogui.FAILSAFE=False


pyautogui.hotkey("win", "m")

serve = Service("chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serve)
time.sleep(2)

driver.maximize_window()
time.sleep(1)

driver.get("https://amritvichar.com/")
time.sleep(6)


# move the mouse pointer to 'not now' option for notifications & click
a, b = pyautogui.locateCenterOnScreen(r"not-now.png")
time.sleep(1)
pyautogui.click(a, b)
time.sleep(1)



####### Moving to category 1(Desh) #######



desh()
time.sleep(1)

scrolling()
time.sleep(1)

if pyautogui.locateCenterOnScreen(r"share.png"):
    time.sleep(1)
    pass
else:
    xtra_scroll()
time.sleep(1)



####### Moving to category 2(videsh) ########



videsh()
time.sleep(1)

scrolling()
time.sleep(1)

if pyautogui.locateCenterOnScreen(r"share.png"):
    time.sleep(1)
    pass
else:
    xtra_scroll()
time.sleep(1)



####### Moving to category 3(karobaar) ########



karobaar()
time.sleep(1)

scrolling()
time.sleep(1)

if pyautogui.locateCenterOnScreen(r"share.png"):
    time.sleep(1)
    pass
else:
    xtra_scroll()
time.sleep(1)



####### Moving to category 4(khel) ########



khel()
time.sleep(1)

scrolling()
time.sleep(1)

if pyautogui.locateCenterOnScreen(r"share.png"):
    time.sleep(1)
    pass
else:
    xtra_scroll()
time.sleep(1)



####### Moving to category 5(manoranjan) ########



manoranjan()
time.sleep(1)

scrolling()
time.sleep(1)

if pyautogui.locateCenterOnScreen(r"share.png"):
    time.sleep(1)
    pass
else:
    xtra_scroll()
time.sleep(1)



####### Moving to category 6(sahitya) ########



sahitya()
time.sleep(1)

scrolling()
time.sleep(1)

if pyautogui.locateCenterOnScreen(r"share.png"):
    time.sleep(1)
    pass
else:
    xtra_scroll()
time.sleep(1)



####### Moving to category 7(nirogi) ########



nirogi()
time.sleep(1)

scrolling()
time.sleep(1)

if pyautogui.locateCenterOnScreen(r"share.png"):
    time.sleep(1)
    pass
else:
    xtra_scroll()
time.sleep(1)



####### Moving to category 8(dharm) ########



dharm()
time.sleep(1)

scrolling()
time.sleep(1)

if pyautogui.locateCenterOnScreen(r"share.png"):
    time.sleep(1)
    pass
else:
    xtra_scroll()
time.sleep(1)



####### Moving to category 9(rashiphal) ########



rashiphal()
time.sleep(1)

scrolling()
time.sleep(1)

if pyautogui.locateCenterOnScreen(r"share.png"):
    time.sleep(1)
    pass
else:
    xtra_scroll()
time.sleep(1)



