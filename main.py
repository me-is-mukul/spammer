import pyautogui
x=1
a = input("enter message to spam : ")
b = int(input("enter amount of messages : "))
c = int(input("press 0 if dont want nummbers at end\npress 1 if want numbers at end\n>>>"))
if c==1:
    while x<=b:
        pyautogui.typewrite("{} {}".format(a ,x))
        pyautogui.press("enter")
        x+=1
elif c==0:
    while x<=b:
        pyautogui.typewrite("{}".format(a))
        pyautogui.press("enter")
        x+=1
