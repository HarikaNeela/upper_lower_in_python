p=input("Enter the statement")
count1=0
count2=0
print(p)
for x in p:
    if x.isupper():
        count1+=1
    elif x.islower():
        count2+=1
    else:
        pass
print("No. of Upper case characters :",count1)
print("No. of Lower case characters :",count2)