def signo_zodiacal(dia:int, mes:int):
    if (dia >= 21 and dia <= 31 and mes == 3) or (dia >= 1 and dia <= 20 and mes == 4):
        return 'aries'
    elif (dia >= 21 and dia <= 30 and mes == 4) or (dia >= 1 and dia <= 20 and mes == 5):
        return 'tauro'
    elif (dia >= 21 and dia <= 31 and mes == 5) or (dia >= 1 and dia <= 21 and mes == 6):
        return 'geminis'
    elif (dia >= 22 and dia <= 30 and mes == 6) or (dia >= 1 and dia <= 22 and mes == 7):
        return 'cancer'
    elif (dia >= 23 and dia <= 31 and mes == 7) or (dia >= 1 and dia <= 22 and mes == 8):
        return 'leo'
    elif (dia >= 23 and dia <= 31 and mes == 8) or (dia >= 1 and dia <= 22 and mes == 9):
        return 'virgo'
    elif (dia >= 23 and dia <= 30 and mes == 9) or (dia >= 1 and dia <= 22 and mes == 10):
        return 'libra'
    elif (dia >= 23 and dia <= 31 and mes == 10) or (dia >= 1 and dia <= 22 and mes == 11):
        return 'escorpio'
    elif (dia >= 23 and dia <= 30 and mes == 11) or (dia >= 1 and dia <= 21 and mes == 12):
        return 'sagitario'
    elif (dia >= 22 and dia <= 31 and mes == 12) or (dia >= 1 and dia <= 20 and mes == 1):
        return 'capricornio'
    elif (dia >= 21 and dia <= 31 and mes == 1) or (dia >= 1 and dia <= 18 and mes == 2):
        return 'acuario'
    elif (dia >= 19 and dia <= 29 and mes == 2) or (dia >= 1 and dia <= 20 and mes == 3):
        return 'piscis'
    else:
        return ''

dia = int(input()) 
mes = int(input())
print(signo_zodiacal(dia, mes))