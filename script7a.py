def c_to_f(c):
    if c < -273.15:
        return "ngawaduk sia nya"
    else:
        f=c*9/5+32
        return f

temperature=[10,-20,-300,100]
for item in temperature:
    print(c_to_f(item))
