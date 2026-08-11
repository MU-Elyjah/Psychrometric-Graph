def main():
#USER INPUT HERE
    Z = 5280 #ft EDIT HERE FOR LOCATION ALTITUDE
    PlotCharts(Z)
    Pt = Altidude(Z)
    Twb = 46.8 #F
    Tdb = 75 #F
    humrat = constWetBulb(Pt,Twb,Tdb)/7000
    RH = relativeHumidity(Pt,Tdb,constWetBulb(Pt,Twb,Tdb)/7000)

    humrat_sat = constRelativeHumid(Pt,100,Tdb)/7000 #Tdb
    print("Humdity ratio @Tdb 100% RH",humrat_sat)
    print("Altitude Pressure [psi]",uc.convertPA2PSI(Altidude(Z)*1000))

    humrat_30 = constRelativeHumid(Pt,30,Tdb)/7000 #Tdp
    print("Humdity ratio @Tdb 30% RH",humrat_30)
    #print("E Hot: ", E1)
