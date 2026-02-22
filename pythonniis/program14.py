#write a python program to find the compound intrest.
print("enter principal")
p=float(input())
print("enter rate")
r=float(input())
print("enter time")
t=float(input())
print("enter number of time compunded")
n=float(input())
ci=p*(1+r/n)**(n*t)-p
print("compound intrest=",ci)