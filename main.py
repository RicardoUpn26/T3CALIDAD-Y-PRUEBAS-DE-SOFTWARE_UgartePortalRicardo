def calcular_promedio(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

def validar_aprobacion(promedio):
    if promedio >= 11:
        return "Aprobado"
    else:
        return "Desaprobado"

if __name__ == "__main__":
    print("**** Sistema Innovatec Education ****")
    notas_estudiante = [15, 18, 12, 14]
    promedio = calcular_promedio(notas_estudiante)
    estado = validar_aprobacion(promedio)
    
    print(f"Notas: {notas_estudiante}")
    print(f"Promedio Final: {promedio}")
    print(f"Estado del estudiante: {estado}")