# Data Science / Machine Learning Helper Functions
Quick helper functions for DS/ML applications

* ## NaNer
  This function was created to deal with numerical columns that contain some unexpected string values. 
  NaNer tries to convert all the values into floats. If any element causes ValueError, NaNer converts this element into np.nan.
  
  Example:
  ```python
  >> import pandas as pd
  >> import numpy as np
  
  >> your_df = pd.DataFrame({'YourColumn': [1, 2, 3, 4, np.nan, 'nan', 5, 6, 'unknown']})
  
  >> your_df['YourColumn'].dtype
  dtype('O')
  
  >> your_df['YourColumn'].transform(NaNer)
  0    1.0
  1    2.0
  2    3.0
  3    4.0
  4    NaN
  5    NaN
  6    5.0
  7    6.0
  8    NaN
  Name: YourColumn, dtype: float64
  ```
  
* ## cov_matrix
  Takes a matrix as 2D numpy.array and return covariance matrix. ```cov_matrix(X)``` default result is compatible with MATLAB/Octave ```cov(X)``` and ```numpy.cov(X, rowvars=False)```.
  
* ## get_logloss
  Takes two array-likes: 
    * actual labels 
    * predicted probabilities
    
  and one float:
    * clipper (width of offset from 0 and 1)
    
  Returns log loss as a float.
 
 
  Example:
  ```python
  >> labels = [1, 0, 1, 1]
  
  >> pred_probs = [0.9, 0.4, 0.2, 0.87]

  >> get_logloss(labels, pred_probs, clipper=1e-14)

  0.5912215297978562
  ```
  
* ## multiclass
  A group of functions to work with multi-class data including ```multilabel_train_test_split()``` for multiclass stratified splitting.
  Code written by **Peter Bull**. Original repo: https://github.com/drivendataorg/box-plots-sklearn/blob/master/src/data/multilabel.py
