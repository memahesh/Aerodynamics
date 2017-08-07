import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Profile
    data = pd.read_csv('profile_data.csv')
    port_data = pd.read_csv('pressure_portdata.csv')
    data = np.array(data)
    port_data = np.array(port_data)
    plt.scatter(port_data[:,0], port_data[:,1], c = 'b')
    plt.plot(data[:,0], data[:,1], linestyle=':')
    plt.xlabel("x/c")
    plt.ylabel("y/c")
    plt.title("Drawing the profile section of Aerofoil")
    plt.show()
    plt.show()

    # AOA0
    aoa0 = pd.read_csv('AOA_0a.csv')
    aoa0 = np.array(aoa0)
    plt.scatter(aoa0[0:12, 1], aoa0[0:12, 4], c='b')
    line_up, = plt.plot(aoa0[0:12, 1], aoa0[0:12, 4], c='b', label = 'Line1')
    plt.scatter(aoa0[12:, 1], aoa0[12:, 4], c='g')
    line_down, = plt.plot(aoa0[12:, 1], aoa0[12:, 4], c='g', label = 'Line2')
    plt.legend([line_up, line_down], ['Cp(upper surface)', 'Cp(lower surface)'])
    plt.xlabel("x/c")
    plt.ylabel("Cp")
    plt.title("x/c Vs Cp at AOA_0")
    plt.show()

    # AOA_M3
    aoa0 = pd.read_csv('AOA_M3a.csv')
    aoa0 = np.array(aoa0)
    plt.scatter(aoa0[0:12, 1], aoa0[0:12, 4], c='b')
    line_up, = plt.plot(aoa0[0:12, 1], aoa0[0:12, 4], c='b', label='Line1')
    plt.scatter(aoa0[12:, 1], aoa0[12:, 4], c='g')
    line_down, = plt.plot(aoa0[12:, 1], aoa0[12:, 4], c='g', label='Line2')
    plt.legend([line_up, line_down], ['Cp(upper surface)', 'Cp(lower surface)'])
    plt.xlabel("x/c")
    plt.ylabel("Cp")
    plt.title("x/c Vs Cp at AOA_M3")
    plt.show()

    # AOA_5
    aoa0 = pd.read_csv('AOA_5a.csv')
    aoa0 = np.array(aoa0)
    plt.scatter(aoa0[0:12, 1], aoa0[0:12, 4], c='b')
    line_up, = plt.plot(aoa0[0:12, 1], aoa0[0:12, 4], c='b', label='Line1')
    plt.scatter(aoa0[12:, 1], aoa0[12:, 4], c='g')
    line_down, = plt.plot(aoa0[12:, 1], aoa0[12:, 4], c='g', label='Line2')
    plt.legend([line_up, line_down], ['Cp(upper surface)', 'Cp(lower surface)'])
    plt.xlabel("x/c")
    plt.ylabel("Cp")
    plt.title("x/c Vs Cp at AOA_5")
    plt.show()

    # AOA_10
    aoa0 = pd.read_csv('AOA_10a.csv')
    aoa0 = np.array(aoa0)
    plt.scatter(aoa0[0:12, 1], aoa0[0:12, 4], c='b')
    line_up, = plt.plot(aoa0[0:12, 1], aoa0[0:12, 4], c='b', label='Line1')
    plt.scatter(aoa0[12:, 1], aoa0[12:, 4], c='g')
    line_down, = plt.plot(aoa0[12:, 1], aoa0[12:, 4], c='g', label='Line2')
    plt.legend([line_up, line_down], ['Cp(upper surface)', 'Cp(lower surface)'])
    plt.xlabel("x/c")
    plt.ylabel("Cp")
    plt.title("x/c Vs Cp at AOA_10")
    plt.show()

    # AOA_15
    aoa0 = pd.read_csv('AOA_15a.csv')
    aoa0 = np.array(aoa0)
    plt.scatter(aoa0[0:12, 1], aoa0[0:12, 4], c='b')
    line_up, = plt.plot(aoa0[0:12, 1], aoa0[0:12, 4], c='b', label='Line1')
    plt.scatter(aoa0[12:, 1], aoa0[12:, 4], c='g')
    line_down, = plt.plot(aoa0[12:, 1], aoa0[12:, 4], c='g', label='Line2')
    plt.legend([line_up, line_down], ['Cp(upper surface)', 'Cp(lower surface)'])
    plt.xlabel("x/c")
    plt.ylabel("Cp")
    plt.title("x/c Vs Cp at AOA_15")
    plt.show()

    # AoA vs Cl
    aoa0 = pd.read_csv('aoavscl.csv')
    aoa0 = np.array(aoa0)
    plt.scatter(aoa0[:, 0], aoa0[:, 1], c='g')
    plt.plot(aoa0[:, 0], aoa0[:, 1], c='g', label='Line2')
    plt.ylabel("Coefficient of lift")
    plt.xlabel("Angle of Attack (in deg)")
    plt.title("Angle of Attack Vs Cl")
    plt.show()




if __name__ == '__main__':
    main()