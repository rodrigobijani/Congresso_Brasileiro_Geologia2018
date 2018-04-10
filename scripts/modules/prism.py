# --------------------------------------------------------------------------------------------------
# Title: Grav-Mag Codes
# Author: Nelson Ribeiro Filho
# Description: Source codes that will be necessary during the masters course.
# Collaborator: Rodrigo Bijani
# --------------------------------------------------------------------------------------------------

import numpy as np

def prism_gx(x, y, z, prism):
    '''
    This function is a Python implementation for the X horizontal component for the gravity field due to 
    a rectangular prism, which has initial and final positions equals to xi and xf, yi and yf, for the X 
    and Y directions. This function also recieve the obsevation points for an array or a grid and also the 
    value for height of the observation, which can be a simple float number (as a level value) or a 1D array.
    
    Inputs:
    x, y - numpy arrays - observation points in x and y directions
    z - numpy array/float - height for the observation
    prism - numpy array - all elements for the prims
        prism[0, 1] - initial and final coordinates at X (dimension at X axis!)
        prism[2, 3] - initial and final coordinates at Y (dimension at Y axis!)
        prism[4, 5] - initial and final coordinates at Z (dimension at Z axis!)
        prism[6] - density value
        
    Output:
    gx - numpy array - vertical component for the gravity atraction
    '''

    # Stablishing some conditions
    if x.shape != y.shape:
        raise ValueError("All inputs must have same shape!")
       
    # Definitions for all distances
    xp = [prism[1] - x, prism[0] - x]
    yp = [prism[3] - y, prism[2] - y]
    zp = [prism[5] - z, prism[4] - z]    

    # Definition for density
    rho = prism[6]
    
    # Definition - some constants
    G = 6.673e-11
    si2mGal = 100000.0
    
    # Numpy zeros array to update the result
    gx = np.zeros_like(x)
    
    # Compute the value for Gx
    for k in range(2):
        for j in range(2):
            for i in range(2):
                r = np.sqrt(xp[i]**2 + yp[j]**2 + zp[k]**2)
                result = -(yp[j]*np.log(zp[k] + r) + zp[k]*np.log(yp[j] + r) - xp[i]*np.arctan2(zp[k]*yp[j], xp[i]*r))
                gx += ((-1.)**(i + j + k))*result*rho

                # Multiplication for all constants and conversion to mGal
    gx *= G*si2mGal
    
    # Return the final output
    return gx

def prism_gy(x, y, z, prism):
    '''
    This function is a Python implementation for the Y horizontal  component for the gravity field due 
    to a rectangular prism, which has initial and final positions equals to xi and xf, yi and yf, for 
    the X and Y directions. This function also recieve the obsevation points for an array or a grid and 
    also the value for height of the observation, which can be a simple float number (as a level value) 
    or a 1D array.
    
    Inputs:
    x, y - numpy arrays - observation points in x and y directions
    z - numpy array/float - height for the observation
    prism - numpy array - all elements for the prims
        prism[0, 1] - initial and final coordinates at X (dimension at X axis!)
        prism[2, 3] - initial and final coordinates at Y (dimension at Y axis!)
        prism[4, 5] - initial and final coordinates at Z (dimension at Z axis!)
        prism[6] - density value
        
    Output:
    gy - numpy array - vertical component for the gravity atraction
    '''
    
    # Stablishing some conditions
    if x.shape != y.shape:
        raise ValueError("All inputs must have same shape!")
       
    # Definitions for all distances
    xp = [prism[1] - x, prism[0] - x]
    yp = [prism[3] - y, prism[2] - y]
    zp = [prism[5] - z, prism[4] - z]  
    
    # Definition for density
    rho = prism[6]
    
    # Definition - some constants
    G = 6.673e-11
    si2mGal = 100000.0
    
    # Numpy zeros array to update the result
    gy = np.zeros_like(x)
    
    # Compute the value for Gy
    for k in range(2):
        for j in range(2):
            for i in range(2):
                r = np.sqrt(xp[i]**2 + yp[j]**2 + zp[k]**2)
                result = -(zp[k]*np.log(xp[i] + r) + xp[i]*np.log(zp[k] + r) - yp[j]*np.arctan2(xp[i]*zp[k], yp[j]*r))
                gy += ((-1.)**(i + j + k))*result*rho
                
    # Multiplication for all constants and conversion to mGal
    gy *= G*si2mGal
    
    # Return the final output
    return gy

def prism_gz(x, y, z, prism):
    '''
    This function is a Python implementation for the vertical component for the gravity field due to a 
    rectangular prism, which has initial and final positions equals to xi and xf, yi and yf, for the X 
    and Y directions. This function also recieve the obsevation points for an array or a grid and also 
    the value for height of the observation, which can be a simple float number (as a level value) or a 
    1D array.
    
    Inputs:
    x, y - numpy arrays - observation points in x and y directions
    z - numpy array/float - height for the observation
    prism - numpy array - all elements for the prims
        prism[0, 1] - initial and final coordinates at X (dimension at X axis!)
        prism[2, 3] - initial and final coordinates at Y (dimension at Y axis!)
        prism[4, 5] - initial and final coordinates at Z (dimension at Z axis!)
        prism[6] - density value
        
    Output:
    gz - numpy array - vertical component for the gravity atraction
    '''

    # Stablishing some conditions
    if x.shape != y.shape:
        raise ValueError("All inputs must have same shape!")
       
    # Definitions for all distances
    xp = [prism[1] - x, prism[0] - x]
    yp = [prism[3] - y, prism[2] - y]
    zp = [prism[5] - z, prism[4] - z]  
    
    # Definition for density
    rho = prism[6]
    
    # Definition - some constants
    G = 6.673e-11
    si2mGal = 100000.0
    
    # Numpy zeros array to update the result
    gz = np.zeros_like(x)
    
    # Compute the value for Gz
    for k in range(2):
        for j in range(2):
            for i in range(2):
                r = np.sqrt(xp[i]**2 + yp[j]**2 + zp[k]**2)
                result = -(xp[i]*np.log(yp[j] + r) + yp[j]*np.log(xp[i] + r) - zp[k]*np.arctan2(xp[i]*yp[j], zp[k]*r))
                gz += ((-1.)**(i + j + k))*result*rho
                
    # Multiplication for all constants and conversion to mGal
    gz *= G*si2mGal
    
    # Return the final output
    return gz