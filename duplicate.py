numbers=[2,3,3,5,1,6,3,7,8,5,7,3,4]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)     
