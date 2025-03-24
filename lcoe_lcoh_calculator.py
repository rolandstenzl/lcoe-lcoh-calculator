'''Levelized cost of electricity VS hydrogen of in energy generation'''
'''Bernd Mildt, 12307808'''
'''Open source energy system modeling 2025'''

import numpy as np
import matplotlib.pyplot as plt

# uniform capital recovery factor ucrf
def calculate_ucrf(ir, lt):
    return (ir * (1 + ir) ** lt) / ((1 + ir) ** lt - 1)

# levelized cost of electricity roduction lcoe
def calculate_lcoe(ir, lt, capex, opex_fix, opex_var, output):
    ucrf = calculate_ucrf(ir, lt)
    return (capex * ucrf + opex_fix) / output + opex_var

# levelized cost of hydrogen production lcoh
def calculate_lcoh(ir, lt, capex, opex_fix, opex_var, output, input, f_in):
    ucrf = calculate_ucrf(ir, lt)
    return (capex * ucrf + opex_fix) / output + opex_var + input * f_in

def main():
    try:
        # general inputs
        ir = float(input("Enter interest rate (as decimal, e.g. 0.05 for 5%): "))
        lt = int(input("Enter lifetime in years: "))

        # electricity inputs
        capex_el = float(input("Enter CAPEX for electricity [EUR/kW]: "))
        opex_fix_el = float(input("Enter fixed OPEX for electricity [EUR/kW-year]: "))
        output_el = float(input("Enter annual electricity output [kWh]: "))
        opex_var_el = float(input("Enter variable OPEX for electricity [EUR/kWh]: "))
        
        # h2 inputs
        capex_h2 = float(input("Enter CAPEX for hydrogen [EUR/kW]: "))
        opex_fix_h2 = float(input("Enter fixed OPEX for hydrogen [EUR/kW-year]: "))
        opex_var_h2 = float(input("Enter variable OPEX for hydrogen [EUR/kWh]: "))
        output_h2 = float(input("Enter annual hydrogen output [kg]: "))
        input_h2 = float(input("Enter energy input per kg of hydrogen [kWh/kg]: "))
        f_in = float(input("Enter electricity cost per kWh [EUR/kWh]: "))

        lcoe = calculate_lcoe(ir, lt, capex_el, opex_fix_el, opex_var_el, output_el)
        lcoh = calculate_lcoh(ir, lt, capex_h2, opex_fix_h2, opex_var_h2, output_h2, input_h2, f_in)
        
        print(f"\nLCOE: {lcoe:.4f} EUR/kWh")
        print(f"LCOH: {lcoh:.4f} EUR/kg")

        interest_rates = np.linspace(0.01, 0.1, 10)
        lcoe_values = [calculate_lcoe(ir, lt, capex_el, opex_fix_el, opex_var_el, output_el) for ir in interest_rates]
        lcoh_values = [calculate_lcoh(ir, lt, capex_h2, opex_fix_h2, opex_var_h2, output_h2, input_h2, f_in) for ir in interest_rates]

        plt.figure(figsize=(8, 5))
        plt.plot(interest_rates * 100, lcoe_values, label='LCOE (EUR/kWh)', marker='o')
        plt.plot(interest_rates * 100, lcoh_values, label='LCOH (EUR/kg)', marker='s')
        plt.xlabel('Interest Rate (%)')
        plt.ylabel('Cost (EUR)')
        plt.title('LCOE vs. LCOH Comparison')
        plt.legend()
        plt.grid()
        plt.show()
    
    except ValueError:
        print("Invalid input, please enter numerical values only")

if __name__ == "__main__":
    main()