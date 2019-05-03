import numpy as np
import cv2 as cv
import argparse
import os
import os.path
import keras
import random
import tensorflow as tf
import psutil
import matplotlib.pyplot as plt
from keras.layers import Conv2D, Conv2DTranspose, UpSampling2D
from keras.layers import Activation, Dense, Dropout, Flatten, InputLayer
from keras.layers.normalization import BatchNormalization
from keras.callbacks import TensorBoard
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from skimage.color import rgb2lab, lab2rgb, rgb2gray
from skimage.io import imsave
from keras.models import model_from_json
import logging as logger
logger.basicConfig(level=logger.INFO)

import PIL
from PIL import Image

resultFolder = os.path.join('static', 'result')
histFolder = os.path.join('static', 'graphs')
def usingTensorFlow(filepath, fileName):
    logger.info("inside tensor flow code")
    json_file = open('backend/TensorFlowModels/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights("backend/TensorFlowModels/model.h5")

    color_me = []
    logger.info("filepath: "+filepath)
    imageName1 = filepath
    width, height = Image.open(imageName1).size

    if width != 256 or height != 256:
        basewidth = 256
        baseheight = 256
        tempImg1 = Image.open(imageName1)
        tempImg1 = tempImg1.resize((basewidth, baseheight), PIL.Image.ANTIALIAS)
        tempImg1.convert('RGB').save(imageName1)

    color_me.append(img_to_array(load_img(imageName1)))
    color_me = np.array(color_me, dtype=float)
    color_me = rgb2lab(1.0/255*color_me)[:,:,:,0]
    color_me = color_me.reshape(color_me.shape+(1,))

    # Test model
    output = model.predict(color_me)
    output = output * 128

    cur = np.zeros((256, 256, 3))
    cur[:,:,0] = color_me[0][:,:,0]
    cur[:,:,1:] = output[0]
    imsave("static/result/colorized_tf_"+fileName, lab2rgb(cur))

    outputFile = 'static/result/' + 'colorized_tf_' + fileName
    logger.info('Colorized image saved as '+ outputFile)
    fileName = outputFile.split('/')[2]

    result = os.path.join(resultFolder, fileName)

    # Histogram Plots
    img = cv.imread(filepath,1)
    hist = cv.calcHist([img],[0],None,[256],[0,256])
    plt.plot(hist)
    plt.xlim([0,256])
    img1 = cv.imread(result,1)
    histr = cv.calcHist([img1],[0],None,[256],[0,256])
    plt.plot(histr)
    plt.xlim([0,256])
    plt.savefig("static/graphs/histogram_tensorflow.png")
    hist_image = os.path.join(histFolder, "histogram_tensorflow.png")
    cpu = psutil.cpu_percent()
    mem=psutil.virtual_memory().percent
    res_list = []
    res_list.append(result)
    res_list.append(hist_image)
    res_list.append(str(cpu))
    res_list.append(str(mem))
    return res_list
