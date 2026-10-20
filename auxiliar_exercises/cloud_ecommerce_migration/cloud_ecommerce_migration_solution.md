# Hogar Norte: migración del comercio electrónico a la nube

Material de estudio y resolución guiada de las ocho consignas. Tiempo en **semanas** y dinero en **dólares estadounidenses (USD)**. Se conserva el [PDF original](Ejercicio_DPI_Migracion_Ecommerce_Hogar_Norte.pdf) y una [transcripción de consulta](exercise_prompt.md).

La planificación termina al cierre de la **semana 17**, una semana antes del límite de 18. El costo presupuestado total es **USD 286.000**. Al cierre de la semana 6 hay menos trabajo terminado que el previsto y el trabajo realizado costó más que su presupuesto. Si se mantiene esa eficiencia, el costo final estimado es **USD 317.032,26**. A continuación se explica de dónde sale cada resultado y qué supuestos necesita.

## 1. Introducción teórica: qué estamos tratando de medir

### 1.1. Del trabajo al tiempo, del tiempo al dinero

Migrar una tienda no consiste en una única tarea: hay que contratar, preparar infraestructura, trasladar datos, desarrollar, probar y publicar. Una **actividad** es una porción de trabajo con una duración, un costo y un resultado identificable. Una **predecesora** es una actividad que impone una condición para ejecutar otra. Por ejemplo, primero debe estar firmado el contrato y después puede aprovisionarse la nube. Un **hito** marca un acontecimiento, como una autorización, sin duración propia. Estas definiciones y atributos se presentan en la clase de plazos, páginas 7–9 [T1].

La **duración** mide cuánto tiempo de calendario relativo ocupa una actividad; el **esfuerzo** mide cuánto trabajo humano requiere. No son lo mismo: 640 horas de trabajo distribuidas entre varias personas pueden realizarse en cuatro semanas. Tampoco las horas de trabajo son dólares: para convertirlas a costo hay que aplicar una tarifa por hora. Esta distinción se obtiene aquí de las unidades de la propia consigna (página 2): informa por separado horas de trabajo y semanas de duración; no se atribuye a una definición textual de las diapositivas.

En el enunciado, **cloud** significa infraestructura informática en la nube; **e-commerce**, comercio electrónico; **UX**, *User Experience* o experiencia de usuario; **UI**, *User Interface* o interfaz de usuario. El rediseño UX/UI define cómo se utiliza y cómo se ve la tienda y la aplicación. Una **app** es una aplicación móvil. **Go-live** es la puesta en producción: el momento y el proceso por el que el sistema comienza a atender usuarios reales. Son aclaraciones de vocabulario del caso, no nuevas exigencias técnicas.

### 1.2. Estimar un costo no es adivinarlo

Una **estimación** es una evaluación cuantitativa del costo probable, no una garantía de precio final. Puede ser puntual, si presenta un solo valor, o multipunto, si incorpora varios escenarios. Fuentes: clase de costos, páginas 8, 10 y 11 [T2].

- **Estimación análoga:** usa el costo de una experiencia anterior comparable. Aquí, el rediseño de Uruguay es la referencia del nuevo rediseño. Sin datos de diferencias de alcance o inflación, se utiliza el valor informado y se reconoce ese límite.
- **Estimación paramétrica:** multiplica una cantidad de trabajo por un costo unitario. Por ejemplo, 100 productos a USD 0,50 por producto cuestan USD 50. Las unidades “producto” se cancelan y queda dinero.
- **Estimación multipunto PERT:** PERT corresponde a *Program Evaluation and Review Technique*, técnica de evaluación y revisión de programas. En este ejercicio se aplica a costos: combina un costo **optimista**, uno **más probable** y uno **pesimista**. Llamaremos **O**, **m** y **P** a esos importes, todos en USD. La fórmula es **costo esperado = (O + 4 × m + P) / 6**. El valor más probable recibe cuatro veces el peso de cada extremo; los pesos suman seis. No es la media simple de tres números y no es una reserva adicional.

Mini ejemplo didáctico: si O = 100, m = 130 y P = 180, el costo PERT es (100 + 4 × 130 + 180) / 6 = USD 133,33. La asimetría del escenario caro eleva el resultado por encima de 130. Este ejemplo se creó para explicar la fórmula de la clase; no pertenece al enunciado.

Si el caso solo informa “cuesta USD 12.000”, conocemos una **estimación puntual dada**, pero no sabemos si provino de juicio experto, una cotización o un cálculo detallado. No corresponde inventar su origen. Sumar luego todos los costos individuales es una **agregación del presupuesto**, no una prueba de que cada costo se haya estimado de manera ascendente.

### 1.3. Cómo leer una red y encontrar el trabajo que no puede atrasarse

Una red **AON**, *Activity on Node* o actividad en el nodo, representa actividades mediante cajas y dependencias mediante flechas. Cada flecha significa una condición de precedencia, no una semana ni un costo. Una relación **FS**, *Finish to Start* o fin a inicio, permite iniciar la sucesora cuando termina la predecesora. En este caso todas las relaciones modeladas son FS sin espera adicional. Fuente: clase de plazos, páginas 16, 18 y 19 [T1].

Un **camino** es una secuencia continua de actividades desde el inicio hasta el fin de la red. El **camino crítico** es el de mayor duración: fija el tiempo mínimo del proyecto con esas duraciones y dependencias. Si una de sus actividades se demora y no se compensa la demora, se retrasa el cierre. El **método del camino crítico**, **CPM** por *Critical Path Method*, permite calcularlo. Fuentes: páginas 21 y 26–28 [T1].

Antes de leer los nodos, definimos sus cuatro tiempos. Todos se miden en **semanas transcurridas desde el inicio**, que es el instante 0:

| Símbolo | Nombre original y traducción | Qué responde |
| --- | --- | --- |
| ES | Early Start, inicio temprano | ¿Cuándo puede comenzar como muy pronto? |
| LS | Late Start, inicio tardío | ¿Hasta cuándo puede posponer su inicio sin mover el fin calculado? |
| EF | Early Finish, fin temprano | ¿Cuándo termina si empieza en ES? |
| LF | Late Finish, fin tardío | ¿Hasta cuándo puede terminar sin mover el fin calculado? |

La **holgura total** es el margen de una actividad respecto del fin calculado: **LS − ES = LF − EF**, en semanas. No se suman las holguras de dos actividades consecutivas como si fueran reservas independientes: pueden compartir el mismo margen de una rama.

El **paso adelante** recorre la red desde el inicio. Para cada actividad, **ES = máximo de los EF de sus predecesoras** y **EF = ES + duración**. Se usa el máximo porque necesita que hayan terminado **todas** sus predecesoras. Sin predecesoras, ES = 0.

