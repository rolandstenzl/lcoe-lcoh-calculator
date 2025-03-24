# osesm25_homework_1
Open source energy system modeling 2025 - homework assingnment nr. 1

The homwork features a levelized cost of electricity and hydrogen calculator, to determine the cost of generation for both of those energy sources.
The calculator follows the simple UCRF and LCO"X" calculations and should work as a standalone executable program.

Entering the parameters can vary greatly for generation methods depending on the primairy energy resource for electricity and on electricity price and electrolizer efficiency for hydrogen.
The following table gives an estimate for possible values for different generation types based on the [IRENA renewable power generation report 2023](https://www.irena.org/Publications/2024/Sep/Renewable-Power-Generation-Costs-in-2023):

| Generation Type | CAPEX [EUR/kW] | OPEX fix [EUR/kW*year] | OPEX var [EUR/kWh] | Output [kWh/year*kW] | LCOE [EUR/kWh] |
|:--------------:|:--------------:|:------------------------:|:-----------------------:|:------------------------:|:--------------:|
|  Wind Onshore  |      1,160     |           53.1           |          0.002          |           3,154          |      0.033     |
|  Wind Offshore |      2,800     |           70.0           |          0.003          |           3,596          |      0.075     |
|    Solar PV    |       758      |           10.0           |          0.005          |           1,402          |      0.044     |
|   Hydropower   |      2,806     |           56.1           |          0.001          |           4,645          |      0.057     |

There are no example values given for the hydrogen electrolizer.
The calcuator plot shows the gap between renewable electricity generation and renewable hydrogen generation.
Goal is to find competetive parameter values.
