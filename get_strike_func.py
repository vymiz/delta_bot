def get_strike(delta_call, strike, delta_put, price):
    diff = []
    for i in strike:
        diff.append(abs(i - price))

    d_c = dict(zip(diff, delta_call))
    s = dict(zip(delta_call, strike))
    d_p = dict(zip(diff, delta_put))

    return d_c[min(d_c.keys())], s[d_c[min(d_c.keys())]], d_p[min(d_p.keys())], price


def get_delta_by_strike(delta_call, strike, delta_put, price):
    call_dict = dict(zip(strike, delta_call))
    put_dict = dict(zip(strike, delta_put))
    return call_dict, put_dict


if __name__ == '__main__':

    from read_file_func import *

    delta_call, strike_first, delta_put, price = read()
    # d_c, s, d_p, p = get_strike(delta_call, strike_first, delta_put, price)
    # print(get_strike(delta_call, strike_first, delta_put, price))
    # print(read())
    cd, pd = (get_delta_by_strike(delta_call, strike_first, delta_put, price))
    print(cd[77250])
    print(pd[77250])
