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

def sphere_bx(x, y, z, sphere, direction):

    '''    
    It is a Python implementation for a Fortran subroutine contained in Blakely (1995). 
    It computes the X component of the magnetic induction caused by a sphere with uniform  
    distribution of magnetization. The direction X and Y represents the north and east, Z 
    represents growth downward. This function receives the coordinates of the points of 
    observation (X, Y, Z - arrays), the coordinates of the center of the sphere (Xe, Ye, Ze), 
    the magnetization intensity M and the values for inclination and declination (in degrees). 
    The observation values are given in meters.
    
    Inputs: 
    x, y, z - numpy arrays - position of the observation points
    sphere[0, 1, 2] - arrays - position of the center of the sphere
    sphere[3] - float - value for the spehre radius  
    sphere[4] - flaot - magnetization intensity value
    direction - numpy array - inclination and declination values
    
    Outputs:
    Bx - induced field on X direction
     
    Ps. The value for Z can be a scalar in the case of one depth, otherwise it can 
    be a set of points.    
    '''
    
    # Stablishing some conditions
    if x.shape != y.shape:
        raise ValueError("All inputs must have same shape!")
    
    # Calculates some constants
    t2nt = 1.e9 # Testa to nT - conversion
    cm = 1.e-7  # Magnetization constant
    
    # Setting the directions
    A, B = direction[0], direction[1]
    
    #Setting some constants
    xe, ye, ze = sphere[0], sphere[1], sphere[2]
    radius = sphere[3]
    mag = sphere[4]
    
    # Distances in all axis directions - x, y e z
    rx = x - xe
    ry = y - ye
    rz = z - ze
    
    # Computes the distance (r) as the module of the other three components
    r2 = rx**2 + ry**2 + rz**2
        
    # Computes the magnetization values for all directions
    mx, my, mz = aux.dircos(A, B)
    
    # Auxiliar calculation
    dot = rx*mx + ry*my + rz*mz  # Scalar product
    m = (4.*np.pi*(radius**3)*mag)/3.    # Magnetic moment
    
    # Component calculation - Bx
    bx = m*(3.*dot*rx - (r2*mx))/(r2**(2.5))

    # Final component calculation
    bx *= cm*t2nt
    
    # Return the final output
    return bx

def sphere_by(x, y, z, sphere, direction):

    '''    
    It is a Python implementation for a Fortran subroutine contained in Blakely (1995). It 
    computes the Y component of the magnetic induction caused by a sphere with uniform  
    distribution of magnetization. The direction X represents the north and Z represents 
    growth downward. This function receives the coordinates of the points of observation 
    (X, Y, Z - arrays), the coordinates of the center  of the sphere (Xe, Ye, Ze), the 
    magnetization intensity M and the values for inclination and declination (in degrees). 
    The observation values are given in meters.
    
    Inputs: 
    x, y, z - numpy arrays - position of the observation points
    sphere[0, 1, 2] - arrays - position of the center of the sphere
    sphere[3] - float - value for the spehre radius  
    sphere[4] - flaot - magnetization intensity value
    direction - numpy array - inclination, declination values
    
    Outputs:
    By - induced field on Y direction
     
    Ps. The value for Z can be a scalar in the case of one depth, otherwise it can be a 
    set of points.    
    '''
    
    # Stablishing some conditions
    if x.shape != y.shape:
        raise ValueError("All inputs must have same shape!")
        
    # Calculates some constants
    t2nt = 1.e9 # Testa to nT - conversion
    cm = 1.e-7  # Magnetization constant
    
    # Setting the directions
    A, B = direction[0], direction[1]
    
    #Setting some constants
    xe, ye, ze = sphere[0], sphere[1], sphere[2]
    radius = sphere[3]
    mag = sphere[4]
    
    # Distances in all axis directions - x, y e z
    rx = x - xe
    ry = y - ye
    rz = z - ze
    
    # Computes the distance (r) as the module of the other three components
    r2 = rx**2 + ry**2 + rz**2
        
    # Computes the magnetization values for all directions
    mx, my, mz = aux.dircos(A, B)
    
    # Auxiliars calculations
    dot = rx*mx + ry*my + rz*mz  # Scalar product
    m = (4.*np.pi*(radius**3)*mag)/3.    # Magnetic moment
    
    # Component calculation - By
    by = m*(3.*dot*ry - (r2*my))/(r2**(2.5))
    
    # Final component calculation
    by *= cm*t2nt
    
    # Return the final output
    return by

def sphere_bz(x, y, z, sphere, direction):

    '''    
    It is a Python implementation for a Fortran subroutine contained in Blakely (1995). It 
    computes the Z component of the magnetic induction caused by a sphere with uniform  
    distribution of magnetization. The direction X represents the north and Z represents 
    growth downward. This function receives the coordinates of the points of observation 
    (X, Y, Z - arrays), the coordinates of the center of the sphere (Xe, Ye, Ze), the
    magnetization intensity M and the values for inclination and declination (in degrees). 
    The observation values are given in meters.
    
    Inputs: 
    x, y, z - numpy arrays - position of the observation points
    sphere[0, 1, 2] - arrays - position of the center of the sphere
    sphere[3] - float - value for the spehre radius  
    sphere[4] - flaot - magnetization intensity value
    direction - numpy array - inclination and declination values
    
    Outputs:
    Bz - induced field on Z direction
     
    Ps. The value for Z can be a scalar in the case of one depth, otherwise it can be a 
    set of points.
    '''
    
    # Stablishing some conditions
    if x.shape != y.shape:
        raise ValueError("All inputs must have same shape!")
    
    # Calculates some constants
    t2nt = 1.e9 # Testa to nT - conversion
    cm = 1.e-7  # Magnetization constant
    
    # Setting the directions
    A, B = direction[0], direction[1]
    
    #Setting some constants
    xe, ye, ze = sphere[0], sphere[1], sphere[2]
    radius = sphere[3]
    mag = sphere[4]
    
    # Distances in all axis directions - x, y e z
    rx = x - xe
    ry = y - ye
    rz = z - ze
    
    # Computes the distance (r) as the module of the other three components
    r2 = rx**2 + ry**2 + rz**2
    
    # Computes the magnetization values for all directions
    mx, my, mz = aux.dircos(A, B)
    
    # Auxiliars calculations
    dot = (rx*mx) + (ry*my) + (rz*mz)  # Scalar product
    m = (4.*np.pi*(radius**3)*mag)/3.    # Magnetic moment
    
    # Component calculation - Bz
    bz = m*(3.*dot*rz - (r2*mz))/(r2**(2.5))

    # Final component calculation
    bz *= cm*t2nt
    
    # Return the final output
    return bz

