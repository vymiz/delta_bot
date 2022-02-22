from addresses import *
from get_strike_func import *
from read_file_func import *
from tb import *
from file_wrtite_func import *

err_counter = 0
old_price = 0

delta_call, strike_first, delta_put, price = read()

delta_call, strike, delta_put, price = get_strike(delta_call, strike_first, delta_put, price)

# old_pose = delta_call + delta_put
old_pose = 0
print('Strike: ', strike)
print('Delta Call : ', delta_call)
print('Delta Put: ', delta_put)
print('Start Pose: ', old_pose)

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
    delta_call_array, strike_array, delta_put_array, price = read()

    # получаем единичные значения
    # delta_call, strike_last, delta_put, price = get_strike(delta_call, strike_last, delta_put, price)
    delta_call_dict, delta_put_dict = get_delta_by_strike(delta_call_array, strike_array, delta_put_array, price)
    delta_call = delta_call_dict[strike]
    delta_put = delta_put_dict[strike]

    new_pose = delta_call + delta_put
    pose = new_pose - old_pose
    old_pose = new_pose

    if pose != 0:
        print('call:%-3d  strike:%-6d  put:%-3d  price:%-6d' % (delta_call, strike, delta_put, price), end='  ')
        print('pose:%-3d' % pose)
        f_write(pose)

    time.sleep(pause)
