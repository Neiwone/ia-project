from mcda.scales import QuantitativeScale
from mcda.matrices import PerformanceTable

# Definindo as escalas para cada critério
scales = {
    0: QuantitativeScale(0, 10),  # Experiência (0 a 10)
    1: QuantitativeScale(0, 10),  # Soft-Skills (0 a 10)
    2: QuantitativeScale(0, 10),  # Hard-Skills (0 a 10)
    3: QuantitativeScale(0, 10),  # Trabalho em Equipe (0 a 10)
    4: QuantitativeScale(0, 10),  # Resolução de Problemas (0 a 10)
}


# Pesos para cada critério
W = {
    0: 20,  # Experiência
    1: 25,  # Soft-Skills
    2: 20,  # Hard-Skills
    3: 20,  # Trabalho em Equipe
    4: 15,  # Resolução de Problemas
}

# Parâmetros de preferência, indiferença e veto
P = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
I = {0: 0.5, 1: 0.5, 2: 0.5, 3: 0.5, 4: 0.5}
V = {0: 2, 1: 2, 2: 2, 3: 2, 4: 2}

profiles = PerformanceTable(
    [
        [6, 7, 6, 7, 6],  # Limite inferior para "Aprovado parcialmente"
        [8, 9, 8, 9, 8],  # Limite inferior para "Aprovado"
    ],
    alternatives=["p1", "p2"],
    scales=scales
)

categories = ['Reprovado', 'Aprovado parcialmente', 'Aprovado']