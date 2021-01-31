i = [11, 13, 27, 30, 29, 13, 21, 1, 8, 20, 17, 5, 19, 9, 11, 22, 15, 23, 0, 6, 12, 7, 17, 14, 16, 4, 28, 3, 8, 4]

for i in range(1, 31):
    if( i% 3 == 0 and  i% 5 == 0):
        print("FizzBuzz")
    elif(i% 5 == 0):
        print('Buzz')
    elif(i% 3 == 0):
        print('Fizz')
    else:
        print(i)
    


    

    