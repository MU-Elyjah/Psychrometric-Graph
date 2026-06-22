from matplotlib import pyplot as plt
import numpy as np

def Enthalpy(Pt, Tdb, phi) -> float:
    """
    Returns the enthalpy from state points where:
    cpa: BTU/lbF MINIMAL CHANGES DUE TO CHANGE IN ABS PRESSURE AND TEMPERATURE
    cpw: BTU/lbF MINIMAL CHANGES DUE TO CHANGE IN ABS PRESSURE AND TEMPERATURE
    Hew: specific enthalpy of water [BTU/lbs] vaporization from 31F or 0C, 0C does not imply no kinetic motion good approx due to change in enthalpy later
    Ha: specific enthalpy of Air H = cp * dT
    Hw: specific enthalpy of water H = cp * dT + H0 where H0 is needed for latent energy where it is isothermal
    
    Parameters
    ----------
    Tdb (float): Drybulb temperature.
    Pt (float): 
    H (float): total specific enthalpy

    Returns
    --------
    H (int): Enthalpy
    """
    cpa: float = 0.240
    cpw: float = 0.444
    hew: float = 1075
    ha: float = cpa * Tdb
    hw: float = cpw * Tdb + hew
    h: float = ha + hw * phi / 7000
    return h


def relativeHumidity(Pt, Tdb, Phi):
    """
    Returns the relative humidity from state points where:
    lbs2kpa: converting
    z: 
    PsT: Magnus-Tetens Equation for Saturated pressure of water empircally driven outputs kpa inputs C
    Pt: User inputs psi and gets Kpa
    Pv: water vapor pressure
    
    Parameters
    ----------
    Tdb (float): Drybulb temperature.
    Pt (float): 
    Phi (float): 

    Returns
    --------
    H (int): Enthalpy
    """
    lbs2kpa = 6.89475729 #
    z = 0.622
    PsT = .61078 * np.exp((17.27 * Tdb) / (Tdb + 237.3))
    Pt = 14.7 * lbs2kpa
    Pv = Phi * Pt / (z + Phi)
    RH = (Pv / PsT) * 100
    return RH


def constRelativeHumid(Pt, rh, Tdb):
    """
    Returns the enthalpy from state points where:
    cpa: BTU/lbF MINIMAL CHANGES DUE TO CHANGE IN ABS PRESSURE AND TEMPERATURE
    cpw: BTU/lbF MINIMAL CHANGES DUE TO CHANGE IN ABS PRESSURE AND TEMPERATURE
    Hew: specific enthalpy of water [BTU/lbs] vaporization from 31F or 0C, 0C does not imply no kinetic motion good approx due to change in enthalpy later
    Ha: specific enthalpy of Air H = cp * dT
    Hw: specific enthalpy of water H = cp * dT + H0 where H0 is needed for latent energy where it is isothermal
    
    Parameters
    ----------
    Tdb (float): Drybulb temperature.
    Pt (float): 
    H (float): total specific enthalpy

    Returns
    --------
    H (int): Enthalpy
    """
    z = .622
    Cdb2 = (Tdb - 32) * 5 / 9 # [C]-->>
    PsT = .61078 * np.exp((17.27 * Cdb2) / (Cdb2 + 237.3)) #Magnus-Tetens Equation for Saturated pressure of water empircally driven outputs kpa inputs C
    Pv2 = (rh * PsT) / 100 # P_vapor = RH*P_sat/100 due to RH equation [psi]
    Phi = z*(Pv2 / (Pt - Pv2)) * 7000 # see appendix A [grains/lbs]
    return Phi


