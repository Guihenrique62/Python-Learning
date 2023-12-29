name = input('Digite seu Nome:')

name_upper = name.upper()
name_low = name.lower()
name_count = ''.join(name.split())
first_name = name.split()[0]

print(name_upper)
print(name_low)
print(len(name_count))
print(first_name)