#Name
#Age
#Favourite Colour
#Favourite Movie
#Mobile number
#Motto in life

def summary(input_name, input_age, input_color, input_movie, input_no, input_motto):
    print("Name: " + input_name)
    print("Age: " + input_age)
    print("Favourite Colour: " + input_color)
    print("Favourite Movie: " + input_movie)
    print("Contact Number: " + input_no)
    print("Motto in life: " + input_motto)

input_name = input("What is your name? ")
input_age = str(input("How old are you? "))
input_color = input("What is your favourite colour? ")
input_movie = input("What's your favourite movie? ")
input_no = str(input("What's your mobile number? "))
input_motto = input("What is your motto in life? ")

summary(input_name, input_age, input_color, input_movie, input_no, input_motto)