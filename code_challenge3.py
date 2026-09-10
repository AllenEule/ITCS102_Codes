#Global Freight Calculator

Sender_name = input("Sender's thy name -----> ")
Type_of_item = input("What is thy item being shipped? ----> ")
is_Fragile = bool(input("Is thy Item fragile? -----> "))
weight = float(input("What is thy weight of thy item -----> "))
distance = float(input("What is thy distance of thy home? ------> "))
is_express = bool(input("Is thy order a express order? ------> "))
is_international = bool(input("Is thy order an international order? ------> "))
base_cost = (weight * 2.50) + (distance * 0.15)
print("-------------------------------------------------")
print("Thy name is", Sender_name)
print("Thy item being shipped is", Type_of_item)

if is_Fragile == 'True':
	print("We will notify thy carrier.")
else:
	print("Thank the for answering.")

print("The weight of the item is", weight,"kg")
print("The distance of the place is", distance,"km")

Total = 0.00
Total1 = (base_cost * 1.40) + 50
Total2 = (base_cost * 1.20) + 25
Total3 = base_cost + 30
  Total4 = base_cost



if weight <= 2.0 or distance <= 100 and is_express == 'False' and is_international == 'False':
	print("The cost of the shipment is $", Total)


elif is_express == 'True' and is_international == 'True':
	print("The cost of the shipment is $", Total1)


elif is_express == 'True' or (is_international == 'True' and weight > 20):
	print("The cost of your shipment is $", Total2)


elif  weight > 30 or distance > 1000:
	print("The cost of your shipment is $", Total3)


else:
	print("The cost of your shipment is $", Total4)

