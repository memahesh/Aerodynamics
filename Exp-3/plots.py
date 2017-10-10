import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    data = pd.read_csv('compiled_data.csv')
    line1 = data.loc[:7,:]
    line2 = data.loc[8:14,:]
    line3 = data.loc[15:21, :]
    line4 = data.loc[22:28, :]
    line5 = data.loc[29:,:]
    # C_L Vs AOA
    plt.plot(line1['AOA'], line1['C_L'])
    plt.show()
    print line1['AOA']


if __name__ == '__main__':
    main()
    
