print('# tempJoaoSantana\n')

temp = int(input('Digite a temperatura: '))

print(f'\nEm qual escala está a sua temperatura?')
escala = int(input('\n# Escalas:\n 1- °C\n 2- °F\n 3- ºK\n = '))

if escala == 1:
    resposta = input(f'\nTemperatura = {temp} / Escala = Celsius.\nAperte ENTER para continuar\n')
    

elif escala == 2:
    resposta = input(f'\nTemperatura = {temp} / Escala = Fahrenheit.\nAperte ENTER para continuar\n')
    

elif escala == 3:
    resposta = input(f'\nTemperatura = {temp} / Escala = Kelvin.\nAperte ENTER para continuar\n')
    

print('\nAgora vamos convertê-la... Aperte ENTER para continuar\n')


resposta = 0

calc = int(input('Em qual escala você quer converter?\n 1- °C\n 2- °F\n 3- ºK\n = '))

if calc != escala:

    if calc == 1:
        print(f'\nCerto, você quer converter {temp}º em Celsius. Aperte ENTER para continuar.')
        input('')
    elif calc == 2:
        print(f'\nCerto, você quer converter {temp}º em Fahrenheit. Aperte ENTER para continuar.')
        input('')
    elif calc == 3:
        print(f'\nCerto, você quer converter {temp}º em Kelvin. Aperte ENTER para continuar.')
        input('')
    else:
        print('\nEsta não é uma das opções...')
        quit()

elif calc == escala:
    print('\nA temperatura já está nessa escala, acho que você se confundiu... Encerrando.')
    input('')
    quit()


if escala == 2 and calc == 1:
    temp = temp - 32

    temp = temp / 9

    formula = 5

    conta = temp * 5

    input(f'Aperte ENTER para ver o resultado.')
    print(f'{conta:.2f}°C')
    input('')


if escala == 1 and calc == 2:
    div = 9 / 5

    temp = temp * div

    soma = temp + 32

    input(f'Aperte ENTER para ver o resultado.')
    print(f'\n{soma:.2f}°F')
    input('')


if escala == 2 and calc == 1:
    temp = temp - 32

    temp = temp / 9

    temp = temp * 5

    input(f'Aperte ENTER para ver o resultado.')
    print(f'\n{temp:.2f}ºK')
    input('')


if escala == 1 and calc == 3:
    temp = temp + 273

    input(f'Aperte ENTER para ver o resultado.')
    print(f'\n{temp:.2f}ºK')
    input('')


if escala == 3 and calc == 1:
    temp = temp - 273.15

    input(f'Aperte ENTER para ver o resultado.')
    print(f'\n{temp:.2f}ºK')
    input('')


if escala == 3 and calc == 2:
    temp = temp - 273.15

    div = 9 / 5

    temp = temp * div

    temp = temp + 32

    input(f'Aperte ENTER para ver o resultado.')
    print(f'\n{temp:.2f}°F')
    input('')


if escala == 2 and calc == 3:
    temp = temp - 32

    div = 5 / 9

    temp = temp * div

    temp = temp + 273.15

    input(f'Aperte ENTER para ver o resultado.')
    print(f'\n{temp:.2f}ºK')

exit()