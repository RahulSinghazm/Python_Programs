Python 3.6.4rc1 (v3.6.4rc1:3398dcb, Dec  5 2017, 20:41:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> price=105.50
qty=36
amount=price*qty
if amount>10000:
    print("10% discount applicable")
    discount=amount*10/100
    amount=amount-discount
else:
    if amount>5000:
    print(" 5% discount applicable ")
    discount=amount*5/100
    amount=amount-discount
    else:
        if amount>2000:
        print(" 2% discount applicable ")
        discount=amount*2/100
        amount=amount-discount
if amount>1000:
    print("1% discount applicable")
    discount=amount*1/100
    amount=amount-discount
else:
print("no discount applicable")
print("amount payable:",amount)
SyntaxError: multiple statements found while compiling a single statement
>>> price=105.50
qty=36
amount=price*qty
if amount>10000:
    print("10% discount applicable")
    discount=amount*10/100
    amount=amount-discount
else:
    if amount>5000:
    print("5% discount applicable")
    discount=amount*5/100
    amount=amount-discount
    else:
        if amount>2000:
        print("2% discount applicable")
        discount=amount*2/100
        amount=amount-discount
        else:
if amount>1000:
    print("1% discount applicable")
    discount=amount*1/100
    amount=amount-discount
else:
print("no discount applicable")
print("amount payable:",amount)
SyntaxError: multiple statements found while compiling a single statement
>>> price=105.50
qty=36
amount=price*qty
if amount>10000:
    print ("10% discount applicable")
    discount=amount*10/100
    amount=amount-discount
else:
    if amount>5000:
        print ("5% discount applicable")
        discount=amount*5/100
        amount=amount-discount
    else:
        if amount>2000:
            print ("2% discount applicable")
            discount=amount*2/100
            amount=amount-discount
        else:
            if amount>1000:
                print ("1% discount applicable")
                discount=amount/100
                amount=amount-discount
            else:
                print ("no discount applicable")
print ("amount payable:",amount)
SyntaxError: multiple statements found while compiling a single statement
>>> price=105.50
qty=36
amount=price*qty
if amount>10000:
    print ("10% discount applicable")
    discount=amount*10/100
    amount=amount-discount
else:
    if amount>5000:
        print ("5% discount applicable")
        discount=amount*5/100
        amount=amount-discount
    else:
        if amount>2000:
            print ("2% discount applicable")
            discount=amount*2/100
            amount=amount-discount
        else:
            if amount>1000:
                print ("1% discount applicable")
                discount=amount/100
                amount=amount-discount
            else:
                print ("no discount applicable")
print ("amount payable:",amount)
SyntaxError: multiple statements found while compiling a single statement
>>> 
