import threading, time, random

tickets = 100
lock = threading.Lock()
LOG = []

def buyer(name):
    global tickets
    time.sleep(random.uniform(0, 0.01))  # embaralha ordem
    while True:
        with lock:
            if tickets <= 0:
                LOG.append(f"{name}: sem ingressos.")
                break
            # reserva e "vende"
            tickets -= 1
            current = tickets
        # simulando processamento fora da seção crítica
        time.sleep(random.uniform(0, 0.005))
        LOG.append(f"{name}: comprou 1 | restantes={current}")

threads = [threading.Thread(target=buyer, args=(f"T{i}",)) for i in range(8)]
for t in threads: t.start()
for t in threads: t.join()

# checagens simples
sold = sum(1 for line in LOG if "comprou 1" in line)
print(f"Vendido: {sold} | Restantes finais: {tickets}")
print("Exemplos de log:")
for line in LOG[:10]:
    print(line)