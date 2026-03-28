mensaje=input('ingrese mensaje')
desplazamiento=int(input('ingrese el desplazamiento'))
caracteres=list(mensaje)
for i in range(len(caracteres)):
     x=caracteres[i]
     if x.isalpha():
         caracteres[i]=chr(ord(x)+desplazamiento)
resultado="".join(caracteres)  
print(resultado)