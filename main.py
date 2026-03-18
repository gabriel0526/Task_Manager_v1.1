salas = []
matricula = []

while True:
    print("\n=== SISTEMA DE ESCOLA === ")
    print("1 - Matricular aluno")
    print("2 - Encontrar matrícula")
    print("3 - Deletar matricula")
    print("4 - Registrar sala")
    print("5 - Encontrar sala")
    print("6 - trocar de sala")
    print("7 - sair")

    opcao = input("\nescolha uma opção: ")
    
    if opcao not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("opção incorreta. Escolha entre 1, 2 , 3 , 4 ,5 , 6 ou 7")

    if opcao == "1":
        numero = input("numero da matricula: ")
        if numero.strip():
            matricula.append(numero)
            print(f"matricula {numero} feita com sucesso.")
        else:
            print("Digite o numero que a matricula sera criada.") 
    elif opcao == "2":
        if len(matricula) == 0:
            print("Nenhuma matricula registrada com esse numero")
        else:
            print("\nMatriculas enumeradas:")
            for i, matricula in enumerate(matricula,1):
                print(f"{i}, {matricula}")   
                nMatricula = input("Qual dessas é a sua? ")
                if nMatricula == i:
                    print("obrigado!")      
    elif opcao == "3":
        dmatricula = input("Qual matricula excluir? ")
        if dmatricula.isdigit():
            valor_matricula = int(dmatricula)
            if 0 < valor_matricula <= len(matricula):
                deletar = matricula.pop(int(dmatricula) - 1)
                decisao = input("tem certeza que deseja excluir? (s/n) ")
                if decisao == 's':               
                    print("ok!")
                else:
                    print("obrigado, ate logo!")
        else:
            print("matricula inválida!")  
    elif opcao == "4":   
        numero_sala = input("digite o numero da sala: ")
        if numero_sala.strip():     
            salas.append(numero_sala)
            print(f"sala {numero_sala} registrada") 
        else:
            print("sala não registrada.")
    elif opcao == "5":
        if len(salas) == 0:
            print("sala não encontrada, tente outro numero!")
        else:
            print("\nsala encontrada.")
            for i, salas in enumerate(salas,1):
                print(f"{i}, {salas}")
    elif opcao == "6":
        if len(salas) == 0:
            print("Sala não registrada!")
        else:
            indice = int(input("digite o numero da sua sala:  "))
            nova = int(input("para qual sala voce deseja ir? "))
            salas[indice] = nova
            print("troca de salas realizada com sucesso!")
    elif opcao == "7":
        print("até logo!")
        break




     


