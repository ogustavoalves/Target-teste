import numpy as np

monthly_billing = np.array([["SP", 67836.43],
["RJ", 36678.66],
["MG", 29229.88],
["ES", 27165.48],
["Outros", 19849.53]
])

total = 0
for x in range(len(monthly_billing)):
    total += float(monthly_billing[x][1])


percentage = lambda state, total : (state/ total) * 100

for y in range(len(monthly_billing)):
    result = percentage(float(monthly_billing[y][1]), total)
    print(f'state {monthly_billing[y][0]} participation percentage: {result:.2f}')