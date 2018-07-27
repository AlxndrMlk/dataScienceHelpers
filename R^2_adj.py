def get_R2_adj(X_test, y_test, y_pred):
    """Computes and returns adjusted R^2 value"""
    return 1 - (1-r2_score(y_test, y_pred))*(len(y_test)-1)/(len(y_test)-X_test.shape[1]-1)
