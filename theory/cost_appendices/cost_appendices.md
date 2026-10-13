# Anexos de costos

Transcripción consolidada de los anexos gráficos sobre estimación, línea base, Curva S y Valor Ganado.

---

## 1. Del cronograma al control de costos en seis pasos

### Objetivo

Guiar al usuario paso a paso en el proceso para transformar la estimación de actividades en una línea base de costos y realizar un control financiero riguroso mediante Valor Ganado.

### Contexto

Procedimiento estructurado para proyectar y controlar los costos del proyecto **«Plataforma de Home Banking Digital»**, integrando alcance, tiempo y presupuesto.

### Paso 1: Estimar actividades

**BAC: USD 50.000**

Se aplica una técnica reconocida —análoga, paramétrica o PERT— a cada actividad hasta sumar un total base de USD 50.000.

> **Error frecuente:** confundir la estimación total (BAC) con la línea base de costos o con el presupuesto total.

### Paso 2: Estructurar reservas

**Línea base: USD 55.000**

Se añade un 10 % para contingencias, con lo que la línea base asciende a USD 55.000. Luego se agrega un 5 % de reserva de gestión sobre la línea base, dando un presupuesto total de USD 57.750.

| Componente | Cálculo | Importe |
|---|---:|---:|
| Estimación | Base | USD 50.000 |
| Contingencias | 10 % | USD 5.000 |
| Línea base de costos | Estimación + contingencias | USD 55.000 |
| Reserva de gestión | 5 % de la línea base | USD 2.750 |
| Presupuesto total | Línea base + reserva de gestión | USD 57.750 |

> **Error frecuente:** incluir la reserva de gestión dentro de la línea base o calcularla sobre la estimación inicial en lugar de hacerlo sobre la línea base.

### Paso 3: Asignar el costo en el tiempo

El costo de cada actividad se reparte linealmente entre su inicio temprano (ES) y su fin temprano (EF).

> **Error frecuente:** repartir el costo fuera de las fechas tempranas del cronograma.

### Paso 4: Acumular el costo diario

**Día 26: USD 50.000**

Se suma el gasto diario acumulado para construir la Curva S del plan de gasto, alcanzando los USD 50.000 al día 26.

> **Error frecuente:** generar desfases en el cierre acumulado. Si no se alcanzan exactamente los USD 50.000 en el día 26, existe un error de distribución.

### Paso 5: Realizar el corte al día 15

Al día 15 se obtienen las siguientes magnitudes clave:

| Métrica | Valor indicado |
|---|---:|
| PV — Valor Planificado | USD 38.000 |
| EV — Valor Ganado | USD 35.600 |
| AC — Costo Actual | USD 42.000 |

> **Error frecuente:** calcular el EV usando el costo real en lugar del presupuestado, o comparar directamente AC con PV ignorando el EV.

### Paso 6: Calcular índices y pronóstico

| Indicador | Valor |
|---|---:|
| CPI | 0,85 |
| SPI | 0,92 |
| EAC | USD 58.989 |

Con un CPI de 0,85 y un SPI de 0,92, se proyecta un EAC de USD 58.989. Antes de decidir, se debe analizar el camino crítico, en particular la actividad F.

> **Error frecuente:** interpretar el desvío de cronograma (SV) como días de atraso en lugar de dinero, o ignorar el camino crítico al evaluar el SPI.

### Idea principal

El control de costos requiere pasar de la estimación individual a la acumulación temporal mediante la Curva S y medir el desempeño real con EVM para tomar decisiones informadas sobre el proyecto.

---

## 2. Costos del proyecto: del costo por actividad a la Curva S

Proceso de construcción del presupuesto desde técnicas de estimación por actividad hasta el comportamiento acumulado de la Curva S.

### 2.1. Técnicas de estimación por actividad

