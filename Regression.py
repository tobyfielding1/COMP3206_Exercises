
import os
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import seaborn as sns
from sklearn import datasets
from sklearn.neighbors.kde import KernelDensity


def f(x):
    return 0.5*(x)*(x**4)/(.05+(x**4))
X=np.linspace(0,1,50)
y0=f(X)+0.03*np.random.normal(0,1,50)
