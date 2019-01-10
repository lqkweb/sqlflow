#!/usr/bin/env python  
# encoding: utf-8  

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# 加载数据
iris_dataset = load_iris()

# 实例化模型
knn = KNeighborsClassifier(n_neighbors=1)

# 切分训练和测试数据集
X_train, X_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"], random_state=0)

# 训练
knn.fit(X_train, y_train)

# 评估模型
print("Test set score:{:.2f}".format(knn.score(X_test, y_test)))

# 预测
X_new = np.array([[5, 2.9, 1, 0.2]])
prediction = knn.predict(X_new)
print("Predicted target name:{}".format(iris_dataset["target_names"][prediction]))
