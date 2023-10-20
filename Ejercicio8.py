a = round(float(input("Dime el precio del producto:")),2)
b = str(a)
print("el producto vale {} € y {} céntimos".format(b[0:-3], b[-2:]))
input()
