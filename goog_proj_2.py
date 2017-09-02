from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree

iris = load_iris()
test_indx =[0, 50, 100]

train_target = np.delete(iris.target, test_indx)
train_data = np.delete(iris.data, test_indx, axis = 0)

test_target = iris.target[test_indx]
test_data = iris.data[test_indx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print(test_target)
print(clf.predict(test_data))

print(test_target[1])
