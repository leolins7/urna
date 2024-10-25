def menu ():
    print ("1 - Candidato Pão com Ovo")
    print ("2 - Candidato Zé Preguiça")
    print ("3 - Voto nulo")
    print ("4 - Voto em branco")
    print ("0 - Encerrar a votação")
paocovo = zepregui = nulo = branco = 0
while True:
    menu ()
    opcao = int(input("Seleciona uma das opçôes acima: "))
    if opcao < 0:
        print ("Opção Inválida! Informe um número válido:")
    elif opcao > 4:
        print ("Opção Inválida! Informe um número válido: ")
    else:
        match (opcao):
            case 1:
                paocovo = paocovo + 1
                continue
            case 2: 
                zepregui = zepregui + 1
                continue
            case 3: 
                nulo = nulo + 1
                continue
            case 4: 
                branco = branco + 1 
                continue
            case 0: 
                
                if paocovo > zepregui:
                    print ("O vencedor das eleições foi o candidato Pão com Ovo!")
                    print ("A quantidade de votos do candidato Pão com ovo foi: ", paocovo)
                    print ("A quantidade de votos do candidato Zé Preguiça foi:", zepregui)
                    print ("A quantidade de votos nulos foi: ", nulo)
                    print ("A quantidade de votos em branco foi: ", branco)
                    break
                elif zepregui > paocovo:
                        print ("O vencedor das eleições foi o candidato Zé Preguiça!")
                        print ("A quantidade de votos do candidato Pão com ovo foi: ", paocovo)
                        print ("A quantidade de votos do candidato Zé Preguiça foi:", zepregui)
                        print ("A quantidade de votos nulos foi: ", nulo)
                        print ("A quantidade de votos em branco foi: ", branco)
                        break
                elif paocovo == zepregui:
                    print ("Houve um empate nessas eleições.")
                    print ("A quantidade de votos do candidato Pão com ovo foi: ", paocovo)
                    print ("A quantidade de votos do candidato Zé Preguiça foi:", zepregui)
                    print ("A quantidade de votos nulos foi: ", nulo)
                    print ("A quantidade de votos em branco foi: ", branco)
                    break