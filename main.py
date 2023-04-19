import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

#Variaveis de Entrada (Antecedent)
comer = ctrl.Antecedent(np.arange(0, 9, 1), 'comer')
tempo_atividade = ctrl.Antecedent(np.arange(0, 9, 1), 'tempo_atividade')

#Variaveis de saída (Consequent)
peso = ctrl.Consequent(np.arange(0, 11, 1), 'peso')

# Triangular
# comer['pouco'] = fuzz.trimf(comer.universe, [-1, 2, 4])
# comer['razoável'] = fuzz.trimf(comer.universe, [2, 5, 7])
# comer['bastante'] = fuzz.trimf(comer.universe, [4, 7, 9])
#
# tempo_atividade['baixa'] = fuzz.trimf(tempo_atividade.universe, [-1, 0, 4])
# tempo_atividade['media'] = fuzz.trimf(tempo_atividade.universe, [0, 4, 9])
# tempo_atividade['alta'] = fuzz.trimf(tempo_atividade.universe, [4, 10, 10])
#
# peso['peso leve'] = fuzz.trimf(peso.universe, [-1, 3, 5])
# peso['peso médio'] = fuzz.trimf(peso.universe, [4, 6, 9])
# peso['pesado'] = fuzz.trimf(peso.universe, [6, 8, 10])

# Gauss
# comer['pouco'] = fuzz.gaussmf(comer.universe, 1, 2)
# comer['razoável'] = fuzz.gaussmf(comer.universe, 5, 2)
# comer['bastante'] = fuzz.gaussmf(comer.universe, 7, 2)
#
# tempo_atividade['baixa'] = fuzz.gaussmf(tempo_atividade.universe, 0, 2)
# tempo_atividade['media'] = fuzz.gaussmf(tempo_atividade.universe, 4, 2)
# tempo_atividade['alta'] = fuzz.gaussmf(tempo_atividade.universe, 9, 2)
#
# peso['peso leve'] = fuzz.gaussmf(peso.universe, 2, 2)
# peso['peso médio'] = fuzz.gaussmf(peso.universe, 6, 2)
# peso['pesado'] = fuzz.gaussmf(peso.universe, 10, 2)

# Trapezoidal
comer['pouco'] = fuzz.trapmf(comer.universe, [-1, -1, 2, 4])
comer['razoável'] = fuzz.trapmf(comer.universe, [2, 4, 6, 7])
comer['bastante'] = fuzz.trapmf(comer.universe, [4, 6, 9, 9])

tempo_atividade['baixa'] = fuzz.trapmf(tempo_atividade.universe, [-1, -1, 3, 4])
tempo_atividade['media'] = fuzz.trapmf(tempo_atividade.universe, [3, 4, 5, 6])
tempo_atividade['alta'] = fuzz.trapmf(tempo_atividade.universe, [5, 6, 10, 10])

peso['peso leve'] = fuzz.trapmf(peso.universe, [-1, -1, 4, 6])
peso['peso médio'] = fuzz.trapmf(peso.universe, [4, 5, 7, 9])
peso['pesado'] = fuzz.trapmf(peso.universe, [7, 9, 10, 10])

#Visualizando as variáveis
comer.view()
tempo_atividade.view()
peso.view()

#Criando as regras
regra_1 = ctrl.Rule(comer['bastante'] & tempo_atividade['media'], peso['pesado'])
regra_2 = ctrl.Rule(comer['razoável'] | tempo_atividade['alta'], peso['peso médio'])
regra_3 = ctrl.Rule(comer['pouco'] & tempo_atividade['alta'], peso['peso leve'])

controlador = ctrl.ControlSystem([
        regra_1,
        regra_2,
        regra_3
])

#Simulando
CalculoObesidade = ctrl.ControlSystemSimulation(controlador)

notaComer = int(input('Comer: '))
notaTempo = int(input('Tempo atividade: '))
CalculoObesidade.input['comer'] = notaComer
CalculoObesidade.input['tempo_atividade'] = notaTempo
CalculoObesidade.compute()

valorPeso = CalculoObesidade.output['peso']

print("\nComer %d\nTempo atividade %d\nPeso de %5.2f" %(
        notaComer,
        notaTempo,
        valorPeso))

comer.view(sim=CalculoObesidade)
tempo_atividade.view(sim=CalculoObesidade)
peso.view(sim=CalculoObesidade)

plt.show()