import math

exact_integral = 0.849726
def fun(x):
    return math.sin(math.sqrt(math.pi) * math.sqrt(x))

def approximation(f, lower_bound, upper_bound, n):
    h = (upper_bound - lower_bound)/(n*1.0)
    approx = f(lower_bound) + f(upper_bound)
    for i in range(1, n):
        xj = (i*h)+lower_bound
        approx = approx + (2*fun(xj))
    return approx*h*0.5, h;

def error(exact, approx):
    return abs(exact-approx)

def main():
    keep_eh = [1,2,4,8,16,32,64,128,156]
    eh = []
    print "n h Th(f) eh e2h/eh"
    for i in range(1, 17):
        a = approximation(fun, 0, 1, i)
        e = error(exact_integral, a[0])
        if (i in keep_eh):
            eh.append(e)
            e2h = eh[len(eh)-2]/e
        else:
            e2h = 0
        print "{0} {1} {2} {3} {4}".format(
            i, a[1], a[0], e, e2h
        ) 

if __name__ == "__main__":
    main()
