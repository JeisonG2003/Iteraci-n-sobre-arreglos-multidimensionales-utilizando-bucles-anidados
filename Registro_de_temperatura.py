# Definir las ciudades y los días de la semana
ciudades = ["Guayaquil", "Daule", "Milagro"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Crear una matriz 3D para almacenar temperaturas diarias en varias ciudades durante 4 semanas
temperaturas = [
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 34}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 31}
        ]
    ],
    [   # Daule
        [   # Semana 1
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 30}
        ]
    ],
    [   # Milagro
        [   # Semana 1
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 34}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 31}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f}°C")

# Pedir al usuario un día de la semana
dia_usuario = input("\nIngresa un día de la semana (Lunes, Martes, etc.): ").capitalize()

# Verificar si el día ingresado es válido
if dia_usuario in dias_semana:
    print(f"\nTemperaturas registradas el {dia_usuario} en cada ciudad:")
    for ciudad_idx, ciudad in enumerate(ciudades):
        temperaturas_dia = [semana[dias_semana.index(dia_usuario)]["temp"] for semana in temperaturas[ciudad_idx]]
        print(f"{ciudad}: {temperaturas_dia}")
else:
    print("Error: Día ingresado no válido. Asegúrate de escribirlo correctamente.")
