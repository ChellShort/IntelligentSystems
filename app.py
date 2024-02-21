from flask import Flask, render_template, request, redirect
##### import controlador #####

# Instancia de Flask
app = Flask(__name__)

#La ruta raiz es la pagina de inicio (aqui se muestra el formulario)
@app.route('/')
def index(): 
    return render_template('Inicio.html')

#La ruta raiz es la pagina de inicio (aqui se muestra el formulario)
@app.route('/registro', methods=['POST'])
def registro(): 
    casosTotales = float(request.form['txtTotales'])
    Confirmados = float(request.form['txtConfirmados'])
    #NoConfirmados = float(request.form['txtNoConfirmados'])
    InfectadosHombre = float(request.form['txtInfectadosM'])
    InfectadasMujer = float(request.form['txtInfectadasF'])
    Hospitalizados = float(request.form['txtHospitalizados'])
    Ambulatorios = float(request.form['txtAmbulatorios'])
    Hipertension = float(request.form['txtHipertension'])
    Obesidad = float(request.form['txtObesidad'])
    Diabetes = float(request.form['txtDiabetes'])
    Tabaquismo = float(request.form['txtTabaquismo'])
    #OtrasEnf = float(request.form['txtOtrasEnfermedades'])
    
    #### EVENTO UNO _ COVID Confirmados ó COVID NO Confirmados ####
    ConfirmadosPorcentaje = 100/casosTotales*Confirmados
    #Probabilidad COVID confirmado 
    proba_A1 = ConfirmadosPorcentaje
    print(f"Probabilidad hombre con COVID confirmado: {proba_A1:.2f}")
    #Probabilidad COVID 'NO' confirmado 
    proba_A2 = 100-ConfirmadosPorcentaje

    #### EVENTO DOS _ Hombres ó Mujeres ####
    #Probabilidad que sea hombre
    proba_B_dado_A1 = InfectadosHombre
    #Probabilidad que sea mujer
    proba_B_dado_A2 = InfectadasMujer
    
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
        denominador = (p_B_dado_A1 * p_A1) + (p_B_dado_A2 * p_A2)

        # Caso base: si el denominador es 0, la probabilidad es 0
        if denominador == 0:
            return 0
        else:
            # Calcular la probabilidad usando la fórmula
            proba_eventoA1 = numerador / denominador
            return proba_eventoA1
    #### EVENTO TRES _ Hospitalizados ó Ambulatorios ####

    #Probabilidad que sea hospitalizado
    proba_C_dado_BA1xC1 = Hospitalizados
    #Probabilidad que sea ambulatorio
    proba_C_dado_BA2xC2 = Ambulatorios
    
    # Llamada a la función previa para obtener porcentajes de:
    #Probabilidad hombre COVID confirmado = proba_eventoA1 
    proba_eventoA1 = round(calcular_prob_suceso(proba_B_dado_A1, proba_B_dado_A2, proba_A1, proba_A2),4)
    print(f"Probabilidad hombre con COVID confirmado: {proba_eventoA1*100:.2f}")
    
    #Probabilidad mujer COVID confirmado = proba_eventoA2
    proba_eventoA2 = round(1-proba_eventoA1,4)
    print(f"Probabilidad mujer con COVID confirmado: {proba_eventoA2*100:.2f}")

    # Llamada función COVID confirmado hombre - queremos saber Hospitalizado o Ambulatorio
    proba_hospitalizadoA1 = round(calcular_prob_suceso(proba_C_dado_BA1xC1, proba_C_dado_BA2xC2, proba_eventoA1, proba_eventoA2),4)
    print(f"Probabilidad hombre hospitalizado con COVID confirmado: {proba_hospitalizadoA1*100:.2f}")
    proba_ambulatorioA2 = round( 1-proba_hospitalizadoA1,4)
    print(f"Probabilidad hombre ambulatorio con COVID confirmado: {proba_ambulatorioA2*100:.2f}")

    # Llamada función COVID confirmado mujer - queremos saber Hospitalizado o Ambulatorio
    proba_hospitalizadaA3 = round(calcular_prob_suceso(proba_C_dado_BA1xC1, proba_C_dado_BA2xC2, proba_eventoA2, proba_eventoA1),4)
    print(f"Probabilidad mujer hospitalizado con COVID confirmado: {proba_hospitalizadaA3*100:.2f}")
    proba_ambulatorioA4 = round(1-proba_hospitalizadaA3,4)
    print(f"Probabilidad mujer ambulatorio con COVID confirmado: {proba_ambulatorioA4*100:.2f}")

    #### EVENTO CUATRO _ Hipertensión u Obesidad o Diabetes o Tabaquismo u Otras ####
    #Probabilidad que sea Hipertensión
    proba_hipertension = proba_D_dado_C1BA1xD1 = proba_D_dado_C2BA2xD1 = Hipertension
    #Probabilidad que sea Obesidad
    proba_obesidad = proba_D_dado_C1BA1xD2 = proba_D_dado_C2BA2xD2 = Obesidad
    #Probabilidad que sea Diabetes
    proba_diabetes = proba_D_dado_C1BA1xD3 = proba_D_dado_C2BA2xD3 = Diabetes
    #Probabilidad que sea Tabaquismo
    proba_tabaquismo = proba_D_dado_C1BA1xD4 = proba_D_dado_C2BA2xD4 = Tabaquismo
    proba_otras_enfermedades=(100-(Hipertension+Obesidad+Diabetes+Tabaquismo))
    #Probabilidad que sea Otras enfermedades
    proba_D_dado_C1BA1xD4 = proba_D_dado_C2BA2xD4 = proba_otras_enfermedades
    # Imprimir el valor de otras enfermedades en procentaje
    print(f"Valor de otras enfermedades: {proba_otras_enfermedades} %")
    
    #Probabilidades EVENTO CUATRO Hombres
    hombreHospitalHipertension=round(proba_hospitalizadoA1*proba_hipertension,4)
    hombreHospitalObesidad=round(proba_hospitalizadoA1*proba_obesidad,4)
    hombreHospitalDiabetes=round(proba_hospitalizadoA1*proba_diabetes,4)
    hombreHospitalTabaquismo=round(proba_hospitalizadoA1*proba_tabaquismo,4)
    hombreHospitalOtrasEnf=round(proba_hospitalizadoA1*proba_otras_enfermedades,4)
    hombreAmbulatorioHipertension=round(proba_ambulatorioA2*proba_hipertension,4)
    hombreAmbulatorioObesidad=round(proba_ambulatorioA2*proba_obesidad,4)
    hombreAmbulatorioDiabetes=round(proba_ambulatorioA2*proba_diabetes,4)
    hombreAmbulatorioTabaquismo=round(proba_ambulatorioA2*proba_tabaquismo,4)
    hombreAmbulatorioOtrasEnf=round(proba_ambulatorioA2*proba_otras_enfermedades,4)
    
    #Probabilidades EVENTO CUATRO Mujeres
    mujerHospitalHipertension=round(proba_hospitalizadaA3*proba_hipertension,4)
    mujerHospitalObesidad=round(proba_hospitalizadaA3*proba_obesidad,4)
    mujerHospitalDiabetes=round(proba_hospitalizadaA3*proba_diabetes,4)
    mujerHospitalTabaquismo=round(proba_hospitalizadaA3*proba_tabaquismo,4)
    mujerHospitalOtrasEnf=round(proba_hospitalizadaA3*proba_otras_enfermedades,4)
    mujerAmbulatorioHipertension=round(proba_ambulatorioA4*proba_hipertension,4)
    mujerAmbulatorioObesidad=round(proba_ambulatorioA4*proba_obesidad,4)
    mujerAmbulatorioDiabetes=round(proba_ambulatorioA4*proba_diabetes,4)
    mujerAmbulatorioTabaquismo=round(proba_ambulatorioA4*proba_tabaquismo,4)
    mujerAmbulatorioOtrasEnf=round(proba_ambulatorioA4*proba_otras_enfermedades,4)
    

    return render_template('Preguntas.html', proba_eventoA1=proba_eventoA1 * 100,proba_eventoA2 = proba_eventoA2 * 100,proba_hospitalizadoA1 =proba_hospitalizadoA1*100,proba_ambulatorioA2 = proba_ambulatorioA2*100,proba_hospitalizadaA3 = proba_hospitalizadaA3 * 100,proba_ambulatorioA4 = proba_ambulatorioA4*100, hombreHospitalHipertension=hombreHospitalHipertension, hombreHospitalObesidad=hombreHospitalObesidad, hombreHospitalDiabetes=hombreHospitalDiabetes, hombreHospitalTabaquismo=hombreHospitalTabaquismo, hombreHospitalOtrasEnf=hombreHospitalOtrasEnf, hombreAmbulatorioHipertension=hombreAmbulatorioHipertension, hombreAmbulatorioObesidad= hombreAmbulatorioObesidad, hombreAmbulatorioDiabetes=hombreAmbulatorioDiabetes, hombreAmbulatorioTabaquismo=hombreAmbulatorioTabaquismo, hombreAmbulatorioOtrasEnf=hombreAmbulatorioOtrasEnf, mujerHospitalHipertension=mujerHospitalHipertension,mujerHospitalObesidad=mujerHospitalObesidad, mujerHospitalDiabetes=mujerHospitalDiabetes, mujerHospitalTabaquismo=mujerHospitalTabaquismo, mujerHospitalOtrasEnf=mujerHospitalOtrasEnf, mujerAmbulatorioHipertension=mujerAmbulatorioHipertension, mujerAmbulatorioObesidad=mujerAmbulatorioObesidad, mujerAmbulatorioDiabetes=mujerAmbulatorioDiabetes, mujerAmbulatorioTabaquismo=mujerAmbulatorioTabaquismo, mujerAmbulatorioOtrasEnf= mujerAmbulatorioOtrasEnf)

@app.route('/probabilidad', methods=['POST'])
def probabilidad(): 
    return render_template('Preguntas.html')

# Ejecutar el servidor
if __name__ == '__main__':
 app.run(port=5800,debug=True)

