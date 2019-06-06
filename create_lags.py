import pandas as pd

def create_lags(df, cols, lags):
    lagged = df.assign(**{
            '{} (t-{})'.format(col, t): bb[col].shift(t)
                    for t in lags
                    for col in cols
            })
    return lagged
