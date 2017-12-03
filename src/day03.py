sums = 1
add = 1
n = 368078
counter = 0
while(sums<=n):
    counter+=1
    add += 8
    sums += add
    print(counter + (n- sums))
