#Uses the Euclidean algorithm to find the greatest common divisor of two integers.
def gcd(int1,int2):
    min_int = min(int1,int2)
    max_int = max(int1,int2)

    remainder = max_int%min_int
  
    if remainder == 0:
        return min_int
    else:
        return gcd(min_int,remainder)
