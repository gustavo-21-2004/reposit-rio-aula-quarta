import threading

# Variável compartilhada
contador = 0

# Função que incrementa o contador
def incrementa():
    global contador
    for _ in range(1000): 
        contador += 1

# Cria as threads
thread1 = threading.Thread(target=incrementa)
thread2 = threading.Thread(target=incrementa)

# Inicia as threads
thread1.start()
thread2.start()

# Aguarda as duas threads terminarem
thread1.join()
thread2.join()

# Exibe o valor final do contador
print(f"Valor final do contador (sem sincronização): {contador}")