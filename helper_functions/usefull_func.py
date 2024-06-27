import matplotlib.pyplot as plt
import numpy as np
import copy

def hist_wo_outliers(array_original, outlier_value=1000, show_outliers = False, mean_line = False, **kwargs):
    """
    Function to build histograms with option to process outliers
    
    Arguments
    ---------
    
    array_original - [list] - should be dimensionless
    
    outlier_value - int - value of outlier
    
    show_outliers - boolean - outlier visulation
    
    mean_line - boolean - show mean of the distribution
     
    """


    array = copy.copy(array_original)
    outliers = [value for value in array if value >= outlier_value]
    array = [value for value in array if value < outlier_value]
    if not show_outliers:
        z,x,c = plt.hist(array, **kwargs)
    else:
        outlier_hist = [outlier_value for _ in outliers]
        array.extend(outlier_hist)
        print(f"Number of outliers = {len(outlier_hist)}")
        z,x,c = plt.hist(array, **kwargs)
    plt.grid(alpha = 0.5)
    if mean_line:
        plt.axvline(x=np.mean(array), color='r', linestyle='--')
    print(f"Mean value of the x_axis = {np.mean(array)} \nStandard deviation = {np.std(array)}")
    

def atmo_thick(height, make_plot=False):
    """ 
    Function that returns atmospheric thickness in g/cm^2
    
    Arguments
    ---------
    height - [m]
        Height for which thickness should be calculated
        
    Returns
    -------
    value of the thickness [g/cm2] for given height
    """
    atmospheric_thickness = [1036, 920, 818, 726, 643, 568, 499, 438, 383, 333, 288, 249, 213, 182, 155, 132, 112, 95, 80, 67, 57]
    altitude = [i for i in range(21)]
    xvals = np.linspace(0, 20, 20000)

    interpolated_thickness = np.interp(xvals, altitude, atmospheric_thickness)
    if make_plot:
        plt.figure()
        plt.scatter(xvals, interpolated_thickness, alpha = 0.2)
        plt.grid()
    
    return interpolated_thickness[height]