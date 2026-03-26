review = """La película sigue a un grupo de astronautas que 
viajan a Marte
en una misión de rescate. El capitán Torres lidera al equipo 
a través
de tormentas solares y fallos en el sistema de navegación. Al 
llegar
a Marte descubren que la base está abandonada y los 
suministros
destruidos. Torres decide sacrificar la nave nodriza para 
salvar
al equipo y logran volver a la Tierra en una cápsula de 
emergencia.
El final revela que Torres sobrevivió gracias a un pasaje 
secreto."""
 
spoilers= input('ingrese palabra considerada spoliers separadas por coma')
lista_spoilers= spoilers.split(',')   
    
palabras=review.split()
resultado=[]
for palabra in palabras:
    if palabra in lista_spoilers:
        resultado.append("*" * len(palabra))
    else:
        resultado.append(palabra)
texto=" ".join(resultado)
print(texto)
          
                         
        

