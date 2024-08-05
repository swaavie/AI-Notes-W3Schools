print(10 > 9)       # True or false, is a larger than b?
print(10 == 9)      # True or false, is a the same size as b?
print(10 < 9)       # True or false, is a smaller than b?

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

num_list = [34,12,93,783,330,896,1,55]
result = (lambda x: (x%10==0))(num_list)