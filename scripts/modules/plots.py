# --------------------------------------------------------------------------------------------------
# Title: Grav-Mag Codes
# Author: Rodrigo Bijani and Victor Carreira
# Description: Source codes for plotting images.
# --------------------------------------------------------------------------------------------------

# Import Python libraries:
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pylab as py

# read file with the coordinates of all point masses
def points3D(x, y, z, theta, phi, xlabel, ylabel, zlabel):
    
    # function to plot 3D points in space:
    # inputs: x,y,z = 1D arrays with coordinates of points
    # phi, theta = integers to define the angle and azimuth of the box plot;
    # xlabel, ylabel, zlabel = strings with the label id:  
    # output: figure with all points
    
    py.rcParams['figure.figsize'] = (15.0, 10.0)#Redimensiona a figura
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, s=80, c = '0.1', depthshade=True )
    ax.set_xlabel(xlabel,fontsize=14)
    ax.set_ylabel(ylabel,fontsize=14)
    ax.set_zlabel(zlabel,fontsize=14)
    ax.view_init(theta, phi)
    return plt.show()
