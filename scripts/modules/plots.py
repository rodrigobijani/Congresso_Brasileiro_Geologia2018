# --------------------------------------------------------------------------------------------------
# Title: Grav-Mag Codes
# Author: Rodrigo Bijani and Victor Carreira
# Description: Source codes for plotting images.
# --------------------------------------------------------------------------------------------------

# Import Python libraries:
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
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
    dens = f[3,:] # density
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


def draw_prism(ax,dike):
    # vertices of a prism
    x1, x2 = dike[0:2]
    y1, y2 = dike[2:4]
    z1, z2 = dike[4:6]
    
    v = np.array([[x1, y1, z1], [x1, y2, z1], [x2, y2, z1],  [x2, y1, z1], 
              [x1, y1, z2], [x1, y2, z2], [x2, y2, z2],  [x2, y1, z2]])
    
    # use scatter plot for plotting the vertices of the prism:
    ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

    # generate list of sides of our prism
    verts = [[v[0],v[1],v[2],v[3]], [v[0],v[1],v[5],v[4]], [v[1],v[2],v[6],v[5]],
         [v[2],v[3],v[7],v[6]], [v[3],v[0],v[4],v[7]], [v[4],v[5],v[6],v[7]]]

    # plot sides
    ax.add_collection3d(Poly3DCollection(verts, facecolors='red', linewidths=1, edgecolors='k', alpha=0.3))

    #change size projection
    x_scale=1.
    y_scale=1.
    z_scale=1.
    scale=np.diag([x_scale, y_scale, z_scale, 1.0])
    scale=scale*(1.0/scale.max())
    scale[3,3]=1.0
    def short_proj():
        return np.dot(Axes3D.get_proj(ax), scale)
    ax.get_proj=short_proj

    # ----- labels (these should be used outside of the function!)
    #ax.set_xlabel('Horizontal coordinate x (m)', labelpad=20 ,fontsize=14)
    #ax.set_ylabel('Horizontal coordinate y (m)', labelpad=20 ,fontsize=14)
    #ax.set_zlim(-1000,40000)
    #ax.set_zlabel('Depth (m)',labelpad=20 ,fontsize=14, rotation = 90)

    #visualization angle
    #ax.view_init(30, 10)
    #ax.invert_zaxis()
    #plt.tight_layout(True)
    return ax
   