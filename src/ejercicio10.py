rounds = [
{
'theme': 'Entrada',
'scores': {
'Valentina': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
'Mateo': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
'Camila': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
'Santiago': {'judge_1': 6, 'judge_2': 7,
'judge_3': 6},
'Lucía': {'judge_1': 8, 'judge_2': 8,
'judge_3': 8},
}
},
{
'theme': 'Plato principal',
'scores': {
'Valentina': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
'Mateo': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
'Camila': {'judge_1': 7, 'judge_2': 6,
'judge_3': 7},
'Santiago': {'judge_1': 9, 'judge_2': 8,
'judge_3': 8},
'Lucía': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
}
},
{
'theme': 'Postre',
'scores': {
'Valentina': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
'Mateo': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
'Camila': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
'Santiago': {'judge_1': 7, 'judge_2': 7,
'judge_3': 6},
'Lucía': {'judge_1': 9, 'judge_2': 9,
'judge_3': 9},
}
},
{
'theme': 'Cocina internacional',
'scores': {
'Valentina': {'judge_1': 8, 'judge_2': 9,
'judge_3': 9},
'Mateo': {'judge_1': 7, 'judge_2': 6,
'judge_3': 7},
'Camila': {'judge_1': 9, 'judge_2': 8,
'judge_3': 8},
'Santiago': {'judge_1': 8, 'judge_2': 9,
'judge_3': 7},
'Lucía': {'judge_1': 7, 'judge_2': 7,
'judge_3': 8},
}
},
{
'theme': 'Final libre',
'scores': {
'Valentina': {'judge_1': 9, 'judge_2': 8,
'judge_3': 9},
'Mateo': {'judge_1': 8, 'judge_2': 9,
'judge_3': 8},
'Camila': {'judge_1': 7, 'judge_2': 7,
'judge_3': 7},
'Santiago': {'judge_1': 9, 'judge_2': 9,
'judge_3': 9},
'Lucía': {'judge_1': 8, 'judge_2': 8,
'judge_3': 7},
}
}
]


puntajemaximo=-1
ganador=""
numero_ronda=1
estadisticas={}

for ronda in rounds:
    print(f"Ronda {numero_ronda} - {ronda['theme']}:")
    for participante in ronda["scores"]: 
        datos=ronda["scores"][participante] 
        if participante not in estadisticas:  
           estadisticas[participante]={
           "total": 0,
           "ganadas": 0,
           "mejor": 0
           }
        puntuacion_total=datos["judge_1"]+datos["judge_2"]+datos["judge_3"] 
        if puntuacion_total>puntajemaximo: 
            puntajemaximo=puntuacion_total 
            ganador=participante 
        estadisticas[participante]["total"]+=puntuacion_total
        if puntuacion_total > estadisticas[participante]["mejor"]:
            estadisticas[participante]["mejor"]=puntuacion_total
    estadisticas[ganador]["ganadas"]+=1
    print(f'ganador: {ganador} ({puntajemaximo} pts) ')    
    numero_ronda+=1
    puntajemaximo=-1
    ganador=""
lista = list(estadisticas.items())
lista.sort(key=lambda x: x[1]["total"], reverse=True)
for nombre,datos in lista:
    promedio=datos['total']/len(rounds)
    print(f'{nombre} - {datos} promedio {promedio}')
    