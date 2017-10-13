'''
    Load in the MNIST dataset, and plot the mean (average) image for each digit class (0....9)
    Recall: mean = sum / number of elements
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

mnist_df = pd.read_csv('../train.csv')

for i in range(10):
    # get rows that is class i (picture 0 ... 9)
    class_i = mnist_df.loc[mnist_df['label'] == i]
    
    # delete 'label' column
    class_i_non_label = class_i.drop('label', axis = 1)

    # calculate mean of each column
    class_i_img = class_i_non_label.mean(axis = 0)

    # plot
    plt.imshow(class_i_img.reshape(28,28), cmap = 'gray')
    plt.show()


