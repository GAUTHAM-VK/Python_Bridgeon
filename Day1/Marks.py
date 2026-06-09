total=0
for i in range(1,6):
    mark=float(input(f"Enter subject {i} mark: "))
    total+=mark
average=total/5
if average>=90:
    print("Grade=A")
elif(average>=80 and average<=89):
    print("Grade=B")
elif(average>=70 and average<=79):
    print("Grade=C")
elif(average>=60 and average<=69):
    print("Grade=D")
else:
    print("Grade=F")

print("Average marks: ", average)   