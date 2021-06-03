import threading
import time

def sec():
    for i in range(0,5):
        print("Segundos:",i+1)
        time.sleep(1)

def dec():
    for i in range(0,50):
        print("Décimos:",i+1)
        time.sleep(0.1)

threading.Thread(target=dec).start()
threading.Thread(target=sec).start()

# Exemplo de thread usando python, enquanto a thread 1 mostra de um em um segundo a 2 ao mesmo tempo mostra o décimos de segundo