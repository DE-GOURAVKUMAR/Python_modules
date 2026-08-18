def square_root_bisection(number, tolerance_value=1e-2,max_iter=10):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if number == 1 or number == 0:
        print(f"The square root of {number} is {number}")
        return number
    num = len(f"{tolerance_value:.10f}".rstrip('0').split('.')[1])
    low = 0.0
    high = max(1.0, float(number))
    j = max_iter

    for _ in range(max_iter):
        mid = (low+high) /2.0
       
        mid_sq = mid * mid
        if abs(mid_sq - number) <= tolerance_value:
            print(f"The square root of {number} is approximately {mid}")
            return mid
        
        if mid_sq > number:
            high = mid
            max_iter -= 1
        else:
            low = mid
            max_iter -= 1
            
    print(f"Failed to converge within {j} iterations")
    return None
        

square_root_bisection(0.001, 1e-7, 30)