import math

def exact_fun(x):
    return (2.0*math.pow(math.e, -x) + x -1)

def de(x, t):
    return t - x

def approx_fun(wi, ti, h):
    return wi + h*(de(wi, ti))

def error(exact, approx):
    return abs(exact-approx)

def main():
    N = 4
    wo = 1
    lower_bound = 0
    upper_bound = 4
    h = (upper_bound - lower_bound)/(N*1.0)
    print "w approx. actual error"
    print "0 {0} {0} 0".format(wo)
    w = [wo]
    for i in range(lower_bound, N):
        wi = w.pop()
        ti = lower_bound + i*h
        t = lower_bound + (1+i)*h
        print "wi {0} ti {1} t {2}".format(wi, ti, t)
        wi1 = approx_fun(wi, ti, h)
        w.append(wi1)
        exact = exact_fun(t)
        err = error(exact, wi1)
        print "{0} {1} {2} {3}".format(
            i+1, wi1, exact, err
        ) 
        print "\n"

if __name__ == "__main__":
    main()
