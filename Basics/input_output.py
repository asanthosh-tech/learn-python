#Topic-2 : Input and output

#Basic input
name=input("Enter your name:") 
city=input("Enter your city name:") 
print(f"Hello {name} from {city}")

#Two numbers
a=int(input("Enter 1st number")) 
b=int(input("Enter 2nd number")) 
print(f"addition:{a+b}") 
print(f"difference:{a-b}")
print(f"product:{a*b}") 

#Multiple inputs
a,b,c=map(int,input("Enter 3 values:").split()) #splits into 3 separate values
print(f"sum:{a+b+c}") 
print(f"average:{(a+b+c)/3}") 

#Age calculation
birth_year=int(input("enter your birth year")) 
age=2025-birth_year
print(f"you are {age} years old") 

#Percentage
total=int(input("Enter total marks:")) 
obtained=int(input("Enter obtained marks:")) 
percentage=(obtained/total) *100
print(f"percentage :{percentage}") 