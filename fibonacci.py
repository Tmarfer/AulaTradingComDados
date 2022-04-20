def fibonacci(num: int) -> int:
    a = 0
    b = 1

    for i in range (num):
       
        a, b = a+b, a

        return a  
        

result = fibonacci(93) 
print ("foi executado")