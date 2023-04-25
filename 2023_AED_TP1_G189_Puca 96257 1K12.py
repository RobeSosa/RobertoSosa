# Argentina: LLNNNLL
# Bolivia:   LLNNNNN
# Brasil:    LLLNLNN
# Uruguay:   LLLNNNN
# Paraguay:  LLLLNNN

# se asume que todos los países cobran un importe base por cada peaje equivalente a 300 pesos,
# salvo Brasil que cobra peajes en una base de 400 pesos,
# y Bolivia una base de 200 pesos. Asuma que en todos los países ese monto está expresado en pesos argentinos

print("\nCabina de Peajes Centro de Cobros Internacional - Pase-Pase")
print("--Sistema automatizado de Cobro--\n")
print("*" * 20)

patente = str(input("Ingrese los 7 Caracteres de la Patente, en mayuscula, sin espacios: "))
tipo_vehic = int(input("Ingrese el tipo de vehiculo: '0' para Moto; '1' para Autos; '2' para Camiones: "))
forma_pago = int(input("Ingrese la Forma de Pago: '1' para Manual; '2' para Telepeaje: "))
pais_cabina = int(input("Ingrese el Pais de la Cabina:  '0' Argentina; '1' Bolivia; '2' Brasil; '3' Paraguay; '4' Uruguay: "))
distancia = float(input("Ingrese la distancia recorrida desde la ultima cabina, en caso de ser la primera '0': "))

tarif_base = 300

if pais_cabina == 2:  # para modificar las tarifa base si corresponde
    tarif_base = 400
elif pais_cabina == 1:
    tarif_base = 200

ctrl_pat = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ctrl_num_pat = "0123456789"
p = patente
# print(p[0], p[1])
# print(len(p))

if len(p) > 7 or len(p) < 7: # para determirar si pertence o no al grupo de 7 caracteres
    origen_pat = "OTRO"
elif p[0] in ctrl_pat and p[1] in ctrl_pat and p[2] in ctrl_pat and p[3] in ctrl_pat and p[4] in ctrl_num_pat and p[5] in ctrl_num_pat and p[6] in ctrl_num_pat:
    origen_pat = "PARAGUAY"
elif p[0] in ctrl_pat and p[1] in ctrl_pat and p[2] in ctrl_pat and p[3] in ctrl_num_pat and p[4] in ctrl_num_pat and p[5] in ctrl_num_pat and p[6] in ctrl_num_pat:
    origen_pat = "URUGUAY"
elif p[0] in ctrl_pat and p[1] in ctrl_pat and p[2] in ctrl_pat and p[3] in ctrl_num_pat and p[4] in ctrl_pat and p[5] in ctrl_num_pat and p[6] in ctrl_num_pat:
    origen_pat = "BRASIL"
elif p[0] in ctrl_pat and p[1] in ctrl_pat and p[2] in ctrl_num_pat and p[3] in ctrl_num_pat and p[4] in ctrl_num_pat and p[5] in ctrl_num_pat and p[6] in ctrl_num_pat:
    origen_pat = "BOLIVIA"
elif p[0] in ctrl_pat and p[1] in ctrl_pat and p[2] in ctrl_num_pat and p[3] in ctrl_num_pat and p[4] in ctrl_num_pat and p[5] in ctrl_pat and p[6] in ctrl_pat:
    origen_pat = "ARGENTINA"
else:
    origen_pat = "OTRO"

if tipo_vehic == 0:    # Para calcular factor de descuento o recargo
    desc_tipo = 0.5
    tipo = "MOTO"
elif tipo_vehic == 1:
    desc_tipo = 1
    tipo = "AUTO"
elif tipo_vehic == 2:
    desc_tipo = 1.6
    tipo = "CAMION"

if forma_pago == 2:
    desc_forma = 0.9
else:
    desc_forma = 1

monto_final = round(tarif_base * desc_forma * desc_tipo, 2)

if distancia > 0:
    valor_km = round(monto_final / distancia, 2)
    recorrido = True
else:
    recorrido = False

# Indicar el país de procedencia del vehículo, considerando el formato de las placas de los países del Mercosur.
# Si la placa no cumpliera con ninguno de esos formatos, informar que el país es “Otro”.
# Indicar el importe básico a pagar por el vehículo, considerando que si el vehículo es una motocicleta se aplica
# un descuento del 50% sobre el importe base que cobra esa cabina, y si el vehículo es un camión se aplica un recargo
# del 60% sobre el importe base de la cabina. Solo los automóviles pagan el importe base.
# Considerando que si la forma de pago fue por telepeaje se aplica un descuento del 10% al importe calculado en el
# punto anterior, indique el valor final del ticket.
# Informe finalmente a cuánto equivale el valor promedio pagado por ese vehículo por cada kilómetro recorrido desde
# la última cabina
# Recuerde que la cantidad de kilómetros puede ser cero, en cuyo caso no aplica el cálculo, y el programa debe
# informar eso con un mensaje). MODIFICACIÓN: Muestre el promedio redondeado a dos decimales (use para ello la función
# round() que el lenguaje ya provee).


print("*" * 20)
print("-- Ticket de cobro --")
# print("Ud esta usando el Peaje de: ", pais_cabina) faltaria ver de hacer los if para poner le pais de la Cabina
print("\nEl Vehiculo ingresado pertenece a ", origen_pat, " y es del Tipo: ", tipo)
print("Monto total a Pagar es de: $ ", monto_final)
# print("El Monto a pagar correponde al: ", desc_tipo * 100, "%")
if recorrido:
    print("\nEl Valor por Km recorrido es de: $ ", valor_km)
else:
    print("\nNo se peude calcular el Valor por Km recorrido")

print("\nGracias por usar el servico de Pase-Pase!!")

