'''
    Continue to work with the MNIST dataset
    Common C programming exercise (with for loops and array indexing)
    Write a function that flips an image 90 degrees clockwise
    Try both the "for loop method" and by making use of Numpy functions
    '''


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import ndimage

print('reading csv file...\n')
csv_file = pd.read_csv('test.csv')
print('file loaded.\n')

imgarray = csv_file.loc[0,:].as_matrix().reshape(28,28)
rotate_img = ndimage.rotate(imgarray, -90)

#plt.imshow(imgarray, cmap = 'gray')
plt.imshow(rotate_img, cmap = 'gray')
plt.show()
