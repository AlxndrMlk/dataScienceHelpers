def get_cv_params(X, y, estimator, params, cv=5, scoring=None):
    estimator_cv = GridSearchCV(estimator, params, cv=cv, scoring=scoring)
    estimator_cv.fit(X, y)
    return estimator_cv.best_score_, estimator_cv.best_params_
