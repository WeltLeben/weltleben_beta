# price = input('Enter the price ($):')
# tax = input('Enter the tax rate (%):')
# net_price = int(price) * int(tax) / 100
# print(f'The net price is ${net_price}')


# a	b	a and b
# True	True	True
# True	False	False
# False	False	False
# False	True	False

# a	b	a or b
# True	True	True
# True	False	True
# False	True	True
# False	False	False

# a	not a
# True	False
# False	True

# Operator	Precedence
# not	High
# and	Medium
# or	Low

# a or b and c	means	a or (b and c)
# a and b or c and d	means	(a and b) or (c and d)
# a and b and c or d	means	((a and b) and c) or d
# not a and b or c	means	((not a) and b) or c


# IF ELSE
# age = input('Enter your age: ')
# if int(age) >= 18:
#     print(f'You are {age} years old')
# else:
#     print(f'Your age {age} years old and you can not smoke')


# IF ELIF ELSE
# age = input('Enter your age: ')
# # convert the string to int
# your_age = int(age)
# # determine the ticket price
# if your_age < 5:
#     ticket_price = 5
# elif your_age < 16:
#     ticket_price = 10
# else:
#     ticket_price = 18
# # show the ticket price
# print(f" You'll pay ${ticket_price} for the ticket")


# Ternary Operator
# age = input('Enter your age: ')
# ticket_price = 20 if int(age) >= 18 else 5
# print(f"The ticket price is {ticket_price}")


# FOR LOOP
# range(start, stop, step)
# for i in range(1, 6):
#     print(i)

# for i in range(0, 11, 2):
#     print(i)

# sum = 0
# for num in range(101):
#     sum += num
# print(sum)

# n = 100
# sum = n * (n + 1) / 2
# print(sum)


# WHILE
# max = 5
# counter = 0
# while counter < max:
#     counter += 1
#     print(counter)

# command = ''
# while command.lower() != 'quit':
#     command = input('>')
#     print(f"Echo: {command}")


# BREAK 
# for i in range(0, 10):
#     print(i)
#     if i == 3:
#         break

# print('-- Help: type quit to exit --')
# while True:
#     color = input('Enter your favorite color: ')
#     if color.lower() == 'quit':
#         break


# CONTINUE
# for i in range(10):
#     if i % 2:
#         continue
#     print(i)

# counter = 0
# while counter < 10:
#     counter += 1
#     if not counter % 2:
#         continue
#     print(counter)


# PASS
# c = 1
# m = 10
# if c <= m:
#     c += 1
# else:
#     pass

# FUNCTION
# def sum(a, b):
#     return a + b
# total = sum(10, 20)
# print(total)

# def greet(name, message='Hi'):
#     return f"{message} {name}"
# greeting = greet('John')
# print(greeting)

# def greet(name, message="Hallo"):
#     return f"{message} {name}"
# greeting = greet('John', 'Hi')
# print(greeting)

# def greet(name='John', message='Hi'):
#     return f"{message} {name}"
# greeting = greet()
# print(greeting)

# def get_net_price(price, diskount):
#     return price * (1 - diskount)
# net_price = get_net_price(100, 0.1)
# print(net_price)

# def get_net_price(price, tax = 0.07, discount = 0.05):
#     return price * (1 + tax - discount)
# net_price = get_net_price(100)
# print(net_price)

# def count_down(start):
#     print(start)
#     next = start - 1
#     if next > 0:
#         count_down(next)
# count_down(10)

# def sum(n):
#     if n > 0:
#         return n + sum(n - 1)
#     return 0
# result = sum(100)
# print(result)

# LISTS
# numbers = [1,2,3,4,5,6]
# numbers.append(100)
# print(numbers)

# numbers = [1,2,3,4,5,6]
# numbers.insert(0, 100)
# print(numbers)

# numbers = [1,2,3,4,5,6]
# del numbers[2]
# print(numbers)

# numbers = [1,2,3,4,5,6]
# last = numbers.pop(2)
# print(last)
# print(numbers)

# numbers = [1,2,3,4,5,6]
# numbers.remove(5)
# print(numbers)

# numbers = [1, 3, 2, 7, 9, 4]
# numbers.clear()
# print(numbers)

# SORT LISTE
# guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
# guests.sort()
# print(guests)

# scores = [5, 7, 4, 6, 9, 8]
# scores.sort(reverse=False)
# print(scores)

# companies = [('Google', 2019, 134.81),
#              ('Apple', 2019, 260.2),
#              ('Facebook', 2019, 70.7)]
# # sort the companies by revenue
# companies.sort(key=lambda company: company[2])
# # show the sorted companies
# print(companies)