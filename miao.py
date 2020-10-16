def newton(a, b, c, d,X):
    x = X
    if a == 0 and c ** 2 - 4 * b * d < 0:
        print("无解")
    elif a == 0 and b == 0 and c == 0 and d != 0:
        print("无解")
    elif a == 0 and b == 0 and c == 0 and d == 0:
        print("恒等")
    else:
        while abs((a * x * x * x + b * x * x + c * x + d) / (3 * a * x * x + 2 * b * x + c)) >(0.5*0.00001):
            x1=x-(a * x * x * x + b * x * x + c * x + d) / (3 * a * x * x + 2 * b * x + c)
            x=x1
            d=x-x1
            print("%.6f"%x1,end=" ")
            print("%.6f"%d)
a,b,c,d,x=input().split()
newton(float(a),float(b),float(c),float(d),float(x))

