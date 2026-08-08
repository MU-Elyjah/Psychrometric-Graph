def convertF2K(F):
    K =  (F - 32) * 5/9 + 273.15
    return K
def convertPSI2PA(PSI):
    PA = PSI*6894.76
    return PA
def convertKG_M3_2_LBM_FT3(KGM3):
    LBMFT3 = KGM3*0.0624279606
    return LBMFT3
def convertPA2PSI(PA):
    PSI = PA/6894.76
    return PSI
def convertPAS2LBM_FT2S(PAS):
    LBM_FT2S =  PAS*0.6719689948130041 #https://www.convertunits.com/from/lb/ft-s/to/Pascal+second
    return LBM_FT2S
def convertJ_kgK(J_kgK):
    btu_lbmF = J_kgK*0.0002390057
    return btu_lbmF
def convertBTU_lbmF(BTU_lbmF):
    J_kgK = BTU_lbmF/0.0002390057
    return J_kgK
def convertBTU_lbm(BTU_lbm):
    Kj_Kg = BTU_lbm*2.326
    return Kj_Kg
def convertKj_Kg(Kj_Kg):
    BTU_lbm = Kj_Kg/2.326
    return BTU_lbm


if __name__ == '__main__':
    print("unitconversions: I am da captain now heh ehhe")
