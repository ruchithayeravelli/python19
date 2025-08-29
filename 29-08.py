# scope - 
num1 = 10 # gobal scope
def test_funtion():
    num1 = 20 # local scope
    def inner_function():
        num1 = 45  #loacl scope
        print(num1)
    inner_function()
    print(num1)
test_funtion()
print(num1)
#  loacl change chesthye adhi gobal lo kuda print kavalii function loo kuda work avali weeee use global
num1 = 10
def test_funtion():
    global num1   #function motham kavali ante edhi us cehyali
    num1 = 35
    globals()['num1'] = 50 # dict ki change chestharu global loo
    print(num1)
test_funtion()
print(num1)
# get answer 35 35 beacause global resigned


# nonlocal
num1 = 10
def printer():
    num2 = 35 # num2 ni change cheyali
    def inner_function():
        nonlocal num2  # ee  enclosed function lo change chesthye local loo  kuda change avuthadhi #inerest dhani medhi work avuthadhi in case two funcations or variabels unte
        num2 = 45
        print(num2)
        print("inner function")
    inner_function()
    print(num2)
printer()



def swap():
    global a
    global b
    a, b = b,a
a = 10
b = 20
# lifetime - scope or same
# scope -work on particular area
# lifetime - num1 antha sepu available untadhi in that particular function
