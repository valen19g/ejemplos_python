mail=input('ingrese mail')
aux=False
def algo():
    print("hola")
if mail.find('@')>-1:
    aux=True
    if not mail.startswith('@') or not mail.endswith('.'):  
         aux=True
         if mail.find('@.')>-1: 
            aux=True
            partes=mail.split('.')
            if  len(partes[-1])>=2:
                aux=True
            else:
                aux=False
         else:
             aux=False
    else:
        aux=False
else:
    aux=False

                
if aux==True:
    print(f"{mail} es valido")
else:
    print(f"{mail} es invalido")
