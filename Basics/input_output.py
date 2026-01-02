#Topic-2 : Input and output

#Basic input
name=input("enter your name:") 
city=input("enter your city name:") 
print(f"Hello {name} from {city}")

#Two numbers
a=int(input("enter a value")) 
b=int(input("enter b value")) 
print(f"addition:{a+b}") 
print(f"difference:{a-b}")
print(f"product:{a*b}) 

#Multiple inputs
a,b,c=map(int,range("enter 3 values:"). split()) #splits into 3 separate values
print(f"sum:{a+b+c}") 
print(f"average:{(a+b+c)/3}") 

#Age calculation
birth_year=int(input("enter your birth year")) 
age=2025-birth_year
print(f"you are {age} years old") 
