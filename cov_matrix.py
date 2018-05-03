import numpy as np

def cov_matrix(A, sample=True):
    """
    Input:
    A:             2D-numpy array
    sample (bool): if true compute sample covariance matrix
                   if false compute population covariance matrix
    Output:
    Covariance matrix as 2D-numpy array
                   """
    if sample < 0 or sample > 1:
        raise ValueError('`sample` parameter has to be 0 or 1')
    
    m = A.shape[0]
    e = np.ones(m)
    X = A - (1/(m))*np.dot(e, A)
    Y = np.dot(X.T, X)
    Sigma = (1/(m-sample))*Y
    
    return Sigma
