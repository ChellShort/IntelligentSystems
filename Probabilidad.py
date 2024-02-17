#### EVENTO UNO _ COVID Confirmados ó COVID NO Confirmados ####

#Probabilidad COVID confirmado 
proba_A1 = 49.84
#Probabilidad COVID 'no' confirmado 
proba_A2 = 50.16

#### EVENTO DOS _ Hombres ó Mujeres ####
#Probabilidad que sea hombre
proba_B_dado_A1 = 53.88
#Probabilidad que sea mujer
proba_B_dado_A2 = 46.12



# Función para calcular la probabilidad (="prob") de Hombre o Mujer con COVID usando Teorema de Bayes
def calcular_prob_suceso(p_B_dado_A1, p_B_dado_A2, p_A1, p_A2):
    # Verificar si las probabilidades están en el rango válido (0% a 100%)
    if not (0 <= p_B_dado_A1 <= 100) or not (0 <= p_B_dado_A2 <= 100) \
            or not (0 <= p_A1 <= 100) or not (0 <= p_A2 <= 100):
        raise ValueError("Las probabilidades deben estar entre 0% y 100%")

    # Imprimir el valor de p_B_dado_A1
    #print(f"Valor de p_B_dado_A1: {p_B_dado_A1}")
    
    # Calcular el numerador de la fórmula
    numerador = p_B_dado_A1 * p_A1

    # Calcular el denominador de la fórmula
    denominador = p_B_dado_A1 * p_A1 + p_B_dado_A2 * p_A2

    # Caso base: si el denominador es 0, la probabilidad es 0
    if denominador == 0:
        return 0
    else:
        # Calcular la probabilidad usando la fórmula
        proba_eventoA1 = numerador / denominador
        return proba_eventoA1


#### EVENTO TRES _ Hospitalizados ó Ambulatorios ####

#Probabilidad que sea hospitalizado
proba_C_dado_BA1xC1 = 7.91
#Probabilidad que sea ambulatorio
proba_C_dado_BA2xC2 = 92.09

# Llamada a la función previa para obtener porcentajes de:
#Probabilidad hombre COVID confirmado = proba_eventoA1 
proba_eventoA1 = calcular_prob_suceso(proba_B_dado_A1, proba_B_dado_A2, proba_A1, proba_A2)
print(f"Probabilidad hombre con COVID confirmado: {proba_eventoA1*100:.2f}")
#Probabilidad mujer COVID confirmado = proba_eventoA2
proba_eventoA2 = 1-proba_eventoA1
print(f"Probabilidad mujer con COVID confirmado: {proba_eventoA2*100:.2f}")

# Llamada función COVID confirmado hombre - queremos saber Hospitalizado o Ambulatorio
proba_hospitalizadoA1 = calcular_prob_suceso(proba_C_dado_BA1xC1, proba_C_dado_BA2xC2, proba_eventoA1, proba_eventoA2)
print(f"Probabilidad hombre hospitalizado con COVID confirmado: {proba_hospitalizadoA1*100:.2f}")
proba_ambulatorioA2 = 1-proba_hospitalizadoA1
print(f"Probabilidad hombre ambulatorio con COVID confirmado: {proba_ambulatorioA2*100:.2f}")

# Llamada función COVID confirmado mujer - queremos saber Hospitalizado o Ambulatorio
proba_hospitalizadaA3 = calcular_prob_suceso(proba_C_dado_BA1xC1, proba_C_dado_BA2xC2, proba_eventoA2, proba_eventoA1)
print(f"Probabilidad mujer hospitalizado con COVID confirmado: {proba_hospitalizadaA3*100:.2f}")
proba_ambulatorioA4 = 1-proba_hospitalizadaA3
print(f"Probabilidad mujer ambulatorio con COVID confirmado: {proba_ambulatorioA4*100:.2f}")

#### EVENTO CUATRO _ Hipertensión u Obesidad o Diabetes o Tabaquismo u Otras ####
#Probabilidad que sea Hipertensión
proba_hipertension = proba_D_dado_C1BA1xD1 = proba_D_dado_C2BA2xD1 = 11.26
#Probabilidad que sea Obesidad
proba_obesidad = proba_D_dado_C1BA1xD2 = proba_D_dado_C2BA2xD2 = 10.28
#Probabilidad que sea Diabetes
proba_diabetes = proba_D_dado_C1BA1xD3 = proba_D_dado_C2BA2xD3 = 8.15
#Probabilidad que sea Tabaquismo
proba_tabaquismo = proba_D_dado_C1BA1xD4 = proba_D_dado_C2BA2xD4 = 5.81
proba_otras_enfermedades=(100-(11.26+10.28+8.15+5.81))
#Probabilidad que sea Otras enfermedades
proba_D_dado_C1BA1xD4 = proba_D_dado_C2BA2xD4 = proba_otras_enfermedades
# Imprimir el valor de otras enfermedades en procentaje
print(f"Valor de otras enfermedades: {proba_otras_enfermedades} %")

