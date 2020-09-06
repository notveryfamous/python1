from urllib import request
import os
import webbrowser

url = 'http://www.baidu.com'
data = request.urlopen(url).read()
print(data.decode())

os.system('C:/Users/Administrator/AppData/Local/Microsoft/Edge SxS/Application/msedge.exe')
os.rename(r'C:\Users\Administrator\Desktop\666.txt', r'C:\Users\Administrator\Desktop\555.txt')
webbrowser.open(url)
