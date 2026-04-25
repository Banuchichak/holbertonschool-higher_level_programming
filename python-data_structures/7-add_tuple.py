#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Tuple-ları ən azı 2 elementli hala gətiririk (çatışmayan yerə 0 əlavə edirik)
    # Əgər element 2-dən çoxdursa, [:2] ilə ilk ikisini götürürük
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    
    res_1 = a[0] + b[0]
    res_2 = a[1] + b[1]
    
    return (res_1, res_2)
