students = [
{"name": " Ana García ", "grade": "8", "status":
"aprobado"},
{"name": "pedro lópez", "grade": "4", "status":
"DESAPROBADO"},
{"name": "MARÍA FERNÁNDEZ", "grade": "10", "status":
"Aprobado"},
{"name": "ana garcía", "grade": "9", "status":
"aprobado"},
{"name": None, "grade": "7", "status": "aprobado"},
{"name": "Luis Martínez ", "grade": None, "status":
"aprobado"},
{"name": " carlos RUIZ", "grade": "6", "status":
"aprobado"},
{"name": "PEDRO LÓPEZ ", "grade": "3", "status":
"desaprobado"},
{"name": " ", "grade": "5", "status": "aprobado"},
{"name": "María Fernández", "grade": "7", "status":
"APROBADO"},
{"name": "Sofía Torres", "grade": "9", "status":
"Aprobado"},
{"name": " sofía torres ", "grade": "8", "status":
"aprobado"},
{"name": "Carlos Ruiz", "grade": "6", "status":
"APROBADO"},
{"name": "Roberto Díaz", "grade": "absent", "status":
"ausente"},
{"name": "roberto díaz", "grade": "", "status":
"Ausente"},
{"name": None, "grade": None, "status": None},
{"name": "Laura Méndez", "grade": "7", "status":
"aprobado"},
{"name": " laura méndez", "grade": "8", "status":
"Aprobado"},
{"name": "GABRIELA RÍOS", "grade": "5", "status":
"aprobado"},
{"name": "gabriela ríos ", "grade": "4", "status":
"Desaprobado"},
]
nuevos_students = []
repetidos=[]
for alumno in students:
    name = alumno["name"]
    grade = alumno["grade"]
    status = alumno["status"]
    if name is None or grade is None or status is None or grade == 'absent':
        continue
    if name.strip() == "" or grade.strip() == "":
        continue
    alumno["name"] = name.strip().title()
    alumno["status"] = status.strip().title()
   
    nuevos_students.append(alumno)
    
nuevos_students.sort(key=lambda x: x["name"])
resultado = []
nom = None

for alu in nuevos_students:
    if nom is None:
        nom = alu
    elif nom["name"] == alu["name"]:
        if int(alu["grade"]) > int(nom["grade"]):
            nom = alu
    else:
        resultado.append(nom)
        nom = alu

if nom is not None:
    resultado.append(nom)
      

print("Registros limpios de alumnos:")
for res in resultado:
    print(f'{res["name"]} {res["grade"]} {res["status"]}  ' )
    
total=len(resultado)    
print(f'Total de alumnos válidos: {total}')    