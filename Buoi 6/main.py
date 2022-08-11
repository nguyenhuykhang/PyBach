# Python program for implementation of Bubble Sort

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Driver code to test above
arr = [34, 64, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")

if __name__ == '__main__':
    bubbleSort(arr)

S1 = "Tiger"
S2 = "tiger"

A = S1 == S2
print( "Value of A:", A )            # Value of A: ____________

B = S1 > S2
print( "Value of B:", B )
D = S1[-1] == S2[-1]
print( "Value of D:", D )            # Value of D: ____________

S3 = "aardvark"
S4 = "anteater"

E = S3 == S4
print( "Value of E:", E )            # Value of E: ____________

F = S3 < S4
print( "Value of F:", F )            # Value of F: ____________

G = len(S3) == len(S4)
print( "Value of G:", G )            # Value of G: ____________

S5 = "ants"
S6 = "anteater"

H1 = S5 < S6
print( "Value of H1:", H1)

I = len(S5) < len(S6)
print( "Value of I:", I )            # Value of I: ____________

J = S5[0] != S6[0]
print( "Value of J:", J )            # Value of J: ____________

K = S5[-1] == S6[-1]
print( "Value of K:", K )            # Value of K: ____________



ZZZ = "Arthur, King of the Britons"

H = ZZZ[:4]
print( "Value of H:", H )

I = ZZZ[-3:]
print( "Value of I:", I )

J = ZZZ[-6:-2]
print( "Value of J:", J )


G = "ad" in "aardvark"
print( "Value of G:", G )

F = "a" in "aardvark"
print( "Value of F:", F)

E = ("A" + "BC") * 2
print( "Value of E:", E )

B = 3 * int( "125" )
print( "Value of B:", B )

A = 3 * "125"
print("Value of A:", A)

D = "a" + "bc" * 2
print( "Value of D:", D)


import string
orig_str = input("Palindrome test -- enter a string: ")
my_str = orig_str.lower()
for bad_char in string.whitespace + string.punctuation:
    my_str = my_str.replace(bad_char, '')
print(my_str)

# index technique
front = 0
end = len(my_str) - 1
mid = len(my_str) / 2

while end >= mid:
    if my_str[front] != my_str[end]:
        print(my_str, 'is not a palindrome')
        break
    end -= 1
    front += 1
else:
    print("It's a palindrome")

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

s = input('Input a string: ')

for ch in s:
    if ch in lowercase:
        print(uppercase[lowercase.find(ch)], end = "")
    else:
        print(ch,end='')