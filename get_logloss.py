def get_logloss(actual, pred_probs, clipper=1e-14):

    """Takes two array-likes:
    actual: an array of actual labels
    pred_probs: an array of predicted probabilities
    and one float:
    clipper: a float defining the width of an offset from 0 and 1
    Outputs:
    logloss as a float"""
    
    if (clipper < 0) or (clipper >= 1):
        raise ValueError('`clipper` value has to be >= 0 and < 1')
        
    actual = np.array(actual)
    predicted = np.array(pred_probs)
    
    predicted = np.clip(predicted, clipper, 1-clipper)
    
    return -1 * (np.mean(actual * np.log(predicted) + (1 - actual) * np.log(1 - predicted)))
