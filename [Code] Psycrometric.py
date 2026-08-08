from matplotlib import pyplot as plt
import numpy as np
import unitconversions as uc
import CoolProp.CoolProp as CP
from pyXSteam.XSteam import XSteam
steamTable = XSteam(XSteam.UNIT_SYSTEM_MKS) 

def Enthalpy(Pt,Tdb,humrat): #pt in KPa
    TdbK = uc.convertF2K(Tdb) 
    PtPA = Pt*1000
    cpaSI = CP.PropsSI('C','T',TdbK,'P',PtPA,"Air") #BTU/lbF MINIMAL CHANGES DUE TO CHANGE IN ABS PRESSURE AND TEMPERATURE
    cpaIP = uc.convertJ_kgK(cpaSI)
    cpwvSI =  CP.PropsSI('C','T',TdbK,'Q',1,"Water") #BTU/lbF MINIMAL CHANGES DUE TO CHANGE IN ABS PRESSURE AND TEMPERATURE
    cpwvIP = uc.convertJ_kgK(cpwvSI)

    Tfreeze = 32
    TfreezeK = uc.convertF2K(Tfreeze)

    HewSI = steamTable.h_tx(TfreezeK,1)#specific enthalpy of water [BTU/lbs] vaporization from 31F or 0C, 0C does not imply no kinetic motion good approx due to change in enthalpy later
    HewIP = uc.convertKj_Kg(HewSI)
    Ha = cpaIP*Tdb #specific enthalpy of Air H = cp * dT
    Hw = cpwvIP*(Tdb - 32) + HewIP #specific enthalpy of water H = cp * dT + H0 where H0 is needed for latent energy where it is isothermal
    H = Ha + Hw*humrat/7000 #total specific enthalpy
    #print(cpwIP)
    #print(cpaIP)
    #print(cpwvIP)
    #print(f"TfreezeIP: {TfreezeK:.2f} Btu/lb")
    #print(f"HewIP: {HewIP:.2f} Btu/lb")
    #print(f"Ha: {Ha:.2f} Btu/lb")
    #print(f"Hw: {Hw:.2f} Btu/lb")
    return H

def relativeHumidity(Pt,Tdb,Phi): #pt in KPa
    lbs2kpa= 6.89475729 #converting
    z = .622
    PsT = .61078 * np.exp((17.27 * Tdb)/(Tdb + 237.3)) #Magnus-Tetens Equation for Saturated pressure of water empircally driven outputs kpa inputs C
    Pv = Phi*Pt/(z + Phi) #water vapor pressure
    RH = (Pv/PsT)*100
    return RH

def constRelativeHumid(Pt,rh,Tdb): #pt in KPa
    z = .622
    Cdb2 = (Tdb - 32)*5/9 # [C]-->>
    PsT = .61078 * np.exp((17.27 * Cdb2)/(Cdb2 + 237.3)) #Magnus-Tetens Equation for Saturated pressure of water empircally driven outputs kpa inputs C
    print(uc.convertPA2PSI(PsT*1000))
    Pv2 = (rh*PsT)/100 # P_vapor = RH*P_sat/100 due to RH equation [psi]
    humrat = z*(Pv2/(Pt-Pv2))*7000 # see appendix A [grains/lbs]
    return humrat

def constSpecificVol(Pt,vspec_a,Tdb): #ISSUES SLIGHTLY OFF FROM OG GRAPH #pt in KPa
    kpa2psi = 0.145037738
    in2ft_cubic = 1/(12**2)

    Ra = 53.53 # lbf/lb*Rs
    z = .622 #molecular mass ratio of water/air mv/ma
    Tdb = Tdb + 459.67 # converting to Rankine temp
    Pv2 = (Pt - ((Ra*Tdb)*in2ft_cubic)/(vspec_a*kpa2psi)) #Vapor pressure
    Phi = z*(Pv2/(Pt-Pv2))*7000 # [grains/lbs] #vapor pressure over air pressure  #molar ratio is equal to pressure ratio (water is essentially an ideal gas)
    return Phi

