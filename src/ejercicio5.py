peso=float(input('ingrese el peso del paquete (kg)'))
destino=input('ingrese la zona del envio (local/regional/nacional')
              
match destino:
    case 'local':
        if peso <= 1:
            resultado=500
        elif peso > 1 and peso <= 5:
            resultado=1000
        else : resultado=2000
    case 'regional':
        if peso <= 1:
            resultado=1000
        elif peso > 1 and peso <= 5:
            resultado=2500
        else : resultado=5000
    case 'nacional':
        if peso <= 1:
            resultado=2000
        elif peso > 1 and peso <= 5:
            resultado=4500
        else : resultado=8000
    case _ :
        print('error las zonas disponible son local,regional,nacional')

print(f'Costo de envio: {resultado}')
            
    
              
              

                
              
              
              
