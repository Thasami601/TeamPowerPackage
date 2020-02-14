#FUNCTION 1

def dictionary_of_metrics(items):
    for item in items:
        return {'mean': round(np.mean(items), 2),  'median': round(np.median(items), 2),
                'var': round(np.var(items, ddof = 1), 2), 
                'std': round(np.std(items, ddof = 1), 2),'min': round(min(items), 2),
                'max': round(max(items), 2)}
        

### END FUNCTION 

#FUNCTION 3
def date_parser(dates):
    data_format = []                 
    for i in dates:                  
        x =  i.split(" ")[0]        
        data_format.append(x)       
                                      
        
     
    return data_format               
