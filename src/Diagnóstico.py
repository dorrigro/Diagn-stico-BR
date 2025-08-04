# File: /diagnostico-app/diagnostico-app/src/Diagnóstico.py

import psutil
import platform
import os
import time
import threading
import keyboard  # Certifique-se de instalar esta biblioteca


def check_cpu_usage(stop_event):
    while not stop_event.is_set():
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"Uso da CPU: {cpu_usage}%")
        if cpu_usage > 80:
            print("Alerta: O uso da CPU está alto. Considere fechar alguns aplicativos.")
            break
        time.sleep(1)

def check_memory_usage(stop_event):
    while not stop_event.is_set():
        memory = psutil.virtual_memory()
        print(f"Uso da Memória: {memory.percent}%")
        if memory.percent > 80:
            print("Alerta: O uso da memória está alto. Considere fechar alguns aplicativos.")
            break
        time.sleep(1)

def check_disk_usage(stop_event):
    while not stop_event.is_set():
        disk = psutil.disk_usage('/')
        print(f"Uso do Disco: {disk.percent}%")
        if disk.percent > 90:
            print("Alerta: O uso do disco está muito alto. Considere liberar espaço.")
            break
        time.sleep(1)

def get_system_info():
    print("Informações do Sistema:")
    print(f"Sistema Operacional: {platform.system()} {platform.release()}")
    print(f"Arquitetura: {platform.architecture()[0]}")
    print(f"Nome do Computador: {platform.node()}")

def monitor_usage(stop_event):
    cpu_thread = threading.Thread(target=check_cpu_usage, args=(stop_event,))
    memory_thread = threading.Thread(target=check_memory_usage, args=(stop_event,))
    disk_thread = threading.Thread(target=check_disk_usage, args=(stop_event,))

    cpu_thread.start()
    memory_thread.start()
    disk_thread.start()

    return cpu_thread, memory_thread, disk_thread

def main():
    print("Iniciando diagnóstico do sistema...\n")
    get_system_info()
    
    stop_event = threading.Event()
    cpu_thread, memory_thread, disk_thread = monitor_usage(stop_event)

    try:
        print("Pressione 'Esc' para encerrar o diagnóstico.")
        while True:
            if keyboard.is_pressed('esc'):
                print("Encerrando diagnóstico...")
                stop_event.set()
                break
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nDiagnóstico interrompido.")
        stop_event.set()

    cpu_thread.join(timeout=2)
    memory_thread.join(timeout=2)
    disk_thread.join(timeout=2)
    print("Diagnóstico encerrado.")

if __name__ == "__main__":
    main()