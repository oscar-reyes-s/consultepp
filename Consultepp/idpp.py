import matplotlib.pyplot as plt  # Import the matplotlib library

def get_score(answers):
    score = 0
    for answer in answers:
        if answer == 1:
            score += 1
        elif answer == 2:
            score += 2
        elif answer == 3:
            score += 3
        elif answer == 4:
            score += 4
    return score

def calculate_t_score(section_score, section_average, section_std_dev):
    t_score = 50 + (section_score - section_average) / section_std_dev
    return t_score

def main():
    questions = [
       "He sido descuidado(a) con cosas que me prestan.",
"Cumplo con todas las reglas y leyes.",
"Cuando estoy con otras personas hablo en voz alta para que se fijen en mí.",
"Me siento con más energía, sin tener razones.",
"Sé lo que las personas piensan sin que me lo digan.",
"Me impacienta cuando tengo que esperar mucho tiempo en una fila.",
"Soy capaz de controlarme en todo tipo de situaciones.",
"Es difícil para mí organizar las responsabilidades que tengo.",
"Mantengo distancia de todas las personas.",
"Me he sentido muy dolido(a) aún por cosas pequeñas que me han hecho.",
"Las personas pierden la paciencia conmigo porque soy muy insistente.",
"He sentido que soy otra persona.",
"Me cuesta concentrarme.",
"Tomo riesgos para que mi vida sea más emocionante.",
"Me han dicho que tengo costumbres poco comunes.",
"He dejado tiradas cosas que estoy haciendo, porque se me ocurrió hacer algo más interesante.",
"Tengo sueños que me avisan sobre cosas que van a pasar.",
"Disfruto mi facilidad para convencer a la gente.",
"Me siento feliz.",
"Miento para obtener lo que quiero.",
"Es mejor no involucrarse en los problemas de otras personas.",
"Me lleno de responsabilidades por ayudar a otros, y eso me cansa.",
"Tengo más energía que las demás personas.",
"Es difícil para mí hacer nuevas amistades.",
"Siento que otras personas pueden leer mis pensamientos.",
"Me es imposible controlar el enojo cuando me siento estresado(a).",
"Me importa poco cuando otros se sienten mal por lo que hago.",
"Se me dificulta concentrarme en las cosas que hago.",
"Aunque me lastimen mucho, reacciono con tranquilidad.",
"Hago mis tareas con tranquilidad, aunque me estén supervisando.",
"Creo que soy un fracasado(a).",
"Resuelvo hasta los problemas más difíciles con poco esfuerzo.",
"Cuando me siento mal hago cosas de las que luego me arrepiento.",
"Las personas hacen lo que quiero con solo pensarlo.",
"Me preocupo tanto que todo se me hace insoportable.",
"Hago lo posible por complacer a las personas.",
"Me cuesta entender mis propios pensamientos.",
"He engañado a algunas personas.",
"Me afectan las críticas o lo que otras personas piensan de mí.",
"Tengo muy claros mis planes y metas a futuro.",
"Me han hecho cosas que me hacen desconfiar de la gente.",
"Busco destacar entre las demás personas.",
"Por más problemas que tenga, soy positivo(a) con lo que pasa en mi vida.",
"En medio de una conversación he olvidado lo que tenía pensado decir.",
"Algunas personas me han criticado injustamente por lo que he hecho.",
"Me divierten los chismes y hablar a espaldas de otras personas.",
"Veo los colores más brillantes que otras personas.",
"Me meto en problemas cuando estoy enojado(a).",
"Puedo pasar mucho tiempo haciendo algo sin tener que parar a descansar.",
"He inventado problemas familiares para evadir obligaciones.",
"Siento que no puedo controlar mi enojo.",
"He tenido problemas con mi familia por tomar alcohol.",
"Me he vengado de personas que me hacen enojar.",
"Tomo riesgos mientras no sean excesivos.",
"Creo que mi vida sin pareja no tiene sentido.",
"Evito los lugares donde hay muchas personas.",
"Me molesto cuando las personas no están de acuerdo conmigo.",
"He convencido a personas para que hagan algo que yo quiero.",
"Me gusta sentir que la gente se fija en mí.",
"Quienes me conocen bien me han dicho que soy imprudente.",
"Me han dicho que cambio de ánimo muy fácilmente.",
"He mentido solo por el gusto de hacerlo.",
"He dicho malas palabras.",
"Me he levantado sin ganas de ir a trabajar o a estudiar.",
"Confío en la mayoría de las personas que conozco.",
"Me gusta relacionarme con personas que hacen cosas nuevas y diferentes.",
"Tengo que estar preparado(a) por si alguna persona me traiciona.",
"Busco nuevas experiencias como visitar lugares que no conozco.",
"He aparentado estar triste para manipular a otras personas más fácilmente.",
"Me esfuerzo por evitar actividades grupales.",
"Estando dormido(a) he soñado con cosas que cuando estoy despierto(a) terminan haciéndose realidad.",
"Disfruto menos las cosas que antes me gustaban.",
"Aun estando furioso(a), soy paciente con los demás.",
"He sentido atracción física por personas que no eran mi pareja.",
"Digo que sí a todo para que la gente no se aleje de mí.",
"Mis pensamientos desaparecen de mi cabeza sin que yo pueda controlarlo.",
"Estando enojado(a) he sido cruel con otras personas.",
"Soy tan impaciente que se me hace difícil seguir con orden las tareas que debo realizar.",
"Prefiero estar solo que con otras personas.",
"Me cuesta demostrar afecto o cariño a las personas.",
"He faltado a citas, reuniones o compromisos si no tengo ganas de ir.",
"He estado tan nervioso(a) que no he podido dormir.",
"Puedo saber lo que pasará en el futuro.",
"Algunas personas se han puesto de acuerdo para hacerme daño.",
"Me considero una persona muy optimista.",
"He tenido problemas en el trabajo por mi consumo de alcohol u otras sustancias.",
"Mantengo relaciones amorosas, aunque estas me hagan sentir peor.",
"He inventado alguna enfermedad o problema para huir de un compromiso.",
"Las personas que me conocen han dicho que soy manipulador(a).",
"Me han dicho que tengo pasatiempos poco comunes.",
"Me molesto cuando me dicen lo que tengo que hacer.",
"Necesito dormir menos horas que las demás personas.",
"He probado la marihuana.",
"He sentido como si mi alma abandonara mi cuerpo.",
"Me encanta ser el centro de atención en fiestas o eventos.",
"A pesar de estar enojado(a) o asustado(a) puedo actuar con cuidado.",
"Soy sincero(a) con las personas, aunque eso perjudique mis intereses.",
"Me obligo a terminar la tarea que estoy haciendo, aunque no tenga sentido que siga.",
"Reacciono con cólera cuando me involucran en un chisme.",
"He perdido relaciones con personas cercanas por una reacción repentina.",
"Me considero una persona solitaria.",
"Hago las cosas solo(a), aunque ocupe ayuda.",
"Algunas personas han robado pensamientos de mi cabeza.",
"He dicho cosas que a otras personas les asusta.",
"Me han dicho que mi forma de hablar es extraña o no se entiende.",
"Miento con facilidad y nadie se da cuenta.",
"Tomar decisiones importantes me pone nervioso(a).",
"He sido grosero(a) con personas que me han provocado.",
"Me gusta estar rodeado(a) de muchas personas.",
"He tomado decisiones sin pensar mucho en las consecuencias.",
"Me siento mal por las cosas que he hecho.",
"He deseado que algo malo le ocurra a alguna persona que no me agrada.",
"Me asusto fácilmente.",
"He tenido amistades que consumen algún tipo de droga.",
"Me es difícil aceptar cuando me equivoco.",
"Las personas afectan mi ánimo por cualquier cosa.",
"Soy exitoso(a) en todo lo que me propongo hacer.",
"He fingido simpatía para que la gente me ayude en alguna tarea.",
"De tantos nervios, he sentido que me voy a morir.",
"Los objetos a mi alrededor de repente me parecen extraños.",
"Procuro decir la verdad, aunque eso me traiga problemas.",
"Las personas que me conocen me han dicho que les demuestro mi aprecio.",
"Me enojo cuando las cosas no salen como espero.",
"Me tiene sin cuidado el reconocimiento de la gente cuando hago algo.",
"Mis gustos para vestir son muy diferentes a los de las demás personas.",
"Tengo problemas para dormir por tanta tensión.",
"En las fiestas tomo más de tres bebidas alcohólicas.",
"He hecho cosas peligrosas, aunque ponga en peligro mi vida.",
"He juzgado a alguna persona solo por su aspecto físico.",
"Tengo buena habilidad para planear cosas con tiempo.",
"Cuando hago algo por demasiado tiempo, me aburro y me pongo a hacer otra cosa.",
"Me afecto emocionalmente cuando personas cercanas me abandonan.",
"He sacado provecho de mi relación con otras personas.",
"He hablado mal de algún ser querido. ",
"De tanta intranquilidad me ha costado concentrarme.",
"Es sencillo ocultar mi tristeza cuando me siento afligido(a).",
"Me cuesta mantenerme concentrado(a) en una sola cosa a la vez.",
"Me pongo impaciente cuando estoy en charlas o reuniones de cualquier tipo.",
"Pienso que el mundo sería un lugar mejor si yo muriera.",
"Me cuesta respirar cuando estoy bajo mucha tensión.",
"Cuando leo algo por mucho rato, me aburro y me pongo a hacer otra cosa.",
"Me esfuerzo poco cuando realizo un trabajo.",
"Durante una conversación me he distraído y perdido el hilo de lo que estaba hablando.",
"Me molesta tener que estarle diciendo a las personas cómo se hacen las cosas.",
"Me han dicho que soy una persona con sentimientos “fríos”.",
"El consumo de alguna bebida alcohólica me ayuda a sobrellevar mis problemas.",
"Invento historias para obtener algún beneficio propio.",
"Siento alegría muy intensa sin tener clara la razón.",
"En momentos de mucha energía hago cosas peligrosas como si nada pudiera pasarme.",
"Gasto mucho dinero comprando bebidas alcohólicas.",
"Me he vestido de forma llamativa para que la gente note mi presencia.",
"Siento como si una parte de mi cuerpo hubiera sido cambiada.",
"He contado a alguien un secreto que otra persona me confió.",
"Me afecta que critiquen mi trabajo.",
"Halago a las personas para que luego me ayuden.",
"Paso de estar muy contento(a) a muy triste de un momento a otro.",
"He sentido la presencia de alguien que las demás personas no pudieron sentir.",
"He comprado cosas que no necesito, solo porque en ese momento me gustaron.",
"He sentido fuerzas negativas a mi alrededor.",
"He dejado de cumplir con tareas pendientes cuando se ponen difíciles.",
"Le he gritado a alguien por contradecirme.",
"He inventado mis propias palabras.",
"Cuando me siento bajo mucha presión tomo alcohol.",
"Trato mal a las personas cuando estoy estresado(a).",
"Me he aprovechado de algunas personas.",
"Evito perder mi tiempo escuchando a personas que saben menos que yo.",
"Me han criticado por llegar tarde a compromisos.",
"La vida es muy triste.",
"He fingido estar enfermo(a) para evitar una responsabilidad.",
"Pienso que tengo un “don especial” que las demás personas no tienen.",
"Me ofende que no me atiendan inmediatamente cuando voy a comer a algún lugar.",
"Necesito consumir alcohol u otras sustancias para sentirme mejor.",
"Si mintiendo obtengo lo que quiero, no dudo en hacerlo.",
"Me siento de repente muy emocionado(a) sin ninguna razón.",
"Soy una persona muy emocional.",
"Me gusta conocer gente nueva.",
"Incluso las cosas más simples pueden hacer que me enfurezca.",
"Si me emociono por algo se me pasa rápido.",
"He tenido la sensación de que algo camina dentro de mi cuerpo.",
"Dejo botadas algunas actividades o proyectos si se ponen difíciles.",
"Reunirme con amistades que no veía hace mucho tiempo no me emociona.",
"Otras personas me han dicho que me comporto de forma extraña.",
"He sentido olores que otras personas no pueden notar.",
"He consumido bebidas alcohólicas varios días seguidos.",
"Hablo lo menos posible cuando estoy con otras personas.",
"Me emociona visitar lugares que podrían ser peligrosos.",
"Tiendo a hacer las cosas de la misma manera, aunque sepa que no va a funcionar.",
"Me impacienta las personas que hablan mucho.",
"Cuando me enojo con alguien no le hablo por mucho tiempo.",
"Necesito hacer muchas actividades para poder liberar energía.",
"Me cuesta compartir información con otras personas por temor a que la usen en mi contra.",
"Me siento humillado cuando me critican por lo que sea.",
"Me han puesto trampas para hacerme quedar mal.",
"En situaciones de emergencia mantengo la calma.",
"Me descontrolo cuando tengo mucha presión.",
"He inventado cosas sobre mí para parecer más interesante ante los demás.",
"Me ha hecho gracia cuando algún desconocido se ha tropezado y cae.",
"Involucro a las personas que conozco en actividades que me benefician.",
"He perdido amistades por consumir alcohol o drogas.",
"La gente envidia mis cualidades.",
"Evito correr riesgos innecesarios.",
"Me ha interesado probar la marihuana u otras drogas.",
"Invento cosas sobre mí mismo(a) para conseguir lo que quiero.",
"Me cuesta disfrutar las cosas porque paso angustiado.",
"Pienso que no sirvo para nada.",
"Me gusta andar en vehículos a alta velocidad.",
"Tengo pensamientos que las demás personas no entienden.",
"Mis emociones son más intensas que las de otras personas.",
"Me aburre vivir en el mismo lugar mucho tiempo.",
"Cuando algo se me pierde sospecho de todas las personas a mi alrededor.",
"Es difícil que me hagan cambiar de opinión, aunque pueda estar equivocado(a).",
"Las fiestas me hacen sentir incómodo(a).",
"Es mejor mentir si eso les evita dolor a las personas.",
"Me da igual cómo me sienta emocionalmente.",
"He hablado de forma grosera con otras personas.",
"Disfruto haciendo quedar mal a la gente.",
"He sentido miedo sin tener un motivo claro.",
"Cuando me enojo por algo me cuesta mucho olvidarlo.",
"He perdido las ganas de esforzarme por mis cosas.",
"Me preocupo tanto que no puedo hacer bien las cosas.",
"Me mantengo tranquilo incluso en situaciones de mucha presión.",
"Evito tratar con personas menos importantes que yo.",
"Me preocupo tanto que podría volverme loco(a).",
"Manejo bien la presión cuando realizo mis obligaciones.",
"Trato de ser cariñoso(a) con las personas que aprecio.",
"He exagerado sobre mis capacidades para conseguir lo que quiero.",
"La gente se aprovecha de mí.",
"Las personas son fáciles de manipular.",
"Pierdo horas de sueño por realizar tareas hasta terminarlas.",
"Me siento nervioso(a) alrededor de otras personas.",
"Creo que soy menos importante que los demás.",
"Tomo mis decisiones luego de un análisis detallado.",
"He comido algo aún sin saber exactamente lo que es.",
"Cuando estoy de mal humor cualquier cosa pequeña me molesta.",
"Me pone nervioso(a) hablar con personas importantes.",
"Me emociona tener varias parejas a la vez.",
"Me organizo tan bien que termino las cosas a tiempo.",
"Me cuesta iniciar tareas que no me gustan, aunque sean urgentes.",
"Comienzo hablando de un tema y cuando me doy cuenta hablo de otro que no tiene nada que ver.",
"Me cuesta mantener mi cabeza centrada en lo que debo hacer.",
"Me siento alegre.",
"Quienes me conocen bien suelen confiar plenamente en mí.",
"He intentado quitarme la vida.",
"Desconfío de las personas demasiado amables.",
"Me cuesta mucho saber cómo se sienten las personas a mi alrededor.",
"Soy capaz de terminar con amistades o relaciones que me parecen dañinas.",
"He conseguido drogas con facilidad.",
"Mi forma de ser no es del agrado de algunas personas.",
"Puedo controlarme cuando estoy enojado(a).",
"Cuando me despido de un grupo de amigos pienso que hablan mal de mí.",
"Pienso que, con todas mis cualidades, debería haber logrado más cosas.",
"He llegado a pensar que tengo un problema con el consumo de licor.",
"Siento tensos mis músculos cuando me enojo.",
"Me cuesta estar calmado(a) cuando hago tareas importantes o complicadas.",
"He dicho groserías a familiares sin sentirme mal por eso.",
"Le he gritado a otras personas estando molesto(a).",
"He sido tan desordenado(a) que me ha costado salir adelante con mis responsabilidades económicas.",
"Tiro objetos estando enojado(a).",
"He sentido envidia por personas que tienen algo que yo quiero.",
"Hago cosas estando muy enojado(a) que después no puedo recordar con claridad.",
"Me distraigo fácilmente cuando veo televisión.",
"Me asombra la cantidad de cosas que sé.",
"A la gente le cuesta trabajo entenderme.",
"Me enoja que las cosas no me salgan bien al primer intento.",
"Si quiero hacer algo, lo hago, aunque sea peligroso.",
"Me he desquitado con personas que me han hecho algún daño.",
"La gente habla mal de mí a mis espaldas.",
"He sentido como si me moviera más despacio que las cosas a mi alrededor.",
"Algunas personas tratan de controlar mis pensamientos.",
"Me cuesta controlar algunas de las cosas que como, a pesar de que me hacen daño.",
"He perdido oportunidades importantes por ser tan obstinado(a).",
"Prefiero los trabajos en los que no tengo que tratar con muchas personas.",
"Acepto mis errores con facilidad.",
"Me molesta no ser reconocido(a) por mis logros.",
"Me siento satisfecho(a) con lo que he logrado.",
"Tengo tanta energía que siento que puedo lograrlo todo.",
"He mentido en un negocio si la ganancia era grande.",
"He actuado sin pensar bien las cosas y después me he arrepentido.",
"Me siento incómodo(a) cuando alguien me comenta sus preocupaciones o problemas.",
"Está bien engañar a las personas si así obtengo lo que quiero.",
"Es difícil para mí pasar de una actividad a otra.",
"Le echo la culpa a los demás para que se sientan culpables y así obtener lo que quiero.",
"He hecho cosas tan extrañas que ni yo mismo me lo esperaba.",
"Me aprovecho de la gente que es fácil de utilizar.",
"Gasto mi dinero solo en cosas estrictamente necesarias.",
"Me importa poco cuando alguien se siente mal por lo que yo le digo.",
"Me han dicho que soy una persona malhumorada.",
"Personas cercanas me han dicho que bebo más de la cuenta.",
"Me siento muy mal cuando estoy solo(a) en la casa, aunque sea por poco tiempo.",
"Cuando tengo algún problema pienso que ocurrirá lo peor.",
"Trato de manera justa a todas las personas por igual.",
"He dejado sin terminar algo y me he puesto a hacer otra cosa.",
"Busco realizar tareas donde la gente me admire.",
"Me preocupa mucho no saber si voy a terminar las cosas a tiempo.",
"Siento que algo horrible me va a pasar.",
"Me han dicho que soy una persona desconfiada.",
"Otras personas pueden escuchar lo que estoy pensando.",
"Me relaciono con la gente solo cuando es necesario.",
"Evito contarle a la gente lo que pienso para que no piensen que soy raro.",
"Escucho voces que nadie más puede.",
"He pensado seriamente que quisiera morirme.",
"Le hago caso a las voces que escucho en mi cabeza.",
"Me ha tocado ser el(a) más inteligente de las personas con las que trato.",
"Se me dificulta mentirle a los demás.",
"He vivido situaciones difíciles que las demás personas no podrían entender.",
"Me gusta participar en actividades en las que pueda sobresalir.",
"He sentido como si el tiempo estuviera detenido.",
"Suelo pasar mucho tiempo tratando de resolver algo, aunque no parezca tener solución.",
"Cuando tengo que decir que no, lo hago, aunque las personas se enojen conmigo.",
"Paso emocionalmente tranquilo(a) la mayor parte del día.",
"Me es difícil dejar de realizar una tarea, aun cuando ya no tengo tiempo para seguir haciéndola.",
"Evito que las personas se sientan en confianza conmigo.",
"He consumido drogas ilegales.",
"Creo que tarde o temprano me voy a suicidar.",
"Me desquito con otras personas cuando estoy enojado(a).",
"Oculto mis errores para que nadie se entere de mis debilidades.",
"Me paralizo o bloqueo cuando trabajo bajo presión.",
"La mayoría de la gente actúa sin malas intenciones.",
"Consumir alcohol me ha causado problemas con personas cercanas.",
"Evito las actividades en las que las personas se pongan muy emotivas."

     
        
    ]

    atencion_answers = []
    enganno_answers = []
    manipulacion_answers = []
    grandiosidad_answers = []
    interpersonal_answers =[]
    irrespondabilidad_answers =[]
    impulsividad_answers = []
    estimulo_answers = []
    distractibilidad_answers =[]
    adiccion_answers =[]
    aislamiento_answers = []
    depresivo_answers = []
    ansiosos_answers = []
    inestabilidad_answers=[]
    hostil_answers=[]
    rigidez_answers=[]
    afecto_answers=[]
    inseguridad_answers=[]
    estres_answers=[]
    hipomaniacas_answers=[]
    inusuales_answers=[]
    paranoia_answers=[]
    desregulacion_answers=[]
    excentricidad_answers=[]

    # <---------------------->
    negacionproblemas_answers=[]
    exageracionvirtudes_answers=[]
    sobrereportedepsicopatia_answers=[]
    exageraciondeseveridad_answers=[]
    inconsistencia_answers=[]
    afectonegativo_answers=[]
    desapego_answers=[]
    antagonismo_answers=[]
    desinhibicion_answers=[]
    psicotismo_answers=[] 


    
    for question in questions:
        print(question)
        answer = int(input("Responda (1/2/3/4): "))
        
        if 1 <= answer <= 4:
            if len(atencion_answers) < 5:
                atencion_answers.append(answer)
            elif len(enganno_answers) < 5:
                enganno_answers.append(answer)
            elif len(manipulacion_answers) < 5:
                manipulacion_answers.append(answer)
            elif len(grandiosidad_answers) < 5:
                grandiosidad_answers.append(answer)
            elif len(interpersonal_answers) < 5:
                interpersonal_answers.append(answer)
            elif len(interpersonal_answers) < 5:
                irrespondabilidad_answers.append(answer)
            elif len(interpersonal_answers) < 5:
                impulsividad_answers.append(answer)
            elif len(estimulo_answers) < 5:
                estimulo_answers.append(answer)
            elif len (distractibilidad_answers) < 5:
                distractibilidad_answers.append(answer)
            elif len (adiccion_answers) < 5:
                adiccion_answers.append(answer)
            elif len (aislamiento_answers) < 5:
                aislamiento_answers.append(answer)
            elif len (depresivo_answers) < 5:
                depresivo_answers.append(answer)
            elif len (ansiosos_answers) < 5:
                ansiosos_answers.append(answer)
            elif len (inestabilidad_answers) < 5:
                inestabilidad_answers.append(answer)
            elif len (hostil_answers) <5:
                hostil_answers.append(answer)
            elif len (rigidez_answers)<5:
                rigidez_answers.append(answer)
            elif len (afecto_answers)<5:
                afecto_answers.append(answer)
            elif len (inseguridad_answers)<5:
                inseguridad_answers.append(answer)
            elif len (estres_answers)<5:
                estres_answers.append(answer)
            elif len (estres_answers)<5:
                estres_answers.append(answer)
            elif len (hipomaniacas_answers)<5:
                hipomaniacas_answers.append(answer)
            elif len (inusuales_answers)<5:
                inusuales_answers.append(answer)
            elif len (paranoia_answers)<5:
                paranoia_answers.append(answer)
            elif len (desregulacion_answers)<5:
                desregulacion_answers.append(answer)
            elif len (excentricidad_answers)<5:
                excentricidad_answers.append(answer)

            elif len (negacionproblemas_answers)<5:
                negacionproblemas_answers.append(answer)
            elif len (exageracionvirtudes_answers)<5:
                exageracionvirtudes_answers.append(answer)
            elif len (sobrereportedepsicopatia_answers)<5:
                sobrereportedepsicopatia_answers.append(answer)
            elif len (exageraciondeseveridad_answers)<5:
                exageraciondeseveridad_answers.append(answer)
            elif len (inconsistencia_answers)<5:
                inconsistencia_answers.append(answer)
            elif len (afectonegativo_answers)<5:
                afectonegativo_answers.append(answer)
            elif len (desapego_answers)<5:
                desapego_answers.append(answer)
            elif len (antagonismo_answers)<5:
                antagonismo_answers.append(answer)
            elif len (desinhibicion_answers)<5:
                desinhibicion_answers.append(answer)
            elif len (psicotismo_answers)<5:
                psicotismo_answers.append(answer)
            
        # <---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
        else:
            print("Invalid input. Please enter a valid choice (1/2/3/4).")



    # Calculate scores for each section
    atencion_score = get_score(atencion_answers)
    enganno_score = get_score(enganno_answers)
    manipulacion_score = get_score(manipulacion_answers)
    grandiosidad_score = get_score(grandiosidad_answers)
    interpersonal_score = get_score(interpersonal_answers)
    irresponsabilidad_score= get_score(interpersonal_answers)
    impulsividad_score=get_score(impulsividad_answers)
    estimulo_score=get_score(estimulo_answers)
    distractibilidad_score = get_score(distractibilidad_answers)
    adiccion_score = get_score(adiccion_answers)
    aislamiento_score = get_score(aislamiento_answers)
    depresivo_score = get_score(depresivo_answers)
    ansioso_score = get_score(ansiosos_answers)
    inestabilidad_score= get_score(inestabilidad_answers)
    hostil_score=get_score(hostil_answers)
    rigidez_score=get_score(rigidez_answers)
    afecto_score=get_score(afecto_answers)
    inseguridad_score=get_score(inseguridad_answers)
    estres_score=get_score(estres_answers)
    hipomaniacas_score=get_score(hipomaniacas_answers)
    inusuales_score=get_score(inusuales_answers)
    paranoia_score=get_score(paranoia_answers)
    desregulacion_score=get_score(desregulacion_answers)
    excentricidad_score=get_score(excentricidad_answers)
    negacionproblemas_score=get_score(negacionproblemas_answers)
    exageracionvirtudes_score=get_score(exageracionvirtudes_answers)
    sobrereportedepsicopatia_score=get_score(sobrereportedepsicopatia_answers)
    exageraciondeseveridad_score=get_score(exageraciondeseveridad_answers)
    inconsistencia_score=get_score(inconsistencia_answers)
    afectonegativo_score=get_score(afecto_answers)
    desapego_score=get_score(desapego_answers)
    antagonismo_score=get_score(antagonismo_answers)
    desinhibicion_score=get_score(desinhibicion_answers)
    psicotismo_score=get_score(psicotismo_answers)






    # Constants for section averages and standard deviations
    #Chart 1
    negacionproblemas_average =42.5109
    negacionproblemas_std_dev =7.21173
    exageracionvirtudes_average =40.7664
    exageracionvirtudes_std_dev =4.96694
    sobrereportedepsicopatia_average =30.7956
    sobrereportedepsicopatia_std_dev =6.6933
    exageraciondeseveridad_average =38.8942
    exageraciondeseveridad_std_dev =9.2372
    inconsistencia_average =11.0000
    inconsistencia_std_dev =4.0428
    afectonegativo_average =85.943971
    afectonegativo_std_dev =28.02867
    desapego_average =38.313796
    desapego_std_dev =11.73598
    antagonismo_average =77.006043
    antagonismo_std_dev =20.83766
    desinhibicion_average =54.506158
    desinhibicion_std_dev =13.31106
    psicotismo_average =69.799650
    psicotismo_std_dev =20.51200

    #ESPECTRO DE EXTERNALIZACIÓN
    atencion_average = 17.583082
    atencion_std_dev = 4.692501
    enganno_average = 20.319277
    enganno_std_dev = 5.654496
    manipulacion_average = 21.174962
    manipulacion_std_dev = 6.438614
    grandiosidad_average = 20.381599
    grandiosidad_std_dev = 5.107079
    interpersonal_average = 21.174962
    interpersonal_std_dev = 5.107079
    irresponsabilidad_average=15.352378
    irresponsabilidad_std_dev=5.643104
    impulsividad_average=14.585899
    impulsividad_std_dev=4.654283
    estimulo_average=21.540682
    estimulo_std_dev=6.091848
    distractibilidad_average = 19.023233
    distractibilidad_std_dev = 7.516042
    adiccion_average= 17.679697
    adiccion_std_dev= 9.231313
    #ESPECTRO DE INTERNALIZACIÓN
    aislamiento_average=22.813468
    aislamiento_std_dev = 8.19557
    depresivo_average = 18.263572
    depresivo_std_dev = 8.42421
    ansiosos_average=17.892442
    ansiosos_std_dev=8.08490
    inestabilidad_average=13.784177
    inestabilidad_std_dev=4.94694
    hostil_average=29.912396
    hostil_std_dev=10.54092
    rigidez_average=15.917559
    rigidez_std_dev=3.76570
    afecto_average=14.532853
    afecto_std_dev=4.49279
    inseguridad_average=13.727388
    inseguridad_std_dev=3.82314
    estres_average=18.685587
    estres_std_dev=6.54518
    hipomaniacas_average=19.516847
    hipomaniacas_std_dev=5.20864
    #ESPECTRO DE PSICOTICISMO
    inusuales_average=14.832992
    inusuales_std_dev=5.42643
    paranoia_average=23.722045
    paranoia_std_dev=6.87312
    desregulacion_average=12.927838
    desregulacion_std_dev=5.29957
    excentricidad_average=14.596008
    excentricidad_std_dev=6.57116


    # Calculate T scores for each section

    negacionproblemas_t_score=calculate_t_score(negacionproblemas_score, negacionproblemas_average, negacionproblemas_std_dev)
    exageracionvirtudes_t_score=calculate_t_score(exageracionvirtudes_score, exageracionvirtudes_average, exageracionvirtudes_std_dev)
    sobrereportedepsicopatia_t_score=calculate_t_score(sobrereportedepsicopatia_score, sobrereportedepsicopatia_average, sobrereportedepsicopatia_std_dev)
    exageraciondeseveridad_t_score=calculate_t_score(exageraciondeseveridad_score, exageraciondeseveridad_average, exageraciondeseveridad_std_dev)
    inconsistencia_t_score=calculate_t_score(inconsistencia_score, inconsistencia_average, inconsistencia_std_dev)
    afectonegativo_t_score=calculate_t_score(afectonegativo_score, afectonegativo_average, afectonegativo_std_dev)
    desapego_t_score=calculate_t_score(desapego_score, desapego_average, desapego_std_dev)
    antagonismo_t_score=calculate_t_score(antagonismo_score, antagonismo_average, antagonismo_std_dev)
    desinhibicion_t_score=calculate_t_score(desinhibicion_score, desinhibicion_average, desinhibicion_std_dev)
    psicotismo_t_score=calculate_t_score(psicotismo_score, psicotismo_average, psicotismo_std_dev)

   #<--------------------------------------------->
    atencion_t_score = calculate_t_score(atencion_score, atencion_average, atencion_std_dev)
    enganno_t_score = calculate_t_score(enganno_score, enganno_average, enganno_std_dev)
    manipulacion_t_score = calculate_t_score(manipulacion_score, manipulacion_average, manipulacion_std_dev)
    grandiosidad_t_score = calculate_t_score(grandiosidad_score, grandiosidad_average, grandiosidad_std_dev)
    interpersonal_t_score = calculate_t_score(interpersonal_score, interpersonal_average, interpersonal_std_dev)
    distractibilidad_t_score = calculate_t_score(distractibilidad_score, distractibilidad_average, distractibilidad_std_dev)
    adiccion_t_score= calculate_t_score(adiccion_score, adiccion_average,adiccion_std_dev)
    aislamiento_t_score = calculate_t_score(aislamiento_score,aislamiento_average, aislamiento_std_dev)
    depresivo_t_score = calculate_t_score(depresivo_score, depresivo_average,depresivo_std_dev)
    ansiosos_t_score = calculate_t_score (ansioso_score, ansiosos_average, ansiosos_std_dev)
    inestabilidad_t_score = calculate_t_score(inestabilidad_score, inestabilidad_average, inestabilidad_std_dev)
    irresponsabilidad_t_score = calculate_t_score(irresponsabilidad_score, irresponsabilidad_average, irresponsabilidad_std_dev)
    impulsividad_t_score = calculate_t_score(impulsividad_score, impulsividad_average,impulsividad_std_dev)
    estimulo_t_score= calculate_t_score(estimulo_score, estimulo_average, estimulo_std_dev)
    #<--------------------------------------------->
    hostil_t_score = calculate_t_score(hostil_score, hostil_average, hostil_std_dev)
    rigidez_t_score= calculate_t_score(rigidez_score, rigidez_average, rigidez_std_dev)
    afecto_t_score= calculate_t_score(afecto_score, afecto_average, afecto_std_dev)
    inseguridad_t_score= calculate_t_score(inseguridad_score, inseguridad_average, inseguridad_std_dev)
    estres_t_score= calculate_t_score(estres_score, estres_average, estres_std_dev)
    hipomaniacas_t_score=calculate_t_score(hipomaniacas_score, hipomaniacas_average, hipomaniacas_std_dev)
    inusuales_t_score=calculate_t_score(inusuales_score, inusuales_average, inusuales_std_dev)
    paranoia_t_score=calculate_t_score(paranoia_score, paranoia_average, paranoia_std_dev)
    desregulacion_t_score=calculate_t_score(desregulacion_score, desregulacion_average, desregulacion_std_dev)
    excentricidad_t_score=calculate_t_score(excentricidad_score, excentricidad_average, excentricidad_std_dev)
    
        # Update section names
    section_labels = [
        'NEGACIÓN DE PROBLEMAS',
        'EXAGERACIÓN DE VIRTUDES',
        'SOBREREPORTE DE PSICOPATOLOGÍA',
        'EXAGERACIÓN DE SEVERIDAD',
        'INCONSISTENCIA',
        'AFECTO NEGATIVO',
        'DESAPEGO',
        'ANTAGONISMO',
        'DESINHIBICIÓN',
        'PSICOTICISMO',


       
    ]

    t_scores = [
        negacionproblemas_t_score,
        exageracionvirtudes_t_score,
        sobrereportedepsicopatia_t_score,
        exageraciondeseveridad_t_score,
        inconsistencia_t_score,
        afectonegativo_t_score,
        desapego_t_score,
        antagonismo_t_score,
        desinhibicion_t_score,
        psicotismo_t_score
    ]
   

    plt.figure(figsize=(12, 6))  # Adjust the figure size
    plt.plot(section_labels, t_scores, marker='o', linestyle='-')
    plt.title('INVENTARIO DIMENSIONAL DE PSICOPATOLOGÍA DE LA PERSONALIDAD (IDPP)ESCALAS DE VALIDEZ Y DOMINIOS DESADAPTATIVOS')
    plt.xlabel('Seccion')
    plt.ylabel('Puntajes T')
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.grid(True)
    plt.tight_layout()  # Adjust layout for better spacing
    plt.show()  # Display the chart
    # Update section names
    section_labels = [
        'BÚSQUEDA DE ATENCIÓN',
        'TENDENCIA AL ENGAÑO',
        'RASGOS MANIPULATORIOS',
        'RASGOS DE GRANDIOSIDAD',
        'Interpersonal',
        'Distractibilidad',
        'Aislamiento',
        'Depresivo',
        'Ansioso',
        'Inestabilidad',
        'Irresponsabilidad',
        'Impulsividad',
        'Estimulo',
        'Distracciones',
        'Adiccion'
    ]

    t_scores = [
        atencion_t_score,
        enganno_t_score,
        manipulacion_t_score,
        grandiosidad_t_score,
        interpersonal_t_score,
        distractibilidad_t_score,
        aislamiento_t_score,
        depresivo_t_score,
        ansiosos_t_score, 
        inestabilidad_t_score,
        irresponsabilidad_t_score,
        impulsividad_t_score,
        estimulo_t_score,
        distractibilidad_t_score,
        adiccion_t_score,

        
    ]
   

    plt.figure(figsize=(12, 6))  # Adjust the figure size
    plt.plot(section_labels, t_scores, marker='o', linestyle='-')
    plt.title('TINVENTARIO DIMENSIONAL DE PSICOPATOLOGÍA DE LA PERSONALIDAD (IDPP) SUPER ESPECTRO DE EXTERNALIZACIÓN')
    plt.xlabel('Seccion')
    plt.ylabel('Puntajes T')
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.grid(True)
    plt.tight_layout()  # Adjust layout for better spacing
    plt.show()  # Display the chart    
    
    
    



    # Update section names
    section_labels = [
        'Depresivos',
        'Ansiosos',
        'Inestabilidad',
        'Rasgos Hostiles',
        'Rigidez',
        'Inseguridad',
        'Estres'
    ]

    t_scores = [
        depresivo_t_score,
        ansiosos_t_score,
        inestabilidad_t_score,
        hostil_t_score,
        rigidez_t_score,
        inseguridad_t_score,
        estres_t_score
        
    ]
   

    plt.figure(figsize=(12, 6))  # Adjust the figure size
    plt.plot(section_labels, t_scores, marker='o', linestyle='-')
    plt.title('INVENTARIO DIMENSIONAL DE PSICOPATOLOGÍA DE LA PERSONALIDAD (IDPP) ESPECTRO DE INTERNALIZACIÓN')
    plt.xlabel('Seccion')
    plt.ylabel('Puntajes T')
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.grid(True)
    plt.tight_layout()  # Adjust layout for better spacing
    plt.show()  # Display the chart

    section_labels = [
        'Inusuales',
        'Paranoia',
        'Cognitiva',
        'Excentricidad',
        'Hipomaniacas',
        'Aislamiento',
        'Afecto Rest'
       
    ]

    t_scores = [
       inusuales_t_score,
       paranoia_t_score,
       desregulacion_t_score,
       excentricidad_t_score,
       hipomaniacas_t_score,
       aislamiento_t_score,
       afecto_t_score
    ]
   

    plt.figure(figsize=(12, 6))  # Adjust the figure size
    plt.plot(section_labels, t_scores, marker='o', linestyle='-')
    plt.title('INVENTARIO DIMENSIONAL DE PSICOPATOLOGÍA DE LA PERSONALIDAD (IDPP) SUPER ESPECTRO DE PSICOSIS')
    plt.xlabel('Seccion')
    plt.ylabel('Puntajes T')
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.grid(True)
    plt.tight_layout()  # Adjust layout for better spacing
    plt.show()  # Display the chart

if __name__ == "__main__":
    main()