El **paso atrás** parte del fin calculado. Para cada actividad, **LF = mínimo de los LS de sus sucesoras** y **LS = LF − duración**. Se usa el mínimo porque no puede bloquear a **ninguna** de sus sucesoras. Para la última actividad, LF coincide con el fin del proyecto.

Mini ejemplo didáctico: dos predecesoras terminan en 5 y 7. Una tarea de dos semanas que necesita a ambas comienza en máximo(5, 7) = 7 y termina en 9. Si debe finalizar como máximo en 10, LS = 10 − 2 = 8 y su holgura es 8 − 7 = una semana.

El **diagrama de Gantt** coloca las actividades en filas y el tiempo en columnas; la longitud y ubicación de cada barra muestran duración e inicio. Es otra vista del mismo cronograma, no un nuevo conjunto de fechas. Fuente: páginas 29–30 [T1].

### 1.4. Del Gantt a la línea base de costos

El **costo directo** puede asignarse a una actividad concreta; el **costo de estructura** sostiene el proyecto en conjunto, como coordinación, herramientas y seguros. Aquí se lo presenta separado para evitar cargarlo dos veces. Fuente conceptual: clase de costos, página 9 [T2]; importes y cambio de tarifa: consigna, página 2.

El **Gantt de costos** distribuye por período el presupuesto de cada actividad. Su suma por columna muestra cuánto se prevé gastar en esa semana; al acumular esas columnas se obtiene la **línea base de costos**, la referencia temporal contra la que se controlará el desempeño. La **Curva S** grafica esos costos acumulados; su forma exacta depende del plan y no tiene que parecer una letra S perfecta. Fuentes: clase de costos, páginas 13–14, 16 y 20–22 [T2].

Usaremos el reparto lineal enseñado por la cátedra: costo semanal de una actividad = costo total / duración, durante sus semanas activas. Mini ejemplo: una tarea de USD 6.000 que ocupa semanas 3 y 4 aporta USD 3.000 en cada una. Al cierre de la semana 3 lleva planificado el 50 %, no el 100 %.

**BAC**, *Budget at Completion*, presupuesto hasta la conclusión, es el total presupuestado del trabajo que controlamos: el último valor de la curva acumulada. En este caso incluye actividades y estructura. La **reserva para contingencias** cubre riesgos identificados y forma parte de la línea base; la **reserva de gestión** queda fuera de ella. El caso no aporta importes ni porcentajes de reserva: no los inventaremos. Fuentes: clase de costos, páginas 16–18 [T2], y clase de medición, página 20 [T3].

### 1.5. Cómo controlar sin confundir “gasté” con “avancé”

El **Método del Valor Ganado**, **EVM** por *Earned Value Management*, convierte trabajo planificado y realizado a una misma unidad monetaria para compararlos con el gasto real. No identifica valor de mercado, ventas ni ganancias del negocio; usa el presupuesto del trabajo. Fuente: clase de medición, páginas 9–12 [T3].

| Símbolo | Significado | Cálculo y unidad |
| --- | --- | --- |
| PV | Planned Value, valor planificado | Suma de presupuesto de cada actividad × su fracción planificada al corte; USD |
| EV | Earned Value, valor ganado | Suma de presupuesto de cada actividad × su fracción realmente terminada al corte; USD |
| AC | Actual Cost, costo real | Suma de los costos efectivamente incurridos al mismo corte; USD |
| CV | Cost Variance, variación de costo | EV − AC; USD. Negativa: el trabajo realizado costó más que su presupuesto |
| SV | Schedule Variance, variación del cronograma | EV − PV; USD. Negativa: se completó menos trabajo presupuestado que el previsto |
| CPI | Cost Performance Index, índice de desempeño del costo | EV / AC; sin unidad. Menor que 1: eficiencia desfavorable |
| SPI | Schedule Performance Index, índice de desempeño del cronograma | EV / PV; sin unidad. Menor que 1: avance valorizado inferior al previsto |

Fuentes de variaciones e índices: páginas 15 y 17–18 [T3]. Una fracción de avance del 40 % se utiliza como 0,40 en la multiplicación. Un CPI de 0,90 significa USD 0,90 de trabajo presupuestado por cada USD 1 gastado. Un SPI de 0,90 significa 90 % del valor de trabajo previsto a esa fecha; **no significa 10 % de semanas de atraso**.

Mini ejemplo: una tarea presupuestada en USD 10.000 debía estar al 50 %, está al 40 % y consumió USD 6.000. PV = 5.000, EV = 4.000 y AC = 6.000. CV = −2.000 y SV = −1.000. Gastar 1.000 más que el plan no cuenta toda la historia: además faltan 1.000 de trabajo planificado que no se ejecutó. El sobrecosto del trabajo efectivamente realizado es 2.000.

### 1.6. Pronosticar no es cambiar el presupuesto aprobado

Estas magnitudes permiten responder las preguntas de futuro. Todas usan la misma fecha de corte y el mismo alcance:

| Símbolo | Nombre y pregunta | Fórmula usada y unidad |
| --- | --- | --- |
| EAC | Estimate at Completion, estimación a la conclusión: ¿cuánto costará todo? | BAC / CPI; USD |
| ETC | Estimate to Complete, estimación para completar: ¿cuánto falta gastar? | EAC − AC; USD |
| VAC | Variance at Completion, variación a la conclusión: ¿sobrará o faltará presupuesto? | BAC − EAC; USD |
| TCPI | To-Complete Performance Index, índice de desempeño del trabajo por completar: ¿qué eficiencia exige el presupuesto original? | (BAC − EV) / (BAC − AC); sin unidad |

Fuentes: clase de medición, páginas 20–23 [T3]. **BAC − EV** es el trabajo pendiente valorizado al presupuesto; **BAC − AC** es el dinero que aún queda dentro del presupuesto. No son la misma cosa.

La fórmula EAC = BAC / CPI supone que la eficiencia de costo observada persistirá en lo que falta; es el método usado por la cátedra. No es una certeza ni una nueva autorización de gasto. Si cambian las causas del desvío, hay que actualizar el pronóstico. Conservaremos todos los decimales de los índices hasta el resultado final.

### 1.7. Quién hace, responde, opina, recibe información y firma

La **matriz RACIS** asigna actividades a roles. Las filas son actividades y las columnas son roles concretos. Fuente: clase de equipo e interesados, páginas 20–21 y 24–25 [T4].

