#FIle Input                                             FEATURE ENGINEER                                                                (LABEL)
#Time by x   | Bitcoin Val | Ethereum Val ||| Bitcoin change/x | Ethereum change/x | Difference of (Bit ch/x) - (Eth ch/x) ||| Etherium change/x at n rows in advance |
#------------|-------------|--------------|||------------------|-------------------|---------------------------------------|||----------------------------------------|
#x=1/10/30min| value       |  value       ||| (r(sub n) - r(sub n-1)) / r(sub n-1) | bitcoin change/x - Ethereum change/x  ||| (Etherium change/x)sub n + (intveral of desired pred time)

# imports up here can be used to 
import pandas as pd
import numpy as np

def azureml_main(Bitcoin_df, Ethereum_df):

    # Execution logic goes here
    print('Input pandas.DataFrame #1:\r\n\r\n{0}'.format(Bitcoin_df))
    
    del Bitcoin_df['low']
    del Bitcoin_df['high']
    del Bitcoin_df['open']
    del Bitcoin_df['Column 0']
    #Bitcoin_df.rename(columns = {'close':'BTCval'})
    Bitcoin_df.rename(
    columns={
        'close' : 'BTCval'
    },
    inplace=True
    )
    
    del Ethereum_df['low']
    del Ethereum_df['high']
    del Ethereum_df['open']
    del Ethereum_df['volume']
    del Ethereum_df['time']
    del Ethereum_df['Column 0']
    Ethereum_df.rename(columns = {'close':'ETHval'})
    Ethereum_df.rename(
    columns={
        'close' : 'ETHval'
    },
    inplace=True
    )
    
    
    
    
    combined_df = pd.concat([Bitcoin_df,Ethereum_df], axis=1)
    
    
    
    #######################  Add the columns
    
    
    combined_df['Ethereum Prediction'] = 0  #Do plus 5 for now
    BTC_val_ind = 1
    ETH_val_ind = 3
            
            
    rows, cols = combined_df.shape
    rowCount_int = 0
    predictAhead =  1 #1
    
    
    while rowCount_int < rows - predictAhead:
        if (rowCount_int > 1):
            #Calculate BTC val and BTC val at (position -1)
            BTC_valCurrent_float = (combined_df.iloc[rowCount_int,BTC_val_ind])
            BTC_valPrevious_float = (combined_df.iloc[rowCount_int - 1,BTC_val_ind])
            BTC_percentChange_float = (BTC_valCurrent_float - BTC_valPrevious_float) / (BTC_valPrevious_float)
            combined_df.at[rowCount_int, 'BTC % Change 1min'] = BTC_percentChange_float
            
            #ETH_valCurrent_float = (combined_df.iloc[rowCount_int,ETH_val_ind])
            #ETH_valPrevious_float = (combined_df.iloc[rowCount_int - 1,ETH_val_ind])
            #ETH_percentChange_float = (ETH_valCurrent_float - ETH_valPrevious_float) / (ETH_valPrevious_float)
            BTC_valCurrent_float = (combined_df.iloc[rowCount_int,BTC_val_ind])
            BTC_valPrevious_float = (combined_df.iloc[rowCount_int - 1,BTC_val_ind])
            BTC_percentChange_float = (BTC_valCurrent_float - BTC_valPrevious_float) / (BTC_valPrevious_float)
            combined_df.at[rowCount_int, 'ETH % Change 1min'] = BTC_percentChange_float
                        
            #ETH_valCurrent_float = (combined_df.iloc[rowCount_int,ETH_val_ind])
            #ETH_valPrevious_float = (combined_df.iloc[rowCount_int - 1,ETH_val_ind])
            #ETH_percentChange_float = (ETH_valCurrent_float - ETH_valPrevious_float) / (ETH_valPrevious_float)
    
            #combined_df.at[rowCount_int, 'ETH % Change'] = ETH_percentChange_float
                        
            #combined_df.at[rowCount_int, 'Difference'] = BTC_percentChange_float - ETH_percentChange_float
                        
            combined_df.at[rowCount_int, 'Ethereum Prediction'] = (combined_df.iloc[rowCount_int +  predictAhead, ETH_val_ind])
            
            
        if (rowCount_int > 2):
            BTC_valCurrent_float = (combined_df.iloc[rowCount_int,BTC_val_ind])
            BTC_valPrevious_float = (combined_df.iloc[rowCount_int - 2,BTC_val_ind])
            BTC_percentChange_float = (BTC_valCurrent_float - BTC_valPrevious_float) / (BTC_valPrevious_float)
            combined_df.at[rowCount_int, 'BTC % Change 2min'] = BTC_percentChange_float
                        
            BTC_volumeCurrent_float = (combined_df.iloc[rowCount_int,BTC_val_ind])
            BTC_volumePrevious_float = (combined_df.iloc[rowCount_int - 2,BTC_val_ind])
            BTC_volumeChange_float = (BTC_volumeCurrent_float - BTC_volumePrevious_float) / (BTC_volumePrevious_float)
            combined_df.at[rowCount_int, 'BTC Vol Change 2min'] = BTC_volumeChange_float
        
        if (rowCount_int > 3):
            BTC_valCurrent_float = (combined_df.iloc[rowCount_int,BTC_val_ind])
            BTC_valPrevious_float = (combined_df.iloc[rowCount_int - 3,BTC_val_ind])
            BTC_percentChange_float = (BTC_valCurrent_float - BTC_valPrevious_float) / (BTC_valPrevious_float)
            combined_df.at[rowCount_int, 'BTC % Change 3min'] = BTC_percentChange_float
                        
            BTC_volumeCurrent_float = (combined_df.iloc[rowCount_int,BTC_val_ind])
            BTC_volumePrevious_float = (combined_df.iloc[rowCount_int - 3,BTC_val_ind])
            BTC_volumeChange_float = (BTC_volumeCurrent_float - BTC_volumePrevious_float) / (BTC_volumePrevious_float)
            combined_df.at[rowCount_int, 'BTC Vol Change 3min'] = BTC_volumeChange_float
        
        if (rowCount_int > 4):
            BTC_valCurrent_float = (combined_df.iloc[rowCount_int,BTC_val_ind])
            BTC_valPrevious_float = (combined_df.iloc[rowCount_int - 4,BTC_val_ind])
            BTC_percentChange_float = (BTC_valCurrent_float - BTC_valPrevious_float) / (BTC_valPrevious_float)
            combined_df.at[rowCount_int, 'BTC % Change 4min'] = BTC_percentChange_float
                        
            BTC_volumeCurrent_float = (combined_df.iloc[rowCount_int,BTC_val_ind])
            BTC_volumePrevious_float = (combined_df.iloc[rowCount_int - 4,BTC_val_ind])
            BTC_volumeChange_float = (BTC_volumeCurrent_float - BTC_volumePrevious_float) / (BTC_volumePrevious_float)
            combined_df.at[rowCount_int, 'BTC Vol Change 4min'] = BTC_volumeChange_float
        
        if (rowCount_int > 5): 
            BTC_valCurrent_float = (combined_df.iloc[rowCount_int,BTC_val_ind])
            BTC_valPrevious_float = (combined_df.iloc[rowCount_int - 5,BTC_val_ind])
            BTC_percentChange_float = (BTC_valCurrent_float - BTC_valPrevious_float) / (BTC_valPrevious_float)
            combined_df.at[rowCount_int, 'BTC % Change 5min'] = BTC_percentChange_float
                        
            BTC_volumeCurrent_float = (combined_df.iloc[rowCount_int,BTC_val_ind])
            BTC_volumePrevious_float = (combined_df.iloc[rowCount_int - 5,BTC_val_ind])
            BTC_volumeChange_float = (BTC_volumeCurrent_float - BTC_volumePrevious_float) / (BTC_volumePrevious_float)
            combined_df.at[rowCount_int, 'BTC Vol Change 5min'] = BTC_volumeChange_float
                        
            diffband_float = ((combined_df.iloc[rowCount_int,BTC_val_ind]) - (combined_df.iloc[rowCount_int,ETH_val_ind])) / ((combined_df.iloc[rowCount_int - 4,BTC_val_ind]) - (combined_df.iloc[rowCount_int - 4,ETH_val_ind]))
            combined_df.at[rowCount_int, 'diffban'] = diffband_float
                        
                        
        rowCount_int = rowCount_int + 1
        
    #Drop unused rows
    
    #combined_df = combined_df.iloc[:rows - predictAhead]
    
    
    combined_df['BTC Rolling avg 5min'] = pd.rolling_mean(combined_df['BTCval'], 5)
    combined_df.drop(combined_df.index[[0,1,2,3,4,5]], inplace=True)
    combined_df['percent change BTC rollavg'] = ((combined_df['BTCval'] - combined_df['BTC Rolling avg 5min']) / combined_df['BTC Rolling avg 5min'])
    combined_df.drop(combined_df.index[[-1]], inplace=True)
    
    
    # Return value must be of a sequence of pandas.DataFrame
    return combined_df
