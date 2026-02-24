#wap take emp salary from keyboard if sal>=5000 da=30% hra=20% if sal<5000 da=20% t
print("enter basic salary")
sal=int(input())
da=sal*0.3 if sal>=5000 else sal*0.2
hra=sal*0.2 if sal>=5000 else sal*0.1
totalsal=sal+da+hra
print("basic salary=",sal)
print("da=",da)
print("hra=",hra)
print("total salary=",totalsal)