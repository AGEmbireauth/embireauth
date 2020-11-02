import socket
HOST = '0.0.0.1'  
PORT = 65437        
auth = False
import subprocess;
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
        
                    if(auth):
                           conn.sendall("For security concerns, all files downloaded will have to be checked by our admins first, that being said please give us the link of the file you want to download\n".encode())
                    data = conn.recv(1024)
                    if not data:
                       break;
                  
                    if(auth):
                     data = data.decode().replace("\n","")
                     data = data.replace("|","").replace(";","").replace("&&","").replace("`","").replace("IFS","");
                     conn.sendall(subprocess.check_output(['curl',data]));
                     break
                    else:    
                         data = data.decode('ascii').replace("\n","")
                         data = data.split()
                         print(data)
                         if(len(data) != 4):
                            conn.sendall("failure\n".encode())
                            continue
                         if(data[0] != "username" and data[1] != "AG" and data[2] != "password" and data[3] != "goodluckguessingme"):
                            conn.sendall("failure\n".encode())
                            continue
                         auth = True
                         conn.sendall("success\n".encode())
