playlist = [
{"title": "Bohemian Rhapsody", "duration": "5:55"},
{"title": "Hotel California", "duration": "6:30"},
{"title": "Stairway to Heaven", "duration": "8:02"},
{"title": "Imagine", "duration": "3:07"},
{"title": "Smells Like Teen Spirit", "duration": "5:01"},
{"title": "Billie Jean", "duration": "4:54"},
{"title": "Hey Jude", "duration": "7:11"},
{"title": "Like a Rolling Stone", "duration": "6:13"},
]
duraciontotalminutos=0
duraciontotalsegundos=0
for cancion in playlist:
    partes=cancion["duration"].split(':')
    duraciontotalminutos+=int(partes[0])
    duraciontotalsegundos+=int(partes[1])
    while duraciontotalsegundos > 60:
        duraciontotalminutos+=1
        duraciontotalsegundos-=60
print(f"duracion total {duraciontotalminutos}m {duraciontotalsegundos}s  ")    
max=-2
cmax=''
min=100000
cmin=''
total=0
for cancion in playlist:
    partes=cancion["duration"].split(':')
    total=int(partes[0])*60+int(partes[1])
    if total > max:
        max=total
        cmax=cancion
    if total < min:
        min=total
        cmin=cancion    
        
print(cmax['title']," ",cmax['duration'])
print('------------')
print(cmin['title']," ",cmin['duration'])
print('----------')