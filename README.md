# Data Science Helper Functions
Quick helper functions for DS applications

* ## NaNer
  This function was created to deal with numerical columns that contain some unexpected string values. 
  NaNer tries to convert all the values into floats. If any element causes ValueError, NaNer converts this element into np.nan.
  
  Example usage:
  ```
  [1] your_df['YourColumn'].dtype
  >> dtype('O')
  
  [2] your_df['YourColumn'].transform(NaNer).dtype
  >> dtype('float64')
  ```
