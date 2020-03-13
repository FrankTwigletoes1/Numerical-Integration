import math
import sympy
import numpy as np
import matplotlib.pyplot as plt


#def Calculate(a,b,n,f):
    
#    delta_x = (b-a)/n
#    total_sum = 0

    
    
#    for i in range(1, n + 1):
#        midt = 0.5 * (2 * a + delta_x * (2 * i - 1))
#        total_sum += f(midt)
#    midtpunkt = total_sum*delta_x
        

    
#    total_sum = f(a)+f(b)
 
    
#    for i in range(1,n):
#        total_sum += f(a + i * delta_x)
#    trapez = total_sum*delta_x/2
            
    
    

    
#    return midtpunkt, trapez

#Midtpunkt
def midtpunkt(f,a,b,n):
    total_sum = 0
    delta_x = (b-a)/n
    for i in range(1, n + 1):
        midt = 0.5 * (2 * a + delta_x * (2 * i - 1))
        total_sum += f(midt)
    return total_sum*delta_x

#Venstre
def venstre(f,a,b,n):   
    delta_x = (b-a)/n
    result = delta_x*sum([f(a+delta_x*i) for i in range(n)])
    return result

#Højre
def hoejre(f,a,b,n):
    delta_x = (b-a)/n
    result = delta_x*sum([f(a+delta_x*(i+1)) for i in range(n)])
    return result



def plotNumericalIntegration(f,a,b,N,n):
    x = np.linspace(a,b,N+1)
    y = f(x)
    X = np.linspace(a,b,n*N+1)
    Y = f(X)
    plt.figure(figsize=(15,5))

    plt.subplot(1,3,1)
    plt.plot(X,Y,'b')
    x_left = x[:-1] # venstre endpoints
    y_left = y[:-1]
    plt.plot(x_left,y_left,'b.',markersize=10)
    plt.bar(x_left,y_left,width=(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
    plt.title(('Venstre-sum, N = {}'.format(N)))

    plt.subplot(1,3,2)
    plt.plot(X,Y,'b')
    x_mid = (x[:-1] + x[1:])/2 # Midpoints
    y_mid = f(x_mid)
    plt.plot(x_mid,y_mid,'b.',markersize=10)
    plt.bar(x_mid,y_mid,width=(b-a)/N,alpha=0.2,edgecolor='b')
    plt.title('Midt-sum, N = {}'.format(N))

    plt.subplot(1,3,3)
    plt.plot(X,Y,'b')
    x_right = x[1:] # venstre endpoints
    y_right = y[1:]
    plt.plot(x_right,y_right,'b.',markersize=10)
    plt.bar(x_right,y_right,width=-(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
    plt.title('Højre-sum, N = {}'.format(N))



    plt.show()

f = lambda x : -0.005*(x**4-9*x**3+23*x**2-15*x-7)
a = 0 
b = 5
N = 100
n = 100


for n in (5, 10, 20, 100, 500):
    print("Venstresum: {0}, N = {1}".format(venstre(f,a,b,n),n))
    print("Højresum: {0}, N = {1}".format(hoejre(f,a,b,n),n))
    print("Midtpunkt: {0}, N = {1} ".format(midtpunkt(f,a,b,n),n))


plotNumericalIntegration(f,a,b,N,n)