- **R — Responsible:** responsable de ejecutar el trabajo.
- **A — Accountable:** quien rinde cuentas por el resultado. Debe haber exactamente uno por fila.
- **C — Consulted:** quien aporta opinión antes o durante el trabajo.
- **I — Informed:** quien recibe información sobre el avance o el resultado.
- **S — Sign:** quien debe firmar documentación vinculada a la actividad.

La firma no convierte automáticamente a alguien en ejecutor ni en quien rinde cuentas. Una contratación puede tener al líder técnico como R, al director del proyecto como A y al gerente general como S. El caso indica que el director del proyecto rinde cuentas en general, y establece excepciones para la campaña y la presentación final.

## 2. Método de resolución y supuestos que hacen falta

La secuencia es: extraer actividades y dependencias → estimar costos → calcular tiempos → comprobar caminos → dibujar Gantt → repartir costos → medir en semana 6 → pronosticar → asignar responsabilidades. Cada paso reutiliza los resultados del anterior; así se evita tener un costo que no coincide con el cronograma o un avance que usa otra base monetaria.

1. **Calendario relativo:** no hay fecha de inicio ni feriados. Se usan semanas consecutivas; el intervalo de tiempo 0–2 corresponde a las semanas 1 y 2. El cierre de la semana 6 es el instante 6. No se inventan fechas de calendario.
2. **Dependencias:** se incorporan las que afirma el caso. El desarrollo web y móvil dependen del rediseño, no del aprovisionamiento cloud; la integración sí depende del aprovisionamiento y de la web. No se agregan restricciones técnicas que el enunciado no dio.
3. **Paralelismo y recursos:** se acepta la ejecución simultánea expresamente indicada. Web y app requieren 160 horas por semana cada una; si se supusieran jornadas de 40 horas, equivaldrían a cuatro personas a tiempo completo por frente. Es una equivalencia de esfuerzo, no una dotación confirmada. El caso no permite comprobar una nivelación de recursos ni agregar demoras por sobreasignación.
4. **Firmas y aprobaciones:** están incluidas en las actividades correspondientes; no se les asigna una duración extra inventada. La presentación final ocupa una semana completa después de la campaña.
5. **Costos:** se distribuyen uniformemente durante cada actividad. Es el modelo pedagógico de la clase; sin calendario de pagos no se puede afirmar que sean desembolsos bancarios efectivos. Se usan los costos PERT calculados en la línea base porque esta consigna lo exige; no se conserva el valor más probable como hace el ejemplo ilustrativo de la clase 5, página 11.
6. **Estructura:** se aplica USD 3.000 por semana hasta antes de comenzar la campaña y USD 1.500 por semana desde su inicio hasta el cierre. Para medirla al corte se usa **nivel de esfuerzo**: el servicio de coordinación prestado durante seis semanas gana el mismo valor previsto para esas seis semanas, USD 18.000. Es un supuesto explícito de medición de soporte; no significa que los entregables técnicos hayan avanzado al ritmo planificado. Su efecto es acercar los índices globales a 1.
7. **Datos reales:** “contratación según lo previsto” se interpreta como finalizada y con costo real de USD 4.000. App “según lo planificado” significa 80 % al cierre de la semana 6. Actividades aún no iniciadas no acumulan trabajo ni gasto, dado que no se informan anticipos.
8. **Pronóstico:** se utiliza la continuidad del CPI de la clase. Las proyecciones de fechas basadas en ritmos de migración se presentarán como escenarios, no como hechos observados.

## 3. Resolución paso a paso

### Paso 1. Lista de actividades y estimación de costos — consigna 1

Usamos letras A–N como identificadores. La letra **M de la actividad campaña** no debe confundirse con el escenario “más probable” de PERT, que aquí se escribió con **m minúscula**.

#### Los dos costos PERT

**C · Aprovisionamiento cloud.** Optimista USD 14.000, más probable USD 18.000 y pesimista USD 28.000:

**(14.000 + 4 × 18.000 + 28.000) / 6 = 114.000 / 6 = USD 19.000.**

**E · Migración de clientes y pedidos.** Optimista USD 10.000, más probable USD 15.000 y pesimista USD 26.000:

**(10.000 + 4 × 15.000 + 26.000) / 6 = 96.000 / 6 = USD 16.000.**

En ambos casos el escenario pesimista está más alejado del más probable que el optimista; por eso el resultado esperado queda por encima del más probable. Estos escenarios son de **costo**, no de duración: C sigue durando dos semanas y E también.

#### Los costos paramétricos y la duración del catálogo

- **D · Catálogo:** 60.000 productos / 15.000 productos por semana = **4 semanas**. Costo: 60.000 × USD 0,50 = **USD 30.000**. Por semana: 15.000 × 0,50 = USD 7.500.
- **G · Web:** 640 horas × USD 50/hora = **USD 32.000**. Se respeta la duración informada de cuatro semanas; 640 no es una duración de calendario.
- **H · App:** 800 horas × USD 50/hora = **USD 40.000**, en las cinco semanas informadas.
- **F · Rediseño:** **USD 15.000** por estimación análoga al trabajo de Uruguay. No se transforma en estimación paramétrica dividiendo el costo por dos semanas: esa división solo sirve luego para distribuirlo.

| ID | Actividad | Duración (sem.) | Predecesoras | Costo (USD) | Estimación |
| --- | --- | --- | --- | --- | --- |
| A | Arquitectura cloud | 2 | — | 12.000 | Puntual dada; origen no especificado |
| B | Contratación cloud | 1 | A | 4.000 | Puntual dada; origen no especificado |
| C | Aprovisionamiento cloud | 2 | B | 19.000 | Multipunto PERT |
| D | Migración del catálogo | 4 | C | 30.000 | Paramétrica: productos × tarifa |
| E | Migración de clientes y pedidos | 2 | C | 16.000 | Multipunto PERT |
| F | Rediseño de tienda y app | 2 | — | 15.000 | Análoga: filial Uruguay |
| G | Desarrollo de tienda web | 4 | F | 32.000 | Paramétrica: horas × tarifa |
| H | Desarrollo de app móvil | 5 | F | 40.000 | Paramétrica: horas × tarifa |
| I | Integración pagos y logística | 2 | G, C | 10.000 | Puntual dada; origen no especificado |
| J | Pruebas integrales y seguridad | 2 | D, E, H, I | 14.000 | Puntual dada; origen no especificado |
| K | Publicación de la app | 1 | J | 2.000 | Puntual dada; origen no especificado |
| L | Puesta en producción de tienda | 2 | J | 8.000 | Puntual dada; origen no especificado |
| M | Campaña de relanzamiento | 3 | K, L | 36.000 | Presupuesto dado; origen no especificado |
| N | Presentación de resultados | 1 | M | 3.000 | Puntual dada; origen no especificado |

