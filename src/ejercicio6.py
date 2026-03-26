posts = [
"Arrancando el lunes con energía #Motivación #NuevaSemana",
"Terminé mi primer proyecto en Python #Python  #Programación #OrgullosoDeMi",
"No puedo creer el final de la serie #SinSpoilers #SerieAdicta",
"Nuevo video en el canal sobre #InteligenciaArtificial y #Python",
"Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain",
"Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología"
"Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta",
"Finde de lluvia, maratón de series #SerieAdicta #Relax",
"Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación"
]
total=[]
for texto in posts: 
    for palabra in texto.split(' '):
        if palabra.startswith('#'):
            total.append(palabra)

mi_set=set(total)
for hashtag in mi_set:
    final=total.count(hashtag)
    d[hashtag]=final
    
diccionario = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

print('Hashtags trending (más de una aparición)')
for elemen in diccionario:
    if diccionario[elemen] >1:
        print(f'{elemen}: {diccionario[elemen]}' )