import os
import cv2
import PIL
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from flask import Flask, request, Response, jsonify

import keras
from tensorflow.keras.models import load_model

vgg_model = load_model('/Users/yudiz-Dhara/Documents/detect_disease_using_CXR/Dr_X_ray/Doctor/models_vgg16/vgg_model.h5')

# from .models_vgg16 import vgg_model

def process_image(image):
    image = tf.cast(image , tf.float32)
    image = tf.image.resize(image , (224 , 224))
    image = image/255
    image = image.numpy()
    return image

# from vectordb import *
from .embed_gen import *


def model_predict(img):

    LABELS = { 0 : "Normal", 1 : "Opacity"}
    # img_data = img.read()
    # img_array = np.frombuffer(img_data, np.uint8)
    # im = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), img)
    with open(save_path, 'rb') as file:
        file_content = file.read()
    # if isgray(im):
        # im = cv2.imread(img)
    # test_image = np.asarray(im)

    print("Processed test image",save_path)
    processed_test_image = cv2.imread(save_path)
    processed_test_image = process_image(processed_test_image)
    processed_test_image = np.expand_dims(processed_test_image, axis = 0)
    
    ps = vgg_model.predict(processed_test_image)
    print("PS: ", ps)
    ps = np.argmax(ps)
    return LABELS[ps]