#Probabilidades EVENTO CUATRO Mujeres
print(f"Probabilidad mujer con hipertension [hospitalizada con COVID confirmado]: {proba_hospitalizadaA3*proba_hipertension:.2f}%")
print(f"Probabilidad mujer con obesidad [hospitalizada con COVID confirmado]: {proba_hospitalizadaA3*proba_obesidad:.2f}%")
print(f"Probabilidad mujer con diabetes [hospitalizada con COVID confirmado]: {proba_hospitalizadaA3*proba_diabetes:.2f}%")
print(f"Probabilidad mujer con tabaquismo [hospitalizada con COVID confirmado]: {proba_hospitalizadaA3*proba_tabaquismo:.2f}%")
print(f"Probabilidad mujer con otras enfermedades [hospitalizada con COVID confirmado]: {proba_hospitalizadaA3*proba_otras_enfermedades:.2f}%")
print(f"Probabilidad mujer con hipertension [en casa - ambulatorio con COVID confirmado]: {proba_ambulatorioA4*proba_hipertension:.2f}%")
print(f"Probabilidad mujer con obesidad [en casa - ambulatorio con COVID confirmado]: {proba_ambulatorioA4*proba_obesidad:.2f}%")
print(f"Probabilidad mujer con diabetes [en casa - ambulatorio con COVID confirmado]: {proba_ambulatorioA4*proba_diabetes:.2f}%")
print(f"Probabilidad mujer con tabaquismo [en casa - ambulatorio con COVID confirmado]: {proba_ambulatorioA4*proba_tabaquismo:.2f}%")
print(f"Probabilidad mujer con otras enfermedades [en casa - ambulatorio con COVID confirmado]: {proba_ambulatorioA4*proba_otras_enfermedades:.2f}%")

totalMujeres=(0.7758+0.7083+0.5615+0.4003+4.4439+10.4842+9.5717+7.5885+5.4097+60.0561)
# total de mujeres con Covid
print(f"Valor total de mujeres con COVID: {totalMujeres} %")

#Probabilidades EVENTO CUATRO Hombres
print(f"Probabilidad hombre con hipertension [hospitalizada con COVID confirmado]: {proba_hospitalizadoA1*proba_hipertension:.2f}%")
print(f"Probabilidad hombre con obesidad [hospitalizada con COVID confirmado]: {proba_hospitalizadoA1*proba_obesidad:.2f}%")
print(f"Probabilidad hombre con diabetes [hospitalizada con COVID confirmado]: {proba_hospitalizadoA1*proba_diabetes:.2f}%")
print(f"Probabilidad hombre con tabaquismo [hospitalizada con COVID confirmado]: {proba_hospitalizadoA1*proba_tabaquismo:.2f}%")
print(f"Probabilidad hombre con otras enfermedades [hospitalizada con COVID confirmado]: {proba_hospitalizadoA1*proba_otras_enfermedades:.2f}%")
print(f"Probabilidad hombre con hipertension [en casa - ambulatorio con COVID confirmado]: {proba_ambulatorioA2*proba_hipertension:.2f}%")
print(f"Probabilidad hombre con obesidad [en casa - ambulatorio con COVID confirmado]: {proba_ambulatorioA2*proba_obesidad:.2f}%")
print(f"Probabilidad hombre con diabetes [en casa - ambulatorio con COVID confirmado]: {proba_ambulatorioA2*proba_diabetes:.2f}%")
print(f"Probabilidad hombre con tabaquismo [en casa - ambulatorio con COVID confirmado]: {proba_ambulatorioA2*proba_tabaquismo:.2f}%")
print(f"Probabilidad hombre con otras enfermedades [en casa - ambulatorio con COVID confirmado]: {proba_ambulatorioA2*proba_otras_enfermedades:.2f}%")

totalHombres=(1.02+0.93+0.74+0.53+5.85+10.24+9.35+7.41+5.28+58.65)
# total de hombres con Covid
print(f"Valor total de hombres con COVID: {totalHombres} %")