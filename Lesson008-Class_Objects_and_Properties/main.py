#Create a class called "Customers"

#Take note of the following information

#Name, Beverage, Food, Total
#Samirah, Iced Caffe Latte, Cinnamon Roll, 225
#Jerry, Caramel Macchiato, Glazed Doughnut, 230

#Create a class variable named "Greeting", with the value "Welcome to the Coffee Palace!"

#Create instance variables for Samirah and Jerry. (ex. c_1)
#Include the attributes listed on the table. (ex. c_1.name)
#Type print(Customers.greeting)
#What does Samirah want to drink? Print her beverage on the console.
#What does Jerry want to eat? Print his food on the console.

import os
clear = lambda: os.system("clear")
clear()

class customers:
    greeting = "Welcome to the Coffee Palace"

c_1 = customers()
c_1.name = "Samirah"
c_1.drink = "Iced Caffe Latte"
c_1.food = "Cinnamon Roll"
c_1.total = "225"

c_2 = customers()
c_2.name = "Jerry"
c_2.drink = "Caramel Macchiato"
c_2.food = "Glazed Doughnut"
c_2.total = "230"

print(customers.greeting)
print(c_1.name)
print(c_1.drink)
print(c_2.food)