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
from itertools import product, combinations

# read file with the coordinates of all point masses
def points3D(points, theta, phi, xlabel, ylabel, zlabel, model):
    
    # function to plot 3D points in space:
    # inputs: points = list containing the x, y ,z and the density of the points. The color of the point is related to the value of density
    # phi, theta = integers to define the angle and azimuth of the box plot;
    # xlabel, ylabel, zlabel = strings with the label id:  
    # color: color of the points: ('black', 'red', 'green', 'blue', 'yellow')
    # output: figure with all points
       
    # function do carreirense para definir as cores das bolinhas:
    
    
    
    f = np.array(points)
    nf = np.size(f,0)
    
    py.rcParams['figure.figsize'] = (15.0, 10.0) #Redimensiona a figura
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    for i in range(nf):    
        ax.scatter(f[i,0], f[i,1], f[i,2], s=80, c = 'k', depthshade=True )
    ax.set_xlabel(xlabel,fontsize=12)
    ax.set_ylabel(ylabel,fontsize=12)
    ax.set_zlabel(zlabel,fontsize=12)
    ax.set_title(model, fontsize=17)
    ax.view_init(theta, phi)
    return plt.show()
####################################################################################################################################

def prism3D(prism, theta, phi, xlabel, ylabel, zlabel ,color, model):
   # plot a 3D prism with a specific color:
   # inputs: model = list with the corners of the prism to be drawn
   # color = string that indicates the color to paint the edges of the prism
   # color can be: ('black', 'red', 'blue', 'yellow', 'green')
   # phi, theta = integers to define the angle and azimuth of the box plot;
   # xlabel, ylabel, zlabel = strings with the label id:  
   # output: the plot of the 3D prism

    fs = 12 # font size 
    py.rcParams['figure.figsize'] = (14.0, 10.0) #Redimensiona a figura
    fig = plt.figure(1)
    ax = fig.gca(projection='3d')
    ax.set_aspect("equal")

    if color=="black":
        c = "k"
    if color=="red":
        c = "r"
    if color=="blue":
        c = "b"
    if color=="yellow":
        c = "y"
    if color =="green":
        c = "g"

    # get the corners of the prism:    
    r = np.array(prism)
    rx = r[0:2] # x corners
    ry = r[2:4] # y corners
    rz = r[4:6] # z corners
    
   # get ranges for plot the prism:
    x = np.zeros( (2) )
    y = np.zeros( (2) )
    z = np.zeros( (2) )
   # limits over all axis for plotting:
    xmin = r[0]
    ymin = r[2]
    zmin = r[4]
    xmax = r[1]
    ymax = r[3]
    zmax = r[5]
   # 50% extra for plotting the prism:
    x[0] = xmin - (0.5 * np.absolute( xmin) )
    x[1] = xmax + (0.5 * np.absolute( xmax) ) 
    y[0] = ymin - (0.5 * np.absolute( ymin) )
    y[1] = ymax + (0.5 * np.absolute( ymax) )
    z[0] = 0.0 
    z[1] = zmax + (2.0 * np.absolute( zmax ) )
   # print x, y, z

    for s, e in combinations(np.array(list(product(rx,ry,rz))), 2):
        
        if np.sum(np.abs(s-e)) == ry[1]-ry[0]:
            ax.plot3D(*zip(s,e), color=c)
            ax.set_xlim3d(x[0], x[1])
            ax.set_ylim3d(y[0], y[1])
            ax.set_zlim3d(z[0], z[1])
            plt.gca().invert_zaxis()    
      
        if np.sum(np.abs(s-e)) == rx[1]-rx[0]:
            ax.plot3D(*zip(s,e), color=c)
            ax.set_xlim3d(x[0], x[1])
            ax.set_ylim3d(y[0], y[1])
            ax.set_zlim3d(z[0], z[1])
            plt.gca().invert_zaxis()

        if np.sum(np.abs(s-e)) == rz[1]-rz[0]:
            ax.plot3D(*zip(s,e), color=c)
            ax.set_xlim3d(x[0], x[1])
            ax.set_ylim3d(y[0], y[1])
            ax.set_zlim3d(z[0], z[1])
            plt.gca().invert_zaxis()

    # set labelsize 
    plt.tick_params(axis='y', labelsize=fs)
    plt.tick_params(axis='x', labelsize=fs)
    plt.tick_params(axis='z', labelsize=fs)
       
    ax.set_xlabel(xlabel,fontsize=fs)
    ax.set_ylabel(ylabel,fontsize=fs)
    ax.set_zlabel(zlabel,fontsize=fs)
    ax.set_title(model, fontsize=fs + 3 )
    ax.view_init(theta, phi)
        
    return plt.show()
