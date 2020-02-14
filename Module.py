#FUNCTION 1

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
        return {'mean': round(np.mean(items), 2),  'median': round(np.median(items), 2),
                'var': round(np.var(items, ddof = 1), 2), 
                'std': round(np.std(items, ddof = 1), 2),'min': round(min(items), 2),
                'max': round(max(items), 2)}
        

### END FUNCTION 

<<<<<<< HEAD
#FUNCTION 2

def five_num_summary(items):
    # your code here
    a = 'max median min q1 q3'.split()
    b = [round(np.max(items),2),round(np.median(items),2),round(np.min(items),2),round(np.quantile(items,0.25),2),round(np.quantile(items, 0.75),2)]
   
    return dict( list(zip(a,b)))
=======
<<<<<<< HEAD
#FUNCTION 3
def date_parser(dates):
    data_format = []                 
    for i in dates:                  
        x =  i.split(" ")[0]        
        data_format.append(x)       
                                      
        
     
    return data_format               
=======
#FUNCTION 6
def word_splitter(df):
    
    split_tweets = []
    for index, row in df.iterrows():
        a = (row['Tweets'].split(' '))
        split_tweets.append([i.lower() for i in a])
    
   
    new_df = df.copy(deep=True)
    new_df['Split Tweets'] = split_tweets
    return new_df

>>>>>>> 6ca4870a7738ea3f5ab755257347088b77ddbae0
>>>>>>> cdfb992842ba647c63b27171ed5bad52dc039aea
