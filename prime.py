prime_list=[]
for number in range (1, 51):
    if number > 1:  
        for i in range(2, number):
            if (number % i) == 0:  
                break  
        else:  
            prime_list.append(number)
print(prime_list)