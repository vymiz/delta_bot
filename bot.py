from addresses import *
from get_strike_func import *
from read_file_func import *
from tb import *
from file_wrtite_func import *

err_counter = 0
old_price = 0

delta_call, strike_first, delta_put, price = read()

delta_call, strike_first, delta_put, price = get_strike(delta_call, strike_first, delta_put, price)

old_pose = delta_call + delta_put

while True:

    # считаем ошибки подключения
    if price == old_price:
        err_counter += 1
    else:
        old_price = price
        err_counter = 0

    # отправляем сообщение, если значение выше триггера
    if err_counter > err_trigger:
        send()

    # получаем массивы данных
    delta_call, strike_last, delta_put, price = read()

    # получаем единичные значения
    delta_call, strike_last, delta_put, price = get_strike(delta_call, strike_last, delta_put, price)

    new_pose = delta_call + delta_put
    trade_pose = new_pose - old_pose
    old_pose = new_pose

    if trade_pose != 0:
        print('call:%-3d  strike:%-6d  put:%-3d  price:%-6d' % (delta_call, strike_first, delta_put, price), end='  ')
        print('pose:%-3d' % trade_pose)
        f_write(trade_pose)

    time.sleep(pause)

    # print('call:%-3d  strike:%-6d  put:%-3d  price:%-6d' % (delta_call, strike_first, delta_put, price), end='  ')
    # print('pose:%-3d' % (delta_call + delta_put))
