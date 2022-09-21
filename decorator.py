# Decorator -- > Its a function, its modify the functionality of i/p function.
# it take input as function and give output as function but with modified functionality of function
# input function --> decorator --> output function (modified functionality)

def decor_result(result_func):                  # mofified function or decorator function
    def distinction(marks):                      # output function of decorator
        for m in marks:
            if m>=70:
                print("Distinction")
            else:
                result_func(marks)
    return distinction
@decor_result                            # this @decore_result is call to decorator function or input function via decorator.  
def result(marks):                      # input function to decorator
    for m in marks:
        if m>33:
            pass
        else:
            print("Fail")
            break
    else:
        print("Pass")
result([70,40,50,60,80])