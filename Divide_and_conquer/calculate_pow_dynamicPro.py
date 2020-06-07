
def pow_dyn(x,n):
    if n == 1:
        return x
    temp = pow(x,n/2)
    if n%2 == 0:
            return temp * temp
    else:
        return temp * temp * x

x = 4
n = 4
print(pow(x,n))
