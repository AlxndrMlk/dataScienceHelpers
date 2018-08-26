def generate_report(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred)
    print(' TN | FP\n FN | TP')
    print(cm)
    print('\n')
    print(classification_report(y_test, y_pred))
    print('Accuracy: {:.2f}'.format((cm[0,0]+cm[1,1]) / (cm[0,0]+cm[0,1]+cm[1,0]+cm[1,1])))
