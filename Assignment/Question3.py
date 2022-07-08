from cgitb import text


print("This program checks for number of alphabets and digits/numbers in a given text.")
text = input("Please Enter the text : ")
#initialize the base variables
alphabets = digits =  0

#Loop through text and check with method
for letters in range(len(text)):
    if(text[letters].isalpha()):
        alphabets = alphabets + 1
    else:
      if (text[letters].isdigit()):
       digits = digits + 1
   
        
print("\nTotal Number of Alphabets given text :  ", alphabets)
print("Total Number of Digits in given text :  ", digits)
