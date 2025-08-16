from datetime import date

Data = input("Informe a data: ")
Data = Data.split("/")
diaNacimento, mesNascimento, anoNascimento = Data[0], Data[1], Data[2]

dataAtual = str(date.today())
print(dataAtual)
print(type(dataAtual))
dataAtual = dataAtual.split("-")
diaAtual, mesAtual, anoAtual = dataAtual[0], dataAtual[1], dataAtual[2]

diaNacimento, mesNascimento, anoNascimento = int(diaNacimento, mesNascimento, anoNascimento)
int(diaAtual, mesAtual, anoAtual)


if anoAtual - anoNascimento > 18:
    print("Maior de idade")
else:
    if mesAtual > mesNascimento:
        print("Maior de idade")
    else:
        if diaAtual >= diaNacimento:
            print("Maior de idade")
        else:
            print("Menor de idade")