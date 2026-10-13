# Ruta 40 Bikes: resolución del ejercicio auxiliar

## Alcance y fuentes verificadas

Esta resolución usa como consigna el [PDF del caso, páginas 2 y 3](<Clase_07_Ruta 40 Bikes.pdf>) y como evidencia de ubicación la [planilla de la Clase 07, hoja `Ruta 40 Bikes - Clase 07`, celdas A4:F20](Ruta40Bikes_Clase07_Ubicacion.xlsx). La planilla informa que las respuestas de los pasos 1 a 7 estaban en las notas del PowerPoint original, pero ese archivo no está disponible en el repositorio.

Las definiciones y convenciones se verificaron visualmente en los originales de la cátedra:

- Red AON, camino crítico, holgura y Gantt: [Clase 04, páginas 16, 20 y 26 a 30](<../../theory/course_material/04_DPI_Clase4_Dominio_Planificacion_Plazos.pdf>).
- Estimación análoga, paramétrica y PERT; Gantt de costos, reservas y Curva S: [Clase 05, páginas 10, 11, 13, 16, 17 y 20](<../../theory/course_material/05_DPI_Clase5_Dominio_Planificacion_Costos.pdf>).
- PV, EV, AC, CV, SV, CPI, SPI, BAC, EAC, VAC y TCPI: [Clase 06, páginas 10 a 12, 15, 17 y 20 a 23](<../../theory/course_material/06_DPI_Clase6_EVM_Medicion.pdf>).

> **Límite de la fuente.** La consigna no indica el porcentaje o monto de la reserva que debe marcarse en la Curva S y tampoco aporta el estado real de avance ni los costos reales al cierre de la semana 6. Por eso los pasos 1 a 4 y el PV del paso 6 tienen resultado numérico definitivo; el tope con reserva, EV, AC y los índices del paso 7 se presentan como fórmulas o escenarios explícitamente condicionales. No se inventan datos faltantes.

## 1. Introducción teórica

### Cronograma: qué representa una red AON

Un proyecto se divide en **actividades**, es decir, trabajos concretos que consumen tiempo. Por ejemplo, “relevar requerimientos” y “configurar la plataforma” son dos actividades. Cada actividad tiene una **duración** y puede depender de que otra termine antes. La actividad que debe ocurrir primero se llama **predecesora**.

Una **red AON** permite ver ese orden. AON es la sigla en inglés de *Activity on Node*, que significa “actividad en el nodo”. La Clase 04 la define como una representación gráfica de las relaciones lógicas entre actividades:

- Cada rectángulo o **nodo** representa una actividad.
- Cada flecha indica una dependencia y se lee de izquierda a derecha.
- En este ejercicio todas las dependencias son **Final-Inicio**: la actividad ubicada después de la flecha solo puede comenzar cuando termina la anterior.

Por ejemplo, `A → C` significa que primero debe completarse A, el relevamiento, y recién después puede comenzar C, la configuración de la plataforma.

### Cómo se calcula el cronograma

El **método del camino crítico**, abreviado CPM por su nombre en inglés *Critical Path Method*, busca responder dos preguntas:

1. ¿Cuál es la fecha más temprana en que puede hacerse cada actividad?
2. ¿Cuánto puede demorarse cada actividad sin atrasar la fecha final del proyecto?

Para contestar la primera pregunta se recorre la red desde el inicio hacia el final. Este recorrido se llama **paso hacia adelante**:

- `ES` (*Early Start*) o **inicio temprano**: primer momento en que una actividad puede comenzar, una vez terminadas todas sus predecesoras.
- `EF` (*Early Finish*) o **fin temprano**: primer momento en que puede terminar. Se calcula como `EF = ES + duración`.

La escala empieza en el instante 0. Por eso, si A dura 2 semanas, tiene `ES = 0` y `EF = 2`: ocupa las semanas 1 y 2. Como C depende de A, C recién puede comenzar en el instante 2.

Para contestar la segunda pregunta se recorre la red desde el final hacia el inicio. Este recorrido se llama **paso hacia atrás**:

- `LF` (*Late Finish*) o **fin tardío**: último momento en que una actividad puede terminar sin atrasar el proyecto.
- `LS` (*Late Start*) o **inicio tardío**: último momento en que puede comenzar sin atrasar el proyecto. Se calcula como `LS = LF - duración`.

La **holgura** es el margen disponible para demorar una actividad sin cambiar la fecha final:

```text
Holgura = inicio tardío - inicio temprano = LS - ES
```

