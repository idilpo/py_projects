'''
Sal's Shipping
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers.
Sal wants to make sure that every single one of his customers has the best,
and most affordable experience shipping their packages.

In this project, you’ll build a program that will take the weight of a package and
determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package:

Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

'''

weight = float(input("Please enter the weight of your package: "))
ground = 20.00
premium = 125.00
drone = 0

if weight <= 2:
    ground += 1.50 * weight
    drone += 4.50 * weight
    print("Ground Shipping: ", ground)
    print("Ground Shipping Premium: ", premium)
    print("Drone Shipping: %.2f" % drone)
    print("Your best shipping option is: %.2f " % min(ground, premium, drone))
elif 2 < weight <= 6:
    ground += 3.00 * weight
    drone += 9.00 * weight
    print("Ground Shipping: ", ground)
    print("Ground Shipping Premium: ", premium)
    print("Drone Shipping: %.2f" % drone)
    print("Your best shipping option is: %.2f " % min(ground, premium, drone))
elif 6 < weight <= 10:
    ground += 4.00 * weight
    drone += 12.00 * weight
    print("Ground Shipping: ", ground)
    print("Ground Shipping Premium: ", premium)
    print("Drone Shipping: %.2f" % drone)
    print("Your best shipping option is: %.2f " % min(ground, premium, drone))
else:
    ground += 4.75 * weight
    drone += 14.25 * weight
    print("Ground Shipping: ", ground)
    print("Ground Shipping Premium: ", premium)
    print("Drone Shipping: %.2f" % drone)
    print("Your best shipping option is: %.2f " % min(ground, premium, drone))
