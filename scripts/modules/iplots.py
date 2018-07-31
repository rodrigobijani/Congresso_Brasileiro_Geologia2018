# --------------------------------------------------------------------------------------------------
# Title: Grav-Mag Codes
# Authors: Rodrigo Bijani and Victor Carreira
# Description: Source codes for plotting interactive images.
# --------------------------------------------------------------------------------------------------

################ python internal packages ###############
import numpy as np
from matplotlib import pyplot, widgets
import pylab as py
from matplotlib.widgets import Cursor

def model_masses(area1, area2):
    """ Function to plant point masses by clicking with the mouse through a 3-D interpretive model. 
    Inputs: area1 = [xmin, xmax, ymin, ymax] : list with horizontal coordinate ranges.
            area2= [rhomin, rhomax, zmin, zmaz] : list with density-constrast and depth ranges.
    Output : x,y,z,rho = lists with the picked values from the mouse clicking. The size is related to the number of clicks
    OBS: PAY ATTENTION TO THE NUMBER OF CLICKS IN BOTH SIDES OF THE PLOT AREA. OTHERWISE THE MODEL WILL BE INCOMPLETE! 
    """

    
    # ------------ auxiliar functios to perform the clicking--------------------------:
    def draw_guide1(px, py):
        if len(x) != 0 or len(y) !=0:
            tmpline1.set_data([x[-1], px], [y[-1], py])
    # --------------------------------------------------------------------------------:
    def draw_guide2(px,py):
        if len(rho) !=0 or len(z) !=0 :
            tmpline2.set_data([rho[-1], px], [z[-1], py])
    # --------------------------------------------------------------------------------:
    def move(event):
        if event.inaxes != ax1 or event.inaxes != ax2:
            return 'plot area wrongly set up. Please, check.'       
        if event.inaxes == ax1:
            if picking[0]:
                draw_guide1(event.xdata, event.ydata)
                ax1.figure.canvas.draw()
        elif event.inaxes == ax2:
            if picking[0]:
                draw_guide2(event.xdata, event.ydata)
                ax2.figure.canvas.draw()
    
    # --------------------------------------------------------------------------------:
    def click(event):
        if event.inaxes == ax1:
            x.append(event.xdata)
            y.append(event.ydata)
            plotx.append(event.xdata)
            ploty.append(event.ydata)
            line1.set_color('k')
            line1.set_marker('o')
            line1.set_linestyle('None')
            line1.set_data(plotx, ploty)
            ax1.figure.canvas.draw()      
        elif event.inaxes == ax2:
            rho.append(event.xdata)
            z.append(event.ydata)
            plotrho.append(event.xdata)
            plotz.append(event.ydata)
            line2.set_color('b')
            line2.set_marker('*')
            line2.set_linestyle('None')
            line2.set_data(plotrho, plotz)
            ax2.figure.canvas.draw()
    # --------------------------------------------------------------------------------:
    def erase(event):
        if event.inaxes == ax1:
            if event.key == 'e' and picking[0]:
                x.pop()
                y.pop()
                plotx.pop()
                ploty.pop()
                line1.set_data(plotx, ploty)
                line1.set_linestyle('None')
                draw_guide1(event.xdata, event.ydata)
                ax1.figure.canvas.draw()
        elif event.inaxes == ax2:
             if event.key == 'e' and picking[0]:
                rho.pop()
                z.pop()
                plotrho.pop()
                plotz.pop()
                line2.set_data(plotrho, plotz)
                line2.set_linestyle('None')
                draw_guide2(event.xdata, event.ydata)
                ax2.figure.canvas.draw()
    #---------------------------------------------------------------------------------:

    fig1, (ax1, ax2) = pyplot.subplots(1, 2)
    ax1.set_title('Click for picking of x y coordinates. Press keybord < e > to erase.' )
    ax1.set_xlim(area1[0], area1[1])
    ax1.set_ylim(area1[2], area1[3])
    ax1.grid()
    ax1.set_xlabel(' Horizontal coordinate x')
    ax1.set_ylabel(' Horizontal coordinate y')

    ax2.set_title('Click for picking densisty-contrast and depth Close fig when done.')
    ax2.set_xlim(area2[0], area2[1])
    ax2.set_ylim(area2[2], area2[3])
    ax2.grid()

# --------- change the position of the tick label--------------:
    ax2.yaxis.tick_right()

# --------- invert axis for depth positive down --------------:
    pyplot.gca().invert_yaxis()
    ax2.set_xlabel(' density contrast')
    ax2.set_ylabel(' Depth')
    
# --------- cursor use for better visualization ------------- :
    cursor1 = Cursor(ax1, useblit=True, color='black', linewidth=2)
    cursor2 = Cursor(ax2, useblit=True, color='blue', linewidth=2)

# -------------- cleaning lists before using -----------------:
    x = []
    y = []
    z = []
    
    plotx = []
    ploty = []

    rho = []
    plotz = []
    plotrho = []
# ----------------- cleaning line object for plotting ------------------:
    line1, = ax1.plot([],[])
    tmpline1, = ax1.plot([],[])
    line2, = ax2.plot([],[])
    tmpline2, = ax2.plot([],[])

# ------------ Hack because Python 2 doesn't like nonlocal variables that change value -------:
# Lists it doesn't mind.
    picking = [True]
    fig1.canvas.mpl_connect('button_press_event', click )
    fig1.canvas.mpl_connect('key_press_event', erase )
    fig1.canvas.mpl_connect('motion_notify_event', move )
    pyplot.show()
    return x,y,z,rho
##################################################################################################################################    
    