La suma de los 14 costos directos es **USD 241.000**. La estructura se calculará después de conocer cuándo empieza la campaña y cuándo termina el proyecto. No se modela como una tarea adicional que condicione la red: es un gasto que acompaña las actividades.

### Paso 2. Cálculo de tiempos y red AON — consigna 2

#### 2.1. Recorrido hacia adelante

**Infraestructura y datos:** A ocupa 0–2; B, 2–3; C, 3–5. Después se abren D, de 5 a 9, y E, de 5 a 7.

**Diseño y desarrollo:** F ocupa 0–2. Desde allí G ocupa 2–6 y H ocupa 2–7. La integración I espera a G y a C: ES de I = máximo(6, 5) = **6**; EF de I = 6 + 2 = **8**.

**Convergencia de pruebas:** J requiere D, E, H e I. Por lo tanto, ES de J = máximo(9, 7, 7, 8) = **9**. Aunque la app y los clientes estén listos en 7, las pruebas tienen que esperar al catálogo hasta 9. J termina en **11**.

**Salida y cierre:** K ocupa 11–12 y L ocupa 11–13. M espera a ambas: ES de M = máximo(12, 13) = **13**; termina en **16**. N ocupa 16–17. La presentación no es un hito de duración cero: el caso le asigna una semana.

#### 2.2. Recorrido hacia atrás

Anclamos el cierre calculado en **17**, no en 18: queremos la holgura respecto del plan de duración mínima. N tiene LF = 17 y LS = 16; M tiene LF = 16 y LS = 13. K y L deben terminar a más tardar en 13: K tiene LS = 12 y L tiene LS = 11.

J alimenta a K y L, por lo que LF de J = mínimo(12, 11) = **11** y LS de J = **9**. Sus cuatro predecesoras tienen que terminar como máximo en 9: D tiene LS = 5; E, LS = 7; H, LS = 4; I, LS = 7.

C alimenta a D, E e I: LF de C = mínimo(5, 7, 7) = **5**, y LS de C = **3**. G tiene LF = 7 y LS = 3. F alimenta a G y H: LF de F = mínimo(3, 4) = **3** y LS de F = **1**. Completamos B y A hasta volver al inicio.

#### 2.3. Tiempos y holguras

Todos los valores de esta tabla están en semanas transcurridas desde el inicio. La holgura usa el fin calculado de 17 semanas.

| ID | ES | LS | EF | LF | Holgura (sem.) | Crítica |
| --- | --- | --- | --- | --- | --- | --- |
| A | 0 | 0 | 2 | 2 | 0 | Sí |
| B | 2 | 2 | 3 | 3 | 0 | Sí |
| C | 3 | 3 | 5 | 5 | 0 | Sí |
| D | 5 | 5 | 9 | 9 | 0 | Sí |
| E | 5 | 7 | 7 | 9 | 2 | No |
| F | 0 | 1 | 2 | 3 | 1 | No |
| G | 2 | 3 | 6 | 7 | 1 | No |
| H | 2 | 4 | 7 | 9 | 2 | No |
| I | 6 | 7 | 8 | 9 | 1 | No |
| J | 9 | 9 | 11 | 11 | 0 | Sí |
| K | 11 | 12 | 12 | 13 | 1 | No |
| L | 11 | 11 | 13 | 13 | 0 | Sí |
| M | 13 | 13 | 16 | 16 | 0 | Sí |
| N | 16 | 16 | 17 | 17 | 0 | Sí |

#### 2.4. Diagrama con el molde de la cátedra

El encabezado de cada nodo separa **ID y duración**. Los tiempos aparecen en cuatro celdas en orden **ES | LS | EF | LF**, y la holgura se indica debajo. Las actividades y flechas críticas son magenta; las demás, grises. Se respeta la estructura de las páginas 19 y 21 de la clase de plazos y la observación docente de la entrega 2. Las flechas tienen puntas individuales; no se fusionan tramos de relaciones diferentes.

![Red AON completa: tiempos, duración y holgura de las 14 actividades](assets/activity_network.svg)

**Camino crítico: A → B → C → D → J → L → M → N.**

**Duración = 2 + 1 + 2 + 4 + 2 + 2 + 3 + 1 = 17 semanas.**

Se cumple el máximo de 18 semanas con **una semana de margen respecto del compromiso externo**. Esa semana no es una reserva agregada al cronograma ni la holgura interna de las tareas críticas. Si se recalcularan los tiempos tardíos tomando 18 como fecha límite, se obtendría margen adicional respecto de esa restricción; aquí no se mezclan ambos criterios.

### Paso 3. Cuántos caminos tiene la red — consigna 3

Para contar, seguimos cada alternativa de flechas de principio a fin. Hasta las pruebas hay cinco ramas: A–B–C–D, A–B–C–E, A–B–C–I, F–G–I y F–H. Después de las pruebas hay dos: K–M–N y L–M–N. Hay **5 × 2 = 10 caminos**. Solo uno tiene 17 semanas.

| N.º | Camino (del inicio al cierre) | Duración (sem.) | Crítico |
| --- | --- | --- | --- |
| 1 | A → B → C → D → J → K → M → N | 16 | No |
| 2 | A → B → C → D → J → L → M → N | 17 | Sí |
| 3 | A → B → C → E → J → K → M → N | 14 | No |
| 4 | A → B → C → E → J → L → M → N | 15 | No |
| 5 | A → B → C → I → J → K → M → N | 14 | No |
| 6 | A → B → C → I → J → L → M → N | 15 | No |
| 7 | F → G → I → J → K → M → N | 15 | No |
| 8 | F → G → I → J → L → M → N | 16 | No |
| 9 | F → H → J → K → M → N | 14 | No |
| 10 | F → H → J → L → M → N | 15 | No |

Un camino de 14 semanas no autoriza a terminar todo el proyecto en 14: en las convergencias hay que esperar también a las otras ramas. La duración del proyecto es la del camino más largo. Los 10 caminos se cuentan con las dependencias explícitas del caso, sin agregar flechas redundantes ni actividades ficticias de costo.

### Paso 4. Diagrama de Gantt — consigna 4

Para ubicar una barra, usamos el inicio y el fin tempranos ya calculados. Una actividad con ES = 5 y EF = 9 ocupa las semanas **6, 7, 8 y 9**. No ocupa la semana 5: esa semana termina precisamente en el instante 5.

![Gantt del proyecto: actividades, escala semanal, corte y fecha límite](assets/schedule_gantt.svg)

