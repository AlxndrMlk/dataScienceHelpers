def get_cv_info(model, X, y, cv=5, scoring=None):
    cv_score = cross_val_score(model, X, y, cv=cv, scoring=scoring)
    stability = cv_score.std()*100/cv_score.mean()
    print('CV scores: {}\nMean score: {}\nStability: {:.3f}%\n_________'\
          .format(cv_score, np.mean(cv_score), stability))
