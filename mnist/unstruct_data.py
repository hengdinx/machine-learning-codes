#!/usr/bin/python3

import struct
from array import array
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class unstruct_file:
    def __init__(self, filename, ftype):
        if ftype == "image":
            self.get_images(filename)
        elif ftype == "label":
            self.get_labels(filename)

    def get_images(self, filename):
        with open(filename, "rb") as f:
            magic, size, rows, cols = struct.unpack(">4I", f.read(16))
            self.images=[]
            cur_row = f.read(rows * cols)
            while cur_row:
                image_data = array("B", cur_row)
                self.images.append(image_data)
                cur_row = f.read(rows * cols)

    def get_labels(self, filename):
        with open(filename, 'rb') as f:
            magic, size = struct.unpack(">2I", f.read(8))
            self.labels=array('B')
            cur_row = f.read(1)
            while cur_row:
                image_data = array("B", cur_row)
                self.labels.append(image_data[0])
                cur_row = f.read(1)

train_images = unstruct_file("train-images-idx3-ubyte", "image")
test_images = unstruct_file("t10k-images-idx3-ubyte", "image")
train_labels = unstruct_file("train-labels-idx1-ubyte", "label")
test_labels = unstruct_file("t10k-labels-idx1-ubyte", "label")
#for i in range(71):
#    print(train_labels.labels[i])
for i,img in enumerate(train_images.images):
    if i < 60000:
        #plt.subplot(9,8,i+1)
        img = np.array(img)
        img = img.reshape((28,28))
        img = Image.fromarray(np.uint8(img))
        img_name = './train_images/'+str(train_labels.labels[i])+"_"+str(i)+'.jpg'
        img.save(img_name, 'jpeg')
        #plt.imshow(img,cmap='gray')
        #plt.axis("off")
    else:
        break
for i,img in enumerate(test_images.images):
    if i < 10000:
        #plt.subplot(9,8,i+1)
        img = np.array(img)
        img = img.reshape((28,28))
        img = Image.fromarray(np.uint8(img))
        img_name = './test_images/'+str(train_labels.labels[i])+"_"+str(i)+'.jpg'
        img.save(img_name, 'jpeg')
        #plt.imshow(img,cmap='gray')
        #plt.axis("off")
    else:
        break
#plt.show()
