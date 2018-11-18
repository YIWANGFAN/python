import numpy as np
import matplotlib.pyplot as plt



#定义函数
def f(x):
    return x**2-4
def paintf():
    # 绘制x轴y轴
    x = [-1,4]
    y1 = [0 * a for a in x]
    y =[-5,12]
    x1 = [0 * a for a in y]
    plt.plot(x, y1, 'black',)
    plt.plot(x1, y, 'black', )

    # 绘制y=x^2-4的图像
    x = np.linspace(0,4)
    y = np.linspace(-4, 12)
    plt.plot(x, x ** 2 - 4, 'b')
#输入a,b
a=0
b=4
paintf()
#进入循环
n=0
while n<100000:
    x0=( (abs(f(a)) * b + abs(f(b)) * a) / (abs(f(b)) + abs(f(a))))
    k = (f(b) - f(a)) / (b - a)
    c = f(a) - k * a
    x = [a,b]
    y = [k * a + c for a in x]
    plt.plot(x, y, 'r--')

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
