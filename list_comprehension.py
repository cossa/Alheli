#check which numbers are even or odd

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_odd = ["even" if num%2 == 0 else "odd" for num in list]
print(even_odd)

#Create a list of multiples of 3

triples = [ num for num in range (1,11) if num%3 == 0]