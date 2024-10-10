memory_mb = 1.44
memory_kb = memory_mb * 1024
memory_b = memory_kb * 1024

pages = 100
str_ = 50
symb = 25
bites = 4
book = pages * str_ * symb * bites

print("Количество книг, помещающихся на дискету:", int(memory_b // book))
