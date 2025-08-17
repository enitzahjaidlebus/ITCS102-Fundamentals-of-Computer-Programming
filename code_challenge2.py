da = eval(input("Enter Amount Here ... "))#hello

onethousand = 1000
fivehundred = 500
twohundred = 200
onehundred = 100
fifty = 50
twenty = 20
ten = 10
five = 5
one = 1#bawal yan

a1 = da // onethousand
da = da % onethousand

b5 = da // fivehundred
da = da % fivehundred

c2 = da // twohundred
da = da % twohundred

d1 = da // onehundred
da = da % onehundred

e5 = da // fifty
da = da % fifty

f2 = da // twenty
da = da % twenty

g1 = da // ten
da = da % ten

h5 = da // five
da = da % five

i1 = da // one
da = da % one

print("Here are the breakdown of the Deposited Amount:")
print("1000", "-" , a1)
print("500", "-" , b5)
print("200", "-" , c2)
print("100", "-" , d1)
print("50", "-" , e5)
print("20", "-" , f2)
print("10", "-" ,g1)
print("5", "-" , h5)
print("1", "-" , i1)#hehehe
