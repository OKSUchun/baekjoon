def mySolution():
    num, base = map(int, input().split())
    answer = ""
    max_digit = 0
    for digit in range(9):# num <= 10 ** 8
        if num < base ** digit :
            max_digit = digit -1
            break
    for i in range(max_digit,-1,-1):
        for j in range(base-1, -1, -1):
            if num >= (base ** i) * j:
                num -= (base ** i) * j
                if j >= 10:
                    answer += chr(j+55)
                    break
                else:
                    answer += str(j)
                    break
            else:
                pass

    print(answer)

 def bookSolution():
    num, base = map(int, input().split())
    answer = ""
    while num:
        if num % base < 10:
            answer += str(num % base)
        else:
            answer += chr((num % base) + 55)
        num = num // base

    print(answer[::-1])

    
    

new_func()