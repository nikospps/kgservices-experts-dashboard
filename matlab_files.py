import pandas as pd
import scipy.io
import numpy as np
#Matlab File Import
mat = scipy.io.loadmat('satellite.mat')#import the matlab file of .mat format

satellite_df = pd.DataFrame(np.hstack((mat['X'], mat['y'])))

satellite_df.head()

from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import cv2
import imutils