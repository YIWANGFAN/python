import numpy as np
import math
import matplotlib.pyplot as plt
#定义函数
def f(x):
    return x**2-4
#绘制图像
def paintf():
    # 绘制x轴y轴
    x = np.arange(-1, 8, 0.05)
    y1 = [0 * a for a in x]
    y = np.arange(-5, 65, 0.05)
    x1 = [0 * a for a in y]
    plt.plot(x, y1, '-', color='black')
    plt.plot(x1, y, '-', color='black')

    # 绘制y=x^2-4的图像
    x = np.linspace(0, 8)
    y = np.linspace(-4, 60)
    plt.plot(x, x ** 2 - 4, '--')
#输入a,b
a=0
b=8
paintf()
#进入循环
n=0
while n<100000:
    x0=(a+b)/2
    y = np.arange(-1, 1, 0.05)
    x = [x0 for a in y]
    plt.plot(x, y, '-b', color='red')
    x1=f(a)
    x2=f(x0)
    #判断结果
    if x2==0:
        break
    else:
        if(x1*x2<0):
            b=x0
        else:
            a=x0
    n+=1
print(x0)
plt.show()