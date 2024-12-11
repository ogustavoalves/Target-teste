import random

def random_number_generator(start, end):
    x = round(random.uniform(start, end), 2)
    return x



monthly_billing = [random_number_generator(200, 1000) for _ in range(31)]

# print(monthly_billing)

# menor valor no mês

# for x in range(len(monthly_billing)):
#     if monthly_billing[x] < min_val:
#         min_val = monthly_billing[x]




# maior valor no mês
min_val = monthly_billing[0]
max_val = monthly_billing[0]
for x in range(len(monthly_billing)):
    if monthly_billing[x] > max_val:
        max_val = monthly_billing[x]
    if monthly_billing[x] < min_val:
        min_val = monthly_billing[x]

print (f"o MAIOR valor na lista é: {max_val:.2f}")
print (f"o MENOR valor na lista é: {min_val:.2f}")