import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
import os

path = os.getcwd()

print(path)

## Read
files = [file for file in glob.glob(path + '/Pics/*.jpg')]
# img = cv2.imread("/content/drive/My Drive/test1.jpg")
file1 = open('greendata.txt','w') 
words = []
for filename in files:
  print(filename)
  img = cv2.imread(os.path.join(path,filename))

## convert to hsv
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  mask = cv2.inRange(hsv, (30, 0, 0), (90, 255,255))

# ## slice the green
  imask = mask>0
  count = np.count_nonzero(imask)
  percentage = count/(img.shape[0]*img.shape[1])
  
#   l = (0, 90, 0)
#   u = (100, 255, 100)

#   lower = np.array(l, dtype = "uint8")
#   upper = np.array(u, dtype = "uint8")

#   mask = cv2.inRange(img, lower, upper)
#   imask = mask>0
#   count = np.count_nonzero(imask)
#   percentage = count/(img.shape[0]*img.shape[1])

  filename = filename.replace(path, '')
  filename = filename.replace(' ', '')
  filename = filename.split(',')[0]
  filename = filename.split('/')[-1]

  ans = filename +' ' + str(percentage) + '\n'
  words.append(ans)
file1.writelines(words)