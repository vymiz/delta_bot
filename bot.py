from addresses import *
from get_strike_func import *
from read_file_func import *

pause = 15

delta_call, strike_first, delta_put, price = read()

delta_call, strike_first, delta_put, price = get_strike(delta_call, strike_first, delta_put, price)


while True:
    delta_call, strike_last, delta_put, price = read()
    delta_call, strike_last, delta_put, price = get_strike(delta_call, strike_last, delta_put, price)
    print(delta_call, strike_first, delta_put, price, end=' ')
    print(delta_call + delta_put)

    time.sleep(pause)