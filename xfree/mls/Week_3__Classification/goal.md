# Instructions

This week, you'll learn the other type of supervised learning, classification.
You'll learn how to predict categories using the logistic regression model.

> - predict: 预测
> - categories: 类别

You'll learn about the problem of overfitting, and how to handle this problem with a method called regularization.

> - overfitting: 过拟合
> - handle: 处理
> - called: 称为
> - regularization: 正则化

You'll get to practice implementing logistic regression with regularization at the end of this week.

> - get to: 得以
> - practice: 实践
> - implementing: 实现

# Learning Objectives

- Use logistic regression for binary classification

> - for: 用于(表示目的或用途)
> - binary classification: 二元分类

- Implement logistic regression for binary classification

> - Implement: 实现

- Address overfitting using regularization, to improve model performance
  > - Address: 处理
  > - regularization: 正则化
  > - improve: 改进
  > - model performance: 模型性能

# 1. Classification with logistic regression: 分类与逻辑回归

- [1.1 Motivations](./video/motivations/motivations_summary.md)

1. 线性回归不适用于分类问题
2. 引入逻辑回归算法
3. 分类问题的实例
4. 二元分类问题
5. 分类问题的表示方法
6. 线性回归在分类问题中的局限性:用线性回归时，添加一个训练样本可能会导致决策边界发生不合理的变化
7. 逻辑回归的优势:逻辑回归的输出值总是在 0 和 1 之间，这使得它在处理分类问题时避免了线性回归所遇到的问题
8. 逻辑回归与线性回归的区别
9. 线性回归用于分类的实验:在可选实验室中，会看到当尝试使用线性回归进行分类时会发生什么，以及为什么这通常不会奏效

- #Lab [Lab: Classification](./lab/C1_W3_Lab01_Classification_Soln.ipynb)
- [1.2 Logistic regression](./video/logistic-regression/logistic-regression_summary.md)

1. 逻辑回归是最广泛使用的分类算法
2. 逻辑回归在实际工作中的应用
3. 逻辑回归用于分类问题，如判断肿瘤是否恶性
4. 逻辑回归与线性回归的不同
5. 逻辑回归的输出解释
6. Sigmoid 函数的重要性
7. Sigmoid 函数的公式和特性
8. 逻辑回归模型的构建
9. 逻辑回归输出的解释：概率预测
10. 逻辑回归在广告领域的应用

- #Lab [Lab: Sigmoid function and logistic refression](./lab/C1_W3_Lab02_Sigmoid_function_Soln.ipynb)
- [1.3 Decision boundary](./video/decision-boundary/decision-boundary_summary.md)

1. 决策边界的概念
2. 逻辑回归模型的输出计算
3. 预测阈值：模型通过设置阈值来预测`y`的值，常见的阈值为 0.5
4. 决策边界的确定：模型预测`1`的条件是`w.x + b >=  0`，反之预测`0`
5. 多特征下的决策边界
6. 非线性决策边界：通过使用多项式特征，逻辑回归可以拟合更复杂的决策边界，如圆形或椭圆形
7. 复杂度的控制:如果不使用高阶多项式特征，逻辑回归的决策边界将始终是线性的

- #Lab [Lab: Decision boundary](./lab/C1_W3_Lab03_Decision_Boundary_Soln.ipynb)
- #Quiz [Quiz: Classification with logistic regression](./W3_1_Quiz.ipynb)

# 2. Cost function for logistic regression

- [Cost function for logistic regression](./video/cost-function-for-logistic-regression/cost-function-for-logistic-regression_summary.md)

1. 成本函数的作用：衡量特定参数集对训练数据的拟合程度
2. 平方误差不是逻辑回归的理想成本函数
3. 逻辑回归模型的训练集
4. 平方误差成本函数的问题
5. 逻辑回归的新成本函数：$J(w, b) = 1/2 * Σ(y * log(f(x)) + (1-y) * log(1-f(x)))$
6. 新成本函数的损失函数
7. 成本函数的凸性
8. 成本函数的计算

- #Lab [Lab: Logistic loss](./lab/C1_W3_Lab04_LogisticLoss_Soln.ipynb)
- [Simplified Cost Function for Logistic Regression](./video/simplified-cost-function-for-logistic-regression/simplified-cost-function-for-logistic-regression_summary.md)
- #Lab [Lab: Cost function for logistic regression](./lab/C1_W3_Lab05_Cost_Function_Soln.ipynb)
- #Quiz [Cost function for logistic regression](./W3_2_Quiz.ipynb)

# 3. Gradient descent for logistic regression

- [Gradient Descent Implementation](./video/W3_3.1_Gradient_Descent_Implementation.md)
- #Lab [Gradient descent for logistic regression](./lab/C1_W3_Lab06_Gradient_Descent_Soln.ipynb)
- #Lab [Logistic regression with scikit-learn](./lab/C1_W3_Lab07_Scikit_Learn_Soln.ipynb)
- #Quiz [Gradient descent for logistic regression](./W3_3_Quiz.ipynb)

# 4. The problem of overfitting

- [The problem of overfitting](./video/W3_4.1_The_Problem_Of_Overfitting.md)
- [Addressing overgitting](./video/W3_4.2_Address_Overfitting.md)
  > - Addressing: 处理
- #Lab [Lab: Overfitting](./lab/C1_W3_Lab08_Overfitting_Soln.ipynb)
- [Cost function with refularization](./video/W3_4.3_Cost_Function_With_Regularization.md)
- [Regularized linear regression](./video/W3_4.4_Regularized_Linear_Regression.md)
- [Regularized logistic regression](./video/W3_4.5_Regularized_Logistic_Regression.md)
- #Lab [Lab: Regularization](./lab/C1_W3_Lab09_Regularization_Soln.ipynjsonb)
  > - Regularization: 正则化
- #Quiz [The problem of overfitting](./W3_4_Quiz.ipynb)

# Lab: Logistic regression with regularization
