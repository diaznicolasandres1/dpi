# Revisión 1 de la entrega N3

## Alcance

Corrección interna solicitada por el usuario, no devolución docente. Se modifica únicamente el PDF para completar el punto 12 de la consigna de N3: probabilidad cualitativa y respuestas preliminares a los riesgos priorizados. Los impactos iniciales, prioridades, identificadores, responsables del registro, presupuesto y cronograma se conservan. La N4 mantiene la escala de 1 a 5, matriz gráfica, planes completos y monitoreo.

Original preservado: [PDF original](<../../Grupo 1_Entrega N3.pdf>). SHA-256: `84fd87f287d9d6686833b62199428ae55069846a27e6feb77ff9d8a9f6691400`.

Salida: [PDF corregido](<Grupo 1_Entrega N3.pdf>). El Excel original no fue modificado: esta revisión contiene únicamente la corrección del PDF, que incorpora los complementos del registro en los apartados 4.1 y 4.2. No se presenta como un par PDF/Excel actualizado.

## Cambios y verificación

| Hallazgo | Cambio | Ubicación | Verificación |
| --- | --- | --- | --- |
| La N3 exige probabilidad; la tabla solo muestra valoraciones de N1 en «Origen» para RI-1 a RI-5. | Incorporar probabilidad cualitativa para los 17 riesgos, sin duplicar el impacto. | Página 13, apartado 4.1. | 2 riesgos altos, 13 medios y 2 bajos; los 17 identificadores están cubiertos una vez en la tabla de probabilidad. Las probabilidades de RI-1 a RI-5 coinciden con N1, p. 8. |
| Respuestas relevantes dispersas en N1 y otras secciones; falta una asociación explícita para los cinco riesgos altos. | Reunir respuestas a RI-1, RI-3, RI-5, RI-7 y RI-8 con responsables, aprovechando medidas previstas. | Página 13, apartado 4.2. | Comparación con N1, p. 8; N3, pp. 2, 7, 9-11. No se cambian fechas, cantidades de usuarios, recursos ni costos. Las acciones nuevas se presentan como propuestas, no como hechos ejecutados. |
| Notas postergan todas las respuestas a N4. | Corregir la separación de alcance entre N3 preliminar y N4 completa. | Páginas 2 y 13. | Comparación con consigna N3, punto 12, y consigna N4 suministrada por el usuario en el chat. |
| Preservación de lo ya entregado. | Mantener 13 páginas y mover intacta la sección 5 dentro de la página 13 para dar lugar al complemento. | Página 13. | Renderizado de las 11 páginas no modificadas idéntico, píxel por píxel, al original; valores y contenido de la sección 5 preservados. Original verificado mediante SHA-256. |

## Fuentes originales y límites de validación

- [N1 original](<../../../submission_1/Grupo 1_Entrega  N1.pdf>), p. 8, apartado 1.10: se revisaron texto y página renderizada. Confirma el orden «impacto / probabilidad», las probabilidades de RI-1 a RI-5 y respuestas iniciales. Se recuperan las medidas pertinentes sin reproducir supuestos temporales antiguos.
- [N3 original](<../../Grupo 1_Entrega N3.pdf>), pp. 2, 7 y 9-13: disponibilidad de 120 usuarios para UAT del 16 al 19/03; funciones de QA y Servicios Generales; comunicaciones C-2 y C-13 a C-15; escalamiento 3.3; cinco riesgos de prioridad alta.
- [Clase de equipo e interesados](<../../../../theory/course_material/08-09_DPI_Clases08y00_Equipo_e_Interesados.pdf>), p. 29: se inspeccionó la diapositiva original, que incluye revisión semanal de riesgos y responsables junto al estatus. No se agregó otro mecanismo de seguimiento a la N3.
- Se buscaron escalas de probabilidad en todos los PDF originales disponibles de las clases. No se encontró una escala específica de riesgos aplicable. Por eso las definiciones de alta/media/baja y las probabilidades de RI-6 a RI-17 se identifican como supuestos cualitativos del caso académico, autorizados por el usuario; no se atribuyen a la cátedra, a mediciones reales ni a entrevistas efectuadas.
- La probabilidad baja de RI-15 supone continuidad de versión y API; queda expresamente condicionada a revisar cualquier anuncio de cambio. No implica que exista una garantía contractual de estabilidad.

## Comprobación de salida

- PDF reabierto y páginas 2, 12 y 13 renderizadas; inspección visual de las páginas modificadas sin recortes ni superposiciones.
- Se preservó la columna «Impacto inicial» completa y la prioridad de los 17 riesgos.
- Se verificó extracción de texto con PyMuPDF y pypdf: las frases sustituidas no permanecen ocultas y la sección 5 aparece una sola vez.
- No se declara validación de un molde de matriz de riesgos de la cátedra; no se incorpora tal matriz en esta revisión.
