a=float(input());
b=float(input());
op=input();
if op=="+": print(a+b);
if op=="-": print(a-b);
if op=="*": print(a*b);
if op=="pow": print(pow(a,b));
if op=="/":
    if b!=0: print(a/b);
    else: print("Деление на 0!");

if op=="mod":
    if b!=0: print(a % b);
    else: print("Деление на 0!");

if op=="div":
    if b!=0: print(a // b);
    else: print("Деление на 0!");
