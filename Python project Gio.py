#Tree Branching Program Using Turtle Module
import turtle

def tree(length):
    if length > 5: # this controlshow for the branches go
        t.forward(length)
        t.right(20)
        tree(length - 15) # recursive call
        t.left(40)
        tree(length - 15)
        t.right(20)
        t.backward(length)

t = turtle.Turtle() #define t as a turtle class
t.left(90) #set turtle's initial direction to go upward
t.color('green') #set color to green
t.speed(1)

tree(90)

