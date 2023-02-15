# programa para convertir una cantidad dada de grados centigrados a su equivalente en grados fahrenheit

print("------------------------------")
print("---Conversor de Temperatura---")
print("------------------------------")

# input
C = int(input (" digite el valor de C: "))

# processing
F = (C * 1.8 + 32)
K = ( C + 273.15)

#output
print("--------------------------------------")
print("-------------RESULTADOS---------------")
print("--------------------------------------")
print("la converción de " + str(C) + " grados celcius a grados fahrenheint es " + str(F))
print("la converción de " + str(C) + " grados celcius a grados Kelvin es " + str (K))