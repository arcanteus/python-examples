def double(x):
    return x* 2

liste1= list(map(double,[1,2,3,4,5,6,7]))
print("liste1=",liste1)

liste2 = list(map(lambda x : x **2,(1,2,3,4,5,6,7,8,9,10)))

print("liste2=",liste2)

exlist1= [1,2,3,4]
exlist2= [5,6,7,8]
exlist3= [9,10,11,12,13]

print(list(map(lambda x,y : x*y , exlist1,exlist2)))