| ID | Semanas de ejecución | Costo/semana (USD) |
| --- | --- | --- |
| A | 1–2 | 6.000 |
| B | 3–3 | 4.000 |
| C | 4–5 | 9.500 |
| D | 6–9 | 7.500 |
| E | 6–7 | 8.000 |
| F | 1–2 | 7.500 |
| G | 3–6 | 8.000 |
| H | 3–7 | 8.000 |
| I | 7–8 | 5.000 |
| J | 10–11 | 7.000 |
| K | 12–12 | 2.000 |
| L | 12–13 | 4.000 |
| M | 14–16 | 12.000 |
| N | 17–17 | 3.000 |

La nueva tienda termina su puesta en producción al cierre de la semana 13; la app está publicada al cierre de la 12. La campaña puede empezar en la **14**, ocupa 14–16 y la presentación se realiza en la **17**. No se inicia la publicidad solo porque la app ya esté publicada: también se necesita la tienda operativa.

### Paso 5. Gantt de costos, Curva S y presupuesto — consigna 5

#### 5.1. Cálculo de los gastos de estructura

Antes del inicio de campaña transcurren 13 semanas: **13 × 3.000 = USD 39.000**. Desde que empieza la campaña hasta el cierre hay cuatro semanas, las 14–17: **4 × 1.500 = USD 6.000**.

**Estructura total = 39.000 + 6.000 = USD 45.000.**

**BAC = 241.000 de actividades + 45.000 de estructura = USD 286.000.**

No se cobran 18 semanas de estructura: 18 es el límite permitido, mientras que el plan termina en 17. Tampoco se baja la tarifa desde el fin de la campaña: el caso dice que baja desde su inicio.

#### 5.2. Distribución por semana

Para cada actividad dividimos costo / duración y colocamos ese importe en cada semana activa. Después sumamos por columna y acumulamos de izquierda a derecha. En las tablas, **— significa costo planificado cero**; los números están en USD. Se divide en dos paneles para conservar la legibilidad, como hace la clase de costos en páginas 13–14 [T2].

**Semanas 1 a 9.**

| Actividad / USD | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | 6.000 | 6.000 | — | — | — | — | — | — | — |
| B | — | — | 4.000 | — | — | — | — | — | — |
| C | — | — | — | 9.500 | 9.500 | — | — | — | — |
| D | — | — | — | — | — | 7.500 | 7.500 | 7.500 | 7.500 |
| E | — | — | — | — | — | 8.000 | 8.000 | — | — |
| F | 7.500 | 7.500 | — | — | — | — | — | — | — |
| G | — | — | 8.000 | 8.000 | 8.000 | 8.000 | — | — | — |
| H | — | — | 8.000 | 8.000 | 8.000 | 8.000 | 8.000 | — | — |
| I | — | — | — | — | — | — | 5.000 | 5.000 | — |
| J | — | — | — | — | — | — | — | — | — |
| K | — | — | — | — | — | — | — | — | — |
| L | — | — | — | — | — | — | — | — | — |
| M | — | — | — | — | — | — | — | — | — |
| N | — | — | — | — | — | — | — | — | — |
| Estructura | 3.000 | 3.000 | 3.000 | 3.000 | 3.000 | 3.000 | 3.000 | 3.000 | 3.000 |
| **Costo semanal** | 16.500 | 16.500 | 23.000 | 28.500 | 28.500 | 34.500 | 31.500 | 15.500 | 10.500 |
| **Costo acumulado** | 16.500 | 33.000 | 56.000 | 84.500 | 113.000 | 147.500 | 179.000 | 194.500 | 205.000 |

**Semanas 10 a 17.**

| Actividad / USD | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | — | — | — | — | — | — | — | — |
| B | — | — | — | — | — | — | — | — |
| C | — | — | — | — | — | — | — | — |
| D | — | — | — | — | — | — | — | — |
| E | — | — | — | — | — | — | — | — |
| F | — | — | — | — | — | — | — | — |
| G | — | — | — | — | — | — | — | — |
| H | — | — | — | — | — | — | — | — |
| I | — | — | — | — | — | — | — | — |
| J | 7.000 | 7.000 | — | — | — | — | — | — |
| K | — | — | 2.000 | — | — | — | — | — |
| L | — | — | 4.000 | 4.000 | — | — | — | — |
| M | — | — | — | — | 12.000 | 12.000 | 12.000 | — |
| N | — | — | — | — | — | — | — | 3.000 |
| Estructura | 3.000 | 3.000 | 3.000 | 3.000 | 1.500 | 1.500 | 1.500 | 1.500 |
| **Costo semanal** | 10.000 | 10.000 | 9.000 | 7.000 | 13.500 | 13.500 | 13.500 | 4.500 |
| **Costo acumulado** | 215.000 | 225.000 | 234.000 | 241.000 | 254.500 | 268.000 | 281.500 | 286.000 |

Ejemplo de lectura, **semana 6**: catálogo 7.500 + clientes 8.000 + web 8.000 + app 8.000 + estructura 3.000 = **USD 34.500**. Hasta la semana 5 se acumularon USD 113.000; por tanto, al cierre de la 6 se acumulan 113.000 + 34.500 = **USD 147.500**. Esa será la referencia planificada del corte, no el presupuesto completo.

En semana 7 ya no se planifica web: aparecen la segunda semana de clientes, la última de app y la primera de integración. El flujo semanal cambia porque cambia el conjunto de tareas activas, no porque se haya modificado arbitrariamente una tarifa.

#### 5.3. Curva S

![Curva S de costos acumulados, con referencia al corte de semana 6 y cierre](assets/cost_baseline.svg)

El eje horizontal muestra el cierre de cada semana y el vertical el costo planificado acumulado en USD. Se parte de cero y se llega a USD 286.000. Esta curva permite leer qué valor de trabajo debía estar programado al corte. No se reemplaza por una recta de 286.000 / 17 por semana: las actividades no tienen el mismo costo ni ocurren simultáneamente durante todo el proyecto.

### Paso 6. Situación al cierre de la semana 6 — consigna 6

#### 6.1. Primero convertir el relato en avances comparables

Al instante 6, A, B, C y F deberían estar y están terminadas. D empezó en el instante 5 y lleva una de cuatro semanas: su avance planificado es **25 %**. Como se migraron 12.000 de 60.000 productos, su avance real es **20 %**. Su gasto real es 12.000 × USD 0,60 = **USD 7.200**; su valor ganado usa el presupuesto de USD 0,50: 12.000 × 0,50 = **USD 6.000**.

E lleva planificada una de sus dos semanas: **50 %**, pero tiene **40 % real**. G debía terminar en el instante 6: **100 % planificado**, frente al **75 % real**. H ocupa 2–7: al corte completó cuatro de cinco semanas y, por avanzar según el plan, tiene **80 % planificado y real**.

