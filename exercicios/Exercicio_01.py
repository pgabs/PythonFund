# Criar uma aplicação de Calculo de média


# Entradas:
    # nome do aluno
    # n1 - nota número 01
    # n2 - nota número 02
    # n3 - nota número 03
    # n4 - nota número 04
# Saída:
    # Retornar a média do aluno no formato:
    
    # Nome do aluno
    # Nota final
    
nome_aluno = input('Digite nome do aluno')
nota_01 = float (input ('Nota 01 '))
nota_02 = float (input ('Nota 02 '))
nota_03 = float (input ('Nota 03 '))
nota_04 = float (input ('Nota 04 '))

media = (nota_01+nota_02+nota_03+nota_04)/4

print ("A nota do aluno' {} 'é igual a:  {} ".format (nome_aluno,media))

