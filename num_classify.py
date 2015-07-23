# -*- coding:utf-8 -*-
import numpy as np
import caffe

MODEL_FILE = '../lenet.prototxt'
PRETRAINED = '../lenet_iter_10000.caffemodel'
IMAGE_FILE = 'image/8.jpg'

input_image = caffe.io.load_image(IMAGE_FILE, color=False)

net = caffe.Classifier(MODEL_FILE, PRETRAINED)
p = net.predict([input_image])
print "input image is \"%s\" ＼(^o^)／"% p[0].argmax()
print p
