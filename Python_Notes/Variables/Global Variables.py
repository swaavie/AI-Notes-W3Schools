def myfunc():
  x = "fantastic"                # This variable will not stay because it is inside a function
  print("Python is " + x)

myfunc()

print(x)            # The number 5 is printed because that is the global value

def myfunc1():
  global x
  x = "Fantastic"                # This variable will keep its value because it is followed by "global"
  print("Python is " + x)

myfunc1()

print(x)            # The value fantastic is printed because that is the global value