| Técnica | Actividad de ejemplo | Cálculo | Estimación |
|---|---|---|---:|
| Estimación análoga | Actividad B — Selección de proveedor biométrico | Basada en proyectos anteriores similares | USD 500 |
| Estimación paramétrica | Actividad C — Portal web | USD 800/día × 10 días | USD 8.000 |
| Estimación PERT / multipunto | Actividad G — Motor de transacciones | (USD 11.000 + 4 × USD 14.000 + USD 20.000) / 6 | USD 14.500 |

Para la actividad G, la línea base indicada es de **USD 14.000**.

### 2.2. Presupuesto en capas

La construcción de abajo hacia arriba queda representada así:

1. **Estimación de actividades (BAC): USD 50.000.** Suma de las nueve actividades del recorte.
2. **Reserva para contingencias: USD 5.000.** Equivale al 10 %.
3. **Línea base de costos: USD 55.000.** Incluye la estimación de actividades y la reserva para contingencias.
4. **Reserva de gestión: USD 2.750.** Equivale al 5 % y se ubica fuera de la línea base de costos.
5. **Presupuesto total del proyecto: USD 57.750.**

### 2.3. Evolución temporal: la Curva S

| Tramo | Momento | Costo acumulado | Descripción |
|---|---:|---:|---|
| Tramo 1 — Arranque lento | Día 2 | USD 3.220 | Acumulado inicial al comenzar el proyecto |
| Tramo 2 — Aceleración | Día 11 | USD 27.333 | Rápido crecimiento del gasto |
| Tramo 2 — Punto de control | Día 15 | USD 38.800 | Se alcanza un hito clave |
| Tramo 3 — Cierre del proyecto | Día 26 | USD 50.000 | Cierre del gasto acumulado al finalizar la actividad I |

---

## 3. Valor Ganado al día 15: Home Banking Digital

### Datos de partida

**BAC: USD 50.000**

| Métrica | Significado | Valor |
|---|---|---:|
| PV | Valor Planificado | USD 38.800 |
| EV | Valor Ganado | USD 35.600 |
| AC | Costo Actual | USD 42.000 |

### Variaciones

#### Variación del costo (CV)

```text
CV = EV − AC
CV = 35.600 − 42.000
CV = −6.400
```

El resultado muestra un **sobrecosto de USD 6.400**.

#### Variación del cronograma (SV)

```text
SV = EV − PV
SV = 35.600 − 38.800
SV = −3.200
```

El resultado muestra un **atraso expresado en valor monetario de USD 3.200**.

### Índices de desempeño

| Índice | Resultado | Estado |
|---|---:|---|
| CPI — Índice de Desempeño del Costo | 0,85 | Amarillo |
| SPI — Índice de Desempeño del Cronograma | 0,92 | Amarillo |

Escala del semáforo:

- **Verde:** igual o superior a 0,95.
- **Amarillo:** entre 0,80 y 0,95.
- **Rojo:** inferior a 0,80.

Ambos índices se encuentran en amarillo.

### Pronósticos al cierre

| Pronóstico | Valor |
|---|---:|
| EAC | USD 58.989 |
| ETC | USD 16.989 |
| VAC | USD −8.989 |
| TCPI | 1,80 |

La proyección al cierre se calcula a partir del desempeño acumulado.

### Análisis previo a la decisión

Antes de decidir, deben analizarse el camino crítico y el sobrecosto:

- La actividad **F** está en el camino crítico y representa **USD −1.800 del SV**.
- La actividad **G** tiene un día de holgura y representa **USD −1.400 del SV**.

---

## Observación sobre los valores de PV

El primer anexo indica **PV = USD 38.000** en su resumen del paso 5, mientras que la Curva S y el anexo específico de Valor Ganado indican **PV = USD 38.800** para el día 15. Ambos valores se conservaron en esta transcripción para reflejar fielmente las imágenes originales; conviene revisar esta diferencia antes de utilizar los datos.

## Imágenes de origen

- `Control_financiero_en_seis_pasos.png`
- `Costos_del_proyecto__Curva_S.png`
- `Valor_ganado__Home_Banking_Digital.png`