Si una actividad tiene holgura 1, podría comenzar una semana después de su inicio temprano sin atrasar el proyecto. Si su holgura es 0, no tiene margen. La secuencia conectada de actividades con holgura cero se denomina **camino crítico**: determina la duración mínima del proyecto y cualquier atraso en una de esas actividades demora el final.

Finalmente, un **diagrama de Gantt** toma ese cronograma y lo dibuja sobre un calendario: cada fila es una actividad, cada columna es una semana y cada barra muestra cuándo se ejecuta el trabajo.

### Costos y técnicas de estimación

**Estimar un costo** significa calcular, antes de ejecutar el trabajo, cuánto dinero probablemente requerirá una actividad. La Clase 05 distingue tres técnicas aplicables al caso:

- **Análoga:** usa el costo histórico de una actividad o proyecto similar. Si un relevamiento comparable costó USD 3.000, ese antecedente sirve como estimación del nuevo relevamiento.
- **Paramétrica:** multiplica una cantidad por una tarifa o costo unitario. Por ejemplo, 24 pantallas a USD 150 cada una cuestan `24 × 150 = USD 3.600`.
- **Multipunto PERT:** PERT es la sigla en inglés de *Program Evaluation and Review Technique*. Esta técnica se usa cuando un único valor sería demasiado incierto. Combina tres escenarios: `O`, costo optimista si todo resulta favorable; `M`, costo más probable; y `P`, costo pesimista si aparecen dificultades. El valor más probable recibe cuatro veces más peso:

```text
Costo PERT = (O + 4 × M + P) / 6
```

Un **Gantt de costos** combina el calendario con el presupuesto. Cada fila sigue siendo una actividad, pero en cada semana se muestra cuánto costo planificado le corresponde. La cátedra adopta una simplificación pedagógica: repartir el costo total de una actividad en partes iguales durante sus semanas activas. El **costo fijo** de USD 500 no depende de una actividad particular; corresponde a licencia y coordinación y se agrega una vez en cada semana hasta la finalización.

El **costo semanal** es lo planificado para una semana. El **costo acumulado** suma esa semana y todas las anteriores. Al graficar el acumulado contra el tiempo se obtiene la **Curva S**, que permite leer cuánto presupuesto debería haberse consumido en cada fecha.

La **reserva para contingencias** es dinero previsto para responder a riesgos ya identificados y forma parte de la **línea base de costos**, es decir, el presupuesto autorizado distribuido en el tiempo contra el cual se controla el proyecto. La **reserva de gestión** cubre trabajo imprevisto dentro del alcance y se mantiene fuera de esa línea base. Como la consigna no fija ninguna tasa, no corresponde adoptar automáticamente el 10 % utilizado en otro ejemplo de la Clase 05.

### Valor Ganado (EVM)

El **Método del Valor Ganado**, abreviado EVM por *Earned Value Management*, integra alcance, tiempo y costo en una misma medición. No compara simplemente “lo gastado” con “lo planificado”: primero traduce el avance físico a dinero presupuestado para que las magnitudes sean comparables.

En una fecha de corte, como el final de la semana 6, se observan tres valores básicos:

- `PV` (*Planned Value*) o **valor planificado**: cuánto debería valer, según el presupuesto, el trabajo programado hasta la fecha. Se calcula como `Σ(costo presupuestado × porcentaje planificado)`.
- `EV` (*Earned Value*) o **valor ganado**: cuánto vale, según el presupuesto, el trabajo que realmente se completó. Se calcula como `Σ(costo presupuestado × porcentaje real)`. No es el dinero gastado.
- `AC` (*Actual Cost*) o **costo real**: cuánto se gastó efectivamente hasta la misma fecha, según facturas, horas y otros registros. No se calcula a partir de PV o EV.

Con esos tres valores se miden los desvíos:

- `CV` (*Cost Variance*) o **variación de costo**: `CV = EV - AC`. Un resultado negativo significa que el trabajo realizado costó más que su valor presupuestado.
- `SV` (*Schedule Variance*) o **variación de cronograma**: `SV = EV - PV`. Un resultado negativo significa que se completó menos trabajo valorizado que el previsto. Se expresa en dinero, no en semanas.
- `CPI` (*Cost Performance Index*) o **índice de desempeño del costo**: `CPI = EV / AC`. Indica cuánto valor presupuestado se obtiene por cada dólar gastado.
- `SPI` (*Schedule Performance Index*) o **índice de desempeño del cronograma**: `SPI = EV / PV`. Indica qué proporción del avance planificado se logró.

Para proyectar el cierre también se usan:

