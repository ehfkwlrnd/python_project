# version 0.0.1

from tkinter import *
import tkinter.filedialog as tkdlg
from webimgdownloader import STWebImgDownloader as swid

def getPath():
    path_input.configure(text=tkdlg.askdirectory())

def oneDownload():
    global base
    global driverLoc
    global title_selector
    global img_selector
    global img_src

    w = swid(base, driverLoc)
    url = url_input.get()
    folder = path_input['text']

    w.one(url, title_selector, img_selector, img_src, folder)
    w.close()

def mulDownload():
    global base
    global dirverLoc
    global title_selector
    global link_selector
    global link_href
    global img_selector
    global img_src
    
    w = swid(base, driverLoc)
    url = url_input.get()
    folder = path_input['text']

    w.multi(url, title_selector, link_selector, link_href, img_selector, img_src, folder)
    w.close()

d = dict()
f = open('params.txt', 'r')
props = f.read().split('\n')
for line in props:
    key, val = line.split('=')
    d.update({key : val})
    line = f.readline()
f.close()

base = d['base']
driverLoc = d['driverLoc']
title_selector = d['title_selector']
link_selector = d['link_selector']
link_href = d['link_href']
img_selector = d['img_selector']
img_src = d['img_src']

                 
root = Tk()

url_label = Label(root, text='URL')
url_input = Entry(root)
path_label = Label(root, text='PATH')
path_input = Label(root, text='')
path_btn = Button(root, text='open', command=getPath)
one_btn = Button(root, text='ONE', command=oneDownload)
mul_btn = Button(root, text='MUL', command=mulDownload)

url_label.grid(row=0, column=0)
url_input.grid(row=0, column=1)
path_label.grid(row=1, column=0)
path_input.grid(row=1, column=1)
path_btn.grid(row=1, column=2)
one_btn.grid(row=2, column=0)
mul_btn.grid(row=2, column=1)

root.mainloop()
