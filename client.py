import socket

def main():
    # Configuración del cliente
    host = '127.0.0.1'  # localhost
    port = 5000

    # Creación del socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conexión al servidor
    client_socket.connect((host, port))

    # Envío de datos al servidor
    message = "Hola desde el cliente"
    client_socket.send(message.encode('utf-8'))

    # Recepción de la respuesta del servidor
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Respuesta del servidor: {data}")

    # Cierre de la conexión
    client_socket.close()

if __name__ == "__main__":
    main()