def constEnthalpy(Pt,H,Tdb):#pt in KPa
    TdbK = uc.convertF2K(Tdb) 
    PtPA = Pt*1000 #Pa
    cpaSI = CP.PropsSI('C','T',TdbK,'P',PtPA,"Air") #BTU/lbF MINIMAL CHANGES DUE TO CHANGE IN ABS PRESSURE AND TEMPERATURE
    cpaIP = uc.convertJ_kgK(cpaSI)
    cpwvSI =  CP.PropsSI('C','T',TdbK,'Q',1,"Water") #BTU/lbF MINIMAL CHANGES DUE TO CHANGE IN ABS PRESSURE AND TEMPERATURE
    cpwvIP = uc.convertJ_kgK(cpwvSI)
    Tfreeze = 32
    TfreezeK = uc.convertF2K(Tfreeze)

    #Hew = steamTable.h_tx(32,1)#specific enthalpy of water [BTU/lbs] vaporization from 31F or 0C, 0C does not imply no kinetic motion good approx due to change in enthalpy later
    HewIS = steamTable.h_tx(TfreezeK,1)#specific enthalpy of water [BTU/lbs] vaporization from 31F or 0C, 0C does not imply no kinetic motion good approx due to change in enthalpy later
    HewIP = uc.convertKj_Kg(HewIS)

    Ha = cpaIP*Tdb #specific enthalpy of Air H = cp * dT
    Hw = cpwvIP*(Tdb -32) + HewIP #specific enthalpy of water H = cp * dT + H0 where H0 is needed for latent energy where it is isothermal
    humrat = ((H - Ha)/Hw)*7000
    #print(steamTable.h_tx(TfreezeK,1))

    return humrat

def constWetBulb(Pt,Twb,Tdb):
    TdbK = uc.convertF2K(Tdb) 
    PtPA = Pt*1000
    #Hg = 1150.3 #Btu/lbm enthalpy of water at x = 1

    Tfreeze = 32
    TfreezeK = uc.convertF2K(Tfreeze)
    #Hew = steamTable.h_tx(32,1)#specific enthalpy of water [BTU/lbs] vaporization from 31F or 0C, 0C does not imply no kinetic motion good approx due to change in enthalpy later
    HgSI = steamTable.h_tx(TfreezeK,1)#specific enthalpy of water [BTU/lbs] vaporization from 31F or 0C, 0C does not imply no kinetic motion good approx due to change in enthalpy later
    HgIP = uc.convertKj_Kg(HgSI)
    cpaSI = CP.PropsSI('C','T',TdbK,'P',PtPA,"Air") #BTU/lbF MINIMAL CHANGES DUE TO CHANGE IN ABS PRESSURE AND TEMPERATURE #KJ/Kg*K specific heat of air T = 25C 77F
    cpwvSI = 1.864 #KJ/Kg*K specific heat of water vapor at T = 25C 77F
    cpwSI = CP.PropsSI('C','T',TdbK,'P',PtPA,"Water") #KJ/Kg*K speciifc heat of water at T = 25C 77F
    cpwvSI = CP.PropsSI('C','T',TdbK,'Q',1,"Water") #KJ/Kg*K speciifc heat of water at T = 25C 77F
    # print(cpwSI)
    # print(cpwvSI)
    # print(cpaSI)

    cpaIP = uc.convertJ_kgK(cpaSI)
    cpwIP = uc.convertJ_kgK(cpwSI)
    cpwvIP = uc.convertJ_kgK(cpwvSI)

    rh_sat = 100
    humratsat = constRelativeHumid(Pt,rh_sat,Twb)
    humratsat = humratsat/7000

    humrat = ((humratsat*(HgIP + (cpwvIP*Twb - cpwIP*Twb)) - cpaIP*(Tdb - Twb))/(HgIP + cpwvIP*Tdb - cpwIP*Twb))*7000

    return humrat

def plotFormat():
    f = plt.figure()
    ax = f.add_subplot(1,1,1)
    ax.yaxis.tick_right()
    ax.autoscale(False)
    minor_ticks_x = np.arange(20,125, 1)
    major_ticks_x = np.arange(20, 125, 5)

    ax.set_xticks(major_ticks_x)
    ax.set_xticks(minor_ticks_x, minor=True)

    minor_ticks_y = np.arange(0,170, 2)
    major_ticks_y = np.arange(0, 170, 10)

    ax.set_yticks(major_ticks_y)
    ax.set_yticks(minor_ticks_y, minor=True)
    ax.grid(which= 'both')

