#FUNCTION 1
### Function to calculate mean, median, variance, standard deviation, min, max
import numpy as np
import pandas as pd

def dictionary_of_metrics(items):
    """Calculates summary statistics of the given list :
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
    # using numpy library to calculate mean, median, min, max, var and std        
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
        Returns a dictionary of summary statistics rounded
        off to two decimal places with the name of the results 
        as keys and the results as the corresponding value.
        
    """
    
    key = 'max median min q1 q3'.split()
    values = [round(np.max(items),2),round(np.median(items),2),
         round(np.min(items),2),round(np.quantile(items,0.25),2),
         round(np.quantile(items, 0.75),2)]
   
    return dict( list(zip(key,values)))



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
    data_format = []                 #Empty list.
    for i in dates:                  #Iterate over elements of dates.
        x =  i.split(" ")[0]         #Split the strings in dates to get rid of the times.
        data_format.append(x)        #append splitted strings to the empty list 'data_format'
                                      
        
     
    return data_format               #Return the new list 'data_format'.
   

###FUNCTION 4

def extract_municipality_hashtags(df):
    '''
    Finds the municipality and hashtags of from tweets.
    
    Parameters
    ----------
    df: dataframe containing tweets and dates of those tweets
    
    External Requirements
    ----------------------
    mun_dict: A dictionary that contains handles and corresponding municipalities

    Returns
    -------
    df: modified dataframe with municipality and hashtags 
    columns corresponding to every tweet 
    '''

    mun_list = []
    hash_list = []

    #Iterates though df.
    for index, row in df.iterrows():
        tweet = row["Tweets"].split()
        hashtags = []

        #Municipality is initial set to NaN.
        municipality = np.nan
        for word in tweet:
            if word[0]=='#':
                #Append hashtags to hash_list.
                hashtags.append(word.lower()) 
            elif word[0] =='@':
                if word in mun_dict.keys():
                    #Append municipalities to mun_list.
                    municipality = mun_dict[word]
        
        #Assigns Nan to hashtags if none are found.
        if len(hashtags)==0:
            hashtags = np.nan
        hash_list.append(hashtags)
        mun_list.append(municipality)
    
    #Adds 'municipality' and 'hashtags' columns to df.
    df['municipality'] = mun_list
    df['hashtags'] = hash_list
    
    return df
### END FUNCTION

### FUNCTION 5

def number_of_tweets_per_day(df):
    '''
    Counts the number of tweets per day
    
    Parameters
    ----------
    df: dataframe containing tweets and dates of those tweets
    
    Returns
    -------
    new_df: dataframe with dates of tweets and number of tweets 
    on that day
    '''

    dates = []
    for index, row in df.iterrows():
        dates.append(row['Date'].split(' ')[0])

    dates_count = []
    count = []
    
    #Appends unique dates to dates_count.
    for i in dates:
        if i in dates_count:
            continue
        else:
            count.append(dates.count(i))
            dates_count.append(i)
    
    #Creates new dataframe.
    new_df = pd.DataFrame()
    
    #Adds 'Date' and 'Tweets' columns to new_df.
    new_df['Date'] = pd.to_datetime(dates_count[::-1])
    new_df['Tweets'] = count[::-1]
    
    return new_df.set_index('Date')

### END FUNCTION



#FUNCTION 6

def word_splitter(df):
    '''
    Splits given tweets and adds them another column in given dataframe
    
    Parameters
    ----------
    df: dataframe containing tweets and dates of those tweets
    
    Returns
    --------
    df: modified dataframe with 'Split Tweets' added column
    '''

    #split tweets in df and append them to a new list 
    split_tweets = []
    for index, row in df.iterrows():
        tweet = (row['Tweets'].split(' '))
        split_tweets.append([i.lower() for i in tweet])
    
    #Add to new column in df
    df['Split Tweets'] = split_tweets
    
    return df


### FUNCTION 7

def stop_words_remover(df):
    '''
    Splits given tweets and removes 'stopwords' from them
    
    Parameters
    ----------
    df: dataframe containing tweets and dates of those tweets

    External Requirements
    ---------------------
    stop_words_dict: A dictionary that contains stop words
    
    Returns
    --------
    df: modified dataframe with 'Without Stop Words' added column
    '''
    #splits and appends tweets without stopwords to a list
    split_tweets = []
    for i in df['Tweets']:
        tweet = []
        for j in i.split(" "):
            if j.lower() in stop_words_dict['stopwords'] or j == '':
                continue
            else:
                tweet.append(j.lower())
        split_tweets.append(tweet)
    #Add 'Without Stop Words' column to df    
    df['Without Stop Words']  = split_tweets    
    return df