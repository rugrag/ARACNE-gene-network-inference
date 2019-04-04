#Multivariate kernel density estimate using a normal kernel
import numpy as np
from scipy.linalg import expm

#KDE multivariate
def p_mkde_M(x,X,h):
    
    X = np.asmatrix(X)
    x = np.asmatrix(x)
    
    N,d = X.shape
    
    X = X.T
    x = x.T
    
    Sxy = np.cov(X)
    
    invS = np.linalg.inv(Sxy)
    detS = np.linalg.det(Sxy)

    s = 0
    
    #maybe write in a better way
    for ix in range(N):

        p2 = np.matmul(invS,(x-X[:,ix]))
        p2 = np.matmul((x-X[:,ix]).T,p2)
        
        ex = np.asscalar(expm(np.divide(-p2,(2*h**2))))

        s = s + (1/np.sqrt(np.multiply((2*np.pi)**d,detS)))*ex
    
    
    pxy = s/(N*h**d)
    
    return pxy

#KDE univariate
def p_kde(x,X,h):
    
    N = len(X)
    
    Sxy = np.var(X)
    
    s = 0
    
    for ix in range(N):
        
        p2 = (x-X[ix])**2
        ex = np.exp(-p2/(Sxy*2*h**2))

        s = s + (1/np.sqrt(2*np.pi*Sxy))*ex
    
    pxy = s/(N*h)
    
    return pxy

#Mutual Information between two columns
def kernel_mi(X,Y):

    d = 2
    nx = len(X)
    
    #Euristics to calculate Kernel width 
    hx = (4/(d+2))**(1/(d+4))*nx**(-1/(d+4))

    Xall = (np.vstack((X,Y))).T
    sum1 = 0
    
    for i in range(nx):

        dummy = np.hstack((X[i],Y[i]))

        pxy = p_mkde_M(dummy,Xall,hx)
        px = p_kde(X[i],X,hx)
        py = p_kde(Y[i],Y,hx)
                     
        sum1 = sum1 + np.log(pxy/(px*py))
  

    return sum1/nx