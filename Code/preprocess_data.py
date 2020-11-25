import numpy as np
import pandas as pd

def get_kinematics(x, y):
	dx = x - x.shift()
	dy = y - y.shift()
	d2x = dx - dx.shift()
	d2y = dy - dy.shift()

	speed = np.sqrt(dx**2 + dy**2)
	acceleration = np.sqrt(d2x**2 + d2y**2)

	return speed, acc

def remove_outliers(data, m):
	d = np.abs(data - np.nanmedian(data))
    mdev = np.nanmedian(d)
    s = d/mdev if mdev else 0.
    
    return np.where(s < m)