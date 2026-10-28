# Validación de la Entrega N4

Fecha de preparación: 27/10/2026. Entrega prevista: 31/10/2026. Estado: propuesta académica preparada para revisión. No implica presentación, firma de contratos ni evidencia de ejecución.

## Fuentes y decisiones verificadas

| Requisito / criterio | Fuente original revisada | Aplicación N4 |
| --- | --- | --- |
| Costo por tarea con recurso, tarifa y días | Feedback N2 puntos 3-5; N2 corregida PDF pp.7-9 y Excel, hojas Tareas/Costos/Partidas | 31 tareas, 84 líneas laborales, 12 partidas; no ajustar al total descendente de USD 398.000 |
| Multipunto O/M/P | DPI5 pp.10-11 | Tres clases de incertidumbre con escenario explícito; PERT=(O+4M+P)/6. M queda en línea base siguiendo ejemplo p.11; se aclara perspectiva del precio fijo K-2 |
| Reserva, línea base y presupuesto | DPI5 pp.16-18; N2 corregida p.9; N3r2 pp.2-4 | Contingencia USD 22.000 dentro; gestión USD 15.788 fuera; presupuesto USD 410.488. Se desagrega provisión heredada en respuestas incrementales, no VME ni P/5 |
| Curva acumulada y mensualización | DPI5 pp.20-22, originales visualizados; N2 corregida p.9 y calendario Excel | Costos acumulados con eje temporal/monetario legible. Devengo N4 revisado de P-3c/P-4b; reserva por exposición, sin prorrateo automático |
| PV/EV/AC y variaciones | DPI6 pp.10-17, originales visualizados | Misma fecha y alcance; EV por aceptación, AC por incurridos; SV en USD. No se usan cifras reales ficticias |
| BAC y pronósticos | DPI6 pp.20-23, originales visualizados | Convención explícita de BAC operativo USD 372.700, excluye reserva no distribuida; conciliación a LB394.700. Transferencia de reserva exige plan y evidencia |
| Calidad | GDP complementario 09 Entrega/Calidad pp.3-6, originales visualizados | Prevención, auditoría del proceso, pruebas del producto, métricas y responsables. Porcentajes nuevos del equipo, sin atribuirlos a clase o ISO |
| Escalas, matriz y respuestas | GDP complementario 07 Incertidumbre pp.10-21, originales visualizados | P/I1-5, máximos por objetivo, umbralesP×I; P vertical/I horizontal; todos los19ID, incluidas coincidencias; respuestas por causa, sin regla mecánica de cuadrante |
| Juicio de Experto | DPI11 pp.4-5 y14, originales visualizados | Consulta propuesta por perfil, alcance/evidencia y protocolo; no se inventan reuniones ni expertos consultados |
| Continuidad riesgos/aceptación | N3r2 PDF pp.12-13; N1 PDF/Markdown aceptaciones revisadas por revisor | 17 riesgos heredados+2 nuevos. Mantener300 concurrentes p95<500ms y500 concurrentes p95<800ms como escenarios distintos; UAT≥9/10 con≥120 usuarios |
| Normas específicas | Ficha oficial ISO/IEC25010:2023 ed.2; OWASP ASVS5.0.0 y fuente etiquetadaV8 | FichaISO pública, sin texto completo ni certificación. Controles v5.0.0-8.1.1,8.2.1,8.2.2,8.3.1 seleccionados y pruebas concretas; no nivelASVS íntegro |

Colecciones DPI y GDP tienen numeración independiente. Se usó GDP complementario para riesgos/calidad: no se mantuvo el diagnóstico histórico de ausencia de clases como bloqueo. La extracción OCR se utilizó para navegar; matriz, escalas, respuestas y fórmulas se cotejaron contra páginas originales renderizadas.

## Conciliaciones

- Mano de obra USD 235.926 = Tandem216.888 + VCA19.038.
- Partidas no laborales USD 136.774 = licencia108.000 + otras28.774.
- Trabajo M USD 372.700; PERT agregado USD 378.476,258333; diferencia5776,258333 no sumada a M ni reserva.
- Contingencia: 21 partidas de respuesta, 13 riesgos con importe, USD 22.000; 19 riesgos registrados. Los6 restantes usan decisiones, escalamiento u obligaciones incluidas en base.
- Línea base USD 394.700; reserva de gestión4%=15.788; presupuesto410.488; margen frente al techo420.000=9.512.
- Suma de siete meses de trabajo=372.700, reserva=22.000, línea base=394.700. Precisión interna completa; PDF muestra USD enteros. Diferencias de redondeo de vistas no son partidas adicionales.
- 31IDs coinciden con EDT; R-3 no se cobra como tarea. PM seguimiento132d ×0,5FTE ×520=34.320.

