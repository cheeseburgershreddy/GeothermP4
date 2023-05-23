import CoolProp.CoolProp as CP
from CoolProp.Plots import PropertyPlot

plot = PropertyPlot('REFPROP::PENTANE[0.9]&BUTANE[0.1]', 'TS', unit_system='EUR', tp_limits='ACHP')
plot.calc_isolines(CP.iQ, num=5)
plot.title(r'$T-s$ Graph for n-Pentane and n-Butane ($90\%$ n-Pentane)')
plot.xlabel(r'$s$ [kJ/kg$^\circ$K]')
plot.ylabel(r'$T$ [$^\circ$C]')
plot.grid()
plot.draw()

plot = PropertyPlot('REFPROP::PENTANE[0.8]&BUTANE[0.2]', 'TS', unit_system='EUR', tp_limits='ACHP')
plot.calc_isolines(CP.iQ, num=5)
plot.title(r'$T-s$ Graph for n-Pentane and n-Butane $(80\% n-Pentane)$')
plot.xlabel(r'$s$ [kJ/kg$^\circ$K]')
plot.ylabel(r'$T$ [$^\circ$C]')
plot.grid()
plot.draw()

plot = PropertyPlot('REFPROP::PENTANE[0.7]&BUTANE[0.3]', 'TS', unit_system='EUR', tp_limits='ACHP')
plot.calc_isolines(CP.iQ, num=5)
plot.title(r'$T-s$ Graph for n-Pentane and n-Butane $(70\% n-Pentane)$')
plot.xlabel(r'$s$ [kJ/kg$^\circ$K]')
plot.ylabel(r'$T$ [$^\circ$C]')
plot.grid()
plot.draw()

plot.show()
