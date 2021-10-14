import socket
import time

def server(host = 'localhost', port=46864):
    data_payload = 2048  # The maximum amount of data to be received at once
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print("Starting up echo server  on %s port %s" % server_address)
    sock.bind(server_address)
    # Listen to clients, argument specifies the max no. of queued connections
    
    sock.listen(5)
    
    
    i = 0
    while True:
        print("Aguardando Cliente se concetar")
        client, address = sock.accept()
        client.sendall(bytes("Bem vindo ao servidor Socket", "utf-8"))
        
        client.setblocking(0)
        
        #data = client.recv(data_payload)
        
        print('Cliente Conectado!')
        while True:
            
            i += 1
            time.sleep(2)
            try:
                client.sendall(bytes("Dados do servidor " +  str(i) + '\r\n', "utf-8"))
            except:
                print('Cliente desconectado')
                break
        
        '''
        if data == str.encode( ID_SENSOR + '_REQUEST'):
           
           print(data) 
           #client.close()
            
        elif data == str.encode(ID_SENSOR + '_RESET'):
           
            client.send(str.encode(ID_SENSOR + '_RST_OK'))
            #client.close()
            
        elif  (ID_SENSOR +  '_SET') in data.decode("utf-8"):
           
            
            string_data = data.decode("utf-8").replace( ID_SENSOR + '_SET', '')
            
            
            string_data = ID_SENSOR + '_NEW_COUNT_' + string_data
            my_str_as_bytes = str.encode(string_data)
            client.send(my_str_as_bytes)
        
            
        elif data == b'CLOSE':
            client.send(b'Close server')
            client.close()
            sock.close()
            break
        else:
            string_data = data.decode("utf-8")
            string_data = 'Invalid Message:' + string_data
            print(string_data)
            
            my_str_as_bytes = str.encode(string_data)
            
            client.send(my_str_as_bytes)
            #client.close()
        '''

server()