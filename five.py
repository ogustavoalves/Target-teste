user_string = 'abcde'
print("original string: ", user_string)

# method 1 - populating an empty string 
reversed_str_method1 = ''
for x in range(len(user_string), 0, -1):
    reversed_str_method1 += user_string[x-1]
print("reversed string - method 1: ", reversed_str_method1)


# method 2 - using join
reversed_str_method2 = ''.join(user_string[x - 1] for x in range(len(user_string), 0, -1))
print("reversed string - method 2: ", reversed_str_method2)


# method 3 - running the array from back to front
reversed_str_method3 = user_string[::-1]
print("reversed string - method 3: ", reversed_str_method2)