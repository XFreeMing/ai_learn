This Week, you'll extend linear regression to handle multiple input features.

> - extend: 扩展

You'll also learn some methods for improving your model's training and performance, such as vectorization,feature scaling, feature engineering and polynomial regression.

> - also: 还
> - improve: 改进
> - performance: 性能
> - vectorization: 矢量化
> - feature scaling: 特征缩放
> - polynomial regression: 多项式回归

At the end of the week, you'll get to practice implementing linear regression in code.

> - at the end of: 在...结束时
> - practice: 实践

## Learning Objectives

- Use vectorization to implement multiple linear regression
  > 使用矢量化来实现多元线性回归
- Use feature scaling, feature engineering, and polynomial regression to improve model training

> 使用特征缩放、特征工程和多项式回归来改进模型训练

- Implement linear regression in code

> 在代码中实现线性回归

## 1. Multiple linear regression

> 多元线性回归

### [1.1 Multiple features](./video/multiple-features/multiple-features_summary.md)

1. 多特征线性回归的引入
2. 新的符号表示: X_1, X_2, X_3, X_4 来表示四个特征 $n$ 表示特征的总数 $X^i$ 表示第 $i$ 个训练样本
3. 模型的表示: 不再是单一的 $f_w(x) = wx + b$，而是 $f_w(X) = w_1x_1 + w_2x_2 + w_3x_3 + w_4x_4 + b$
4. 向量表示和点积:引入了向量 $W$ 和 $X$ 的概念，其中 $W$ 是参数向量，$X$ 是特征向量,模型可以被重写为 $f(x) = W \cdot X + b$
5. 多特征线性回归的定义: 这种包含多个输入特征的线性回归模型被称为多特征线性回归

### [1.2 Vectorization part 1](./video/vectorization-part-1/vectorization-part-1_summary.md)

1. 非向量化的实现方式: 1. 手动计算 2. 使用循环 3. 逐项计算
2. 向量化的实现方式:使用 NumPy 的 `dot` 函数可以实现向量化的点积操作
3. 向量化的优势:代码更短，运行更快
4. 向量化背后的原理:向量化代码之所以运行更快的原因是 NumPy 能够利用计算机的并行硬件

### [1.3 Vectorization part 2](./video/vectorization-part-2/vectorization-part-2_summary.md)

1. 向量化的效率提升
2. 向量化的工作原理
3. 向量化在机器学习中的重要性
4. 向量化在多变量线性回归中的应用
5. 向量化与非向量化代码的对比
6. NumPy 库的介绍
7. 向量化代码的效率
8. 学习向量化的重要性:学习向量化是实现机器学习算法中最重要和最有用的技术之一

### [Lab: Multiple linear regression](./lab/C1_W2_Lab01_Python_Numpy_Vectorization_Soln.ipynb)

### [1.4 Gradient descent for multiple linear regression](./video/gradient-descent-for-multiple-linear-regression/gradient-descent-for-multiple-linear-regression_summary.md)

1. 梯度下降法在多元线性回归中的应用
2. 多元线性回归模型的向量化表示: $f_{\vec{w}},_b(\vec{X}) = \vec{W} \cdot \vec{X} + b$
3. 成本函数的向量化表示:成本函数 $J$ 也被表示为向量 $J(\vec{\mathbf{w}},b)$
4. 梯度下降的向量化表示：

   $$
   w_j = w_j - \alpha \frac{\partial J(\vec{\mathbf{w}},b)}{\partial w_j} \\
   b = b - \alpha \frac{\partial J(\vec{\mathbf{w}},b)}{\partial b}
   $$

5. 梯度下降法的更新规则
   $$
   \frac{\partial J(\vec{\mathbf{w}},b)}{\partial w_j} = \frac{1}{m} \sum_{i=1}^{m} (f_{\vec{w},b}(\vec{X}^i) - y^i) x_j^i
   $$
6. 梯度下降法与正态方程的比较
7. 梯度下降法的优势
8. 多元线性回归的实践应用

## 2. Gradient descent in practice

> 实践中的梯度下降

### [2.1 Feature scaling part 1](./video/feature-scaling-part-1/feature-scaling-part-1_summary.md)

1. 特征缩放的必要性：可以使得梯度下降算法运行得更快
2. 特征值范围对参数选择的影响
3. 特征值范围对梯度下降的影响
4. 特征缩放对梯度下降的优化作用

### [2.2 Feature scaling part 2](./video/feature-scaling-part-2/feature-scaling-part-2_summary.md)

