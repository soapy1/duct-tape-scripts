import math

def exact_fun(x):
    return x 

def de(x, t):
    return 2 - (x*1.0/t)

def approx_fun(wi, ti, h):
    return wi + h*(de(wi, ti))

def error(exact, approx):
    return abs(exact-approx)

def theoretical_error(n):
    return ((35.0/(6*n))*(math.pow(math.e, 30)-1))

def get_approx_at_upper_bound(n):
    N = n
    wo = 1
    lower_bound = 1
    upper_bound = 6
    h = (upper_bound - lower_bound)/(N*1.0)
    w = [wo]
    for i in range(lower_bound, N):
        wi = w.pop()
        ti = lower_bound + i*h
        t = lower_bound + (1+i)*h
        wi1 = approx_fun(wi, ti, h)
        w.append(wi1)
        exact = exact_fun(t)
    
    return h, wi1

def b():
    print "h, approx. sol, error ratio"
    error = [0]
    for i in range(1, 5):
        n = 5*math.pow(2, i)
        a = get_approx_at_upper_bound(int(n))
        err = abs(6 - a[1])
        err_ratio = error.pop()/err
        error.append(err)
        print "{0} {1} {2}".format(
            a[0], a[1], err_ratio
        )

def a():
    print "h, approx. sol, error ratio"
    error = [0]
    for i in range(1, 5):
        n = 5*math.pow(2, i)
        a = get_approx_at_upper_bound(int(n))
        err = theoretical_error(n)
        err_ratio = error.pop()/err
        error.append(err)
        print "{0} {1} {2}".format(
            a[0], a[1], err_ratio
        )

if __name__ == "__main__":
    b()