def sphere_tf(x, y, z, sphere, direction, field, F):
    
    '''    
    This function computes the total field anomaly produced due to a solid sphere, which has 
    its center located in xe, ye and ze, radius equals to r and also the magnetic property 
    (magnetic intensity). This function receives the coordinates of the points of observation 
    (X, Y, Z - arrays), the elements of the sphere, the values for inclination, declination and 
    azimuth (in one array only!) and the elements of the field (intensity, inclination, declination 
    and azimuth - IN THAT ORDER!). The observation values are given in meters.
    
    Inputs: 
    x, y, z - numpy arrays - position of the observation points
    sphere[0, 1, 2] - arrays - position of the center of the sphere
    sphere[3] - float - value for the spehre radius  
    sphere[4] - float - magnetization intensity value
    direction - numpy array - inclination and declination values
    field - numpy array - values for the field and its orientations
    
    Outputs:
    totalfield - numpy array - calculated total field anomaly
    
    Ps. The value for Z can be a scalar in the case of one depth, otherwise it can be a set of points.    
    '''
    
    # Stablishing some conditions
    if x.shape != y.shape:
        raise ValueError("All inputs must have same shape!")
       
    # Setting contants
    inc, dec = field[0], field[1]
    
    # Compute de regional field    
    reg = aux.regional(F, field)
    
    # Computing the components and the regional field
    bx = sphere_bx(x, y, z, sphere, direction) + reg[0]
    by = sphere_by(x, y, z, sphere, direction) + reg[1]
    bz = sphere_bz(x, y, z, sphere, direction) + reg[2]
    
    # Final value for the total field anomaly
    tf = np.sqrt(bx**2 + by**2 + bz**2) - F
    
    # Return the final output
    return tf

def sphere_tfa(x, y, z, sphere, direction, field):

    '''    
    This function computes the total field anomaly produced due to a solid sphere, which has 
    its center located in xe, ye and ze, radius equals to r and also the magnetic property 
    (magnetic intensity). This function receives the coordinates of the points of observation 
    (X, Y, Z - arrays), the elements of the sphere, the values for inclination, declination 
    and azimuth (in one array only!) and the elements of the field (intensity, inclination, 
    declination and azimuth - IN THAT ORDER!). The observation values are given in meters.
    
    Inputs: 
    x, y, z - numpy arrays - position of the observation points
    sphere[0, 1, 2] - arrays - position of the center of the sphere
    sphere[3] - float - value for the spehre radius  
    sphere[4] - flaot - magnetization intensity value
    direction - numpy array - inclination and declination values
    field - numpy array - inclination and declination values for the field
    
    Outputs:
    tf_aprox - numpy array - approximated total field anomaly
    
    Ps. The value for Z can be a scalar in the case of one depth, otherwise it can be a 
    set of points.    
    '''
    
    # Stablishing some conditions
    if x.shape != y.shape:
        raise ValueError("All inputs must have same shape!")
    
    # Setting some values
    inc, dec = field[0], field[1]
    
    # Compute de regional field    
    fx, fy, fz = aux.dircos(inc, dec)
    
    # Computing the components and the regional field
    bx = sphere_bx(x, y, z, sphere, direction)
    by = sphere_by(x, y, z, sphere, direction)
    bz = sphere_bz(x, y, z, sphere, direction)
    
    # Final value for the total field anomaly
    tf_aprox = fx*bx + fy*by + fz*bz
    
    # Return the final output
    return tf_aprox

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
        sphere[3] - radius
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
    radius = sphere[3]
    rho = sphere[4]
    
    # Definition for some constants
    G = 6.673e-11
    si2mGal = 100000.0
    
    # Compute the constant which is result due to the product
    const = (4./3.)*np.pi*rho*(radius**3)
    
    # Compute the distance
    r = np.sqrt(dx**2 + dy**2 + dz**2)
    
    # Compute the vertical component 
    gz += const*dz/(r**3)
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
    radius = sphere[3]
    rho = sphere[4]
    
    # Definition for some constants
    G = 6.673e-11
    si2mGal = 100000.0
    
    # Compute the constant which is result due to the product
    const = (4./3.)*np.pi*rho*(radius**3)
    
    # Compute the distance
    r = np.sqrt(dx**2 + dy**2 + dz**2)
    
    # Compute the vertical component 
    gx += const*dx/(r**3)
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
    radius = sphere[3]
    rho = sphere[4]
    
    # Definition for some constants
    G = 6.673e-11
    si2mGal = 100000.0
    
    # Compute the constant which is result due to the product
    const = (4./3.)*np.pi*rho*(radius**3)
    
    # Compute the distance
    r = np.sqrt(dx**2 + dy**2 + dz**2)
    
    # Compute the vertical component 
    gy += const*dy/(r**3)
    gy *= G*si2mGal
    
    # Return the final outpu
    return gy

