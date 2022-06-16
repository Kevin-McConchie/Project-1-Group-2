import pandas as pd

def get_participant_count(p_value):
  
    #global df
    l_return = []
    try:
        for dat in p_value: #original value from the dataframe
            
            
            l_series = []
            dat2 = dat.split('||')    # double pipes removed

            
            for d in dat2: #for each series item created from the original file, another loop initiated to remove :: and create clean data

                dat3 = d.split('::')

        
                l_series.append(dat3)

        
            l_return.append(l_series)
            result = len(l_return)
    except Exception as e:
        print(e)  
        l_return = ''
    
    return l_return    