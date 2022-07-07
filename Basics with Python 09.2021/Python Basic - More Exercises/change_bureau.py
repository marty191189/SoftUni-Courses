number_of_bitcoin = int(input())
number_of_ch_u = float(input())
perc_tax = float(input())

one_bitcoin_in_leva = number_of_bitcoin * 1168
one_ch_u_in_dollar = number_of_ch_u * 0.15
one_dollar_in_leva = one_ch_u_in_dollar * 1.76

total_leva = one_bitcoin_in_leva + one_dollar_in_leva
leva_euro = total_leva / 1.95

tax = (perc_tax / 100) * leva_euro

result = leva_euro - tax

print(f"{result:.2f}")
