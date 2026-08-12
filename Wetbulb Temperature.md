# HOW WET BULB TEMPERATURE IS CALCULATED
<img width="1646" height="886" alt="image" src="https://github.com/user-attachments/assets/368fe113-28f2-4f13-8558-147bc47e6b20" />

$$ E_{in} = E_{out} $$
$$ \color{red}{E_{air}^1} + \color{blue}E_{water} \color{black}= \color{red}{E^2_{air}} $$
$$ \color{red}C_{pa}T_{db} + \omega(c_{pwv}T_{db} + H_0) + \color{blue}(\omega_s - \omega)*c_{pw}T_{wb} \color{black}= \color{red}c_{pa}T_{wb} + \omega(c_{pwv}T_{wb} + H_0)$$
$$ \omega_s = \omega(Pt, 100RH, Twb)$$

# CONCLUSION

Solving for wet bulb temperature here is difficult due to the implicit nature of the equation. It can be found using tabulated data. The process would to find the dry bulb temperature and humidity and then determine the wet bulb temperature from that tabulated values of the wet bulb temperature. However, it is hardly used in practice as a driving point for HVAC and is typically supplemental. 

It is important to note that cooling using the constant wet bulb line is highly energy efficient then typical methods. Current issues with this cooling method is the maintenance cost, region needs to be dry with low RH but optimized such that the output air is not too humid for indoor spaces, and water is available 
