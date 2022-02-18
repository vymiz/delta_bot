import openpyxl
from addresses import *
import time
from vars import *


def read():
    delta_call = []
    delta_put = []
    strike = []
    price = 0
    try:
        excel_file = openpyxl.load_workbook(xl)
        data_sheet = excel_file['src']
    except:
        time.sleep(1)
        excel_file = openpyxl.load_workbook(xl)
        data_sheet = excel_file['src']

    # currently_active_sheet = excel_file.active

    cells = data_sheet['A1':'D20']

    for d_c, s, d_p, p in cells:
        # print(f'{delta.value}, {strike.value}, {price.value}')
        delta_call.append(int(d_c.value * delta_pose))
        strike.append(s.value)
        delta_put.append(int(d_p.value * delta_pose))
        price = p.value

    return delta_call, strike, delta_put, price


if __name__ == '__main__':
    print(read())

'''
Sub Save1()
Application.DisplayAlerts = False
ThisWorkbook.Save
Application.DisplayAlerts = True

Application.OnTime Now + TimeValue("00:01:00"), "Save1"
End Sub
'''
