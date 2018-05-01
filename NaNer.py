# This function was created to deal with numerical columns that contain some unexpected string values. 
# NaNer converts all string values into np.nans

def NaNer(x):
    
    """Takes a value and converts it into a float. 
    If ValueError: returns np.nan
    Originally designed to use with pandas DataFrames.
    
    Example: your_df['YourColumn'].transform(NaNer)
    """
    
    try:
        x = float(x)
    except ValueError:
        x = np.nan
        
    return x