- `BAC` (*Budget at Completion*) o **presupuesto hasta la conclusión**: presupuesto aprobado para todo el trabajo medido, sin reservas.
- `EAC` (*Estimate at Completion*) o **estimación a la conclusión**: costo final pronosticado. Bajo el supuesto usado por la cátedra, `EAC = BAC / CPI`.
- `VAC` (*Variance at Completion*) o **variación a la conclusión**: diferencia esperada entre presupuesto y pronóstico, `VAC = BAC - EAC`.
- `TCPI` (*To-Complete Performance Index*) o **índice de desempeño del trabajo por completar**: eficiencia que debería alcanzarse en el trabajo restante para terminar en el BAC, `TCPI = (BAC - EV) / (BAC - AC)`.

La cátedra exige interpretar el SPI junto con el camino crítico: un desvío monetario de plazo no equivale por sí solo a semanas de atraso.

## 2. Método aplicado

1. Identificar actividades, duraciones, predecesoras y bases de costo.
2. Calcular cada costo con la técnica indicada por el relato.
3. Hacer el paso hacia adelante para obtener las fechas más tempranas y el paso hacia atrás para obtener los límites que no atrasan el proyecto.
4. Programar todas las actividades en sus inicios tempranos.
5. Prorratear linealmente cada costo y sumar USD 500 por semana.
6. Acumular los costos semanales para formar la Curva S.
7. En la semana 6, leer el PV de esa curva y calcular EV y AC solo si existen datos reales.
8. Calcular e interpretar los indicadores EVM sin redondear los índices intermedios.

Cada actividad recibe una letra de `A` a `H` como **identificador** (`ID`) para poder referirse a ella sin repetir su nombre completo. Las duraciones se expresan en semanas. `USD` significa dólares estadounidenses y es la unidad de todos los costos y variaciones monetarias.

## 3. Resolución

### Paso 1. Actividades y estimación de costos

| ID | Actividad | Duración | Predecesoras | Técnica | Cálculo del costo | Costo (USD) |
|---|---|---:|---|---|---:|---:|
| A | Relevamiento de requerimientos | 2 sem. | — | Análoga | Proyecto similar | 3.000 |
| B | Diseño UX/UI | 3 sem. | A | Paramétrica | 24 pantallas × 150 | 3.600 |
| C | Configuración de la plataforma | 4 sem. | A | PERT | `(6.000 + 4 × 8.000 + 12.400) / 6` | 8.400 |
| D | Campaña de prelanzamiento | 3 sem. | A | Paramétrica | 3 semanas × 800 | 2.400 |
| E | Carga del catálogo | 2 sem. | B | Paramétrica | 400 productos × 5 | 2.000 |
| F | Integración con la pasarela de pagos | 2 sem. | C | Paramétrica | 80 horas × 50 | 4.000 |
| G | Pruebas integrales | 2 sem. | E, F | Análoga | Tienda anterior | 3.000 |
| H | Lanzamiento y capacitación | 1 sem. | G, D | Análoga | Último lanzamiento | 1.600 |
| CF | Licencia de plataforma y coordinación | Toda la duración del proyecto | No aplica: costo de nivel de esfuerzo, no actividad AON | Costo fijo | 11 semanas × 500 | 5.500 |
|  | **Total de actividades secuenciables** |  |  |  |  | **28.000** |
|  | **Costo fijo del proyecto** |  |  |  |  | **5.500** |
|  | **BAC sin reservas** |  |  |  |  | **33.500** |

La fila `CF` se incluye para reconciliar el presupuesto completo. No aparece como nodo en la red AON porque no representa un trabajo que deba empezar o terminar después de otra actividad: es un costo de nivel de esfuerzo que se incurre durante todo el proyecto. Su duración final se conoce después de calcular el cronograma: 11 semanas.

Verificación de PERT para C:

```text
(6.000 + 4 × 8.000 + 12.400) / 6
= 50.400 / 6
= USD 8.400
```

### Paso 2. Red AON, ida, vuelta y camino crítico

Red lógica:

```text
Inicio → A ┬→ B → E ┐
           ├→ C → F ┼→ G → H → Fin
           └→ D ─────────→ H
```

La convergencia en G obliga a esperar tanto E como F. La convergencia en H obliga a esperar G y D. Cada nodo de la red debe leerse con el molde de la cátedra: encabezado `ID | duración`, nombre de la actividad, cuatro celdas de tiempo en el orden `ES | LS | EF | LF` y holgura debajo.

