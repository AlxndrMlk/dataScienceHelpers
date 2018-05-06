from statsmodels.stats.outliers_influence import variance_inflation_factor as vif

def get_vif(X):
    
    if isinstance(data, pd.DataFrame) == False:
        X = pd.DataFrame(X)
    
    X['__INTERCEPT'] = np.ones(X.shape[0])
    
    for i in range(X.shape[1]-1):
        the_vif = vif(X.values, i)
        print("VIF for column {:03}: {:.02f}".format(i, the_vif))
