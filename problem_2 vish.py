def euler_2(limit = 4000000):
    limit_check = True
    fibonacci = [1,2]
    even_sum = 2
    
    while limit_check:
        new_term = fibonacci[-1] + fibonacci[-2]
        if new_term%2==0:
            even_sum+=new_term
        fibonacci.append(new_term)

        if new_term>limit:
            limit_check = False
        
    print(even_sum)

euler_2()


        
