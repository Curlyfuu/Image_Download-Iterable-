
from tkinter import *
import threading
from urllib.request import Request, urlopen, urlretrieve
from urllib.error import URLError, HTTPError
import os
import re
window=Tk()
window.title('图片批量下载')
window.geometry('700x300')

# urlfront='https://t1.onvshen.com:85/gallery/21501/23542/'
def img_save():
	urlfront=var_urlfront.get()
	urlfront=re.findall('(.*?)0\d*\d*.jpg',urlfront)[0]
	print(urlfront)
	path_dir=var_path.get()
	a=[]
	a.append(urlfront+'0.jpg')
	for i in range(1,10):
		a.append(urlfront+'00'+str(i)+'.jpg')
	for i in range(10,100):

		a.append(urlfront+'0'+str(i)+'.jpg')
	x= 0
	# path_dir='imgsave2'
	os.mkdir(path_dir)
	for imgurl in a:
		req = Request(imgurl)
		try:
			response = urlopen(req)
		except HTTPError as e:
			break
		except URLError as e:
			break
		else:

			urlretrieve(imgurl,path_dir+'/%s.jpg' % str(x+1),encoding='UTF-8')
			print(str(x+1))
			x+=1
			l.config(text='正在下载第%s张图片'% str(x))
			window.update_idletasks()

	l.config(text='共%d张图片\n已经保存在%s/下' % (x,path_dir))

var_urlfront = StringVar()
var_urlfront.set('https://t1.onvshen.com:85/gallery/21501/23542/002.jpg')
var_path = StringVar()
var_path.set('DonwoadIm0')
Label(window,text='图片URL:').place(x=100,y=60)
Label(window,text='文件夹名称:').place(x=100,y=100)
l=Label(window,bg='#000',fg = 'white',width=31,height = 3,text='文件夹名称:')
l.place(x=130,y=140)
Entry(window,textvariable = var_urlfront,width = 60).place(x=175,y=60)
Entry(window,textvariable = var_path).place(x=175,y=100)
b=Button(window,text = '提交',command = img_save,height=3,width = 8)
b.place(x = 400, y = 140)




window.mainloop()
# https://img.onvshen.com:85/gallery/21501/17266/005.jpg