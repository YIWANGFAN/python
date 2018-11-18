import numpy as np
import matplotlib.pyplot as plt
#定义函数
def f(x):
    return 2*x**2-4
#绘制图像
def paintf():
    # 绘制x轴y轴
    x = [-1,5]
    y1 = [0 * a for a in x]
    y = [-5,28]
    x1 = [0 * a for a in y]
    plt.plot(x, y1, 'black',)
    plt.plot(x1, y, 'black', )

    # 绘制y=x^2-4的图像
    x = np.linspace(0,4)
    y = np.linspace(-4, 28)
    plt.plot(x,2* x ** 2 - 4, 'b')
#输入a,b
a=0
b=8
paintf()
#进入循环
n=0
while n<100:
    x0=(a+b)/2
    y = [-4,28]
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