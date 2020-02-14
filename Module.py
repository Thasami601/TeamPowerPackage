#FUNCTION 1
### Function to calculate mean, median, variance, standard deviation, min, max
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
    
    # using numpy library to calculate mean, median, var and std
    for item in items:
        return {'mean': round(np.mean(items), 2),  'median': round(np.median(items), 2),
                'var': round(np.var(items, ddof = 1), 2), 
                'std': round(np.std(items, ddof = 1), 2),'min': round(min(items), 2),
                'max': round(max(items), 2)}
        

### END FUNCTION 

#FUNCTION 2
def five_num_summary(items):
    """ Calculates summary statistics of the given list :
    maximum, minimum, median, quartile 1, quartile 3
    
    Parameters
    ----------
    items: A list of intergers/floats
    
    
    Returns
    -------
    dict: 
        Returns values of the dictionary as the summary staistics rounded
        off to two decimal places and the description
        of the values as keys.
    
    """
    # your code here
    a = 'max median min q1 q3'.split()   #Creates a list with keys for the dictionary
    b = [round(np.max(items),2),round(np.median(items),2),
         round(np.min(items),2),round(np.quantile(items,0.25),2),
         round(np.quantile(items, 0.75),2)]   #Creates a list of values for the dictionary
   
    return dict( list(zip(a,b)))   #returns a dictionary matching the keys and values from the lists


#FUNCTION 3
def date_parser(dates):
    
    """Date Parser - changes dates to date format 'yyyy-mm-dd'  
        
        Parameters
        ----------
        dates: list
                list of datetime strings in the format 'yyyy-mm-dd hh:mm:ss'
        
        Returns
        -------
        A list of only the date in 'yyyy-mm-dd' format.
    """  
    # your code here
    
    data_format = []                 #Empty list.
    for i in dates:                  #Iterate over elements of dates.
        x =  i.split(" ")[0]         #Split the strings in dates to get rid of the times.
        data_format.append(x)        #append splitted strings to the empty list 'data_format'
                                      
        
     
    return data_format               #Return the new list 'data_format'.

#FUNCTION 6
def word_splitter(df):
    '''word_split - split tweets in the dataframe and append them to a new list  
        
        Parameters
        ----------
        df: dataframe 
    
        
        Returns
        -------
        splited tweets in lowercase and merges and merges 
        the new list into the dataframe column'''

    
    
    split_tweets = []
    for index, row in df.iterrows():
        a = (row['Tweets'].split(' '))
        split_tweets.append([i.lower() for i in a])
    
    #Add to new column in df
    new_df = df.copy(deep=True)
    new_df['Split Tweets'] = split_tweets
    return new_df

