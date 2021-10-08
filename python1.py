print("Hello Word")
data = int(input("Que dia é hoje?"))

ontem = data - 1
amanha = data + 1

if data == 31:
    amanha = 1
    print("Ontem foi dia", ontem)
    print("Hoje é dia", data)
    print("Amanha é dia", amanha)
elif data <= 1:
    ontem = 31
    print("Ontem foi dia", ontem, "ou", ontem-1)
    print("Hoje é dia", data)
    print("Amanha é dia", amanha)
elif data > 31:
    print("ESTE DIA NÃO EXISTE")
else:
    print("Ontem foi dia", ontem)
    print("Hoje é dia", data)
    print("Amanha é dia", amanha)
