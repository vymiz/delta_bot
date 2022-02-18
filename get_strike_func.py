def get_strike(delta_call, strike, delta_put, price):
    diff = []
    for i in strike:
        diff.append(abs(i - price))

    d_c = dict(zip(diff, delta_call))
    s = dict(zip(delta_call, strike))
    d_p = dict(zip(diff, delta_put))

    return d_c[min(d_c.keys())], s[d_c[min(d_c.keys())]], d_p[min(d_p.keys())], price

