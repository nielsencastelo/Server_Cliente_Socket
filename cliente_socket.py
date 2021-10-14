import socket
def client(host = '10.91.132.92', port=46864):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server
    server_address = (host, port)
    print ("Conectando na  %s port %s" % server_address)
    sock.connect(server_address)
    
    # Send data
    try:
        
        #message = '05_REQUEST'
        #print ("Sending %s" % message)
        #rodando = sock.sendall(message.encode('utf-8'))
        recebido = None
        while True:
            
                # Send data
                # ID_REQUEST Informa o valor de contagem atual do sensor
                # 03_RESET Reseta o valor de contagem do sensor
                # ID_SET Modifica o valor de contagem atual
                # CLOSE finaliza o servidor
                
           
                # recebe a resposta do servidor
            #data = sock.recv(16)
            recebido = sock.recv(16)
            if recebido:
                print('Recebido: ', recebido.decode())
    
        
    except socket.error as e:
        print ("Socket error: %s" %str(e))
    except Exception as e:
        print ("Other exception: %s" %str(e))
    finally:
        print ("Closing connection to the server")    
    sock.close()

client()
