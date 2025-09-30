import random
from datetime import datetime, timedelta

# Archivo de salida
output_file = "consulta_dirty_data.csv"

fecha_base = datetime(2025, 1, 1, 8, 0, 0)  # 1 de enero 2025, 8 AM

numero_consultas_duplicadas = 249

filas_incompletas = random.sample(range(1, 1001), numero_consultas_duplicadas)
filas_duplicadas = random.sample(range(1, 1001), numero_consultas_duplicadas)

with open(output_file, "w", encoding="utf-8") as f:
    f.write("pacienteID,medicoID,cuartoID,citaProgramada,horaLlegadaConsulta,horaInicioConsulta,horaFinConsulta\n")

    values = []
    for paciente_id in range(1, 1001):
        medico_id = random.randint(1, 150)
        cuarto_id = random.randint(1, 75)
        cita_programada = random.randint(0, 1)

        llegada = fecha_base + timedelta(days=random.randint(0, 30),
                                         hours=random.randint(7, 17),
                                         minutes=random.randint(0, 59))
        
        inicio = llegada + timedelta(minutes=random.randint(30, 240))
        fin = inicio + timedelta(minutes=random.randint(15, 60))

        llegada_str = llegada.strftime("'%m-%d-%Y %H:%M:%S'")
        inicio_str = inicio.strftime("'%m-%d-%Y %H:%M:%S'")
        fin_str = fin.strftime("'%m-%d-%Y %H:%M:%S'")

        columnas = [
            paciente_id,
            medico_id,
            cuarto_id,
            cita_programada,
            llegada_str,
            inicio_str,
            fin_str
        ]

        def formatear_fila(cols):
            return ", ".join(str(c) if c is not None else "" for c in cols)

        # Si está en filas duplicadas, agregamos una copia
        if paciente_id in filas_duplicadas:
            values.append(formatear_fila(columnas))

        # Si está en filas incompletas, generamos una fila con 3 campos faltantes
        if paciente_id in filas_incompletas:
            columnas_con_nulos = columnas.copy()
            indices_a_borrar = random.sample(range(len(columnas)), 3)
            for idx in indices_a_borrar:
                columnas_con_nulos[idx] = None
            values.append(formatear_fila(columnas_con_nulos))
        else:
            # Fila "limpia"
            values.append(formatear_fila(columnas))

    f.write("\n".join(values))

print(f"Archivo {output_file} generado con éxito.")
