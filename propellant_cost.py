# propellant_cost
# by Chris Y. Taylor 01/02/2024
# calculates specific cost of propellant based on fuel
# and oxidizer cost and mixture ratio

fuel_cost = float(input("What is specific fuel cost? "))
oxidizer_cost = float(input("What is specific oxidizer cost? "))
mixture_ratio = float(input("What is the mixture ratio (oxidizer mass/fuel mass)?"))
propellant_cost = (oxidizer_cost*(mixture_ratio/(mixture_ratio+1)))+(fuel_cost*(1/(mixture_ratio+1)))
print ("The specific propellant cost is:")
print (propellant_cost)

