#Every top right corner is equal to (2*n-1)**2,sum it with the bottom right corner, which is equal to ((2*n-1)**2)-6(n-1), then you multiply that sum by 2 (to take into account the top left corner and the bottom left corner)
def diagonalSum(n):
    return 16*(n**2)-28*n+16
answer=1 #the formula doesn't work for 1
for i in range(2,502):
    answer+=diagonalSum(i)
print(answer)