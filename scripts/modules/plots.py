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
def points3D(fig, points, theta, phi, area, xlabel=None, ylabel=None, zlabel=None, title=None):
    
    # function to plot 3D points in space:
    # inputs: points = list containing the x, y ,z and the density of the points. The color of the point is related to the value of density
    # phi, theta = integers to define the angle and azimuth of the box plot;
    # xlabel, ylabel, zlabel = strings with the label id:  
    # output: figure with all points
     
    ax = fig.add_subplot(111, projection='3d')
    
    # transform the list points into array:
    f = np.array(points)
    nf = np.size(f,0)
        
    # set the properties of each point:
    dens = f[4,:] # density
    # r = f[3,:] # radius(not used for plotting issues)
    x = f[0,:] # x coordinate (center of the sphere)
    y = f[1,:] # y coordinate (center of the sphere)
    z = f[2,:] # z coordinate (center of the sphere)
    p = ax.scatter(x, y, z, s=80, c = dens, depthshade=True )
    cbar = fig.colorbar(p, aspect=50, fraction = 0.03, orientation="vertical")
    cbar.set_label('density-constrast ( $ kg/m^{3}$ )',fontsize=10, rotation = 90)
    
    #if area==True:
    x0, x1, y0, y1, z0, z1 = area
    ax.set_xlim3d(x0, x1)
    ax.set_ylim3d(y0, y1)
    ax.set_zlim3d(z0, z1)
    # z points downward:
    ax.invert_zaxis()
    ax.view_init(theta, phi)    
    #if xlabel==True:
    ax.set_xlabel(xlabel, labelpad=25, fontsize=12)
    #if ylabel==True:
    ax.set_ylabel(ylabel, labelpad=25, fontsize=12)
   # if zlabel == True:
    ax.set_zlabel(zlabel, labelpad=25, fontsize=12)
   # if title == True:
    ax.set_title(title, fontsize=17)
      
    return plt.show()
###############################################################################################################################

def prism3D(fig, prism, color, theta, phi, area, xlabel, ylabel, zlabel ,title):
   # plot a 3D prism with a specific color:
   # fig: figure box created outside of the function: An option is copy and paste the following two lines:
   # py.rcParams['figure.figsize'] = (15.0, 10.0) #Redimensiona a figura
   # fig = plt.figure()
   # inputs: prism = list with the corners of the prism to be drawn
   # color = string that indicates the color to paint the edges of the prism
   # color can be: ('black', 'red', 'blue', 'yellow', 'green')
   # phi, theta = integers to define the angle and azimuth of the box plot;
   # xlabel, ylabel, zlabel = strings with the label id:  
   # output: the plot of the 3D prism

   
    ax = fig.add_subplot(111, projection='3d')
    fs = 15
   
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

    
    x0, x1, y0, y1, z0, z1 = area
   
        # get the corners of the prism:    
    r = np.array(prism)
    rx = r[0:2] # x corners
    ry = r[2:4] # y corners
    rz = r[4:6] # z corners
    
    for s, e in combinations(np.array(list(product(rx,ry,rz))), 2):
        
        if np.sum(np.abs(s-e)) == ry[1]-ry[0]:
            ax.plot3D(*zip(s,e), color=c)
            ax.set_xlim3d(x0, x1)
            ax.set_ylim3d(y0, y1)
            ax.set_zlim3d(z0, z1)
            ax.invert_zaxis()    
      
        if np.sum(np.abs(s-e)) == rx[1]-rx[0]:
            ax.plot3D(*zip(s,e), color=c)
            ax.set_xlim3d(x0, x1)
            ax.set_ylim3d(y0, y1)
            ax.set_zlim3d(z0, z1)
            ax.invert_zaxis()

        if np.sum(np.abs(s-e)) == rz[1]-rz[0]:
            ax.plot3D(*zip(s,e), color=c)
            ax.set_xlim3d(x0, x1)
            ax.set_ylim3d(y0, y1)
            ax.set_zlim3d(z0, z1)
            ax.invert_zaxis() 
    
    ax.set_xlabel(xlabel, labelpad=25 ,fontsize=fs) # labelpad = distance between the label and the axis
    ax.set_ylabel(ylabel, labelpad=25 ,fontsize=fs)
    ax.set_zlabel(zlabel, labelpad=25,fontsize=fs)
    ax.set_title(title, fontsize=fs + 3 )
    ax.view_init(theta, phi)
      
    # set labelsize 
    plt.tick_params(axis='y', labelsize=fs-3)
    plt.tick_params(axis='x', labelsize=fs-3)
    plt.tick_params(axis='z', labelsize=fs-3)
          
    return plt.show()

####################################################################################################################################

def rectangle(area, style='-k', linewidth=1, fill=None, alpha=1., label=None):
    """
    Plot a rectangle over a contour map.

    Parameters:

    * area : list = [x1, x2, y1, y2]
        Borders of the rectangle
    * style : str
        String with the color and line style (as in matplotlib.pyplot.plot)
    * linewidth : float
        Line width
    * fill : str
        A color string used to fill the square. If None, the square is not
        filled
    * alpha : float
        Transparency of the fill (1 >= alpha >= 0). 0 is transparent and 1 is
        opaque
    * label : str
        label associated with the square.
    * xy2ne : True or False
        If True, will exchange the x and y axis so that the x coordinates of
        the polygon are north. Use this when drawing on a map viewed from
        above. If the y-axis of the plot is supposed to be z (depth), then use
        ``xy2ne=False``.

    Returns:

    * axes : ``matplitlib.axes``
        The axes element of the plot

    """
    x1, x2, y1, y2 = area
   # if xy2ne:
   #     x1, x2, y1, y2 = y1, y2, x1, x2
    xs = [x1, x1, x2, x2, x1]
    ys = [y1, y2, y2, y1, y1]
    kwargs = {'linewidth': linewidth}
    if label is not None:
        kwargs['label'] = label
    plot, = plt.plot(xs, ys, style, **kwargs)
    if fill is not None:
        plt.fill(xs, ys, color=fill, alpha=alpha)
    return plot
    
    
