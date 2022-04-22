from tensorflow import keras
import numpy as np
import tensorflow as tf
from keras.models import load_model
import keras.preprocessing.image
import matplotlib.pyplot as plt

def load_image(img_path, img_size):
    img = keras.preprocessing.image.load_img(img_path, target_size=img_size)

    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis
    return img_array

def plot_imgs_with_pred_bar(model, labels):
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(7,5), dpi=100)

    # for i in range(1, 50):
    for i in range(2600, 2800):
        ax1.clear()
        ax2.clear()
        img_path = f"data/EuroSAT/2750/AnnualCrop/AnnualCrop_{i}.jpg"
        img = load_image(img_path, (64, 64, 3)) / 255    
        predictions = predict(model, img)
        print(predictions)
        print(labels[np.argmax(predictions)])
        ax1.imshow(np.squeeze(img))
        ax2.bar(labels, predictions)
        plt.draw()
        plt.pause(0.1)

def predict(model, img_array):
    predictions = model.predict(img_array)
    return predictions[0]

if __name__ == "__main__":
    model_path = "data/weights/eurosat_best_checkpoint.hdf5"
    model = load_model(model_path)
    labels = ['AnnualCrop','Forest', 'HerbaceousVegetation', 'Highway',"Industrial", 'Pasture', 'PermanentCrop','Residential', 'River', 'SeaLake']
    plot_imgs_with_pred_bar(model, labels)
    