def constSpecificVol(Pt, vspec_a, Tdb): #ISSUES SLIGHTLY OFF FROM OG GRAPH
    """
    Returns the enthalpy from state points where:
    cpa: BTU/lbF MINIMAL CHANGES DUE TO CHANGE IN ABS PRESSURE AND TEMPERATURE
    cpw: BTU/lbF MINIMAL CHANGES DUE TO CHANGE IN ABS PRESSURE AND TEMPERATURE
    Hew: specific enthalpy of water [BTU/lbs] vaporization from 31F or 0C, 0C does not imply no kinetic motion good approx due to change in enthalpy later
    Ha: specific enthalpy of Air H = cp * dT
    Hw: specific enthalpy of water H = cp * dT + H0 where H0 is needed for latent energy where it is isothermal
    
    Parameters
    ----------
    Tdb (float): Drybulb temperature.
    Pt (float): 
    H (float): total specific enthalpy

    Returns
    --------
    H (int): Enthalpy
    """
    kpa2psi = 0.145037738
    Ra = 53.53 # lbf/lb*Rs
    z = 0.622
    in2ft_cubic = 1 / (12 ** 2)
    Cdb2 = (Tdb - 32) * 5 / 9 # [C]-->>
    PsT = .61078 * np.exp((17.27 * Cdb2) / (Cdb2 + 237.3)) #Magnus-Tetens Equation for Saturated pressure of water empircally driven outputs kpa inputs
    #Pv = (rh*PsT)/100 # P_vapor = RH*P_sat/100 due to RH equation [psi]
    #print(Pv)

    #vspec_a= (Ra*Tdb/((Pt - Pv2)*kpa2psi))*in2ft_cubic #specific volume of air P*v = Ra*T [in^3/lb]
    Tdb = Tdb + 459.67 # converting to Rankine temp
    Pv2 = (Pt - ((Ra * Tdb) * in2ft_cubic) / (vspec_a * kpa2psi))#air pressure

    Phi = z * (Pv2 / (Pt - Pv2)) * 7000 # see appendix A [grains/lbs]
    #Pv = Phi*Pt/(z*7000 + Phi)

    return Phi


def constEnthalpy(Pt, H, Tdb):
    cpa = .240 #BTU/lb_a*F MINIMAL CHANGES DUE TO CHANGE IN ABS PRESSURE AND TEMPERATURE
    cpw = .444 #BTU/lb_w*F MINIMAL CHANGES DUE TO CHANGE IN ABS PRESSURE AND TEMPERATURE
    Hew = 1075 #specific enthalpy of water [BTU/lbs] vaporization from 31F NEED TO PULL FROM STEAM TABLES based off of temp and pressure
    Ha = cpa * Tdb #specific enthalpy of Air H = cp * dT
    Hw = cpw * Tdb + Hew #specific enthalpy of water H = cp * dT + H0 where H0 is needed for latent energy where it is isothermal
    #H = Ha + Hw*Phi2/7000 #total specific enthalpy
    Phi = ((H - Ha) / Hw) * 7000
    return Phi


def constWetBulb(Pt, Twb, Tdb):
    #Hg = 1150.3 #Btu/lbm enthalpy of water at x = 1
    Hg = 2501 #KJ/Kg enthalpy of water at x = 1 recursive due to wetbulb temp depenance
    cpa = 1.006 #KJ/Kg*K specific heat of air T = 25C 77F
    cpwv = 1.864 #KJ/Kg*K specific heat of water vapor at T = 25C 77F
    cpw = 4.18 #KJ/Kg*K speciifc heat of water at T = 25C 77F
    rh_sat = 100
    phisat = constRelativeHumid(Pt, rh_sat, Twb)
    phisat = phisat / 7000
    Twb = (Twb - 32) * 5 / 9
    Tdb = (Tdb - 32) * 5 / 9

    #print(phisat)
    #Hv = Hg + cpwv*Tdb #Water vapor enthalpy calc
    #Ha = cpa*Tdb #Air enthalpy calc
    #Hini = Hv + Ha
    #deltaH2sat = (phi - phisat)*(cpw*Twb)
    #hsat = cpa*Twb + cpw*Twb*phisat + phisat*Hg
    #hsat = Hini + deltaH2sat = cpa*Twb + cpw*Twb*phisat + phisat*Hg #solve for wet bulb temp

    phi = ((phisat * (Hg + (cpwv*Twb - cpw*Twb)) - cpa*(Tdb - Twb)) / (Hg + cpwv*Tdb - cpw*Twb)) * 7000

    return phi


