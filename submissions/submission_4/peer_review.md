# Revisión independiente de N4

Fecha: 27/10/2026. Preparación delegada por pedido del usuario a GPT-6.1 (`gpt-6.1-sol`), razonamiento medium. Revisión del agente principal sobre los archivos exportados, los antecedentes y las fuentes.

## Resultado

Los tres bloques de la consigna están desarrollados: costos detallados y EVM; calidad técnica y controles; registro de 19 riesgos, escalas 1–5, matriz, respuestas, monitoreo y justificación de Juicio de Experto. No quedan hallazgos de cálculo o presentación abiertos en el alcance revisado. La propuesta no acredita presentación a la cátedra ni aprobación operativa.

## Comprobaciones independientes

- Se cotejaron los 31 identificadores y duraciones con el Excel N2 corregido. Se recalcularon 84 líneas de esfuerzo por tarifa, la asignación única de 12 partidas, O/M/P y PERT por tarea.
- Mano de obra 235.926 + partidas 136.774 = 372.700 USD. PERT técnico 378.476,258333 USD. M permanece como base siguiendo DPI5 p.11 y la perspectiva de precio fijo; PERT no se suma como gasto ni reserva.
- Se cotejaron los valores de cada tarea en el XLSX exportado con el modelo, además de resumen y componentes EVM. Línea base 394.700; gestión 15.788; presupuesto 410.488 USD. Conciliaciones monetarias nulas tras redondeo.
- Se comprobó suma mensual, 19 identificadores únicos, P/I en 1–5 y asignación de 22.000 USD a respuestas. Se revisó el fundamento incremental de las respuestas y la exclusión de obligaciones ya incluidas en contratos.
- EVM ilustrativo recalculado independientemente: CPI 0,923076923; SPI 0,9; EAC 403.758,333333; ETC 208.758,333333; VAC −31.058,333333 USD; TCPI 1,08441193. Los 43 presupuestos de componentes suman 372.700 USD. El reporte real permanece pendiente por ausencia de datos comprobados.
- Se inspeccionaron vistas de las hojas, la curva final y las referencias de series del gráfico en el XML exportado. El XLSX no contiene celdas exportadas con errores de fórmula. Se contrastaron las pruebas de cambio de tarifa, entrada inválida, costo negativo y ceros registradas por el constructor.
- Se revisaron visualmente tablas de costos, controles, matriz, respuestas y fuentes del PDF. Se reabrieron páginas actualizadas 10, 11, 16 y 17 a tamaño de lectura. El autor registró la inspección de las 17 páginas y las 11 hojas en validation_notes.md.
- Fuentes de contraste: N2 corregida PDF pp.7–9 y Excel; N3 vigente pp.2–4 y 12–13; criterios de aceptación N1; DPI5 p.11 y DPI6 p.20 para convenciones; GDP Incertidumbre p.17 para ejes/adaptación. Las fuentes externas se verificaron en las páginas oficiales de ISO y en el tag OWASP ASVS v5.0.0, capítulo V8, citados en la entrega.

## Hallazgos corregidos durante la revisión

1. Encabezados de PDF oscuros sobre fondo oscuro: texto blanco y nueva inspección.
2. Matriz Markdown y enlaces de fuentes: tabla válida y enlaces navegables.
3. Reserva sin desglose cuantitativo: 21 partidas incrementales con cantidades, precios, exclusiones e hipótesis.
4. Gráfico Excel vacío: referencias de datos reparadas y curva final visible hasta 394.700 USD.
5. Columna de trabajo acumulado confundida con PV físico: rótulo corregido; medición EVM separada.
6. Duración duplicada por recurso: enlace a duración maestra, con calendario congelado expresamente documentado.
7. Datos fuera de dominio y denominadores cero: guardas y estados explícitos; no se informa cero como resultado favorable.
8. Conciliación roja por error de coma flotante y FTE redondeadas: tolerancia monetaria y tres decimales para dedicación.
9. Contexto histórico de falta de material: disponibilidad actualizada para reflejar GDP y la propuesta preparada.

## Límites que siguen explícitos

No se probó Microsoft Excel nativo; se verificaron cálculo en Artifact Tool, exportado y renders. El calendario es el del antecedente, sin reprogramación automática por cambios de duración. Tarifas, rangos, reservas, controles y consultas de expertos son supuestos académicos o propuestas, sin inventar cotizaciones, contratos firmados, reuniones ni avance real. El formato PDF + Excel se adopta por el antecedente docente, porque N4 no lo detalla.

## Archivos revisados

- `Grupo 1_Entrega N4.pdf` · SHA-256 `4a3890450223f5c8faa98cf023ae8b09d68264df6d1a976fcfe97f34142b7047`
- `Grupo 1_Entrega N4.xlsx` · SHA-256 `5daa30171736dee6a02a060467159dbef0793970169c4ab6e3b687a3c7d16583`
