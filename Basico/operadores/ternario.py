lockdown = False
grana = 30

status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuuu'
# TERNARIO = RESULTADO VERDADEIRO + EXPRESSAO LOGICA + RESULTADO FALSO

print(f'O status e: {status}')