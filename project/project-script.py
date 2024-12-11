
#T11
def ler_config(S):
    config = open(f"dados_v11\config_{S}.txt",'r')
    populacao = {}
    for line in config:
        value = line.replace(" ","")
        value = line.split('=')
        value = [item.strip() for item in value]
        print(value)
        if value[0] == "DESCONTOS":
            populacao.update({value[0]:float(value[1])})
        elif value[0] == "MORTALIDADE":
            populacao.update({value[0]:eval(value[1])})
        elif value[0] == "IDADE_REFORMA":
            try:
                populacao.update({value[0]:eval(value[1])})
            except:
                populacao.update({value[0]:value[1]})
        elif value[0] == "ACTIVO" or value[0] == "PENSIONISTA":
            try:
                populacao.update({value[0]:eval(value[1])})
            except:
                populacao.update({value[0]:value[1]})
        else:
            populacao.update({value[0]:eval(value[1])}) 
    return populacao

#T12
contador_cc = 1000000
def nova_pessoa(idade = 0):
    global contador_cc
    cc = contador_cc
    contador_cc += 1
    genero = 'M'
    if contador_cc %2 != 0:
        genero = 'F'
    pessoa={
        'cc':cc,
        'nome':f'Pessoa_{cc}',
        'genero': genero,
        'idade': idade,
        'salário':1000,
        'pensão':500
    } 
    return pessoa

#T13

def ler_populacao_inicial(S):
    populacao_incial = open(f"dados_v11\populacao_inicial_{S}.txt",'r')
    for line in populacao_incial:
        value = line.replace(" ","")
        value = line.split(',')
        value = [item.strip() for item in value]
        pessoa = nova_pessoa(value[3])
    return pessoa

print(ler_config(11))
print(ler_populacao_inicial(11))
