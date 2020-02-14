#FUNCTION 1

def dictionary_of_metrics(items):
    for item in items:
        return {'mean': round(np.mean(items), 2),  'median': round(np.median(items), 2),
                'var': round(np.var(items, ddof = 1), 2), 
                'std': round(np.std(items, ddof = 1), 2),'min': round(min(items), 2),
                'max': round(max(items), 2)}
        

### END FUNCTION 

#FUNCTION 2

def five_num_summary(items):
    # your code here
    a = 'max median min q1 q3'.split()
    b = [round(np.max(items),2),round(np.median(items),2),round(np.min(items),2),round(np.quantile(items,0.25),2),round(np.quantile(items, 0.75),2)]
   
    return dict( list(zip(a,b)))
