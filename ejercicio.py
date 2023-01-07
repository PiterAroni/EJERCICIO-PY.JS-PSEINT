decimal_base = float(input("Ingrese primer decimal: "))
print("decimal_base : ", decimal_base)

while True:
    decimal_next = float(input("Ingrese siguiente decimal: "))
    print(decimal_next)
    if decimal_next < decimal_base:
        print("PROGRAMA FINALIZADO")
        break

