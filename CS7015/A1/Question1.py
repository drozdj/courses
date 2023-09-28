'''Download the fashion-MNIST dataset and plot 1 sample image for each class as shown in the grid below. Use "from keras.datasets import fashion_mnist" for getting the fashion mnist dataset. '''
'''(2 Marks)'''

#import packages
import wandb
import numpy as np
from keras.datasets import fashion_mnist

# define wandb
project = "CS7015 | FFN implementation"
config = {
    "learning_rate": 0.02,
    "architecture": "FNN",
    "dataset": "fashion-mnist",
    "epochs": 10,}

fashion_mnist_mapping = {0: "T-shirt/top", 1: "Trouser", 2: "Pullover", 3: "Dress", 4: "Coat", 5: "Sandal", 6: "Shirt", 7: "Sneaker", 8: "Bag", 9: "Ankle boot",}

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

wandb.init(project=project, config=config)
# Question 1 (2 Marks)
examples = []
for i in range(50):
    pixels = x_train[i]
    image = wandb.Image(pixels, caption=f"{fashion_mnist_mapping[y_train[i]]}")
    examples.append(image)
wandb.log({"examples": examples})
wandb.finish()
