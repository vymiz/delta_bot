from addresses import *


def f_write(posa):
    with open(real_out_file, 'w') as f:
        tmp = str(posa + '\n')
        f.write(tmp)
