# -*- coding:utf-8 -*-
import sys
import numpy as np
import caffe


def input_arg(argvs, argc):
    if (argc != 2):   # 引数が足りない場合は、その旨を表示
        print 'Usage: # python %s image/0.jpg' % argvs[0]
        quit()        # プログラムの終了

    print 'Input filename = %s' % argvs[1]
    # 引数でとったディレクトリの文字列をリターン
    return argvs


if __name__ == "__main__":
    argvs = sys.argv   # コマンドライン引数を格納したリストの取得
    argc = len(argvs)  # 引数の個数
    src = input_arg(argvs, argc)

    MODEL_FILE = '../lenet.prototxt'
    PRETRAINED = '../lenet_iter_10000.caffemodel'
    IMAGE_FILE = src[1]

    input_image = caffe.io.load_image(IMAGE_FILE, color=False)

    net = caffe.Classifier(MODEL_FILE, PRETRAINED)
    p = net.predict([input_image])
    print "input image is \" %s \" ＼(^o^)／"% p[0].argmax()
    print p