def PlotCharts(Z):
    plotFormat()
    Tdb2 = np.linspace(30,120) # [F]
    RH2 = np.linspace(10,100,10) #%
    SPV = np.linspace(12.5,15,6)
    ENTH = np.linspace(10,50,11)
    WETB = np.linspace(20,95,16)
    psi2kpa= 6.89475729 #converting
    Pt = (14.696*(1 - 6.8754*10**(-6)*Z)**5.2559)*psi2kpa #
    #print(Pt)

    for rh in RH2:
        #Pv2 = (rh*PsT2)/100 # P_vapor = RH*P_sat/100 due to RH equation [psi]
        #Phi2 = z*(Pv2/(Pt-Pv2))*7000 # see appendix A [grains/lbs]
        Phi2 = constRelativeHumid(Pt,rh,Tdb2)
        plt.plot(Tdb2,Phi2, color = 'red')
        xlabel = Tdb2[int(len(Tdb2)/2 - 1)] #location for label in x
        ylabel = Phi2[int(len(Phi2)/2)] #location for label in y
        plt.text(xlabel,ylabel,f'{rh}%',fontsize = 9,rotation = 45, color = "red") #label graphs positions with rh change to string

        #print(Phi2)

    for spv in SPV:
        #Pv2 = (rh*PsT2)/100 # P_vapor = RH*P_sat/100 due to RH equation [psi]
        #Phi2 = z*(Pv2/(Pt-Pv2))*7000 # see appendix A [grains/lbs]
        Phi2 = constSpecificVol(Pt,spv,Tdb2)

        plt.plot(Tdb2,Phi2, color = 'green')

        xlabel = Tdb2[int(len(Tdb2)/2 - 1)] #location for label in x
        ylabel = Phi2[int(len(Phi2)/2)] #location for label in y

    for enth in ENTH:
        #Pv2 = (rh*PsT2)/100 # P_vapor = RH*P_sat/100 due to RH equation [psi]
        #Phi2 = z*(Pv2/(Pt-Pv2))*7000 # see appendix A [grains/lbs]
        Phi2 = constEnthalpy(Pt,enth,Tdb2)
        xlabel = Tdb2[1] #location for label in x
        ylabel = Phi2[1] #location for label in y

        plt.plot(Tdb2,Phi2,color = 'blue')
        plt.text(xlabel,ylabel,f'{enth}!',fontsize = 9,rotation = 4, color = "Blue") #label graphs positions with rh change to string


        xlabel = Tdb2[int(len(Tdb2)/2 - 1)] #location for label in x
        ylabel = Phi2[int(len(Phi2)/2)] #location for label in y

    for wetb in WETB:
        #Pv2 = (rh*PsT2)/100 # P_vapor = RH*P_sat/100 due to RH equation [psi]
        #Phi2 = z*(Pv2/(Pt-Pv2))*7000 # see appendix A [grains/lbs]
        Phi2 = constWetBulb(Pt,wetb,Tdb2)
        #print(wetb)
        #print(Phi2)
        #print(Tdb2)
        plt.plot(Tdb2,Phi2, color = 'orange')
        xlabel = Tdb2[0] #location for label in x
        ylabel = Phi2[0] #location for label in y
        plt.text(xlabel,ylabel,f'{wetb}',fontsize = 9,rotation = 45, color = "orange") #label graphs positions with rh change to string


    plt.xlabel("Dry Bulb Temperature")
    plt.ylabel("Humidity Ratio")
    plt.show()


def main():
#USER INPUT HERE
    Z = 1000 #ft EDIT HERE FOR LOCATION ALTITUDE
    #PlotCharts(Z)
    Ppsi = 14.696
    PKpa = uc.convertPSI2PA(Ppsi)/1000
    print(constRelativeHumid(PKpa,100,55))
    E1 = Enthalpy(PKpa,55,constRelativeHumid(PKpa,100,55))
    print("E Hot: ", E1)
main()
