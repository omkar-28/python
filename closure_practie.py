def to_power(x):
    def calc_power(n):
        return n**x
    
    return calc_power

power = to_power(4)
print(power(3))