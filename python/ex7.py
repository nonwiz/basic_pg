
num, is_prime = int(input('Input an integer number:')), True  
if num % 2 == 0: 
    if num == 2:
        print(num, 'is a prime number!')
    else:
        print(num, 'is not a prime number!')   
else:  
    for n in range(3, num, 2):  
        if num % n == 0:
            print('-->', n, 'can divide', num)
            is_prime = False
            break       
    if is_prime:
        print(num, 'is a prime number!')
    else:
        print(num, 'is not a prime number!')  
        
# while True:
#     num = input('Input "s" to start the program and any other key to exit:')
#     if num != 's':
#         break
#     try:
       
#     except:
#         print('The input is not integer type!')
#     print('='*100)
        