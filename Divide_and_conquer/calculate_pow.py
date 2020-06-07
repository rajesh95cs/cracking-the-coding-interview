
import time

def pow(x,n):
    if n == 1:
        return x
    else:
        if n%2 == 0:
            return pow(x,n/2) * pow(x,n/2)
        else:
            return pow(x,n/2) * pow(x,n/2) * x

def pow_dyn(x,n):
    if n == 1:
        return x
    temp = pow(x,n/2)
    if n%2 == 0:
            return temp * temp
    else:
        return temp * temp * x


x = 2
n = 16
start_time = time.time()
pow1 = pow(x,n)
end_time = time.time()
execution_time_1 = start_time - end_time
print "execution_time_pow = ",abs(execution_time_1)
print pow1
start_time = time.time()
pow2 = pow_dyn(x,n)
end_time = time.time()
execution_time_2 = start_time - end_time
print "execution_time_pow_dynamic = ",abs(execution_time_2)
print pow2

time_difference = execution_time_1 - execution_time_2
print "time_difference = ",abs(time_difference)
