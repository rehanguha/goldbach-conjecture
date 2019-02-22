def prim(n):
    primes = []
    for num in range(1, n + 1):     
        limit = int(num ** 0.5) + 1 # search limit
        for div in range(2, limit): # searching for divider
            if (num % div) == 0:    # divider found
                break               
        else:                       
            primes.append(num)      # no divider found hence prime
    return(primes)

num = int(input('Input an even number: '))
#num =100
primes = prim(num)               

for i in range(num//2 + 1):
    if num % 2 != 0:
        print(num, 'not even'); break
    if i in primes and (num - i) in primes:
        print(i, num - i)
