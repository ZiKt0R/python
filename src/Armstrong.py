n = int(input("Enter the number : "))                      
p = len(str(n))                                           
sum = 0                                                     
k = n                                                     
while k>0:                                                
    d = k%10                                              
    s = s + (d**p)                                        
    k = k//10                                             
if n == s:                                                
    print('{} is an Armstrong number'.format(n))          
else:                                                       
    print('{} is not an Armstrong number'.format(n))