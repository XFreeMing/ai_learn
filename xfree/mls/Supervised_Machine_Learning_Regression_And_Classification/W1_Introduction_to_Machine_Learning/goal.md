# Instructions
Welcome to the Machine Learning Specialization!
> 欢迎来到机器学习专业化课程！
You're joining millions of others who have taken either this or the original course, which led to the founding of Coursera,and has helped mullions of other learners, like you, take a look at the exciting world of machine learning!
> 你将加入数百万其他学习者，他们已经参加了这门课程或原始课程，这些课程导致了Coursera的成立，并帮助了数百万其他学习者，比如你，了解令人兴奋的机器学习世界！


# Learning Objectives

- Define machine learning
- Define supervised learning
1. 使用带有正确答案的数据来训练模型。
- Define unsupervised learning
- Write and run Python code in Jupyter Notebooks
- Define a regression model
> 它使用单一输入变量进行预测，也称为一元线性回归
- implement and visualize a cost function
> 实现和可视化成本函数
- implement gradient descent
> 实现梯度下降
- Optimize a regression model using gradient descent
> 使用梯度下降优化回归模型

# 1. Overview of Machine Learning

- [1.1 Welcome to machine learning](./video/W1_1.1_Welcome_To_Maching_Learning.md)
- [1.2 Application of machine learning](./video/W1_1.2_Application_Of_Machine_Learning.md)

# 2. Supervised vs. Unsupervised Machine Learning

- [2.1 What is machine learning](./video/W1_2.1_What_Is_Machine_Learning.md)
- [2.2 Supervised learning part1](./video/W1_2.2_Supervised_Learning_Part1.md)
- [2.3 Supervised learning part2](./video/W1_2.3_Supervised_Learning_Part2.md)
- [2.4 Unsupervised learning part1](./video/W1_2.4_Unsupervised_Learning_Part1.md)
- [2.5 Unsupervised learning part2](./video/W1_2.5_Unsupervised_Learning_Part2.md)
- [2.6 Jupyter Notebook](./video/W1_2.6_Jupyter_Notebooks.md)
- [Lab:Python And Jupyter Notebook](./lab/C1_W1_Lab01_Python_Jupyter_Soln.ipynb)
- [Quiz:Supervised vs unsupervised learning](./quiz.ipynb#W1-2)

# 3. Regression Model

- [3.1 Linear regression model part1](./video/W1_3.1_Linear_Regression_Model_Part1.md)
1. 线性回归模型是监督学习过程中的基础模型，是一条直线拟合数据集，实现预测。
2. 回归模型和分类模型的区别在于输出类型，回归模型输出连续值，分类模型输出离散值。
3. Training set概念
4. x = input variable, y = output/target variable,m = number of training examples, i = index of training example

- [3.2 Linear regression model part1](./video/W1_3.2_Linear_Regression_Model_Part2.md)
1. 预测值 = y-hat, 目标值 = y
2. 线性回归模型的表示：f_w,b(x) = w*x + b
- 【OK】[Lab:Model_representation](./lab/C1_W1_Lab02_Model_Representation_Soln.ipynb)
没涉及w,b 的动态更新，只是简单的模型表示
- [3.3 Cost function formula](./video/W1_3.3_Cost_Function_Formula.md)
- [3.4 Visualizing the cost function](./video/W1_3.4_Cost_Function_Intuition.md)
- [3.5 Visualization examples](./video/W1_3.5_Visualization_Examples.md)
- [Lab:Cost function](./lab/C1_W1_Lab03_Cost_function_Soln.ipynb)
- [Quiz:Regression Model](./quiz.ipynb#W1-3)

# 4. Train the model with gradient descent
> 使用梯度下降训练模型
- [4.1 Gradient descent](./video/W1_4.1_Gradient_Descent.md)
1. 梯度下降算法的工作原理 = 不断调整参数来减少成本函数的值直至找到成本函数的最小值
2. 初始参数的选择对结果影响不大通常是0
3. 损失函数可能存在多个局部最小值
![alt text](./images/Gradient_Descent.png)
- [4.2 Implementing gradient descent](./video/W1_4.2_Implementing_Gradient_Descent.md)
- [4.3 Gradient descent intuition](./video/W1_4.3_Gradient_Descent_Intuition.md)
- [4.4 Learning rate](./video/W1_4.4_Learning_Rate.md)
- [4.5 Gradient descent for linear regression](./video/W1_4.5_Gradient_Descent_For_Linear_Regression.md)
- [4.6 Running gradient descent](./video/W1_4.6_Running_Gradient_Descent.md)
- [Lab:Gradient descent](./lab/C1_W1_Lab04_Gradient_Descent_Soln.ipynb)
- [Quiz:Train the model with gradient descent](./quiz.ipynb#W1-4)