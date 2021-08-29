print("Hello, World!")
a=3 
b=0
c=a+b
print(a+b)
if c>4 :
    print("no is greater than 4")
    print("yes it is greater than 4")
    print(c*c)
print("i am outside block")

def addition():
    d=5
    e=3
    print(d+e)
print("after addition function")
addition()
def parameter_addition(num1,num2):
    print(num1+num2)
parameter_addition(3,7)
print(type(a))
h="Manish"
print(type(h))
print(type(str(a)))
print("this is no a "+str(a))
f="i am manish kumar living in kalyani"
g=f.split()#splitted the function from space 
print(g)
g1=f.split("k")
print(g1)
f1="             i     am manish    kumar      living in kalyani      "
g2=f1.strip() #remove 1st and last space in string
print(g2)
g3=f1.replace(" ","")
print(g3)
g4=f1.replace(" ","*")
print(g4)
g5=f1.replace("kalyani","004") #replace kalyani with 004
print(g5)
g6=f1.upper().replace(" ","") #reple space with none
print(g6)
f2="I AM MANISH KUMAR"
g7=f2.lower()
print(g7)
g8=f2.capitalize()#it change; 1st letter into uppercase
print(g8)
g9=f2.casefold() #it changes into lowercase but it is stronger than lower function
print(g9)
f3="Manish"
g10=f3.center(30)#place string into centre of given argument length
print(g10)
g11=f2.count("M") #it reflect no of times that string or char occurs.
print(g11)
g12=f3[4] #reflect char at specified position
print(g12)
g13=f3[4:6] #4 to 5 string value(last excluded)
print(g13)
g14=f3.encode()
print(g14)















