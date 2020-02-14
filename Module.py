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
        

<<<<<<< HEAD
### END FUNCTION

###FUNCTION4

def extract_municipality_hashtags(df):
    
    mun_list = []
    hash_list = []

    for index, row in df.iterrows():
        tweet = row["Tweets"].split()
        hashtags = []

        municipality = np.nan
        for word in tweet:
            if word[0]=='#':
                hashtags.append(word.lower()) 
            elif word[0] =='@':
                if word in mun_dict.keys():
                    municipality = mun_dict[word]

        if len(hashtags)==0:
            hashtags = np.nan
        hash_list.append(hashtags)
        mun_list.append(municipality)

    df['municipality'] = mun_list
    df['hashtags'] = hash_list
    
    return df
### END FUNCTION

### FUNCTION 5

def number_of_tweets_per_day(df):

    dates = []
    for index, row in df.iterrows():
        dates.append(row['Date'].split(' ')[0])

    dates_count = []
    count = []

    for i in dates:
        if i in dates_count:
            continue
        else:
            count.append(dates.count(i))
            dates_count.append(i)
 
    new_df = pd.DataFrame()
    new_df['Date'] = pd.to_datetime(dates_count[::-1])
    new_df['Tweets'] = count[::-1]
    
    return new_df.set_index('Date')

### END FUNCTION

### FUNCTION 7

def stop_words_remover(df):

    split_tweets = []
    for index,row in df.iterrows():
        tweet = row['Tweets'].split(" ")
        split_tweets.append([i.lower() for i in tweet if i.lower() not in stop_words_dict['stopwords']])
    df['Without Stop Words'] = split_tweets
    return df

### END FUNCTION
=======
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
     """Date Parser - changes dates to date format 'yyyy-mm-dd'  
        
        Parameters
        ----------
        dates: list
                list of datetime strings in the format 'yyyy-mm-dd hh:mm:ss'
        
        Returns
        -------
        A list of only the date in 'yyyy-mm-dd' format.
        """"
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
>>>>>>> 7d33a759cdc7f9d2c1964b0d4bd5676c6e3705f5
