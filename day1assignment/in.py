# Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.
# for num in range(50):
#     if num**3 > 1000:
#         break
#     print(num**3)

# Get first prime numbers up to 100
prime_numbers=[]
num =2
for num in range(2,101):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        prime_numbers.append(num)
print(prime_numbers)