## Verificación de archivos

- PDF único A4 horizontal,17 páginas. Se renderizaron e inspeccionaron las17 páginas a tamaño de lectura; controles específicos: tablas de costos pp.3-4, métricas p.10, matriz p.11 y base cuantitativa de contingencia p.16. Encabezados blancos sobre fondo azul, tablas legibles, sin páginas partidas o tablas cortadas. Se corrigió un primer defecto de contraste de encabezados antes de exportar versión final.
- Excel generado y recalculado por Artifact Tool; inspección de valores/fórmulas, cero coincidencias de errores de fórmula. Renders de todas las11 hojas y vista de respuestas; se reparó un gráfico inicialmente vacío mediante rango auxiliar contiguo vinculado a acumulados y meses. El gráfico final se verificó visualmente y sus referencias a las series se comprobaron en el XML exportado.
- Pruebas de entrada con restauración: cambiar tarifaPM actualiza costo y total; cambiarP deRI-1 mueve el riesgo en matriz. Todos los valores originales restaurados. El archivo `workbook_validation.json` registra resultados.
- Plantilla EVM real con43 componentes (31 laborales+12 partidas), entradas vacías y estado pendiente. Un avance1,1 oACnegativo produce dato inválido; completar con ceros produce CPI/EAC no calculables. No se presenta cero como eficiencia sana. Escenario ilustrativo separado con PV200.000,EV180.000,AC195.000: CPI0,9230769,SPI0,9,EAC403.758,3333,TCPI1,0844119.
- Duración laboral enlazada a entrada maestra deTareas; FTE visibles con3 decimales. Calendario/ponderaciones congeladas del antecedente explícitamente documentadas. No se promete reprogramación automática completa ni se afirma revisión de capacidad de escenariosP.
- No se realizó prueba en MicrosoftExcel nativo. La verificación usa cálculo Artifact Tool, lectura del exportado y revisión visual. Esta limitación está visible en README/Excel.

## Diferencias y pendientes operativos

1. Se priorizó N2 corregida sobre conversiones N2 antiguas. El PDF N3r2 es la última entrega confirmada; Excel N3 original preservado sin presumir actualización.
2. Se elige conservar M por la continuidad contractual a precio fijo y el criterio de DPI5p11. PERT sirve para discutir exposición técnica, no incrementa contrato por sí solo.
3. P-4b se devenga desde30/10 conforme necesidad N3; P-3c logística de30sesiones pasa a22-30/03 después de balances/UAT. Son ajustes de planificación, no hechos consumados. Se debe validar disponibilidad de referentes y participación.
4. RI-9/17 suben a alta yRI-15 a media por escalas explícitas de bloqueo/criticidad; no se afirma ocurrencia. Riesgos informáticos: RI-1/2/6/9/10/11/12/14/15/17/18/19.
5. Reservas y rangos son hipótesis académicas: validar cantidades incrementales, precios nuevos, capacidad y exclusiones contractuales con expertos. Provisión22.000 no demuestra cobertura estadística. Si no alcanza, se pide cambio; no se ajustan artificialmente nuevas estimaciones.
6. Fechas anteriores27/10 son plan base sin estado comprobado. Verificar de inmediato situación de compras/sandbox antes de usar el plan. No se inventaron gastos ni avances reales.
7. La consigna no confirmó patrón de nombre/formato. Se adopta PDF único+Excel y `Grupo 1_Entrega N4` por antecedente docenteN2. No pedir confirmación bloqueó el trabajo; el supuesto queda documentado.

## Mantenimiento del hub

Se agregan PDF/Excel al manifiesto con conversiones `exported_text.md` y `workbook.md`, separadas de la fuente editorial `submission.md`. Se actualizan README, INDEX, índice de entregas y DECISIONS. Los originales previos no se modifican. Se ejecutaron `make hub-update` y `make hub-check` con `PYTHON=/Users/nico/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`: actualización de 31 conversiones y validación exitosa con 0 advertencias. El Python del sistema carecía de dependencias; se usó el runtime bundled sin instalar paquetes.
