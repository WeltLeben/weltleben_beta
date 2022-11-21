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