def plotFormat():
    f = plt.figure()
    ax = f.add_subplot(1, 1, 1)
    ax.yaxis.tick_right()
    ax.autoscale(False)
    minor_ticks_x = np.arange(20, 125, 1)
    major_ticks_x = np.arange(20, 125, 5)

    ax.set_xticks(major_ticks_x)
    ax.set_xticks(minor_ticks_x, minor=True)

    minor_ticks_y = np.arange(0, 170, 2)
    major_ticks_y = np.arange(0, 170, 10)

    ax.set_yticks(major_ticks_y)
    ax.set_yticks(minor_ticks_y, minor = True)
    ax.grid(which = 'both')


def PlotCharts():
    plotFormat()
    Tdb2 = np.linspace(30, 120) # [F]
    RH2 = np.linspace(10, 100, 10) #%
    SPV = np.linspace(12.5, 15, 6)
    ENTH = np.linspace(10, 50, 5)
    WETB = np.linspace(20, 95, 16)
    lbs2kpa = 6.89475729 #converting
    Pt = 14.7 * lbs2kpa #NOTE Change for different eleveations

    for rh in RH2:
        #Pv2 = (rh*PsT2)/100 # P_vapor = RH*P_sat/100 due to RH equation [psi]
        #Phi2 = z*(Pv2/(Pt-Pv2))*7000 # see appendix A [grains/lbs]
        Phi2 = constRelativeHumid(Pt, rh, Tdb2)

        plt.plot(Tdb2, Phi2, color = 'red')

        xlabel = Tdb2[int(len(Tdb2) / 2 - 1)] #location for label in x
        ylabel = Phi2[int(len(Phi2) / 2)] #location for label in y
        plt.text(xlabel, ylabel, f'{rh}%', fontsize = 9, rotation = 45) #label graphs positions with rh change to string

    for spv in SPV:
        #Pv2 = (rh*PsT2)/100 # P_vapor = RH*P_sat/100 due to RH equation [psi]
        #Phi2 = z*(Pv2/(Pt-Pv2))*7000 # see appendix A [grains/lbs]
        Phi2 = constSpecificVol(Pt, spv, Tdb2)

        plt.plot(Tdb2, Phi2, color = 'green')

        xlabel = Tdb2[int(len(Tdb2) / 2 - 1)] #location for label in x
        ylabel = Phi2[int(len(Phi2) / 2)] #location for label in y

    for enth in ENTH:
        #Pv2 = (rh*PsT2)/100 # P_vapor = RH*P_sat/100 due to RH equation [psi]
        #Phi2 = z*(Pv2/(Pt-Pv2))*7000 # see appendix A [grains/lbs]
        Phi2 = constEnthalpy(Pt, enth, Tdb2)
        xlabel = Tdb2[1] #location for label in x
        ylabel = Phi2[1] #location for label in y

        plt.plot(Tdb2, Phi2, color = 'blue')
        plt.text(xlabel, ylabel, f'{enth}!', fontsize = 9, rotation = 45) #label graphs positions with rh change to string


        xlabel = Tdb2[int(len(Tdb2) / 2 - 1)] #location for label in x
        ylabel = Phi2[int(len(Phi2) / 2)] #location for label in y

    for wetb in WETB:
        #Pv2 = (rh*PsT2)/100 # P_vapor = RH*P_sat/100 due to RH equation [psi]
        #Phi2 = z*(Pv2/(Pt-Pv2))*7000 # see appendix A [grains/lbs]
        Phi2 = constWetBulb(Pt, wetb, Tdb2)
        #print(wetb)
        #print(Phi2)
        #print(Tdb2)
        plt.plot(Tdb2, Phi2, color = 'orange')
        xlabel = Tdb2[0] #location for label in x
        ylabel = Phi2[0] #location for label in y
        plt.text(xlabel, ylabel, f'{wetb}', fontsize = 9, rotation = 45) #label graphs positions with rh change to string


    plt.xlabel("Dry Bulb Temperature")
    plt.ylabel("Humidity Ratio")
    plt.show()


def main():
#USER INPUT HERE
    PlotCharts()


if __name__ == "__main__":
    main()
