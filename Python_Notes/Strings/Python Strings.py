# Strings are arrays
a = "Hello World!"
print(a[1])                         # This function prints to the screen
print(len(a))                       # This function prints the length of a to the screen (12)
print("Hell" in a)                  # This function returns a boolean output, finding keywords in strings

if "World" in a:                    # This line is asking is World is part of a
  print("Yes, 'World' is present.") # This line prints a confirmation message that the query is true or false

for x in "banana":                  # This loop says for every letter in banana 
    print(x)                        # Print all values of x to the screen
        
print("Hello" not in a)             # This checks if the input is in a or not

if "Goodbye" not in a:              # This line uses an if statement to say "if you cannot find 'goodbye' in a, print a confirmation"
  print("No, 'Goodbye' is NOT present.")
  
  