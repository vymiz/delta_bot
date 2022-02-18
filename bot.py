from addresses import *
from get_strike_func import *
from read_file_func import *

pause = 15

delta_call, strike_first, delta_put, price = read()

delta_call, strike_first, delta_put, price = get_strike(delta_call, strike_first, delta_put, price)

old_pose = delta_call + delta_put

while True:
    # получаем массивы данных
    delta_call, strike_last, delta_put, price = read()

    # получаем единичные значения
    delta_call, strike_last, delta_put, price = get_strike(delta_call, strike_last, delta_put, price)

    new_pose = delta_call + delta_put
    trade_pose = new_pose - old_pose
    old_pose = new_pose

    print('call:%-3d  strike:%-6d  put:%-3d  price:%-6d' % (delta_call, strike_first, delta_put, price), end='  ')
    print('pose:%-3d' % trade_pose)

    time.sleep(pause)

    # print('call:%-3d  strike:%-6d  put:%-3d  price:%-6d' % (delta_call, strike_first, delta_put, price), end='  ')
    # print('pose:%-3d' % (delta_call + delta_put))
