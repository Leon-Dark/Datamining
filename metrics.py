# -*- coding: utf-8 -*-

import numpy as np
from sklearn.metrics import normalized_mutual_info_score
from sklearn import metrics
nmi = normalized_mutual_info_score
homogeneity=metrics.homogeneity_score
completeness=metrics.completeness_score
v_measure=metrics.v_measure_score
def acc(y_true, y_pred):
    y_true=np.array(y_true)
    y_true = y_true.astype(np.int64)
    assert y_pred.size == y_true.size
    D = max(y_pred.max(), y_true.max()) + 1
    w = np.zeros((D, D), dtype=np.int64)
    for i in range(y_pred.size):
        w[y_pred[i], y_true[i]] += 1
    from sklearn.utils.linear_assignment_ import linear_assignment
    ind = linear_assignment(w.max() - w)
    return sum([w[i, j] for i, j in ind]) * 1.0 / y_pred.size
