# Get sklearn metrics + confusion matrix

import re
import matplotlib.pyplot as plt
import seaborn as sns

def get_metrics(y_true, y_pred, metric=[f1_score]):
    for m in metric:
        metric_name = s = re.search('\s\S+\s', str(m)).group(0).strip()
        print(f'{metric_name:30}== {m(y_true, y_pred):.4f}')
    print('\n')
    print(classification_report(y_true, y_pred))
    print('\n')
    # Create conf mtrx
    mtrx = confusion_matrix(y_true, y_pred)
    sns.heatmap(mtrx.T, square=True, annot=True, fmt='d', cbar=False)
    plt.xlabel('true label')
    plt.ylabel('predicted label')
    plt.title('Confusion matrix')
    plt.show()
