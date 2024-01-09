# propellant_cost
# by Chris Y. Taylor
# calculates specific cost of propellant based on fuel
# and oxidizer cost and mixture ratio

bad_input = True  #not really bad yet, just nothing entered at this point
while bad_input == True:
    fuel_cost = float(input("What is specific fuel cost? "))
    oxidizer_cost = float(input("What is specific oxidizer cost? "))
    mixture_ratio = float(input("What is the mixture ratio (oxidizer mass/fuel mass)? "))
    if fuel_cost >= 0 and oxidizer_cost >= 0 and mixture_ratio > 0:
        bad_input = False
    else:
        print ("Mixture ratio must be a positive number.  Costs must be positive or zero.")
propellant_cost = (oxidizer_cost*(mixture_ratio/(mixture_ratio+1)))+(fuel_cost*(1/(mixture_ratio+1)))
print ("The specific propellant cost is:")
print (propellant_cost)

