#FUNCTION 1
### Function to calculate mean, median, variance, standard deviation, min, max
import numpy as np
gauteng = [39660.0,
            36024.0,
            32127.0,
            39488.0,
            18422.0,
            23532.0,
            8842.0,
            37416.0,
            16156.0,
            18730.0,
            19261.0,
            25275.0]

def dictionary_of_metrics(items):

    """ Calculates summary statistics of the given list :
    maximum, minimum, median, mean, variance, standard deviation 
    
    Parameters
    ----------
    items: A list of intergers/floats
    
    
    Returns
    -------
    dict: 
        Returns values of the dictionary as the summary staistics rounded
        off to two decimal places and the description
        of the values as keys."""    
    for item in items:
 # using numpy library to calculate mean, median, var and std        
        return {'mean': round(np.mean(items), 2),  'median': round(np.median(items), 2),
                'var': round(np.var(items, ddof = 1), 2), 
                'std': round(np.std(items, ddof = 1), 2),'min': round(min(items), 2),
                'max': round(max(items), 2)}
        

