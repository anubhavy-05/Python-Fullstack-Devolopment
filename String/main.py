S1="mysirg"
print(S1)
print(S1[0]) # To access the first character of the string.
print(S1[2]) # To access the third character of the string. 
print(S1[-1]) # To access the last character of the string.
print(S1[0:3]) # To get a substring of the first three characters.
print(S1[2:5]) # To get a substring of the third to fifth characters.
print(min(S1)) # To find the minimum character in the string.
print(max(S1)) # To find the maximum character in the string.   


sorted_S1=sorted(S1) # To sort the characters of the string in ascending order.
print("The sorted characters of the string are:", sorted_S1)   

               
              #concatination and repetition of string

S1="sir"
S2="mysir"
S3=S1+S2 # Concatenation of S1 and S2.
print("The concatenated string is:", S3)
S4=S1*3 # Repetition of S1 three times.
print("The repeated string is:", S4)


                 #comperision operators

S1="abc"
S2="xyz"    
print(S1==S2) # To check if S1 and S2 are equal.
print(S1!=S2) # To check if S1 and S2 are not equal
print(S1>S2) # To check if S1 is greater than S2 (lexicographically).
print(S1<S2) # To check if S1 is less than S2 (lexicographically).


                  #str object methods 

#index() method is used to find the index of the first occurrence of a specified substring in a string. If the substring is not found, it raises a ValueError.             
#find() method is used to find the index of the first occurrence of a specified substring in a string. If the substring is not found, it returns -1.
#count() method is used to count the number of occurrences of a specified substring in a string.
#replace() method is used to replace all occurrences of a specified substring with another substring in a string.
#upper() method is used to convert all characters in a string to uppercase.
#lower() method is used to convert all characters in a string to lowercase.
#strip() method is used to remove leading and trailing whitespace from a string.
#split() method is used to split a string into a list of substrings based on a specified delimiter (default is whitespace).     
#join() method is used to join a list of strings into a single string using a specified delimiter.


s1="mysirg education system"
print(s1.index("s")) # To find the index of the first occurrence of "s" in s1.
print(s1.find("s")) # To find the index of the first occurrence of "s" in s1.
print(s1.count("s")) # To count the number of occurrences of "s" in s1.
print(s1.replace("s", "S")) # To replace all occurrences of "s" with "S" in s1.
print(s1.upper()) # To convert all characters in s1 to uppercase.   
print(s1.lower()) # To convert all characters in s1 to lowercase.
print(s1.strip()) # To remove leading and trailing whitespace from s1.
print(s1.split()) # To split s1 into a list of substrings based on whitespace.
print("-".join(s1.split())) # To join the list of substrings in s1 into a single string using "-" as a delimiter.   
































#WAP to take a string input from the user and print the number of occurrences of each character in the string.

user_input = input("Enter a string: ")
char_count = {}
for char in user_input:
    char_count[char] = char_count.get(char, 0) + 1
for char, count in char_count.items():
    print(f"Character '{char}' occurs {count} times.")