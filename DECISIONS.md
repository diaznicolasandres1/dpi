# Decisions and Accumulated Feedback

## Repository decisions

- Los archivos originales se conservan sin reemplazo.
- Las carpetas y los archivos Markdown usan nombres en inglés.
- El contenido académico permanece en español.
- Los Markdown funcionan como capa de búsqueda; el original prevalece para formato, diagramas y valores visuales.
- Cada nueva entrega debe tener su propio directorio `submissions/submission_N/` y un `README.md`.
- Las reglas comunes para agentes se mantienen en `AI_GUIDE.md`; `AGENTS.md` y `CLAUDE.md` son puntos de entrada específicos para Codex y Claude.

## Submission N1

**Result:** 8/10.

Decisiones derivadas de la devolución:

- Reducir extensión y evitar contenido correspondiente a entregas futuras.
- No duplicar en la declaración del alcance la identificación ya incluida en el Charter.
- Mantener consistencia entre el texto de la EDT y su diagrama.
- Separar correctamente contingencias y reserva de gestión.
- Revisar la secuencia temporal entre elaboración, firma del Acta, aprobación del alcance e inicio.
- Mantener trazabilidad entre los 31 paquetes de la EDT y las 20 a 30 tareas solicitadas.
- Reconciliar el presupuesto preliminar con el costo base declarado de USD 398.000.

## Submission N2

**Result:** 6/10.

Decisiones derivadas de la devolución:

- Preparar un documento PDF único más la planilla Excel cuando ese sea el formato requerido.
- No usar ZIP ni entregar archivos sueltos innecesarios.
- Distinguir la duración de la red lógica de la duración real con calendario y restricciones.
- Recalcular el camino crítico después de incorporar la restricción de balances.
- No acortar duraciones sin justificar los recursos o cambios que lo permiten.
- La estimación ascendente debe validar la descendente, no ajustarse artificialmente a ella.
- Mostrar recurso, tarifa y días para cada tarea.
- Corregir diferencias de duración entre listados y Gantt. La tarea 1.5 figuró con 91 y 133 días.
- Ajustar el nodo AON al molde de la cátedra y evitar flechas con tramos compartidos.
- Evitar reproducir la N1 dentro del documento principal de N2.

## Submission N4 — decisiones de preparación (27/10/2026)

- La continuidad presupuestaria usa los originales N2 corregidos en `submissions/submission_2/corrected_review/`: costo de trabajo USD372.700 y línea base USD394.700, concordantes con N3 revisión2 confirmada. Los Markdown N2 originales conservan cifras antiguas y no representan esa corrección.
- N4 calcula O/M/P y PERT por las31tareas; conserva M en línea base según ejemplo DPI5p11 y condición de precio fijo de K-2. PERT técnico no incrementa automáticamente el compromiso VCA ni se suma a contingencia.
- Se usa BAC operativo sin reservas (DPI6p20), conciliado como trabajo372.700+contingencia no distribuida22.000=línea base394.700. Activar una respuesta exige transferir presupuesto a trabajo medible, sin ganarEV por reservar fondos.
- La contingencia22.000 se conserva como provisión heredada y se propone un desglose por cantidades/tarifas incrementales. Es hipótesis pendiente de juicio experto, no VME ni demostración de suficiencia. No se fuerza una nueva estimación a ese techo.
- Calidad y riesgos se validan con GDP complementario, numeración independiente de DPI. ISO/IEC25010:2023 y OWASP ASVS5.0.0 son marcos elegidos; coberturas y porcentajes nuevos son decisiones académicas, sin afirmar certificación.
- Devengo de sandbox se alinea con necesidad30/10 de N3 y logística masiva se ubica22-30/03 después de balances/UAT. Cantidades/costos e hitos se preservan; disponibilidad de referentes requiere validación.
- PDF único más Excel con base `Grupo 1_Entrega N4` es supuesto de formato por antecedente docenteN2; consignaN4 no confirmó nombre exacto.

## Open issues

- Validar si el PV del día 15 es USD 38.000 o USD 38.800. Los anexos contienen ambos valores.
- Confirmar en cada nueva consigna el patrón exacto de nombre y la cantidad de archivos requeridos.
- Confirmar qué restricción de balances produjo la diferencia entre los 98 días hábiles de la red y los 140 días del calendario de N2.
- Recuperar las notas de las diapositivas 23 a 25 de `07_DPI_Clase7_Ejercitacion_EVM_Reservas_Contingencia.pptx`: el PDF disponible de Ruta 40 Bikes no incluye la tasa de reserva ni el estado real y los costos reales de la semana 6 necesarios para cerrar numéricamente los pasos 5 a 7.
