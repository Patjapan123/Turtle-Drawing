import turtle 
print("What color do you like your background to be?")
j=input()
wn = turtle.Screen()
wn.bgcolor(j)
print("What color do you like your turtle to be?")
n=input()
pat = turtle.Turtle()
pat.color(n)
print("What color do you like to fill your shape?")
miles=input()
pat.fillcolor(miles)
print("How many sides are your shape?")
print("This program can generate a shape that has 3 sides to 8 sides")
p=int(input())
print("How thick do you want your line to be?")
number=int(input())
pat.width(number)
pat.begin_fill()
for i in range(p):
    if p == 3:
        pat.forward(100)
        pat.right(120)
    if p == 4:
        pat.forward(100)
        pat.right(90)
    if p == 5:
        pat.forward(100)
        pat.right(72)
    if p == 6:
        pat.forward(100)
        pat.right(60)
    if p == 7:
        pat.forward(100)
        pat.right(51.43)
    if p == 8:
        pat.forward(100)
        pat.right(45)
pat.end_fill()
turtle.done()


#type in list of colorandside and it will draw the shape 