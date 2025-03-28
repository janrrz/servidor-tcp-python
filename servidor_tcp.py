import socket

def servidor_tcp():
    """
    Crea un servidor TCP que escucha en localhost:5000.
    """
    host = 'localhost'
    puerto = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((host, puerto))
        servidor.listen()
        print(f"Servidor escuchando en {host}:{puerto}")

        while True:
            conexion, direccion = servidor.accept()
            print(f"Conexión establecida con {direccion}")

            with conexion:
                while True:
                    datos = conexion.recv(1024).decode()
                    if not datos:
                        break

                    if datos == "DESCONEXION":
                        print(f"Cliente {direccion} solicitó desconexión.")
                        break
                    else:
                        mensaje_mayusculas = datos.upper()
                        conexion.sendall(mensaje_mayusculas.encode())

            print(f"Conexión con {direccion} cerrada.")

if __name__ == "__main__":
    servidor_tcp()
