import os
from spacepy import pycdf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import xarray as xr


data = pycdf.CDF('data.cdf')

# df = pd.Series()

AMPL1_I = data['AMPL1_I'][0:300]
BF1 = data['BF1'][0:300]
BGSE = data['BGSE'][0:300]
BGSM = data['BGSM'][0:300]
RANGE = data['RANGE'][:]
Time_PB5 = data['Time_PB5'][:]

print(BGSE)


# AMPL1_O: CDF_REAL4 [1440, 3, 8]
# BF1: CDF_REAL4 [925803, 1]
# BGSE: CDF_REAL4 [925803, 3]
# BGSM: CDF_REAL4 [925803, 3]
# Epoch: CDF_EPOCH [925803, 1]
# Epoch1: CDF_EPOCH [1440, 1]
# FLAG1_I: CDF_INT4 [1440, 1]
# FLAG1_O: CDF_INT4 [1440, 1]
# MAG_MODE: CDF_INT4 [925803, 1]
# NUM1_PTS_I: CDF_INT4 [1440, 1]
# NUM1_PTS_O: CDF_INT4 [1440, 1]
# ORTH1_I: CDF_REAL8 [1440, 3, 3]
# ORTH1_O: CDF_REAL8 [1440, 3, 3]
# PAYLD1_I: CDF_REAL8 [1440, 3, 3]
# PAYLD1_O: CDF_REAL8 [1440, 3, 3]
# RANGE: CDF_INT4 [925803, 1]
# SENS1_I: CDF_REAL4 [1440, 3, 8]
# SENS1_O: CDF_REAL4 [1440, 3, 8]
# SPC_MODE: CDF_INT4 [925803, 1]
# Time1_PB5: CDF_INT4 [1440, 3]
# Time_PB5: CDF_INT4 [925803, 3]
# ZERO1_I: CDF_REAL4 [1440, 3, 8]
# ZERO1_O: CDF_REAL4 [1440, 3, 8]
# cartesian: CDF_CHAR*11 [3] NRV
# format_time: CDF_CHAR*2 [3] NRV
# label_bgse: CDF_CHAR*8 [3] NRV
# label_bgsm: CDF_CHAR*8 [3] NRV
# label_time:
    
# print(data['BF1'][...])
# print(AMPL1_I)
