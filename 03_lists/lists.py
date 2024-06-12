# message = 'Hello There. My name is Sadık Turan'.split()
# print(message[0])

# my_list = [1, 2, 3]
# my_list = ['bir', 2, True, 5.6]
# print(my_list)

list = ['one', 'two', 'three']
list2 = ['four', 'five', 'six']

numbers = list + list2
print(numbers)
print(len(numbers))

# message = 'Hello There. My name is Sadık Turan'
# print(message[0])


userA = ['Sadık', 35]
userB = ['Çınar', 2]

users = [userA, userB] # liste içinde liste

print(users[0][0])


# liste içinden stringi integer'a çevirip toplama yapma

deneme = ['a12']

print(int(deneme[0][1:3]) + 1)