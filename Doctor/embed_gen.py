import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, GlobalAveragePooling2D
from tensorflow.keras.applications.efficientnet import EfficientNetB0, preprocess_input
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from PIL import Image
from tensorflow.keras.models import Model,Sequential
# Load the VGG16 model pre-trained on ImageNet, excluding the top classification layer
base_model = VGG16(weights='imagenet', include_top=False, pooling='avg')

# Define a function to preprocess the image and get embeddings
def get_image_embedding_vgg16(img):
    img = Image.open(img.stream)
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0 

    print("Loading img: ", img)

    img_array = image.img_to_array(img)
    print("Image array333: ", img_array)
    img_array = np.expand_dims(img_array, axis=0)
    print("Image222: ", img_array)
    img_array = preprocess_input(img_array)
    print("Image111: ", img_array)
    
    # Get the embedding vector
    embedding_vector = base_model.predict(img_array)
    
    return embedding_vector

def get_image_embedding_vgg16_test(img_path):
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    # Get the embedding vector
    embedding_vector = base_model.predict(img_array)
    
    return embedding_vector

# Define a simple custom CNN
def create_custom_cnn():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        GlobalAveragePooling2D(),
        Dense(256, activation='relu')
    ])
    return model

# Instantiate and compile the model
custom_cnn = create_custom_cnn()
custom_cnn.compile(optimizer='adam', loss='categorical_crossentropy')

# Load weights if available, or train the model here if necessary

# Define a function to preprocess the image and get embeddings using the custom CNN
def get_image_embedding_custom_cnn(img_path):
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalizing the image
    
    # Get the embedding vector
    embedding_vector = custom_cnn.predict(img_array)
    
    return embedding_vector



# Load the EfficientNetB0 model pre-trained on ImageNet, excluding the top classification layer
base_model = EfficientNetB0(weights='imagenet', include_top=False, pooling='avg')

# Define a function to preprocess the image and get embeddings
def get_image_embedding_efficientnet(img_path):
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    # Get the embedding vector
    embedding_vector = base_model.predict(img_array)
    
    return embedding_vector




# Load the InceptionV3 model pre-trained on ImageNet, excluding the top classification layer
base_model = InceptionV3(weights='imagenet', include_top=False, pooling='avg')

# Define a function to preprocess the image and get embeddings
def get_image_embedding_inceptionv3(img_path):
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(299, 299))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    # Get the embedding vector
    embedding_vector = base_model.predict(img_array)
    
    return embedding_vector




# Load the ResNet50 model pre-trained on ImageNet, excluding the top classification layer
base_model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

# Define a function to preprocess the image and get embeddings
def get_image_embedding(img_path):
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    # Get the embedding vector
    embedding_vector = base_model.predict(img_array)
    
    return embedding_vector