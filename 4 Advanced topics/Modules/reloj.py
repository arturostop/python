import datetime, locale, time, os
locale.setlocale(locale.LC_ALL, '')

# loop infinito
while True:
    
    # dt = fecha y hora actual
    dt = datetime.datetime.now()
    # Muestra fecha formateada
    print(dt.strftime("%A %d %B %Y - %H:%M:%S"))
    # Espera 1 segundo
    time.sleep(1)
    # Limpia la pantalla
    os.system('cls')