I comienza en el instante 6, es decir, al **inicio de la semana 7**. Al cierre de la 6 tiene avance planificado cero. Que todavía no haya comenzado no es por sí solo un atraso al corte; el retraso de G sí pone en riesgo su inicio. J, K, L, M y N tampoco tenían trabajo previsto aún.

#### 6.2. Presupuesto, valor ganado y gasto por actividad

Cada fila aplica las mismas reglas: PV usa el avance planificado; EV, el avance real sobre el costo presupuestado; AC, el gasto informado. CV y SV permiten localizar qué actividad aporta cada desvío. En “Estructura”, los USD 18.000 corresponden al soporte de las seis semanas transcurridas, bajo el supuesto de nivel de esfuerzo explicado antes.

| ID | Plan al corte | Real al corte | PV (USD) | EV (USD) | AC (USD) | CV (USD) | SV (USD) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | 100% | 100% | 12.000 | 12.000 | 13.000 | -1.000 | 0 |
| B | 100% | 100% | 4.000 | 4.000 | 4.000 | 0 | 0 |
| C | 100% | 100% | 19.000 | 19.000 | 22.000 | -3.000 | 0 |
| D | 25% | 20% | 7.500 | 6.000 | 7.200 | -1.200 | -1.500 |
| E | 50% | 40% | 8.000 | 6.400 | 7.000 | -600 | -1.600 |
| F | 100% | 100% | 15.000 | 15.000 | 14.000 | 1.000 | 0 |
| G | 100% | 75% | 32.000 | 24.000 | 30.000 | -6.000 | -8.000 |
| H | 80% | 80% | 32.000 | 32.000 | 36.000 | -4.000 | 0 |
| I | 0% | 0% | 0 | 0 | 0 | 0 | 0 |
| J | 0% | 0% | 0 | 0 | 0 | 0 | 0 |
| K | 0% | 0% | 0 | 0 | 0 | 0 | 0 |
| L | 0% | 0% | 0 | 0 | 0 | 0 | 0 |
| M | 0% | 0% | 0 | 0 | 0 | 0 | 0 |
| N | 0% | 0% | 0 | 0 | 0 | 0 | 0 |
| Estructura | 6 sem. | 6 sem. | 18.000 | 18.000 | 18.000 | 0 | 0 |
| **Total** | — | — | 147.500 | 136.400 | 151.200 | -14.800 | -11.100 |

Sumas desarrolladas para comprobar:

**PV = 12.000 + 4.000 + 19.000 + 7.500 + 8.000 + 15.000 + 32.000 + 32.000 + 18.000 = USD 147.500.**

**EV = 12.000 + 4.000 + 19.000 + 6.000 + 6.400 + 15.000 + 24.000 + 32.000 + 18.000 = USD 136.400.**

**AC = 13.000 + 4.000 + 22.000 + 7.200 + 7.000 + 14.000 + 30.000 + 36.000 + 18.000 = USD 151.200.**

#### 6.3. Variaciones e índices, con interpretación

- **CV = 136.400 − 151.200 = −USD 14.800.** El trabajo realizado costó 14.800 más que su valor presupuestado. No es la diferencia entre gasto y plan temporal.
- **SV = 136.400 − 147.500 = −USD 11.100.** Falta trabajo que a esta fecha debía haber ganado 11.100 de presupuesto. Se expresa en dinero, no en semanas.
- **CPI = 136.400 / 151.200 = 0,902116… ≈ 0,9021.** Cada USD 1 gastado generó aproximadamente USD 0,9021 de trabajo presupuestado.
- **SPI = 136.400 / 147.500 = 0,924745… ≈ 0,9247.** Se ganó aproximadamente el 92,47 % del valor que debía haberse ganado al corte.

Ambos índices son menores que 1: el proyecto está desfavorable en costo y en avance valorizado. Comparar solo AC − PV = 151.200 − 147.500 = **USD 3.700** subestimaría el problema de eficiencia: hay trabajo previsto que todavía no se realizó.

La suma del atraso valorizado es **1.500 en catálogo + 1.600 en clientes + 8.000 en web = USD 11.100**. La suma de los desvíos de costo es **−1.000 arquitectura −3.000 infraestructura −1.200 catálogo −600 clientes +1.000 rediseño −6.000 web −4.000 app = −USD 14.800**. El ahorro del rediseño compensa una parte de los sobrecostos, no los elimina.

![Control al cierre de semana 6: comparación PV, EV y AC; variaciones; índices](assets/earned_value_control.svg)

No se dibujan curvas reales históricas de EV y AC: el caso solo da el estado acumulado al cierre de la semana 6. Los gráficos comparan ese corte, como el gráfico de barras de la clase 6, página 14. Interpolar una historia real semana por semana inventaría datos.

#### 6.4. Qué compromete la fecha final

**Catálogo D: prioridad por estar en el camino crítico.** Debían haberse migrado 15.000 productos y se migraron 12.000: faltan 3.000 frente al plan. Su holgura interna es cero. Para cerrar al final de la semana 9 quedan tres semanas y 48.000 productos: se necesitarían **16.000 productos por semana**, por encima tanto del ritmo observado de 12.000 como del nominal de 15.000. Esa capacidad adicional exige validar recursos, herramienta y costo; no se la supone gratis.

Si después del corte se recuperara el ritmo nominal de 15.000 por semana, faltarían 48.000 / 15.000 = **3,2 semanas**: D terminaría en 9,2 y, manteniendo el resto de duraciones, el proyecto terminaría en **17,2**. Si se mantuviera el ritmo observado de 12.000 por semana, faltarían cuatro semanas: D terminaría en **10** y el proyecto en **18**. Ambos son escenarios condicionados; el segundo consume todo el margen frente al Directorio. Si la ejecución solo admite planificación en semanas enteras, el primer escenario se redondearía operativamente hacia el cierre de la semana 10.

**Web G: atraso en una rama con solo una semana de holgura.** Su plan era terminar en 6 y llega al 75 %. Si el 25 % restante se completa en una semana adicional al ritmo original, G termina en 7; I pasa a 7–9 y todavía llega a J en 9. Así consume el margen compartido de G e I, sin retrasar por sí sola el fin base. No se suman sus holguras como dos semanas disponibles. Si el cierre web supera el instante 7, esa rama empezará a desplazar las pruebas, salvo otra recuperación.

**Clientes E:** está por debajo del avance previsto, pero tiene dos semanas de holgura total. Al corte, con 60 % pendiente, debe terminar antes del instante 9 para no desplazar J. Puede comprometer la fecha si empeora; el 40 % informado no basta para declarar por sí solo un atraso del cierre.

