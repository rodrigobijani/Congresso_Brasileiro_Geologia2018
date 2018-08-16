# module with numeric issues:
import numpy as np
import scipy as sp
import warnings

def addnoise(data, v0, std):
    '''
    This function adds noise along the input data using a normal Gaussian distribution for each 
    point along the data set.
    If data is a numpy 1D array whit N elements, this function returns a simple length N vector, 
    else it returns a 2D array with NM elements.    
    '''
    assert np.min(data) <= np.mean(data), 'Mean must be greater than minimum'
    assert np.max(data) >= np.mean(data), 'Maximum must be greater than mean'
    assert std <= 10., 'Noise must not be greater than 1'
    assert std >= 1e-12, 'Noise should not be smaller than 1 micro unit'
    
    # Define the values for size and shape of the data
    size = data.size
    shape = data.shape
    
    # Creat the zero vector such as data
    noise = np.zeros_like(data)
    
    # Calculate the local number
    #local = np.abs((data.max() - data.min())*(1e-2))
    
    # Verify if data is a 1D or 2D array
    if data.shape[0] == size or data.shape[1] == size:
        noise = np.random.normal(loc = v0, scale = std, size = size)
    else:
        noise = np.random.normal(loc = v0, scale = std, size = shape)
        
    # Return the final output
    return data + noise
