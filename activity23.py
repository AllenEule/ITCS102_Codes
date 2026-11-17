#   Jeepney_loop

#JEEPNEY SIMULATOR (interactive)
passengers = ["Ana", "Ben", "Carla"]
passengers.append("Dan")
passengers.insert(0, "Lola")
passengers.remove("Ben")
x = passengers.pop()
y = passengers.pop(0)
len(passengers)
"Ana in passengers"
passengers.reverse()







route = ["Terminal", "Perez Park", "Pacific Mall"]
passengers = []
seats = 6
Fare = 13
total = 0

while True:
    print()
    print("Sakay:", passengers)
    print(len(passengers), "of", seats, "seats")
    print("1 Sakay 2 Priority seat 3 Para po!")
    print("4 Baba sa pinto 5 Baba sa harap")
    print("6 Seat check 7 Balikan 8 Exit")
    choice = input("Choice: ")
    print("-------------------------------------------------------")

    if choice == "1":
        if len(passengers) == seats:
            print("Puno na!")
            print("-------------------------------------------------------")
        else:
            name = input("Name: ")
            passengers.append(name)
            total = total + Fare
            print(name , "boarded at the back.")
            print("-------------------------------------------------------")
    elif choice == "2":
         if len(passengers) == seats:
                print("Puno na!")
                print("-------------------------------------------------------")
         else:
                 name = input("Name: ")
                 passengers.insert(0,name)
                 total = total + Fare
                 print(name , "took the priority seat")
                 print("-------------------------------------------------------")
    elif choice == "3":
        name = input("Who is getting off? ")
        if name in passengers:
         passengers.remove(name)
         print(name, "got off. Ingat po!")
         print("-------------------------------------------------------")
        else:
            print(name , "is not in the jeep")
            print("-------------------------------------------------------")
    elif choice == "4":
        if len(passengers) == 0:
              print("The jeep is empty.")
              print("-------------------------------------------------------")
        else:
              left = passengers.pop()
              print(left, "got off at the door.")
              print("-------------------------------------------------------")
    elif choice == "5":
        if len(passengers) == 0:
                  print("The jeep is empty.")
                  print("-------------------------------------------------------")
        else:
                  front = passengers.pop(0)
                  print(front, "got off at the front")
                  print("-------------------------------------------------------")
    elif choice == "6":
         for i in range(len(passengers)):
              print("Seat", i + 1, passengers[i])
              print("-------------------------------------------------------")
    elif choice == "7":
         route.reverse()
         print("Route:", route)
         print("-------------------------------------------------------")
    elif choice == "8":
         print("Total fare today:", total)
         print("-------------------------------------------------------")
    else:
         print("Invalid choice.")
         print("-------------------------------------------------------")

         

