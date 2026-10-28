# Entrega N4 (TP N.° 4)

**Costos detallados, control de gestión, calidad y riesgos completa**

**Fecha de entrega:** sábado 31 de octubre de 2026.  
**Obligatoriedad:** obligatoria.  
**Estado:** propuesta completa preparada y revisada; no acredita una entrega presentada ni aprobaciones operativas.

- [Consigna](assignment.md)
- [Disponibilidad de clases y pendientes](material_readiness.md)
- [Texto de la consigna conservado](source/assignment_prompt.txt)
- [Documento PDF único](<Grupo 1_Entrega N4.pdf>)
- [Planilla Excel](<Grupo 1_Entrega N4.xlsx>)
- [Fuente del contenido](submission.md)
- [Notas de validación y decisiones](validation_notes.md)
- [Revisión independiente](peer_review.md)
- [Texto extraído del PDF](exported_text.md)
- [Conversión del Excel](workbook.md)

## Archivos de entrega

Entregar únicamente `Grupo 1_Entrega N4.pdf` y `Grupo 1_Entrega N4.xlsx`. La consigna N4 no establece patrón exacto de nombre ni formato; se adopta por hipótesis el antecedente docente de N2 (PDF único más Excel, número adaptado). Los Markdown, JSON, builders y notas son soporte interno del hub y no se envían como archivos adicionales.

## Base utilizada

- N2 corregida: [PDF](<../submission_2/corrected_review/Grupo 1_Entrega N2.pdf>) y [Excel](<../submission_2/corrected_review/Grupo 1_Entrega N2.xlsx>). Conserva 31 tareas, USD 235.926 laborales, USD 136.774 no laborales y USD 372.700 de trabajo.
- N3 vigente: [revisión 2 confirmada](<../submission_3/revisions/revision_2/Grupo 1_Entrega N3.pdf>). Se preservan sus 17 riesgos y se agregan 2 de software. El Excel N3 original no se presume actualizado.
- Se mantiene M en la línea base conforme DPI5 p.11 y precio fijo K-2; PERT se calcula como contraste técnico, USD 378.476,2583. Línea base USD 394.700 = trabajo USD 372.700 + contingencia USD 22.000. Gestión USD 15.788 fuera de línea base; total USD 410.488.
- La reserva de USD 22.000 es una provisión heredada. Se propone una distribución por 21 partidas de respuesta incremental, pendiente de validación, sin afirmar suficiencia probabilística ni forzar un nuevo cálculo a ese techo.
- Se ajusta devengo de sandbox al 30/10 y logística masiva a marzo. La distribución mensual N4 cambia, el total no. La disponibilidad de referentes y el calendario corporativo siguen siendo supuestos por validar.

## Reproducción

Los builders usan dependencias bundled de Codex y no instalan paquetes en el repositorio. `build_submission.py` lee el Excel N2 corregido, genera `model_data.json`, el Markdown y el PDF; `build_workbook.mjs` consume ese JSON y genera el Excel con Artifact Tool. No usa openpyxl para autoría: solo para lectura del antecedente.

1. Ejecutar los marcadores de inicio de operación de los skills PDF y spreadsheets al iniciar una nueva autoría.
2. Ejecutar `build_submission.py` con el Python indicado por `load_workspace_dependencies`.
3. Crear temporalmente un enlace `node_modules` a los paquetes bundled, ejecutar `build_workbook.mjs` con Node bundled y retirar ese enlace al terminar. Las vistas se generan en `work/` (ignorado).
4. Revisar los renders y `workbook_validation.json`; correr `make hub-update` y `make hub-check`.

No se verificó el comportamiento de las fórmulas en Microsoft Excel nativo. Sí se calcularon con Artifact Tool, se comprobó el XLSX exportado y se inspeccionaron sus vistas y el gráfico. El calendario heredado queda congelado como ponderaciones: cambiar duraciones recalcula esfuerzo/costo, pero exige revisar fechas y ponderaciones antes de usar la curva temporal.
