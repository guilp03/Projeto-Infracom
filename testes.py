import datetime

hora_data_atual = datetime.datetime.now()

def Formatar_Horario(horario):
    separacao = horario.split(" ")
    data = separacao[0]
    hora = separacao[1]
    data_separada = data.split("-")
    hora_separada = hora.split(".")
    data_fomatada = f"{data_separada[2]}/{data_separada[1]}/{data_separada[0]}"
    hora_data = f"{hora_separada[0]} {data_fomatada}"
    return hora_data
tempo = Formatar_Horario(str(hora_data_atual))
print(tempo)