| ID | Predecesoras | Duración | ES | EF | LS | LF | Holgura | ¿Crítica? |
|---|---|---:|---:|---:|---:|---:|---:|---|
| A | — | 2 | 0 | 2 | 0 | 2 | 0 | Sí |
| B | A | 3 | 2 | 5 | 3 | 6 | 1 | No |
| C | A | 4 | 2 | 6 | 2 | 6 | 0 | Sí |
| D | A | 3 | 2 | 5 | 7 | 10 | 5 | No |
| E | B | 2 | 5 | 7 | 6 | 8 | 1 | No |
| F | C | 2 | 6 | 8 | 6 | 8 | 0 | Sí |
| G | E, F | 2 | 8 | 10 | 8 | 10 | 0 | Sí |
| H | G, D | 1 | 10 | 11 | 10 | 11 | 0 | Sí |

Representación textual del contenido de cada nodo, con el mismo orden de campos que el diagrama HTML:

```text
┌────────────── A | 2 semanas ──────────────┐
│ Relevamiento de requerimientos              │
├──── ES ────┬──── LS ────┬──── EF ────┬──── LF ────┤
│     0      │     0      │     2      │     2      │
├────────────────────────────────────────────┤
│ Holgura: 0 semana                           │
└────────────────────────────────────────────┘
```

El diagrama HTML repite ese molde para las ocho actividades; las críticas están en magenta y las no críticas en gris, como en la diapositiva de la Clase 04.

**Camino crítico:** `A → C → F → G → H`.

```text
Duración = 2 + 4 + 2 + 2 + 1 = 11 semanas
```

Las ramas `A → B → E` y `A → D` no dominan las convergencias. B y E tienen una semana de holgura; D tiene cinco.

### Paso 3. Diagrama de Gantt

Las barras `██` indican actividad planificada. Las actividades críticas están marcadas con `*`.

| ID | Actividad | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| A* | Relevamiento | ██ | ██ |  |  |  |  |  |  |  |  |  |
| B | Diseño UX/UI |  |  | ██ | ██ | ██ |  |  |  |  |  |  |
| C* | Configuración plataforma |  |  | ██ | ██ | ██ | ██ |  |  |  |  |  |
| D | Campaña prelanzamiento |  |  | ██ | ██ | ██ |  |  |  |  |  |  |
| E | Carga catálogo |  |  |  |  |  | ██ | ██ |  |  |  |  |
| F* | Pasarela de pagos |  |  |  |  |  |  | ██ | ██ |  |  |  |
| G* | Pruebas integrales |  |  |  |  |  |  |  |  | ██ | ██ |  |
| H* | Lanzamiento y capacitación |  |  |  |  |  |  |  |  |  |  | ██ |

### Paso 4. Gantt de costos y acumulado

Prorrateos semanales:

| ID | Costo total | Costo por semana activa |
|---|---:|---:|
| A | 3.000 | 1.500 |
| B | 3.600 | 1.200 |
| C | 8.400 | 2.100 |
| D | 2.400 | 800 |
| E | 2.000 | 1.000 |
| F | 4.000 | 2.000 |
| G | 3.000 | 1.500 |
| H | 1.600 | 1.600 |
| Fijo | 5.500 | 500 durante 11 semanas |

| Concepto / Semana | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A | 1.500 | 1.500 | — | — | — | — | — | — | — | — | — |
| B | — | — | 1.200 | 1.200 | 1.200 | — | — | — | — | — | — |
| C | — | — | 2.100 | 2.100 | 2.100 | 2.100 | — | — | — | — | — |
| D | — | — | 800 | 800 | 800 | — | — | — | — | — | — |
| E | — | — | — | — | — | 1.000 | 1.000 | — | — | — | — |
| F | — | — | — | — | — | — | 2.000 | 2.000 | — | — | — |
| G | — | — | — | — | — | — | — | — | 1.500 | 1.500 | — |
| H | — | — | — | — | — | — | — | — | — | — | 1.600 |
| Costo fijo | 500 | 500 | 500 | 500 | 500 | 500 | 500 | 500 | 500 | 500 | 500 |
| **Costo semanal** | **2.000** | **2.000** | **4.600** | **4.600** | **4.600** | **3.600** | **3.500** | **2.500** | **2.000** | **2.000** | **2.100** |
| **Costo acumulado** | **2.000** | **4.000** | **8.600** | **13.200** | **17.800** | **21.400** | **24.900** | **27.400** | **29.400** | **31.400** | **33.500** |

Comprobaciones:

```text
Costos de actividades = USD 28.000
Costo fijo = 11 semanas × USD 500 = USD 5.500
BAC = 28.000 + 5.500 = USD 33.500
Suma de costos semanales = USD 33.500
Último acumulado = USD 33.500
```

### Paso 5. Curva S y tope con reserva

