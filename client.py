import socket            
 
s = socket.socket()      
host = socket.gethostname()
port = 51125
               
 
s.connect((host, port))
data = s.recv(1024)
 
keys = repr(data)
 
print 'alice secret key is: ' ,keys[3:]
 
print 'bob secret Key is : ' , keys[:3]
 
 
 
s.close()