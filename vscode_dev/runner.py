import sys
import os
import warnings
import logging

sys.dont_write_bytecode = True
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
warnings.filterwarnings('ignore')
print(sys.path)

from config import DEFAULT as cfg
from z3 import *
#import numpy as np
#import pandas as pd
#import scipy
#import matplotlib
#import seaborn
#import sklearn
#import tensorflow as tf
#import keras

if __name__ == "__main__":
    print(cfg.FILES_ROOT)
    ##############
    x = Real('x')
    y = Real('y')
    z = Real('z')
    s = Solver()
    s.add(3*x + 2*y - z == 1)
    s.add(2*x - 2*y + 4*z == -2) 
    s.add(-x + 0.5*y - z == 0) 
    print(s.check())
    print(s.model())

    ####
    x = Real('x')
    y = Real('y')
    s = Solver()
    s.add(x**2 + y**2 - 1 <= 0) 
    s.add(x**2 + y**2 - 6*x+5 < 0) 
    print(s.check())