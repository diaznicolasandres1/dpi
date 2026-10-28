# TP4 — Disponibilidad de materiales

Relevamiento actualizado el 27/10/2026. La consigna está en [assignment.md](assignment.md). La propuesta N4 ya está preparada: consultar [README](README.md), [contenido](submission.md) y [validación](validation_notes.md). Este archivo registra las fuentes disponibles y conserva las referencias a clases DPI todavía no incorporadas.

## Colección complementaria GDP incorporada

Se incorporó una [colección GDP independiente](../../theory/gdp_material/README.md), cuya numeración no equivale a las clases DPI. Incluye [Incertidumbre](../../theory/gdp_material/07_uncertainty_domain.md) y [Entrega y calidad](../../theory/gdp_material/09_delivery_and_quality.md). Por tanto, la falta de las clases DPI específicas que se registra abajo no implica ausencia total de teoría sobre estos temas en el hub.

Incertidumbre desarrolla matriz de probabilidad e impacto, definición de escalas y umbrales (PDF, pp. 10–18) y respuestas a amenazas (pp. 19–21). La p. 17 fue inspeccionada visualmente; su gráfico usa probabilidades e impactos entre 0 y 1, mientras la consigna N4 exige 1 a 5: deberá aplicarse la escala de la consigna y documentar la adaptación. La p. 3 de Entrega y calidad fue inspeccionada visualmente y desarrolla cumplimiento de requisitos, expectativas y criterios de aceptación. La disponibilidad no equivale a una validación completa de los controles específicos de software solicitados.

Las conversiones de esta colección requieren OCR en páginas sin texto seleccionable. Consultar los PDF originales para fórmulas, tablas y gráficos.

## Cobertura

| Requisito | Material disponible | Estado |
|---|---|---|
| Estimación análoga o multipunto por tarea | [Clase 5, PDF](../../theory/course_material/05_DPI_Clase5_Dominio_Planificacion_Costos.pdf), pp. 10–11 | Disponible: técnicas y ejemplo de tres valores |
| Línea base, contingencias, reserva de gestión y distribución temporal | Clase 5, pp. 16–18 y 20–22 | Disponible |
| Seguimiento mediante Valor Ganado (EVM) | [Clase 6, PDF](../../theory/course_material/06_DPI_Clase6_EVM_Medicion.pdf), pp. 10–17 y 20–23 | Disponible: valores, variaciones, índices y pronósticos |
| Plan de calidad, estándares y controles de software | [GDP Entrega y calidad](../../theory/gdp_material/09_delivery_and_quality.md), pp. 3–6; fuentes oficiales ISO/IEC 25010:2023 y OWASP ASVS 5.0.0 citadas en la propuesta | Base disponible y aplicada; umbrales propios justificados, sin afirmar certificación |
| Registro de ≥10 riesgos, escalas 1–5, gráfico, respuestas y monitoreo | [GDP Incertidumbre](../../theory/gdp_material/07_uncertainty_domain.md), pp. 10–21 | Base disponible y aplicada: 19 riesgos, matriz 1–5 y respuestas; las clases DPI 13–14 siguen sin incorporarse |
| Justificación de Juicio de Experto para costos y riesgos | [Clase 11, PDF](../../theory/course_material/11_DPI_Clase11_Taller_OBS_RACI_Juicio_Experto.pdf), pp. 4–5 y 14; [Markdown](../../theory/course_material/11_obs_raci_expert_judgment_workshop.md) | Disponible: definición, ejemplos de costos y referencia explícita a la nota del TP4 |

Las fuentes se cotejaron contra los originales y se verificaron las representaciones finales según las [notas de validación](validation_notes.md). La colección GDP complementaria y los estándares externos identificados permiten preparar la propuesta sin esperar las clases DPI pendientes.

## Hasta qué clase llega el hub

Hay originales de las clases 1, 2, 3, 4, 5, 6, 8, un archivo conjunto de clases 8–9, y las clases 10 (Recursos Humanos), 11 (Taller OBS, RACI y Juicio de Experto) y 12 (Abastecimiento y Adquisiciones). El máximo incorporado es la clase 12. De clase 7 está el ejercicio Ruta 40 Bikes, pero falta la presentación completa. No se encontraron clases 13 en adelante.

Los materiales anteriores anunciaban el taller de Juicio de Experto como clase 10; el archivo recibido lo identifica como clase 11. Se usa la numeración del original recibido.

## Continuidad y precauciones para resolver

- Retomar presupuesto, recursos y tareas de [N2](../submission_2/README.md), corrigiendo lo señalado en su [devolución](../submission_2/feedback.md): costo sustentado por recurso, tarifa y días; partidas no laborales justificadas; no forzar el total para coincidir con N1.
- Usar los riesgos preliminares de [N3, revisión vigente](../submission_3/revisions/revision_2/submission.md) como insumo, y completar lo exigido en N4. La entrega previa no sustituye la teoría faltante.
- Clase 5, p. 11: el ejemplo calcula PERT, pero conserva el valor más probable en su línea base. Documentar la elección del valor aplicado a cada tarea y su fundamento; no trasladar cifras del ejemplo al proyecto.
- Clase 6, p. 20: el ejemplo usa como BAC la suma de actividades sin reservas. Explicitar esa convención y reconciliarla con la línea base y el presupuesto; distinguir contingencia de gestión.
- Falta incorporar la unidad de Calidad y las clases 13–14 de riesgos. Sus números provienen de referencias internas; verificar el título real al recibir los originales. El taller de Juicio de Experto ya está incorporado como clase 11.
- La consigna no fija porcentajes concretos de revisión por pares ni de pruebas: deberán proponerse y justificarse, sin atribuirlos como cifras obligatorias de la cátedra.

## Lista de alcance del TP4 — contrastar con la propuesta y sus notas de validación

- [x] Costos por tarea con técnica análoga o tres valores y base de cálculo verificable.
- [x] Línea base formal e indicadores de Valor Ganado con fuentes, responsables y frecuencia de seguimiento.
- [x] Criterios técnicos de calidad y mecanismos de control basados en estándares.
- [x] Registro de al menos 10 riesgos de desarrollo informático.
- [x] Probabilidad e impacto de 1 a 5 y gráfico de matriz.
- [x] Respuestas concretas, planes de acción y mecanismos de monitoreo.
- [x] Nota justificando Juicio de Experto para riesgos y costos.
- [x] Verificación contra los originales disponibles de DPI/GDP; sin afirmar validación contra clases DPI no recibidas.
