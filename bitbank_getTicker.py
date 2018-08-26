import python_bitbankcc

pub = python_bitbankcc.public()
value = pub.get_ticker(
    'xrp_jpy'
)
print(value)

print('sell:' + value['sell'])
print('buy:' + value['buy'])
print('high:' + value['high'])
print('low:' + value['low'])
