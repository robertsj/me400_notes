import numpy as np


def thermo_table():
    from iapws import IAPWS97
    Ts = np.linspace(100+273.15, 300+273.15, 13)
    f = open('thermo_data.txt', 'w')
    s= '  T [K]   P [MPa]  h_l [kJ/kg] h_v [kJ/kg]\n'
    f.write(s)
    for i in range(len(Ts)):
        sat_steam = IAPWS97(T=Ts[i],x=0)
        sat_liquid = IAPWS97(T=Ts[i],x=1)
        T = Ts[i]
        P = sat_steam.P
        h_v = sat_liquid.h
        h_l = sat_steam.h
        s= "{:8.3f}  {:6.3f}  {:10.3f}  {:10.3f}\n".format(T, P, h_v, h_l)
        print(s)
        f.write(s)
    f.close()

def thermo_table_2d():
    from iapws import IAPWS97
    Ps = [2, 4, 6, 8]
    Ts = np.array([20, 40, 60, 80, 100])+273.15
    f = open('thermo_data2.txt', 'w')
    s= '  T [K]   P [MPa]  rho [kg/m^3]\n'
    f.write(s)
    for i in range(len(Ts)):
        for j in range(len(Ps)):  
            dat = IAPWS97(T=Ts[i], P=Ps[j])
            rho = dat.rho
            x = dat.rho
            s= "{:8.3f}  {:6.3f} {:10.3f}\n".format(Ts[i], Ps[j], rho)
            print(s)
            f.write(s)
    f.close()


thermo_table_2d()