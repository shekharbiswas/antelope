import string
a = list(string.ascii_uppercase)

for company in 'HAL':
     print(a[a.index(company) + 1])