"""
age = 36
txt = "My name is John, I am " + age
print(txt) 
    
This results in an error as you cannot concatenate int
"""

age = 36
txt = f"My name is John, I am {age}"        # Using an F-String allows you to concatenate int's to strings
print(txt)

# Placeholders can contain variables, operations, functions, and modifiers to format value

price = 59
txt1 = f"The price is {price} dollars"           # Price is a placeholder
print(txt1)

txt2 = f"The price is {price:.2f} dollars"       # The term ":.2f", which adds two decimals, is called a modifier. This values the value after it becomes a variable
print(txt2)

txt3 = f"The price is {20 * 59} dollars"         # Modifiers can also contain python code, like math operations
print(txt3)