La serie de la Curva S es el costo acumulado de la tabla anterior:

| Semana | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Acumulado (USD) | 0 | 2.000 | 4.000 | 8.600 | 13.200 | 17.800 | 21.400 | 24.900 | 27.400 | 29.400 | 31.400 | 33.500 |

El final de la curva sin reservas coincide con el BAC de USD 33.500.

Como la consigna no fija la reserva, el tope solo puede expresarse así:

```text
Reserva para contingencias = r × USD 33.500
Línea base con contingencia = USD 33.500 × (1 + r)
```

**Escenario ilustrativo, no dato de la consigna:** si la cátedra confirmara `r = 10 %`, la contingencia sería USD 3.350 y el tope de la línea base sería USD 36.850. Ese 10 % no se adopta como respuesta definitiva.

### Paso 6. Corte al final de la semana 6

#### PV verificable

Al finalizar la semana 6, el plan acumuló USD 21.400:

```text
PV6 = USD 21.400
```

Desglose del PV:

- A, B, C y D: 100 % planificado.
- E: 50 % planificado, porque lleva una de sus dos semanas.
- F, G y H: 0 % planificado.
- Costo fijo: seis semanas × USD 500 = USD 3.000.

```text
PV6 = 3.000 + 3.600 + 8.400 + 2.400 + (2.000 × 50 %) + 3.000
    = USD 21.400
```

#### EV y AC no determinables con los archivos disponibles

Para obtener EV se necesitan los porcentajes reales de avance a la semana 6. Para AC se necesitan los costos reales registrados al mismo corte. Ninguno de esos datos figura en la consigna visible.

Si el costo fijo se gestiona como nivel de esfuerzo y se gana por el mero transcurso del tiempo, la fórmula sería:

```text
EV6 = 3.000×%A + 3.600×%B + 8.400×%C + 2.400×%D
    + 2.000×%E + 4.000×%F + 3.000×%G + 1.600×%H
    + 3.000 de nivel de esfuerzo

AC6 = suma de costos reales de A a H al corte
    + licencia y coordinación realmente pagadas hasta la semana 6
```

La medición del costo fijo como nivel de esfuerzo es una hipótesis metodológica que debe confirmar la pauta original.

### Paso 7. Índices, pronóstico y lectura

Con `PV6 = USD 21.400` y `BAC = USD 33.500`, una vez conocidos `EV6` y `AC6` se calcula:

| Indicador | Fórmula en la semana 6 | Lectura |
|---|---|---|
| CV | `EV6 - AC6` | Negativo: sobrecosto |
| SV | `EV6 - 21.400` | Negativo: menor avance valorizado que el plan |
| CPI | `EV6 / AC6` | Menor que 1: ineficiencia de costo |
| SPI | `EV6 / 21.400` | Menor que 1: avance inferior al plan |
| EAC | `33.500 / CPI` | Pronóstico si continúa la eficiencia actual |
| VAC | `33.500 - EAC` | Negativo: sobrecosto proyectado |
| TCPI | `(33.500 - EV6) / (33.500 - AC6)` | Eficiencia necesaria para cerrar en el BAC |

No se redondean CPI o SPI antes de calcular EAC, VAC o TCPI.

La lectura de plazo debe volver a la red:

- Si el atraso real está en A, C, F, G o H, afecta directamente el plazo final porque son críticas.
- B y E disponen de una semana de holgura cada una.
- D dispone de cinco semanas de holgura; un atraso dentro de ese margen puede reducir el SPI sin modificar todavía la fecha final.

## 4. Verificación final

| Control | Resultado |
|---|---|
| PERT de configuración | USD 8.400 |
| Suma de costos de actividades | USD 28.000 |
| Duración CPM | 11 semanas |
| Camino crítico | A → C → F → G → H |
| Costo fijo total | USD 5.500 |
| BAC sin reservas | USD 33.500 |
| Acumulado final de la Curva S | USD 33.500 |
| PV al final de semana 6 | USD 21.400 |
| Tope con reserva | Pendiente de tasa o monto en la fuente |
| EV, AC e índices numéricos | Pendientes del estado real y costos reales |

La solución numérica disponible es internamente consistente: la red, el Gantt, el Gantt de costos y la Curva S cierran sobre 11 semanas y USD 33.500. Para cerrar los pasos 5 a 7 de manera definitiva se necesita recuperar las notas de las diapositivas 23 a 25 del archivo `07_DPI_Clase7_Ejercitacion_EVM_Reservas_Contingencia.pptx`, o recibir del docente la reserva, los porcentajes reales y los costos reales de la semana 6.
