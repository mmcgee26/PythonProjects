def toBin(n):
   
    # base case
    if n <= 1:
        return str(n)
   
    return toBin(n//2) + str(n % 2)

print(toBin(14))

## print nth Fibonacci number : Using loop technique
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
print (fib(5))

 
## print nth Fibonacci number : Using recursion
def fibR(n):
    if n==1 or n==2:
        return 1
    return fibR(n-1)+fibR(n-2)

print (fibR(5))



def hanoi(num, _from, _by, _to):
    # base condition, when n == 1, move 1 disk from A to C, which is same as printing the disk move
    if num == 1:
        print("from {} to {} : move disk {}".format(_from, _to, num))
        return

    # pattern for the minimal moves
    hanoi(num-1, _from, _to, _by)                                   # move n-1 disks from A to B
    print("from {} to {} : move disk {}".format(_from, _to, num))   # move 1 disk from A to C (print the disk move)
    hanoi(num-1, _by, _from, _to)                                   # move n-1 disks from B to C

hanoi(3, 'A', 'B', 'C')



