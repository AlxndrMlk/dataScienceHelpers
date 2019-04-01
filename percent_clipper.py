import numpy as np

def percent_clipper(x, percentiles):
  """
  Takes data as np.ndarray and percentiles as array-like
  Returns clipped ndarray
  """
  
  LOWERBOUND, UPPERBOUND = np.percentile(x, [percentiles[0], percentiles[1])
  
  return np.clip(x, LOWERBOUND, UPPERBOUND)