1. 特征缩放的方法

   1. 最大值缩放: 通过将每个原始特征值除以其最大值来实现
   2. 均值归一化(Mean normalization): 通过将原始特征重新缩放，使其围绕零中心化，从而包含负值和正值

      1. 先找到特征的平均值，然后将每个特征值减去平均值
      2. 然后将每个特征值除以最大值减去最小值

   3. Z 分数归一化（Z-score normalization）

      1. 计算标准差（Sigma）
      2. 计算均值（Mu）
      3. 对每个特征值减去均值，然后除以标准差

2. 征缩放的目标范围:目标范围大约在-1 到+1 之间，但这个范围可以略有宽松，如-3 到+3 或-0.3 到+0.3

3. 特征缩放的实际应用

   1. 对于范围差异很大的特征，如-100 到+100，进行缩放是更好的选择
   2. 对于非常小的值，如-0.001 到+0.001，可能也需要进行缩放

### [2.3 Checking gradient descent for convergence](./video/checking-gradient-descent-for-convergence/checking-gradient-descent-for-convergence_summary.md)

1. 判断梯度下降是否收敛：观察参数接近全局最小值的程度来判断其是否收敛
2. 学习率 Alpha 的选择：识别梯度下降良好运行的特征有助于后续选择适当的学习率 Alpha。
3. 梯度下降规则：梯度下降规则是关键，其中一个重要选择是学习率 Alpha。
4. 监控梯度下降：通过绘制成本函数 J 随梯度下降迭代次数变化的图表来监控梯度下降的工作情况
5. 学习曲线：成本函数 J 随迭代次数变化的曲线称为学习曲线，有助于判断梯度下降是否收敛。
6. 梯度下降正常工作的迹象：如果梯度下降正常工作，成本 J 应在每次迭代后减少。
7. 梯度下降收敛的迹象：如果成本 J 在一定迭代次数后趋于平稳，不再显著下降，表明梯度下降已基本收敛。
8. 迭代次数的不确定性：梯度下降收敛所需的迭代次数在不同应用间差异很大，难以提前确定。
9. 自动收敛测试：通过设定一个阈值 epsilon，如果成本 J 在一次迭代中减少的量小于 epsilon，则可以认为梯度下降已收敛。
10. 图形监控的重要性：相比于自动收敛测试，作者更倾向于通过观察学习曲线图来判断梯度下降的工作情况。

### [2.4 Choosing the learning rate](./video/choosing-the-learning-rate/choosing-the-learning-rate_summary.md)

1. 学习率的重要性：学习算法的性能很大程度上取决于学习率的选择。如果学习率太小，算法运行缓慢；如果太大，可能无法收敛
2. 学习率选择的技巧

   1. 通过观察成本函数随迭代次数的变化，可以判断学习率是否合适。如果成本函数波动，可能是学习率太大或代码有误
   2. 过大的学习率可能导致梯度下降算法过冲最小值，导致成本函数上升，为了修复这个问题，可以使用更小的学习率
   3. 调试时，可以使用非常小的学习率来检查成本函数是否在每次迭代中减少

3. 学习率的调试和选择
   1. 设置非常小的学习率是作为调试步骤，并不适用于实际训练
   2. 学习率太小会导致梯度下降需要更多迭代才能收敛
   3. 建议尝试一系列学习率值，从较小的值开始，逐步增加，直到找到太大的值

### [Lab: Feature scaling and learning rate](./lab/C1_W2_Lab03_Feature_Scaling_and_Learning_Rate_Soln.ipynb)

### [2.5 Feature engineering](./video/feature-engineering/feature-engineering_summary.md)

1. 特征选择对学习算法性能的影响
2. 特征选择在实际应用中的重要性
3. 特征工程的目的和方法
4. 特征工程的实际案例分析
5. 特征的定义和模型构建
6. 特征转换和新特征的创建
7. 特征工程的定义和作用
8. 特征工程对模型性能的提升
9. 特征工程与非线性函数拟合

### [2.6 Polynormial regression](./video/polynomial-regression/polynomial-regression_summary.md)

1. 多项式回归的引入:之前我们仅使用直线拟合数据，现在引入多项式回归，可以拟合曲线和非线性函数到数据上
2. 多项式回归的应用示例
3. 特征工程的重要性
4. 特征选择的多样性
5. 实践和工具的使用:一个实现多项式回归，另一个使用 Scikit-learn 库
6. 本周总结和展望:分类算法

### [Lab: Feature engineering and Poynomial regression](./lab/C1_W2_Lab04_FeatEng_PolyReg_Soln.ipynb)

### [Lab: Linear regression with scikit-learn](./lab/C1_W2_Lab05_Sklearn_GD_Soln.ipynb)

> 实践中的梯度下降

## 3. [Quize: Gradient descent in practice](./quiz.ipynb#W2-2)

> 练习测验：实践中的梯度下降

## 4. [Practice lab:Linear regression](./code/C1_W2_Linear_Regression.ipynb)

> W2 实践实验室：线性回归
