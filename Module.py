#FUNCTION 1

def dictionary_of_metrics(items):
    for item in items:
        return {'mean': round(np.mean(items), 2),  'median': round(np.median(items), 2),
                'var': round(np.var(items, ddof = 1), 2), 
                'std': round(np.std(items, ddof = 1), 2),'min': round(min(items), 2),
                'max': round(max(items), 2)}
        

### END FUNCTION 

#FUNCTION 2
def word_splitter(df):
    
    split_tweets = []
    for index, row in df.iterrows():
        a = (row['Tweets'].split(' '))
        split_tweets.append([i.lower() for i in a])
    
   
    new_df = df.copy(deep=True)
    new_df['Split Tweets'] = split_tweets
    return new_df