**App H:** tiene 80 % real y planificado; no aporta atraso de valor ganado, aunque sí USD 4.000 de sobrecosto. Le resta una semana al ritmo previsto y tiene dos semanas de holgura interna. A, B, C y F ya finalizaron, por lo que no causarán nuevos atrasos de terminación, salvo retrabajo no informado.

**Acción propuesta:** revisar primero capacidad y calidad de migración del catálogo; asegurar el cierre del 25 % pendiente de web y preparar la integración; comprobar que clientes termine antes de pruebas. Registrar cualquier recuperación con recursos, riesgo y costo. No cambiar las dependencias obligatorias de seguridad ni lanzar campaña antes de ambas publicaciones para aparentar cumplimiento.

### Paso 7. Costo final, dinero restante y eficiencia requerida — consigna 7

Aplicamos el método de continuidad del CPI que enseña la clase. Aunque mostremos cuatro decimales en la explicación, para calcular se usa la fracción exacta **136.400 / 151.200**.

**EAC = BAC / CPI = 286.000 / (136.400 / 151.200) = USD 317.032,26.**

Es el costo total proyectado si persiste la eficiencia actual. **No** es el dinero adicional que falta gastar: incluye lo ya consumido.

**ETC = EAC − AC = 317.032,258064… − 151.200 = USD 165.832,26.**

Este es el dinero que se estima necesario para terminar desde el corte. Comprobación equivalente: trabajo pendiente a presupuesto = BAC − EV = 286.000 − 136.400 = **USD 149.600**. Si cuesta más producirlo por la ineficiencia observada, ETC = 149.600 / CPI = **USD 165.832,26**.

**VAC = BAC − EAC = 286.000 − 317.032,258064… = −USD 31.032,26.**

Se proyecta un exceso total de **USD 31.032,26**, aproximadamente **10,85 %** del presupuesto original. Este exceso es distinto de los USD 165.832,26 que faltan gastar.

Para terminar dentro del presupuesto todavía quedarían **BAC − AC = 286.000 − 151.200 = USD 134.800**. Con ese dinero habría que producir USD 149.600 de trabajo presupuestado:

**TCPI = (BAC − EV) / (BAC − AC) = 149.600 / 134.800 = 1,109792… ≈ 1,1098.**

El trabajo restante tendría que generar aproximadamente USD 1,1098 de valor presupuestado por cada dólar gastado, frente a los USD 0,9021 logrados hasta ahora. Es una mejora relativa de eficiencia de aproximadamente **23,02 %**: (1,109792… / 0,902116… − 1) × 100. El índice mayor que 1 expresa una exigencia futura; no significa que ya se esté logrando esa eficiencia. El cálculo no prueba que la mejora sea factible.

| Pregunta de gestión | Resultado |
| --- | --- |
| ¿Cuánto estaba presupuestado para todo el proyecto? | USD 286.000 |
| ¿Cuánto se estima que costará todo si sigue la eficiencia actual? | USD 317.032,26 |
| ¿Cuánto falta gastar en ese escenario? | USD 165.832,26 |
| ¿Cuánto dinero queda dentro del presupuesto original? | USD 134.800 |
| ¿Cuánto excedería el costo total al presupuesto? | USD 31.032,26 |
| ¿Qué eficiencia se necesitaría de ahora en adelante para respetarlo? | TCPI = 1,1098 |

**Límite del pronóstico:** el EAC no calcula automáticamente una nueva fecha ni agrega por separado las semanas adicionales de estructura. Ya extrapola la ineficiencia global. Si se construye un nuevo cronograma operativo, habrá que reestimar sus costos restantes, incluidas las nuevas semanas de estructura, y reconciliar ese pronóstico con este. No se deben sumar indiscriminadamente ambos modelos, porque podría duplicarse el efecto del atraso.

### Paso 8. Matriz RACIS — consigna 8

Se usan exactamente los seis roles pedidos y las ocho actividades indicadas. **— significa que el caso no asigna una participación para esa combinación**, no que la persona tenga prohibido intervenir. El equipo ejecutor se representa bajo su líder, pues son las columnas requeridas.

| Actividad | Gerente General | Director/a del Proyecto | Líder de Infraestructura Cloud | Líder de Desarrollo | Seguridad Informática | Gerencia Comercial y de Marketing |
| --- | --- | --- | --- | --- | --- | --- |
| A · Arquitectura | I | A | R | C | C | — |
| B · Contratación | S | A | R | — | C | — |
| D · Catálogo | — | A | R | I | — | C |
| H · App | — | A | I | R | C | C |
| J · Pruebas | — | A | C | R | S | I |
| L · Producción | S | A | R | C | — | I |
| M · Campaña | A | C | — | C | — | R |
| N · Resultados | A | R | I | I | I | C |

Lectura razonada de cada fila:

1. **Arquitectura A:** Infraestructura ejecuta; el director del proyecto rinde cuentas por la regla general. Desarrollo y Seguridad aportan requisitos; el gerente recibe el diseño final. No se inventa una firma sobre ese diseño.
2. **Contratación B:** Infraestructura negocia y ejecuta. El director del proyecto conserva A. Seguridad revisa las cláusulas y es C. El gerente tiene S porque sin su firma el contrato no vale; S no reemplaza a A.
3. **Catálogo D:** Infraestructura ejecuta. Comercial y Marketing valida precios y descripciones como C; Desarrollo recibe el avance como I. El director del proyecto tiene A.
4. **App H:** Desarrollo ejecuta. Comercial y Marketing opina sobre funcionalidades y Seguridad sobre autenticación: ambos C. Infraestructura recibe requerimientos de capacidad: I. El director del proyecto mantiene A.
5. **Pruebas J:** Desarrollo ejecuta; Infraestructura es C y Comercial y Marketing recibe resultados como I. Seguridad tiene S por el certificado obligatorio, sin agregarle R o A que el relato no le asigna. El director del proyecto es A.
6. **Puesta en producción L:** Infraestructura ejecuta, Desarrollo es C y Comercial y Marketing es I. El gerente firma el acta: S. El director del proyecto sigue como A.
7. **Campaña M:** Comercial y Marketing ejecuta con su agencia, representada en esa misma columna. **El gerente general es A**, por la excepción explícita del caso; el director del proyecto y Desarrollo son C para coordinar fechas y capacidad. No se agrega una firma comercial que no fue requerida.
8. **Presentación N:** el director del proyecto prepara y expone: **R**. **El gerente general es A** ante el Directorio. Comercial y Marketing aporta métricas: C. Los tres responsables técnicos reciben el informe final: I.

