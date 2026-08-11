## HOW RELATIVE HUMIDITY IS CALCULATED 

$$P_vV = n_vRT$$
$$P_aV = n_aRT$$

$$ \frac{P_v}{P_a} = \frac{n_V}{n_a} $$
$$ \frac{P_v}{P_a}\frac{M_v}{M_a} = \frac{n_V}{n_a}\frac{M_v}{M_a}$$
$$ .622 \frac{P_v}{P_a} = W $$


$$ P_a = \frac{.622 P_v}{W} $$
$$ P_t = P_a + P_v $$
$$P_v = \frac{WP_a}{.622 + W}$$ 

Vapor pressure

$$ P(Tdb)_{sat} = .61078 e^{\frac{17.27T}{T + 273}} $$ 

> Magnus - Tentens Equation: This describes the saturated vapor pressure of water at X = 1 at the T = Tdb not shown on the graph.

<img width="397" height="310" alt="image" src="https://github.com/user-attachments/assets/0551d4c5-a72e-4e5f-ab8c-be97aaa365f9" />

> The image above represents what the Magnus-Tentens equation depicts. It represent the second half of the vapor dome. 
> https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node61.html

Saturated vapor pressure i.e. pressure where the Pv = Pv_sat the max amount of pressure the water will see at 100% relative humidity 

It is important to note the ASHRAE uses:

$$ \phi = \frac{e(Tdp)}{e(Tdb)} $$

Where e(Tdp) is the partial pressure of water at the dew point. In this way the partial pressure of water would be the same as the actual partial pressure of the air [Reference ideal gas law for mathematical proof]. e(Tb) is the saturated partial pressure at the dry bulb temperature where X = 1. 

$$RH = 100\frac{P_v}{P(Tdb)_{sat}} $$

# CONCLUSION

Relative humidity is a calculation on the capability of water vapor evaporating in the air due to pressure differences being proportional to the energy of evaporation here. 
