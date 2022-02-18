from addresses import *
from get_strike_func import *
from read_file_func import *

delta_call, strike, delta_put, price = read()

delta_call, strike, delta_put, price = get_strike(delta_call, strike, delta_put, price)

print(delta_call, strike, delta_put, price)


