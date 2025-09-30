import random

# Archivo de salida
output_file = "queja_dirty_data.txt"

# Lista de descripciones genéricas
quejas_genericas = [
    "El tiempo de espera fue demasiado largo.",
    "La atención del personal no fue satisfactoria.",
    "El médico no explicó claramente el diagnóstico.",
    "El cuarto asignado estaba en malas condiciones.",
    "Problemas con la facturación del servicio.",
    "Falta de disponibilidad de medicamentos.",
    "La atención se sintió apresurada.",
    "El personal administrativo fue poco cordial.",
    "La cita fue cancelada sin previo aviso.",
    "Se extraviaron documentos clínicos importantes."
]

# Número total de quejas
num_quejas = 647

# Porcentaje de filas sucias
porcentaje_duplicadas = 0.20
porcentaje_incompletas = 0.15
porcentaje_malformateadas = 0.10

# Número de filas sucias por tipo
num_duplicadas = int(num_quejas * porcentaje_duplicadas)
num_incompletas = int(num_quejas * porcentaje_incompletas)
num_malformateadas = int(num_quejas * porcentaje_malformateadas)

# IDs únicos para las quejas (consultaID)
consulta_ids = random.sample(range(1, 1001), num_quejas)

# Seleccionar índices para filas sucias
indices_duplicadas = set(random.sample(range(num_quejas), num_duplicadas))
indices_incompletas = set(random.sample(range(num_quejas), num_incompletas))
indices_malformateadas = set(random.sample(range(num_quejas), num_malformateadas))

# Escribir archivo
with open(output_file, "w", encoding="utf-8") as f:
    f.write("consultaID, categoriaID, descripcion\n")

    values = []

    for i, consulta_id in enumerate(consulta_ids):
        categoria_id = random.randint(1, 4)
        descripcion = random.choice(quejas_genericas)

        # -- Crear fila limpia --
        fila = [str(consulta_id), str(categoria_id), descripcion]

        # -- Fila malformateada --
        if i in indices_malformateadas:
            error_type = random.choice(['string_in_num', 'bad_escape', 'extra_delim'])
            if error_type == 'string_in_num':
                # Poner texto en consultaID o categoriaID
                if random.choice([True, False]):
                    fila[0] = "ABC123"  # consultaID inválido
                else:
                    fila[1] = "???"     # categoriaID inválido
            elif error_type == 'bad_escape':
                fila[2] = "El médico dijo: 'todo bien' sin explicación"  # sin escapar comillas simples
            elif error_type == 'extra_delim':
                fila[2] = descripcion + ",,,"  # delimitadores de más

        # -- Fila incompleta --
        if i in indices_incompletas:
            columnas_a_eliminar = random.sample([0, 1, 2], random.randint(1, 2))
            for idx in columnas_a_eliminar:
                fila[idx] = ""  # Dejar campo vacío

        values.append(", ".join(fila))

        # -- Fila duplicada (después de la original) --
        if i in indices_duplicadas:
            values.append(", ".join(fila))  # Duplicado exacto

    f.write("\n".join(values))

print(f"Archivo {output_file} generado con éxito.")
