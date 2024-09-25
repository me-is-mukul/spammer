import pyautogui
x=0
a = input("enter message to spam : ")
while True:
    pyautogui.typewrite("{} {}".format(a ,x))
    pyautogui.press("enter")
    x+=1