Comprobación: cada fila tiene exactamente **un A** y al menos **un R**. Solo hay S en contratación, pruebas y puesta en producción, donde el caso pide contrato, certificado y acta firmados. El Directorio recibe la presentación, pero no se agrega como séptima columna porque la consigna requiere seis roles.

## 4. Comprobaciones y preguntas para estudiar

### 4.1. Verificaciones realizadas

- Se preservó el PDF original sin alterar su contenido; los datos se contrastaron con sus tres páginas.
- Las duraciones, dependencias y costos se calcularon por actividad. Se verificó que cada sucesora empiece después del fin temprano de todas sus predecesoras y que las dos fórmulas de holgura coincidan.
- Se enumeraron los 10 caminos completos y se sumó su duración independientemente del recorrido de tiempos. Uno alcanza 17 semanas y coincide con las ocho actividades de holgura cero.
- Cada fila de costos semanales suma su costo completo; la estructura suma 45.000; los costos directos suman 241.000; el último acumulado es 286.000. El acumulado de semana 6 coincide con el PV de 147.500 calculado por avances.
- Se calcularon importes e índices con aritmética racional, sin redondeo intermedio. Se comprobó AC + ETC = EAC y BAC − EAC = VAC.
- Se revisó que cada fila RACIS tenga un único A, al menos un R y firmas respaldadas por la consigna.
- Se compararon visualmente los moldes originales de nodos, Gantt, flujo de costos y matriz con los usados aquí. Se revisó la versión HTML renderizada, sus fórmulas, gráficos, tablas y navegación. Las tablas anchas admiten desplazamiento horizontal para conservar tamaño de lectura.

### 4.2. Preguntas para comprobar comprensión

**¿Por qué la campaña no empieza en semana 13 si la app ya está publicada?** Porque falta terminar la puesta en producción de la tienda, que ocupa también la semana 13. La campaña necesita ambas condiciones y empieza en la 14.

**¿Por qué no se usa el costo real de USD 0,60 para calcular el EV del catálogo?** Porque EV debe valorar la producción real con el presupuesto aprobado de USD 0,50. Usar el costo real borraría justamente la comparación de eficiencia.

**¿Por qué la web explica más atraso monetario, pero el catálogo merece prioridad de plazo?** Porque el monto del trabajo pendiente no equivale al impacto temporal. Web conserva un margen limitado en su rama; catálogo está en el camino crítico y no tiene holgura interna.

**¿La semana libre frente al Directorio hace que las tareas críticas tengan holgura interna uno?** No bajo el cálculo presentado: su referencia es el fin base en 17. La semana adicional es margen respecto del límite externo de 18.

**¿Se puede concluir que el proyecto terminará en 17 / 0,9247 semanas?** No. El SPI agrega avance valorizado y no actualiza la lógica, los ritmos ni la ruta crítica. Hay que recalcular las actividades pendientes con sus dependencias.

**¿Por qué la estructura tiene EV si la migración va atrasada?** Porque se adoptó una medición de soporte por tiempo de servicio prestado, distinta del avance de productos migrados. Está explicitada; no se usa para afirmar que el trabajo técnico está al día.

**¿Firmar la contratación convierte al gerente en A?** No. S y A son responsabilidades distintas. El texto mantiene al director del proyecto como A salvo las excepciones expresas de campaña y presentación.

**¿Un pronóstico mayor que el presupuesto autoriza a gastar más?** No. Revela la necesidad de una decisión: evaluar recuperación, riesgos, recursos y autorización de cambios. El BAC permanece como referencia hasta que se apruebe modificarlo.

## 5. Fuentes y trazabilidad

Los números de página siguientes corresponden a la posición de página del PDF original, contada desde 1. Los originales se consultaron para las definiciones y fórmulas, y se inspeccionaron visualmente los modelos utilizados. Los párrafos explicativos y mini ejemplos didácticos son elaboración de esta resolución.

- **[E] Consigna:** [Ejercicio DPI: Migración del e-commerce de Hogar Norte](Ejercicio_DPI_Migracion_Ecommerce_Hogar_Norte.pdf). Página 1: contexto, infraestructura, migraciones y diseño; página 2: desarrollos, integración, pruebas, publicación, campaña, cierre y estructura; página 3: estado en semana 6 y consignas 6–8.
- **[T1] Plazos:** [04_DPI_Clase4_Dominio_Planificacion_Plazos.pdf](../../theory/course_material/04_DPI_Clase4_Dominio_Planificacion_Plazos.pdf). Páginas 7–9: actividad e hito; 16 y 18: red y dependencias; 19 y 21: formato de nodo y holgura; 26–28: camino crítico y recorridos; 29–30: Gantt. Se inspeccionaron los diseños de las páginas 19, 21, 26, 29 y 30.
- **[T2] Costos:** [05_DPI_Clase5_Dominio_Planificacion_Costos.pdf](../../theory/course_material/05_DPI_Clase5_Dominio_Planificacion_Costos.pdf). Páginas 8–11: estimaciones, tipos de costo, análoga, paramétrica y PERT; 13–14: matriz de flujo por actividad y período; 16–18: línea base y reservas; 20–22: distribución lineal y Curva S. Se inspeccionaron visualmente las páginas 13, 20 y 21.
- **[T3] Medición:** [06_DPI_Clase6_EVM_Medicion.pdf](../../theory/course_material/06_DPI_Clase6_EVM_Medicion.pdf). Páginas 9–12: EVM, PV, EV y AC; 14: gráfico comparativo al corte; 15: CV y SV; 17–18: índices e interpretación; 20–23: BAC, EAC, ETC, VAC y TCPI. Se inspeccionó visualmente el gráfico de página 14. El supuesto de medición de estructura por nivel de esfuerzo se declara para este caso y no se atribuye a una explicación específica de esa clase.
- **[T4] Responsabilidades:** [08-09_DPI_Clases08y00_Equipo_e_Interesados.pdf](../../theory/course_material/08-09_DPI_Clases08y00_Equipo_e_Interesados.pdf). Páginas 20–21: letras RACIS y organización de filas y columnas; 24: reglas de validación; 25: ejemplo del curso. Se inspeccionó visualmente la estructura de la página 21.
- **Criterio docente complementario:** [devolución de la entrega 2](../../submissions/submission_2/feedback.md), puntos 2, 3 y 6: distinguir red y calendario, justificar reducciones y conservar el orden ES | LS | EF | LF con holgura debajo.

No se trasladaron a este ejercicio los porcentajes de reservas ni los montos del ejemplo de Home Banking de las clases. Tampoco se trasladó la incertidumbre pendiente del ejercicio Ruta 40 Bikes: este PDF sí contiene datos de control suficientes para resolver el corte, bajo los supuestos documentados.
