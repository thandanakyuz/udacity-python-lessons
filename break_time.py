import time
import webbrowser

num = 0

print ("This program started on " + time.ctime())
while num < 3:
    print ("This video played at " + time.ctime())
    time.sleep(3)
    webbrowser.open("https://youtu.be/tL241A5132k")
    num += 1
