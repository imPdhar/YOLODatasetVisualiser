

import os, random
import cv2
import matplotlib.pyplot as plt
imgpath="/content/images/train"
txtpath="/content/labels/train"
imglist=[]
a=random.choice(os.listdir(imgpath))
b=a
classes = {0:"person", 1:"car"} #Enter classes
b=b.strip('jpg')
b=txtpath+"/"+b+"txt"
#print(b)
a=imgpath+"/"+a
#print(a)
img = cv2.imread(a)
dh, dw, _ = img.shape

fl = open(b, 'r')
data = fl.readlines()
fl.close()

for dt in data:

    # Split string to float
    _, x, y, w, h = map(float, dt.split(' '))
    label, _, _, _, _ = map(str, dt.split(' '))
    label=classes[int(label)]


    l = int((x - w / 2) * dw)
    r = int((x + w / 2) * dw)
    t = int((y - h / 2) * dh)
    b = int((y + h / 2) * dh)
    
    if l < 0:
        l = 0
    if r > dw - 1:
        r = dw - 1
    if t < 0:
        t = 0
    if b > dh - 1:
        b = dh - 1

    cv2.rectangle(img, (l, t), (r, b), (255, 0, 0), 3)
    cv2.putText(img, label , (l, t-10), cv2.FONT_HERSHEY_SIMPLEX, 2, (36,255,12), 2)

plt.imshow(img)
plt.show()

