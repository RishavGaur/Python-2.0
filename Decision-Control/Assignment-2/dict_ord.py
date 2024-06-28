# Write a python script to print a set of words in dictionary order. Words are given by user.

# First Method
print("Enter three cities names:")
a,b,c=input(),input(),input()

if a<b<c:
    print(a,b,c)
elif a<c<b:
    print(a,c,b)
elif b<a<c:
    print(b,a,c)
elif b<c<a:
    print(b,c,a)
elif c<a<b:
    print(c,a,b)
else:
    print(c,b,a)


# Second Method

'''print("Enter three words:")
a,b,c= input(),input(),input()

x= min(a,b,c)
print("All words in Sequence are:",x,end=" ")
if x==a:
    print(min(b,c),max(b,c))
elif x==b:
    print(min(a,c),max(a,c))
else:
    print(min(a,b),max(a,b))'''


# Third Method

''' taken_words= input("Enter the words seperated by spaces: ").split()

words= sorted(taken_words)
for word in words:
    print(word) '''