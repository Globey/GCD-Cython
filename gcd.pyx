%cython
def gcd(long int1,long int2):
    cdef long min_int = min(int1,int2)
    cdef long max_int = max(int1,int2)

    remainder = max_int%min_int

    if remainder == 0:
        return min_int
    else:
        return gcd(min_int,remainder)
