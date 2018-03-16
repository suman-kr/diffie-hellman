import socket  

print("")
print ("***********************")
print ("*    Diffie Hellman   *")
print ("*     Key Exchange    *")
print ("***********************")
 
Prime=input("Input prime number: ")     # p
Base =input("Input base number : ")      # g
 
aliceSecret = input("Enter Alice Secret here:")      # a
bobSecret =   input("Enter Bob Secret here:")
 
print "-----------------------------------------"  

print "Publicly Shared Variables:"
print "    Publicly Shared Prime: " , Prime 
print "    Publicly Shared Base:  " , Base 

print "-----------------------------------------" 
 
A = Base**aliceSecret % Prime
print "\n  Alice Sends Over Public Chanel: " , A 
 
 
B = (Base ** bobSecret) % Prime
print  "\n  Bob Sends Over Public Chanel: " ,B 
 
print "------------------------------------------" 
print "Privately Calculated Shared Secret:" 
 
aliceSharedSecret = B ** aliceSecret % Prime
print "    Alice Shared Secret: ", aliceSharedSecret 
 
 
bobSharedSecret = (A**bobSecret) % Prime
print "    Bob Shared Secret: ", bobSharedSecret 

print "------------------------------------------"  
 
if bobSharedSecret == aliceSharedSecret :
    print "Connection established"
 
print "******************************************"

s = socket.socket()        
host = socket.gethostname()
port = 51125              
s.bind((host, port))      
 
 
 
s.listen(5)                
while True:
   c, addr = s.accept()    
   print 'Got connection from', addr
   c.send(str(aliceSharedSecret)+str(bobSharedSecret))
   
   c.close()                
print  "    Alice Shared Secret: ", aliceSharedSecret 