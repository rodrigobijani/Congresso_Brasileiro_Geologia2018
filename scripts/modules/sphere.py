# --------------------------------------------------------------------------------------------------
# Title: Grav-Mag Codes
# Author: Nelson Ribeiro Filho
# Description: Source codes that will be necessary during the masters course.
# Collaborator: Rodrigo Bijani
# --------------------------------------------------------------------------------------------------

# Import Python libraries
import numpy as np
# Import my libraries
#import auxiliars as aux
def sphere_gz(x, y, z, sphere):
    '''    
    This function calculates the gravity contribution due to a solid sphere. This is a Python 
    implementation for the subroutine presented in Blakely (1995). On this function, there are 
    received the value of the initial and final observation points (X and Y) and the properties 
    of the sphere. The inputs sphere is allocated as: 
    sphere[size = 5] = sphere[x center, y center, z center, radius , density]
    
    Inputs:
    sphere - numpy array - elements of the sphere
        sphere[0, 1, 2] - positions of the sphere center at x, y and z directions
        # sphere[3] - radius -  not used in this case!
        sphere[4] - density value
    Output:
    gz - numpy array - vertical component for the gravity signal due to a solid sphere    
    '''
    
    # Stablishing some conditions
    if x.shape != y.shape:
        raise ValueError("All inputs must have same shape!")
    
    # Setting the initial value
    gz = 0.
    
    # Setting coordinate values
    dx = sphere[0] - x
    dy = sphere[1] - y
    dz = sphere[2] - z
    radius = 1000.0 #(unitary radius for convenience in meters)  #sphere[3]
    rho = sphere[3]
    
    # Definition for some constants
    G = 6.673e-11
    si2mGal = 100000.0
    
    # Compute the constant which is result due to the product
    const = (4./3.)*np.pi*rho*(radius**3)
    
    # Compute the distance
    r = np.sqrt(dx**2 + dy**2 + dz**2)
    
    # Compute the vertical component 
    gz = const*dz/(r**3)
    gz *= G*si2mGal
    
    # Return the final outpu
    return gz

   ###########################################################################################################################
def sphere_gx(x, y, z, sphere):
    '''    
    This function calculates the gravity contribution due to a solid sphere. This is a Python 
    implementation for the subroutine presented in Blakely (1995). On this function, there are 
    received the value of the initial and final observation points (X and Y) and the properties 
    of the sphere. The inputs sphere is allocated as: 
    sphere[size = 5] = sphere[x center, y center, z center, radius , density]
    
    Inputs:
    sphere - numpy array - elements of the sphere
        sphere[0, 1, 2] - positions of the sphere center at x, y and z directions
        sphere[3] - radius
        sphere[4] - density value
    Output:
    gx - numpy array - vertical component for the gravity signal due to a solid sphere    
    '''
    
    # Stablishing some conditions
    if x.shape != y.shape:
        raise ValueError("All inputs must have same shape!")
    
    # Setting the initial value
    gx = 0.
    
    # Setting coordinate values
    dx = sphere[0] - x
    dy = sphere[1] - y
    dz = sphere[2] - z
    radius = 1000.0 # unitary radius in meters #sphere[3]
    rho = sphere[3]
    
    # Definition for some constants
    G = 6.673e-11
    si2mGal = 100000.0
    
    # Compute the constant which is result due to the product
    const = (4./3.)*np.pi*rho*(radius**3)
    
    # Compute the distance
    r = np.sqrt(dx**2 + dy**2 + dz**2)
    
    # Compute the vertical component 
    gx = const*dx/(r**3)
    gx *= G*si2mGal
    
    # Return the final outpu
    return gx
##################################################################################################################################

def sphere_gy(x, y, z, sphere):
    '''    
    This function calculates the gravity contribution due to a solid sphere. This is a Python 
    implementation for the subroutine presented in Blakely (1995). On this function, there are 
    received the value of the initial and final observation points (X and Y) and the properties 
    of the sphere. The inputs sphere is allocated as: 
    sphere[size = 5] = sphere[x center, y center, z center, radius , density]
    
    Inputs:
    sphere - numpy array - elements of the sphere
        sphere[0, 1, 2] - positions of the sphere center at x, y and z directions
        sphere[3] - radius
        sphere[4] - density value
    Output:
    gy - numpy array - vertical component for the gravity signal due to a solid sphere    
    '''
    
    # Stablishing some conditions
    if x.shape != y.shape:
        raise ValueError("All inputs must have same shape!")
    
    # Setting the initial value
    gy = 0.
    
    # Setting coordinate values
    dx = sphere[0] - x
    dy = sphere[1] - y
    dz = sphere[2] - z
    radius =  1000.0 # unitary radius in meters for convenience #sphere[3]
    rho = sphere[3]
    
    # Definition for some constants
    G = 6.673e-11
    si2mGal = 100000.0
    
    # Compute the constant which is result due to the product
    const = (4./3.)*np.pi*rho*(radius**3)
    
    # Compute the distance
    r = np.sqrt(dx**2 + dy**2 + dz**2)
    
    # Compute the vertical component 
    gy = const*dy/(r**3)
    gy *= G*si2mGal
    
    # Return the final outpu
    return gy

