# Grupo 1 · Entrega N4

UADE · Dirección de Proyectos Informáticos · 2026

WorkHub · Entrega N4

Costos detallados, control de gestión, calidad y riesgos

**Grupo 1** · Abosch, Nicolás (líder) · Jeandet · Diaz · Garcia · Gonzalez<br/>Docente: Mag. Ezequiel Pietracupa<br/>VCA, sede Catalinas · proveedor Tandem · Proyecto WKH-2026<br/>Fecha de entrega: 31 de octubre de 2026


### Decisión de presupuesto

Se mantiene como propuesta de control la línea base de **USD 394.700** de la N2 corregida, citada por la última N3 confirmada. La estimación multipunto aporta rangos y contraste PERT a las 31 tareas. El precio fijo de implementación no aumenta por la variabilidad técnica del proveedor. Esta entrega es un plan académico: no acredita gastos, avance real, contratos firmados ni aprobaciones nuevas.

| Componente | USD | Criterio |
| --- | --- | --- |
| Actividades y partidas (M) | 372.700 | 235.926 de mano de obra + 136.774 no laborales |
| Contingencia | 22.000 | Dentro de la línea base; asignada a acciones residuales identificadas |
| Línea base de costos | 394.700 | 372.700 + 22.000 |
| Reserva de gestión (4 %) | 15.788 | Fuera de la línea base; libera el Comité |
| Presupuesto total | 410.488 | Línea base + gestión |
| Techo del Acta / margen no asignado | 420.000 / 9.512 | El margen no es una reserva adicional |

El documento concentra la N4. El Excel permite auditar recursos, tarifas, esfuerzo, partidas, escenarios, distribución mensual, controles de calidad y los 19 riesgos. Los 17 riesgos de la N3 se conservan; RI-18 y RI-19 amplían riesgos propios del software. Se requieren cotizaciones, revisión de expertos y ratificación del plan antes de su uso operativo.


---



## 1. Base de estimación y continuidad

Fuente de continuidad: N2 corregida, PDF pp. 7-9 y Excel, y N3 revisión 2, PDF pp. 2-4 y 12-13. No se toma el presupuesto de USD 398.000 del Markdown N2 original como la versión corregida. Las 31 tareas conservan identificadores de la Estructura de Desglose del Trabajo (EDT), duraciones y recursos. La externalidad R-3, ventana de balances, no es un paquete ni una tarea con costo propio.


### Recursos, esfuerzo y precios

| Recurso | USD/día | Recurso | USD/día | Regla |
| --- | --- | --- | --- | --- |
| PM / PO | 520 / 480 | UX / DEV | 420 / 440 | Día-persona de 8 horas; esfuerzo = FTE × duración |
| QA / INT | 360 / 480 | OPS / CAM | 460 / 400 | FTE = dedicación equivalente a tiempo completo |
| TEC / SG | 190 / 170 | RH / USR | 160 / 150 | Horas VCA a costo interno cargado; Tandem a tarifa de venta |

PM: dirección de proyecto; PO: responsable de producto; UX: diseño de experiencia de usuario; DEV: desarrollo; QA: aseguramiento de calidad; INT: integraciones; OPS: DevOps; CAM: gestión del cambio; TEC: Tecnología VCA; SG: Servicios Generales; RH: RR.HH.; USR: usuarios de prueba.

Las tarifas y precios heredados son supuestos de simulación, no precios de mercado verificados. La licencia de USD 108.000 proviene del caso N1, sin adjuntar una cotización comercial comprobada. No se suman impuestos, inflación ni tipo de cambio: moneda USD nominal y tarifa constante, supuesto académico pendiente de contrato. El modelo mide costo del proyecto VCA, incluyendo costo de oportunidad de sus horas. No confundir esfuerzo con duración: dos recursos durante 10 días pueden producir 20 días-persona.


### Técnica multipunto y decisión de línea base

O es costo optimista, M el más probable y P el pesimista, todos en USD y para el mismo alcance. PERT (técnica de evaluación y revisión de programas) calcula (O + 4 × M + P) / 6. Se aplica a la mano de obra con tres clases de incertidumbre; las partidas no laborales se conservan en O=M=P por precio/cantidad contractual supuestos. No se inventan históricos para llamarlo estimación análoga.

| Clase | Escenario que explica O/M/P |
| --- | --- |
| A · Gestión y validación acotada | O: documentación disponible y una ronda; M: dedicación N2; P: ronda adicional de revisión. Rango técnico ±10 % de mano de obra. |
| B · Configuración y adopción | O: reglas, planos y materiales reutilizables; M: configuración prevista; P: ajustes de interfaces o materiales dentro del alcance. Mano de obra -15 % / +30 %. |
| C · Integración y verificación compleja | O: contratos API y datos válidos al primer ensayo; M: pruebas planificadas; P: diagnóstico y una iteración adicional, sin cambiar alcance. Mano de obra -20 % / +40 %. |

Las bandas son hipótesis académicas iniciales, no probabilidades ni intervalos de confianza. PERT agregado: **USD 378.476**, diferencia de USD 5.776 frente a M. Siguiendo DPI5 p. 11 se mantiene M en la línea base y PERT como contraste. K-2 de N3 fija USD 216.888 de Tandem; su retrabajo dentro del alcance se cubre con ese precio. Cambios aprobados o mayores obligaciones de VCA requieren decisión expresa, no un incremento automático por PERT. La suma de extremos no constituye un pronóstico probabilístico del proyecto.


---



## 1.1 Costos por tarea · gestión y plataforma

USD. Base de mano de obra = días-persona × tarifa diaria. NL = partidas no laborales asignadas una sola vez. M = mano de obra + NL. O/P solo varían mano de obra según clase A/B/C. PERT se muestra redondeado; el Excel conserva precisión.

| EDT / tarea | Dur./clase | Días-persona × USD/día | NL | O | M | P | PERT |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 Acta de constitución | 2 d / A | PM 2 × 520 | 108.000 | 108.936 | 109.040 | 109.144 | 109.040 |
| 1.2 Declaración del alcance y EDT | 6 d / A | PM 3 × 520; PO 1.2 × 480 | 0 | 1.922 | 2.136 | 2.350 | 2.136 |
| 1.3 Cronograma, presupuesto y línea base | 6 d / A | PM 1.8 × 520 | 0 | 842 | 936 | 1.030 | 936 |
| 1.4 Registro de riesgos e interesados | 5 d / A | PM 1 × 520; RH 0.5 × 160 | 0 | 540 | 600 | 660 | 600 |
| 1.5 Seguimiento, cambios e informes (tarea resumen) | 132 d / A | PM 66 × 520 | 0 | 30.888 | 34.320 | 37.752 | 34.320 |
| 1.6 Cierre y lecciones aprendidas | 5 d / A | PM 1.5 × 520; PO 0.5 × 480 | 0 | 918 | 1.020 | 1.122 | 1.020 |
| 2.1 Relevamiento y reglas de negocio | 10 d / B | PO 10 × 480; PM 2 × 520; SG 2 × 170; RH 1 × 160; QA 2 × 360 | 0 | 6.001 | 7.060 | 9.178 | 7.236 |
| 2.2 Planos e inventario de espacios | 15 d / B | SG 7.5 × 170; OPS 3 × 460 | 0 | 2.257 | 2.655 | 3.452 | 2.721 |
| 2.3 Módulo de reserva de escritorios | 18 d / B | DEV 18 × 440; UX 3.6 × 420; QA 3.6 × 360 | 0 | 9.119 | 10.728 | 13.946 | 10.996 |
| 2.4 Módulo de reserva de salas | 15 d / B | DEV 15 × 440; UX 3 × 420; QA 3 × 360 | 0 | 7.599 | 8.940 | 11.622 | 9.164 |
| 2.5 Check-in, check-out y liberación | 12 d / C | DEV 12 × 440; QA 2.4 × 360 | 0 | 4.915 | 6.144 | 8.602 | 6.349 |
| 2.6 Notificaciones y sugerencias | 15 d / B | DEV 15 × 440; PO 3 × 480; QA 3 × 360 | 0 | 7.752 | 9.120 | 11.856 | 9.348 |
| 2.7 Diseño UX | 15 d / B | UX 9 × 420; PO 3 × 480 | 0 | 4.437 | 5.220 | 6.786 | 5.350 |
| 2.8 Implementación bot de Teams | 10 d / C | DEV 5 × 440; QA 2 × 360 | 0 | 2.336 | 2.920 | 4.088 | 3.017 |
| 2.9 Configuración web | 12 d / B | DEV 12 × 440; UX 3.6 × 420; QA 2.4 × 360 | 0 | 6.508 | 7.656 | 9.953 | 7.847 |
| 3.1 SSO y SCIM con Entra ID | 12 d / C | INT 24 × 480; TEC 6 × 190 | 0 | 10.128 | 12.660 | 17.724 | 13.082 |


---



## 1.2 Costos por tarea · integración, adopción y cierre

USD. Base de mano de obra = días-persona × tarifa diaria. NL = partidas no laborales asignadas una sola vez. M = mano de obra + NL. O/P solo varían mano de obra según clase A/B/C. PERT se muestra redondeado; el Excel conserva precisión.

| EDT / tarea | Dur./clase | Días-persona × USD/día | NL | O | M | P | PERT |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3.2 Sincronización con HRIS | 10 d / C | INT 10 × 480; TEC 3 × 190 | 2.400 | 6.696 | 7.770 | 9.918 | 7.949 |
| 3.3 Exchange, Outlook y Teams | 10 d / C | INT 10 × 480; TEC 2 × 190 | 0 | 4.144 | 5.180 | 7.252 | 5.353 |
| 3.4 Seguridad y endurecimiento | 15 d / C | QA 4.5 × 360; INT 15 × 480 | 7.500 | 14.556 | 16.320 | 19.848 | 16.614 |
| 3.5 Pruebas de integración y carga | 12 d / C | QA 7.2 × 360; INT 12 × 480 | 0 | 6.682 | 8.352 | 11.693 | 8.630 |
| 4.1 Impacto e interesados con RR.HH. | 10 d / B | CAM 10 × 400; RH 4 × 160 | 900 | 4.844 | 5.540 | 6.932 | 5.656 |
| 4.2 Política de trabajo flexible | 10 d / B | CAM 10 × 400; RH 4 × 160 | 0 | 3.944 | 4.640 | 6.032 | 4.756 |
| 4.3 Comunicación y lanzamiento | 15 d / B | CAM 15 × 400; RH 7.5 × 160 | 3.600 | 9.720 | 10.800 | 12.960 | 10.980 |
| 4.4 Referentes y capacitación | 15 d / B | CAM 15 × 400; RH 6 × 160 | 7.200 | 13.116 | 14.160 | 16.248 | 14.334 |
| 4.5 Materiales y mesa de ayuda N1 | 10 d / B | CAM 10 × 400; RH 4 × 160 | 0 | 3.944 | 4.640 | 6.032 | 4.756 |
| 5.1 Ambientes, migración y despliegue | 12 d / B | OPS 9.6 × 460 | 6.330 | 10.084 | 10.746 | 12.071 | 10.856 |
| 5.2 Piloto y ajustes | 20 d / C | PM 4 × 520; PO 10 × 480; DEV 10 × 440; QA 6 × 360; UX 5 × 420; TEC 6 × 190; RH 2 × 160; SG 4 × 170 | 0 | 14.144 | 17.680 | 24.752 | 18.269 |
| 5.3 UAT y acta de aceptación | 4 d / C | QA 4 × 360; PO 4 × 480; RH 2 × 160; SG 2 × 170; TEC 1.2 × 190; USR 22.5 × 150 | 0 | 6.098 | 7.623 | 10.672 | 7.877 |
| 5.4 Go-live y estabilización (4 semanas) | 20 d / C | PM 4 × 520; PO 6 × 480; DEV 30 × 440; QA 10 × 360; OPS 10 × 460; UX 4 × 420; TEC 6 × 190; RH 10 × 160 | 844 | 25.468 | 31.624 | 43.936 | 32.650 |
| 5.5 Tablero y transferencia del seguimiento | 10 d / B | PO 3 × 480; DEV 3 × 440; RH 4 × 160; TEC 2 × 190 | 0 | 3.213 | 3.780 | 4.914 | 3.874 |
| 5.6 Informe de ocupación y recomendación | 10 d / B | PO 2 × 480; DEV 2 × 440; SG 5 × 170 | 0 | 2.286 | 2.690 | 3.497 | 2.757 |

Control: 31 paquetes, USD 235.926 laborales + USD 136.774 no laborales = USD 372.700. PM de seguimiento: 132 días × 0,5 FTE × USD 520 = USD 34.320. R-3 no agrega horas. No se reducen duraciones ni se promete capacidad adicional. Para ejecutar el escenario P debe revalidarse carga y calendario; no autoriza recortes de plazo.


---



## 1.3 Partidas no laborales y trazabilidad contractual

| Partida / concepto | Cantidad × USD/unidad | USD | EDT | Período de devengo N4 |
| --- | --- | --- | --- | --- |
| P-1 Licencia WorkHub, 1.200 usuarios nominados (primer año de soporte incluido) | 1200 usuarios × 90 | 108.000 | 1.1 | 2026-10-01 a 2026-10-01 |
| P-2a Entorno de desarrollo (Azure Brasil Sur) | 7 meses × 150 | 1.050 | 5.1 | 2026-10-14 a 2027-04-30 |
| P-2b Entorno de QA / staging | 6 meses × 250 | 1.500 | 5.1 | 2026-10-14 a 2027-04-28 |
| P-2c Entorno de producción (alineado al hosting anual de N1: USD 5.060 / 12) | 2 meses × 422 | 844 | 5.4 | 2027-03-31 a 2027-04-30 |
| P-2d Observabilidad y logs (APM) | 7 meses × 300 | 2.100 | 5.1 | 2026-10-14 a 2027-04-30 |
| P-2e Herramientas de soporte del equipo (CI/CD, backlog, bóveda de secretos) | 42 usuario-mes × 40 | 1.680 | 5.1 | 2026-10-14 a 2027-04-30 |
| P-3a Piezas de la campaña de lanzamiento (diseño y producción) | 12 piezas × 300 | 3.600 | 4.3 | 2027-03-01 a 2027-03-19 |
| P-3b Materiales de capacitación (video-tutoriales y guías) | 8 materiales × 450 | 3.600 | 4.4 | 2026-11-10 a 2026-12-17 |
| P-3c Sesiones de capacitación a 1.200 colaboradores (logística) | 30 sesiones × 120 | 3.600 | 4.4 | 2027-03-22 a 2027-03-30 |
| P-3d Encuestas de intención de uso y pulso | 1 servicio × 900 | 900 | 4.1 | 2026-10-13 a 2026-10-26 |
| P-4a Prueba de intrusión externa (requisito RA-2) | 1 servicio × 7500 | 7.500 | 3.4 | 2026-11-13 a 2026-12-04 |
| P-4b Entornos sandbox de conectores (HRIS y Exchange) | 2 conectores × 1200 | 2.400 | 3.2 | 2026-10-30 a 2026-11-12 |

Asignación presupuestaria: ambientes y herramientas comunes se cargan a 5.1 para evitar duplicación por cada módulo, conservando su devengo real por período. P-4b se asigna a 3.2 como cuenta agrupadora para ambos conectores; el registro de partidas conserva su alcance. Producción usa 422 USD/mes redondeados de la hipótesis N1; se retiene el precio unitario N2 para reproducir sus USD 844.

Conciliación: K-1/K-3 a K-9 (no laborales) USD 136.774 + K-2 Tandem USD 216.888 + horas VCA USD 19.038 = USD 372.700. El precio fijo y las garantías se tratan como condiciones contractuales propuestas en N3, sin afirmar firma o transferencia efectiva. La contingencia no paga defectos ya incluidos en K-2/K-5.

Ajustes de calendario de costos: sandbox se devenga desde 30/10, coherente con necesidad de N3 (N2 partidas usaba 14/10); los USD 3.600 de logística de las 30 sesiones masivas se devengan del 22 al 30/03, después de balances y de UAT. Las piezas y formación de referentes permanecen antes. Las sesiones se replican por referentes formados, supuesto N3; su disponibilidad debe validarse. No cambia ningún total ni hito, pero se corrige la distribución mensual respecto de N2. La fecha de pago contractual no determina por sí sola el avance ganado.


---



## 1.4 Línea base distribuida y reservas

La línea base integra USD 372.700 de trabajo planificado y USD 22.000 de contingencia. Las actividades laborales se devengan linealmente en días hábiles de N2; las partidas se distribuyen en su período explícito. Es una aproximación del costo devengado, no un cronograma de pagos. La contingencia ahora se ubica en el mes de exposición del riesgo y no se prorratea como N2.

| Mes | Actividades USD | Contingencia USD | Línea base mensual USD | Acumulada USD |
| --- | --- | --- | --- | --- |
| 2026-10 | 157.676 | 0 | 157.676 | 157.676 |
| 2026-11 | 75.022 | 4.700 | 79.722 | 237.397 |
| 2026-12 | 46.021 | 2.500 | 48.521 | 285.918 |
| 2027-01 | 14.689 | 0 | 14.689 | 300.606 |
| 2027-02 | 5.546 | 0 | 5.546 | 306.153 |
| 2027-03 | 29.763 | 9.800 | 39.563 | 345.716 |
| 2027-04 | 43.984 | 5.000 | 48.984 | 394.700 |
| Total | 372.700 | 22.000 | 394.700 | 394.700 |

Control de reservas: USD 22.000 es una provisión agregada para acciones residuales concretas del registro, no la suma de pérdidas máximas ni P×I monetizado. La asignación es una propuesta de juicio experto pendiente de validar. Si el evento no ocurre, se libera saldo. PM puede autorizar hasta USD 5.000 por evento; más de ese monto va al Sponsor. Cambiar línea base, alcance o cierre, o impacto >5 %, requiere Comité. Gestión: USD 15.788 fuera de línea base; no se gana valor por mantenerla disponible.


---



## 2. Control de gestión mediante Valor Ganado

EVM, Earned Value Management (gestión del valor ganado), compara trabajo previsto, trabajo aceptado y costo incurrido a una misma fecha. No hay datos reales comprobados de avance o gasto de WorkHub en estas fuentes. El Excel separa entradas reales vacías de un ejemplo numérico rotulado ilustrativo.

| Indicador / unidad | Definición y cálculo | Uso |
| --- | --- | --- |
| PV · USD | Valor planificado: suma del presupuesto de cada tarea × avance previsto a la fecha. | Se calcula con períodos y criterios de medición aprobados; no con facturas pagadas. |
| EV · USD | Valor ganado: suma del presupuesto de cada tarea × avance físico aceptado. | 0/100 para entregables breves; hitos ponderados para módulos e integraciones; LOE de 1.5 solo por servicio de gestión prestado. |
| AC · USD | Costo real incurrido: horas valorizadas, facturas y provisiones devengadas por tarea. | Conciliar con Contabilidad, mismo alcance/corte; no inferir AC a partir de EV. |
| CV / SV · USD | Variación de costo CV=EV−AC; variación de cronograma SV=EV−PV. | Negativo es desfavorable. SV expresa dinero de trabajo pendiente, no días de atraso. |
| CPI / SPI · razón | Índice de costo CPI=EV/AC; índice de cronograma SPI=EV/PV. | <1 desfavorable; ≥1 requiere interpretar calidad y camino crítico, no solo gasto. |
| BAC / EAC / ETC / VAC · USD | BAC: presupuesto hasta la conclusión; EAC: estimación a la conclusión = BAC/CPI; ETC: costo estimado para completar = EAC−AC; VAC: variación a la conclusión = BAC−EAC. | Pronóstico por eficiencia pasada, útil si es representativa. Complementar estimación ascendente cuando cambia el contexto. |
| TCPI · razón | Índice de desempeño requerido para cumplir BAC: (BAC−EV)/(BAC−AC). | Solo si BAC−AC>0; si no, informar objetivo inviable y revisar EAC. |

**Convención BAC:** se sigue DPI6 p.20: BAC operativo = USD 372.700 (trabajo de las 31 tareas). Contingencia USD 22.000 permanece en línea base como reserva no distribuida; BAC operativo + reserva = USD 394.700. La curva anterior muestra línea base completa; para PV/EV usar solo trabajo distribuido, excluyendo reserva aún no autorizada. No se gana valor por el paso del tiempo sobre una reserva. Al activar respuesta, transferir presupuesto desde contingencia a tarea/paquete, con plan futuro y evidencia, sin alterar línea base total salvo cambio aprobado. Así BAC operativo aumenta y reserva disminuye por igual.


### Método de medición y evidencia

Antes de cada módulo 2.3-2.9 o conector 3.1-3.3: acordar hitos 20 % diseño aprobado, 50 % configuración/código integrado y revisión completa, 30 % pruebas de aceptación del paquete aprobadas. No acreditar porcentajes subjetivos. Para tareas de documentos y servicios breves, EV=0 hasta aceptación y 100 % al cerrar. Licencia gana valor cuando está habilitada y aceptada, no por anticipo. En tareas con partidas comunes, medir por separado disponibilidad del servicio y entregable laboral; el costo asignado a 5.1 no implica ganar siete meses de nube al crear el ambiente.


---



## 2.1 Cortes, alertas y escenario ilustrativo

El plan temporal por día hábil permite distribuir costos; para usarlo como PV de hitos discretos debe acordarse y cargar la fecha de aceptación planificada por componente. La hoja EVM recibe PV validado del plan por componente, EV aceptado y AC conciliado. No usa automáticamente el gasto mensual de la línea base completa como PV. El reporte operativo queda pendiente hasta cargar esa evidencia.

| Control | Responsable / frecuencia | Umbral propuesto y acción |
| --- | --- | --- |
| Cierre de estado | PM + QA + Contabilidad; viernes semanal y cierre mensual | QA confirma entregables, PM congela corte, Contabilidad concilia incurridos. Informe C-8 y mensual C-10. |
| Alerta de desempeño | PM; cada corte | CPI o SPI <0,95: analizar causas y plan en 2 días hábiles. <0,90: Sponsor en 48 h. Umbrales del equipo, no exigencia normativa. |
| Pronóstico y reservas | PM / Sponsor; mensual | EAC operativo + reserva residual >410.488: elevar al Comité. Cualquier cambio de línea base o hito se aprueba, no se oculta con reserva. |
| Cronograma crítico | PM; weekly y diario en UAT | Verificar R-3→5.3→5.4→5.5/5.6→1.6 y H-3; SPI no sustituye camino crítico ni calendario. |
| Calidad y cierre | QA / Sponsor; cada entrega | No ganar valor por código rechazado, trabajo rehacer ni porcentaje de gasto. Bloqueos de calidad prevalecen sobre semáforo EVM. |


### Ejemplo de cálculo, sin datos reales de WorkHub

| Entrada ilustrativa | Valor | Resultado calculado | Valor |
| --- | --- | --- | --- |
| BAC operativo | 372.700 | CPI / SPI | 0.9231 / 0.9000 |
| PV / EV / AC | 200.000 / 180.000 / 195.000 | CV / SV USD | −15.000 / −20.000 |
| Reserva no distribuida / gestión | 22.000 / 15.788 | EAC / ETC USD | 403.758 / 208.758 |
| Fecha de corte del ejemplo | 30/11/2026 (ficticia) | VAC USD / TCPI | -31.058 / 1.0844 |

Interpretación ilustrativa: el trabajo ganado equivale a 90 % de lo previsto y cada USD gastado gana USD 0.9231 presupuestados. Si esa eficiencia persistiera, EAC operativo sería USD 403.758; sumando una reserva residual hipotética intacta de USD 22.000, la necesidad sería USD 425.758, superior al presupuesto total de USD 410.488. Se requeriría decisión del Comité. Esta suma conservadora no aplica si el EAC ya incorpora las respuestas; evitar doble conteo. No equivale a afirmar un atraso de 20.000 días ni una fecha final nueva.


---



## 3. Plan de gestión de calidad del software

Calidad significa cumplir requisitos y expectativas de uso. El plan combina prevención en proceso y verificación de entregables (GDP Calidad pp.3-6). El objetivo es liberar reservas e integraciones seguras, datos confiables y una plataforma operable para 1.200 usuarios. Las dimensiones técnicas se organizan con ISO/IEC 25010:2023, edición 2, modelo de calidad de producto, y OWASP ASVS 5.0.0 como marco de verificación de seguridad web. No se afirma certificación, auditoría de norma íntegra ni cumplimiento de un nivel ASVS completo.


### Prevención, control y responsabilidad

| Etapa / momento | Mecanismo y evidencia | Responsabilidad y salida |
| --- | --- | --- |
| Diseño · 2.1/2.7 y 3.1 | Vincular requisito→EDT→caso de prueba→aceptación. Revisar reglas, arquitectura, flujos de datos y amenazas. Registro de observaciones y cierre. | PO y QA con Tecnología/Seguridad; diseño aprobado antes de construir componente. |
| Construcción · cada cambio | Revisión por pares distinta del autor, rama protegida, CI (integración continua), pruebas unitarias, análisis estático y de dependencias. Versionar configuración e infraestructura. | DEV/INT/OPS corrigen; par aprueba; QA audita semanalmente muestra de PR y excepciones. |
| Integración · 3.4/3.5 | Pruebas de contrato, punta a punta, concurrencia, carga y seguridad independientes. Ambiente equivalente a producción y datos sintéticos/desidentificados autorizados. | QA coordina, tercero K-5 prueba seguridad y Tecnología valida resultados. |
| Piloto y UAT · 5.2/5.3 | 300 usuarios piloto; UAT 120 usuarios. Casos y encuestas versionados, defectos con severidad, evidencia y repetición. | RR.HH./SG validan uso; QA verifica criterios; Sponsor firma aceptación UAT. |
| Pase y estabilización · 5.4 | Checklist de versión, aprobaciones, respaldo, restauración, observabilidad, mesa N1 y reversión. Comparar métricas con umbrales. | DevOps prepara; Tecnología autoriza pase; Sponsor acepta cierre con evidencia. |

Tratamiento de defectos: bloqueante impide función crítica o compromete integridad/seguridad; alto afecta criterio sin alternativa aceptable; medio tiene alternativa; bajo es cosmético sin pérdida funcional. QA clasifica con PO y Seguridad. Bloqueantes y altos deben cerrarse y repetir pruebas antes del pase. Medios/bajos solo con aceptación escrita, responsable y fecha; nunca exceptuar un requisito crítico. Registrar hallazgo, versión, caso, severidad, dueño, vencimiento y evidencia de re-test.

Presupuesto de calidad: revisiones y pruebas están en días DEV/QA/INT de cada tarea, pruebas integradas en 3.4/3.5 y K-5 USD 7.500; herramientas en P-2e y observabilidad P-2d. No agregar nuevamente estos costos como reserva. Auditoría semanal de proceso por QA: verificar evidencia de PR, trazabilidad de casos y cierres; el PM sigue acciones, sin suponer que esas auditorías ya ocurrieron.


---



## 3.1 Métricas y puertas de aceptación

Los porcentajes 100 % de revisión, 80 % de líneas, 70 % de ramas y demás métodos nuevos son decisiones propuestas del equipo por criticidad e integraciones; no porcentajes impuestos por ISO ni por la clase. Las metas heredadas se identifican. Los valores se validarán con VCA y Tandem antes de ejecutar.

| ID / dimensión | Umbral y alcance | Medición / evidencia | Quién y cuándo / incumplimiento |
| --- | --- | --- | --- |
| Q-1 Revisión por pares | 100 % de cambios propios de código, scripts, infraestructura y configuración versionable aprobados por al menos un par distinto del autor. | PR aprobados / PR integrados ×100; checklist y trazabilidad a requisito. Excluir binarios del fabricante; revisar su configuración y versión. | DEV/INT/OPS ejecutan, PO controla. En cada PR; ramas protegidas. Si falta aprobación, no integrar. |
| Q-2 Pruebas unitarias | ≥80 % de líneas y ≥70 % de ramas del código propio; 100 % de reglas críticas de reserva, permisos e idempotencia con casos positivos y negativos. | Informe CI; cobertura sobre código ejecutable propio; exclusiones generadas/documentadas aprobadas por QA. Casos críticos pasados / inventario crítico =100 %. | DEV/INT ejecutan, QA verifica. En cada build; si incumple, bloquear candidato y añadir pruebas. |
| Q-3 Conformidad funcional | 100 % de casos críticos de extremo a extremo aprobados; cero solapamientos de reservas; error de sincronización ≤0,5 %. | Suite con SSO, altas/bajas, reserva/cancelación, check-in y doble reserva. Errores / registros procesados ×100. Evidencia de datos y logs. | QA e Integraciones; Tecnología acepta. Cada integración y antes de piloto/UAT. Fallo crítico impide pase. |
| Q-4 Seguridad | Cero hallazgos críticos o altos abiertos. ASVS v5.0.0-8.1.1: permisos documentados; 8.2.1: función con permiso explícito; 8.2.2: autorización por objeto; 8.3.1: control en servicio confiable. | Prueba independiente K-5; usuario A no cancela reserva B; rol sin permiso no administra salas; acceso directo a API tampoco elude control. Análisis estático/dependencias y re-test. No se afirma nivel ASVS completo. | Tercero prueba; Seguridad VCA acepta. Antes de piloto: controles de acceso y revisión preliminar; informe final al 04/12, re-test antes de UAT. Si falla, bloquear. |
| Q-5 Rendimiento | p95<500 ms a 300 concurrentes (CE-3), y p95<800 ms a 500 concurrentes (aceptación 3.0); error técnico <1 % en cada escenario. | Carga 30 min tras 5 min de calentamiento, mezcla reproducible reserva/búsqueda/cancelación; mismo tamaño de datos y topología prevista. p95 sobre solicitudes exitosas y errores por separado. | QA mide; DevOps ajusta; Tecnología acepta. 3.5 y candidato final. Repetir tras cambio de consulta, configuración o capacidad. |
| Q-6 Confiabilidad y resiliencia | Disponibilidad ≥99,5 % durante estabilización; recuperación ≤4 h y pérdida de datos ≤24 h en ensayo de restauración. | Disponibilidad=(minutos acordados−indisponibilidad no planificada)/minutos acordados. Ventana24×7, sin excluir incidentes propios. Logs y prueba de restauración en staging. | DevOps; Tecnología VCA acepta. Monitoreo diario; ensayo antes de go-live. Incumplimiento genera incidente y plan correctivo. |
| Q-7 Datos e inventario | Discrepancia inventario ≤1 % y ocupación real versus sistema ≤5 %. | Inventario: diferencias / puestos relevados. Ocupación: diferencia absoluta / conteo manual, por planta y franja; al menos 5 días de muestra. Cero manual se informa aparte. | Servicios Generales; PO concilia. Inventario antes de piloto; ocupación semanal en piloto y estabilización. No emitir recomendación con muestra insuficiente. |
| Q-8 Aceptación y usabilidad | UAT ≥9,0/10 con al menos 120 usuarios; mediana de reserva + check-in ≤2 min; 100 % de escenarios críticos ejecutados; cero defectos bloqueantes. | Puntaje medio de cuestionario aprobado por RR.HH.; lista de participantes y evidencia por caso. No sustituir ejecución por satisfacción. | QA coordina, RR.HH. verifica; Sponsor firma. 16-19/03; evaluación diaria. Si falla, corregir, repetir casos y gestionar impacto en H-5. |


---



## 4. Riesgos: escalas, prioridad y mapa

Se conservan RI-1 a RI-17 de N3 y se agregan RI-18/19. Riesgo inherente = exposición antes de las respuestas N4. Probabilidad P e impacto I se valoran de 1 a 5 para todo el horizonte hasta 30/04/2027. Las probabilidades son juicio académico, no frecuencias observadas. N3 alta se lleva a P4, media a P3 y baja a P2; se revalidarán con evidencia. No se usa P5 para eventos ya ocurridos.

| Valor | Probabilidad orientativa | Impacto: tomar máximo en costo, plazo o calidad |
| --- | --- | --- |
| 1 | Muy baja: ≤10 % | Costo adicional ≤1.000 USD; demora ≤1 día; defecto menor sin criterio de aceptación afectado. |
| 2 | Baja: >10 a 30 % | >1.000 a 3.000 USD; >1 a 3 días; componente secundario con alternativa operativa. |
| 3 | Media: >30 a 50 % | >3.000 a 8.000 USD; >3 a 5 días; retrabajo de módulo recuperable antes del hito. |
| 4 | Alta: >50 a 80 % | >8.000 a 15.000 USD; >5 a 10 días o riesgo de H-3; aceptación de módulo principal comprometida. |
| 5 | Muy alta: >80 a <100 % | >15.000 USD; >10 días o cualquier desvío H-5/H-6/H-7; bloqueo de seguridad, integridad o beneficio principal. |

Prioridad = P×I: baja 1-5 (seguimiento mensual), media 6-12 (semanal), alta 15-25 (semanal con Sponsor; diaria ante disparador). Las celdas 13/14 no son posibles con enteros 1-5. Una consecuencia crítica de seguridad o un hito obligatorio se escala aunque el producto sea medio. P e I residuales son metas posteriores a respuesta, no evidencia de reducción ya lograda. Los USD de reserva son límites de acción, no equivalentes al puntaje.


### Matriz inherente

| P / I | I=1 | I=2 | I=3 | I=4 | I=5 |
| --- | --- | --- | --- | --- | --- |
| P=5 | 5;  | 10;  | 15;  | 20;  | 25;  |
| P=4 | 4;  | 8;  | 12;  | 16; RI-3, RI-7 | 20;  |
| P=3 | 3;  | 6;  | 9; RI-6, RI-16 | 12; RI-2, RI-10, RI-11, RI-12, RI-13, RI-14, RI-19 | 15; RI-1, RI-5, RI-8, RI-9, RI-17, RI-18 |
| P=2 | 2;  | 4;  | 6;  | 8; RI-15 | 10; RI-4 |
| P=1 | 1;  | 2;  | 3;  | 4;  | 5;  |

Verde: baja · ámbar: media · rojo: alta. Eje vertical: probabilidad creciente hacia arriba; horizontal: impacto creciente hacia la derecha. Se adapta el artefacto GDP Incertidumbre pp.10-18 a la escala 1-5 exigida por N4. La estrategia se decide por causa y capacidad de respuesta; el cuadrante no impone automáticamente una estrategia.


---



## 4.1 Registro y respuestas · RI-1 a RI-5

Estado de todos: identificado / plan propuesto, pendiente de validación. P/I son inherentes; R=P×I; residual=P/I meta. Los montos son límites incrementales de contingencia VCA. La prevención habitual ya está en M; el gasto residual solo se autoriza ante disparador y no duplica obligación del proveedor.


### RI-1 · P3 / I5 / R15 · Mitigar · residual 2/4 · reserva USD 2.000

**Causa, evento y efecto:** Omisión de check-in o geocerca imprecisa produce registros de ocupación inexactos y una discrepancia >5 % que invalida la recomendación de planta 4. **EDT:** 2.5,5.4,5.6. **Dueño:** PO / Servicios Generales.

**Plan preventivo:** Activar recordatorios y liberación automática. Validar QR y conteo manual en piloto. **Disparador y respuesta:** Si discrepancia >5 % en dos muestras: congelar informe, ampliar conteo manual y corregir reglas.

**Monitoreo y evidencia:** Semanal en piloto y estabilización; SG concilia registros con muestra estratificada por planta. **Mes de exposición:** 2027-04.


### RI-2 · P3 / I4 / R12 · Mitigar · residual 2/3 · reserva USD 2.400

**Causa, evento y efecto:** Permisos insuficientes, límites o incompatibilidad de Entra ID, HRIS o Graph bloquean conectores y requieren retrabajo. **EDT:** 3.1-3.5,5.2. **Dueño:** Tecnología VCA.

**Plan preventivo:** Probar autenticación, cuotas y contratos API en sandbox antes de integrar. **Disparador y respuesta:** Si error de permisos persiste >1 día: escalar al fabricante y habilitar cuota/entorno adicional autorizado.

**Monitoreo y evidencia:** Semanal C-4 y diario durante integración; log de fallos y bloqueos. **Mes de exposición:** 2026-11.


### RI-3 · P4 / I4 / R16 · Mitigar · residual 3/3 · reserva USD 1.800

**Causa, evento y efecto:** Temor al control de presentismo y pérdida del puesto fijo genera resistencia y adopción inferior al 70 %. **EDT:** 4.1-4.5,5.3. **Dueño:** RR.HH. VCA.

**Plan preventivo:** Comunicar uso agregado de datos, política y referentes. Medir intención antes del piloto. **Disparador y respuesta:** Si intención <70 % o UAT <9: sesiones focalizadas y piezas aclaratorias antes del lanzamiento.

**Monitoreo y evidencia:** Quincenal C-13/C-15; encuestas y motivos de rechazo. **Mes de exposición:** 2027-03.


### RI-4 · P2 / I5 / R10 · Aceptar pasiva · residual 2/5 · reserva USD 0

**Causa, evento y efecto:** Pico de demanda o cláusula de alquiler impide devolver planta 4 aunque WorkHub funcione. **EDT:** 5.6. **Dueño:** Sponsor / Servicios Generales.

**Plan preventivo:** No se presupone devolución ni ahorro realizado. El informe conserva escenarios de ocupación. **Disparador y respuesta:** Si demanda excede capacidad o contrato impide salida: Sponsor revisa el caso de negocio, sin gasto automático del proyecto.

**Monitoreo y evidencia:** Mensual al Comité; informe de demanda y revisión contractual. **Mes de exposición:** 2027-04.


### RI-5 · P3 / I5 / R15 · Aceptar activa · residual 3/5 · reserva USD 0

**Causa, evento y efecto:** Extensión del cierre de balances más allá del 15/03 bloquea UAT crítica y desplaza hitos. **EDT:** 5.3,5.4,1.6. **Dueño:** Sponsor.

**Plan preventivo:** Reservar ventana y participantes por escrito. Preparar casos y ambiente sin despliegue masivo durante balances. **Disparador y respuesta:** Si al 08/03 no se confirma 16/03: escalar al Sponsor en 48 h y tramitar cambio de hitos. No comprar una fecha ficticia.

**Monitoreo y evidencia:** Semanal desde febrero y diario al 15/03; confirmación de Finanzas. **Mes de exposición:** 2027-03.


---



## 4.2 Registro y respuestas · RI-6 a RI-10

Estado de todos: identificado / plan propuesto, pendiente de validación. P/I son inherentes; R=P×I; residual=P/I meta. Los montos son límites incrementales de contingencia VCA. La prevención habitual ya está en M; el gasto residual solo se autoriza ante disparador y no duplica obligación del proveedor.


### RI-6 · P3 / I3 / R9 · Mitigar · residual 2/3 · reserva USD 0

**Causa, evento y efecto:** Solape SS+5 inicia escritorios antes de cerrar reglas y cambios tardíos generan retrabajo que amenaza H-3. **EDT:** 2.1,2.3,5.2. **Dueño:** PO.

**Plan preventivo:** Validar reglas críticas en primera semana y versionar decisiones. **Disparador y respuesta:** Si regla cambia después de diseño: analizar impacto, corregir dentro de K-2; cambio de alcance solo por comité.

**Monitoreo y evidencia:** Semanal; registro de cambios y holgura restante del piloto. **Mes de exposición:** 2026-11.


### RI-7 · P4 / I4 / R16 · Mitigar · residual 2/4 · reserva USD 1.500

**Causa, evento y efecto:** Vacaciones y feriados reducen participación de 300 usuarios del piloto y ponen H-3 del 19/12 en riesgo. **EDT:** 5.2. **Dueño:** PO.

**Plan preventivo:** Confirmar participantes y suplentes antes del 18/11; distribuir casos por sesión. **Disparador y respuesta:** Si ejecución <90 % de casos programados en weekly: recuperar sesiones VCA antes del 18/12; si no alcanza, escalar H-3.

**Monitoreo y evidencia:** Diario C-2 durante piloto; asistencia y casos ejecutados. **Mes de exposición:** 2026-12.


### RI-8 · P3 / I5 / R15 · Mitigar · residual 2/5 · reserva USD 2.500

**Causa, evento y efecto:** UAT concentrada en cuatro días y 120 usuarios deja sesiones incompletas o puntaje <9 y demora el go-live. **EDT:** 5.3,5.4. **Dueño:** QA / RR.HH..

**Plan preventivo:** Confirmar 120 usuarios y suplentes, datos y casos listos al 15/03; sesiones paralelas de 90 min. **Disparador y respuesta:** Si al segundo día se ejecutó <50 % de casos o nota proyectada <9: recuperar sesiones y ampliar dedicación VCA autorizada; no omitir aceptación.

**Monitoreo y evidencia:** Diario 16-19/03; tablero de casos, defectos y puntajes. **Mes de exposición:** 2027-03.


### RI-9 · P3 / I5 / R15 · Transferir · residual 2/5 · reserva USD 0

**Causa, evento y efecto:** Vulnerabilidades de configuración o bot producen hallazgos críticos/altos e impiden RA-2. **EDT:** 3.4,2.8,2.9. **Dueño:** Seguridad VCA / Integraciones.

**Plan preventivo:** Exigir en K-2 corrección de defectos y en K-5 prueba independiente y re-test incluidos; criterios Q-4. **Disparador y respuesta:** Hallazgo crítico/alto: bloquear pase y exigir corrección y re-test al proveedor. Transferencia propuesta por contrato, sin suponer contrato firmado.

**Monitoreo y evidencia:** Semanal desde 13/11; informe del tercero y cierre validado por Seguridad. **Mes de exposición:** 2026-12.


### RI-10 · P3 / I4 / R12 · Mitigar · residual 2/3 · reserva USD 2.000

**Causa, evento y efecto:** Consulta de planos y dimensionamiento insuficiente no alcanzan p95<500 ms a 300 usuarios y exige capacidad extra. **EDT:** 3.5,5.1,5.4. **Dueño:** DevOps.

**Plan preventivo:** Ejecutar carga representativa y perfilar consultas antes de UAT. **Disparador y respuesta:** Si p95≥500 ms a 300 concurrentes o ≥800 ms a 500: optimizar en K-2 y habilitar capacidad Azure adicional por consumo, con tope autorizado.

**Monitoreo y evidencia:** Cada build candidato y durante estabilización; p95, errores y costo diario. **Mes de exposición:** 2027-03.


---



## 4.3 Registro y respuestas · RI-11 a RI-15

Estado de todos: identificado / plan propuesto, pendiente de validación. P/I son inherentes; R=P×I; residual=P/I meta. Los montos son límites incrementales de contingencia VCA. La prevención habitual ya está en M; el gasto residual solo se autoriza ante disparador y no duplica obligación del proveedor.


### RI-11 · P3 / I4 / R12 · Mitigar · residual 2/3 · reserva USD 1.800

**Causa, evento y efecto:** Datos HRIS o planos desactualizados causan errores de sincronización >0,5 % o inventario >1 % y reservas inválidas. **EDT:** 2.2,3.2. **Dueño:** Tecnología / Servicios Generales.

**Plan preventivo:** Perfilar datos, validar inventario y hacer carga de ensayo con conciliación. **Disparador y respuesta:** Si se excede umbral: detener importación, corregir fuente VCA y repetir conciliación antes de habilitar.

**Monitoreo y evidencia:** Por importación y semanal en piloto; conteo esperado versus recibido. **Mes de exposición:** 2026-11.


### RI-12 · P3 / I4 / R12 · Mitigar · residual 2/4 · reserva USD 0

**Causa, evento y efecto:** Reservas simultáneas WorkHub/Exchange producen dobles reservas y violan CE-2. **EDT:** 2.4,3.3. **Dueño:** Integraciones.

**Plan preventivo:** Pruebas de concurrencia, idempotencia, reintento y conciliación bidireccional. **Disparador y respuesta:** Un solapamiento confirmado: bloquear conector afectado, aplicar corrección K-2 y repetir casos de carrera.

**Monitoreo y evidencia:** Cada despliegue y diario en piloto; alertas de duplicados. **Mes de exposición:** 2026-12.


### RI-13 · P3 / I4 / R12 · Mitigar · residual 2/3 · reserva USD 1.500

**Causa, evento y efecto:** Ausencia de referentes VCA con dedicación limitada o rotación de Tandem demora validaciones y pierde conocimiento. **EDT:** 2.1,5.2,5.3. **Dueño:** PM.

**Plan preventivo:** Nombrar suplentes y mantener runbooks y revisión cruzada dentro de tareas existentes. **Disparador y respuesta:** Ausencia >2 días en ruta sensible: activar suplente; financiar solo transferencia adicional VCA, reemplazo Tandem a cargo K-2.

**Monitoreo y evidencia:** Weekly; disponibilidad confirmada dos semanas hacia adelante. **Mes de exposición:** 2027-03.


### RI-14 · P3 / I4 / R12 · Evitar · residual 1/4 · reserva USD 0

**Causa, evento y efecto:** Geocerca sin conformidad de Legal o Seguridad impide su uso y requiere rediseño del check-in. **EDT:** 2.5,4.2. **Dueño:** Seguridad / RR.HH..

**Plan preventivo:** Impedir activación de geocerca hasta aprobación formal; usar QR ya previsto en entorno de prueba. **Disparador y respuesta:** Si se rechaza geocerca: tramitar decisión de alcance y comunicación; no remover requisito unilateralmente ni recolectar ubicación.

**Monitoreo y evidencia:** Antes de piloto y cada cambio de tratamiento de datos; acta de aprobación. **Mes de exposición:** 2026-11.


### RI-15 · P2 / I4 / R8 · Mitigar · residual 1/4 · reserva USD 1.000

**Causa, evento y efecto:** Actualización de WorkHub o API del bot genera regresiones y repetición de pruebas cerca del go-live. **EDT:** 2.x,3.x,5.4. **Dueño:** PO.

**Plan preventivo:** Fijar versión soportada, congelar cambios y mantener regresión automatizada. **Disparador y respuesta:** Aviso de versión incompatible: analizar en sandbox y postergar actualización; entorno de pruebas extendido si no es posible.

**Monitoreo y evidencia:** Semanal; avisos fabricante y resultados de regresión. **Mes de exposición:** 2027-03.


---



## 4.4 Registro y respuestas · RI-16 a RI-19

Estado de todos: identificado / plan propuesto, pendiente de validación. P/I son inherentes; R=P×I; residual=P/I meta. Los montos son límites incrementales de contingencia VCA. La prevención habitual ya está en M; el gasto residual solo se autoriza ante disparador y no duplica obligación del proveedor.


### RI-16 · P3 / I3 / R9 · Mitigar · residual 2/3 · reserva USD 500

**Causa, evento y efecto:** Demora de cotizaciones o firma K-5/K-7 impide sandbox y pentest a tiempo. **EDT:** 3.2-3.4,4.4. **Dueño:** PM.

**Plan preventivo:** Preparar alcance y aprobaciones antes de fechas N3: sandbox 23/10, pentest 06/11. **Disparador y respuesta:** Si no se adjudica a fecha objetivo: escalar a Sponsor y activar proveedor alternativo aprobado; solo costo administrativo adicional de VCA.

**Monitoreo y evidencia:** Dos veces por semana hasta adjudicar; orden y fecha comprometida. **Mes de exposición:** 2026-11.


### RI-17 · P3 / I5 / R15 · Aceptar activa · residual 2/4 · reserva USD 3.000

**Causa, evento y efecto:** Defectos y dudas al corte simultáneo superan mesa de ayuda y degradan disponibilidad <99,5 %. **EDT:** 4.5,5.4. **Dueño:** DevOps / Tecnología VCA.

**Plan preventivo:** Reservar guardia VCA adicional y ensayar reversión con runbook. K-2 mantiene corrección de defectos. **Disparador y respuesta:** Si incidente crítico o cola >20 tickets por 2 h: activar guardia, priorizar incidente y ejecutar rollback si integridad está comprometida.

**Monitoreo y evidencia:** Diario primera semana y weekly de estabilización; disponibilidad y cola. **Mes de exposición:** 2027-04.


### RI-18 · P3 / I5 / R15 · Mitigar · residual 1/5 · reserva USD 1.000

**Causa, evento y efecto:** Error de pipeline, secreto o configuración despliega una versión no aprobada y causa caída o acceso indebido. **EDT:** 5.1,5.4. **Dueño:** DevOps.

**Plan preventivo:** Separar ambientes y credenciales; aprobación de dos personas, artefacto firmado y ensayo de rollback. **Disparador y respuesta:** Build sin evidencia o diferencia de configuración: detener pase; recuperar secretos/tenant con soporte externo si excede capacidad VCA.

**Monitoreo y evidencia:** Cada despliegue; auditoría de pipeline y prueba de restauración. **Mes de exposición:** 2027-03.


### RI-19 · P3 / I4 / R12 · Mitigar · residual 2/4 · reserva USD 1.000

**Causa, evento y efecto:** Dependencia vulnerable o sin soporte aparece en análisis de componentes y obliga a detener liberación. **EDT:** 2.8,2.9,3.4. **Dueño:** Integraciones / Seguridad.

**Plan preventivo:** Inventariar componentes y versiones, analizar dependencias en CI y revisar avisos semanales. **Disparador y respuesta:** Hallazgo alto/crítico: bloquear release; proveedor corrige bajo K-2; financiar solo evaluación independiente de alternativa de tercero si se requiere.

**Monitoreo y evidencia:** Por build y semanal; inventario y reporte de composición. **Mes de exposición:** 2026-12.

Suma de asignaciones: USD 22.000. RI-5 tiene aceptación activa con plan de contingencia de fecha y escalamiento, sin reserva monetaria específica: dinero no elimina el bloqueo de balances. RI-4 es aceptación pasiva del beneficio, vigilada por el Sponsor. La transferencia RI-9 reduce exposición económica propuesta, conserva riesgo de calidad y responsabilidad de aceptación en VCA.


---



## 4.5 Base de cálculo de la contingencia

Los USD 22.000 conservan el techo de provisión heredado y se desagregan en una propuesta inicial de paquetes de respuesta. Cada cantidad es capacidad incremental condicionada al disparador, sin evidencia de gasto ni cotización. Las tarifas de roles existentes son las de N2; los servicios y perfiles nuevos son hipótesis explícitas. Esta suma no constituye valor monetario esperado ni demuestra suficiencia estadística. Reestimar de forma independiente al validar los riesgos; si el costo necesario supera la provisión, elevar cambio, sin forzar el resultado a USD 22.000.

| Riesgo | Cantidad incremental × tarifa/precio | USD | Exclusión y fundamento |
| --- | --- | --- | --- |
| RI-1 | 8 días SG × USD 170; 4 días RH × USD 160 | 2.000 | Conteo manual adicional VCA; no corrección de software K-2; Validación adicional de muestra VCA |
| RI-2 | 2 entornos adicionales × USD 1200 | 2.400 | Dos entornos extra por incompatibilidad, además de los dos sandbox iniciales P-4b; precio unitario supuesto |
| RI-3 | 4 piezas adicionales × USD 300; 5 sesiones adicionales × USD 120 | 1.800 | Ampliación focalizada de campaña, fuera de 12 piezas P-3a; Logística extra a las 30 sesiones P-3c |
| RI-7 | 10 días-persona USR × USD 150 | 1.500 | Recuperación extraordinaria de piloto; no horas ya planificadas |
| RI-8 | 10 días-persona USR × USD 150; 4 días SG × USD 170; 2 días RH × USD 160 | 2.500 | Sesiones adicionales a 22,5 días-persona UAT base; Apoyo adicional UAT; Coordinación adicional UAT |
| RI-10 | 2 meses capacidad adicional × USD 1000 | 2.000 | Incremento cloud marzo/abril, fuera de P-2c; capacidad y precio por validar |
| RI-11 | 5 días SG × USD 170; 5 días TEC × USD 190 | 1.800 | Corrección adicional de fuente de inventario VCA; Corrección adicional de fuente HRIS VCA |
| RI-13 | 2 días TEC × USD 190; 7 días RH × USD 160 | 1.500 | Transferencia extraordinaria VCA; sustitución Tandem cubierta K-2; Inducción adicional de referente VCA |
| RI-15 | 1 extensión sandbox × USD 1000 | 1.000 | Extensión extraordinaria de prueba de nueva versión, distinta de P-4b inicial; precio supuesto |
| RI-16 | 2 días Compras/Legal VCA × USD 250 | 500 | Costo interno adicional supuesto; no PM Tandem ya incluido |
| RI-17 | 8 días TEC × USD 190; 4 días SG × USD 170; 5 días RH × USD 160 | 3.000 | Guardia VCA extra primera semana; no corrección de defectos K-2; Guardia VCA adicional; Guardia adicional de referentes |
| RI-18 | 1 servicio recuperación tenant × USD 1000 | 1.000 | Soporte externo extraordinario a VCA; no retrabajo de pipeline contratado K-2 |
| RI-19 | 2 días especialista independiente × USD 500 | 1.000 | Evaluación adicional de alternativa de tercero; no corrección propia ni re-test K-5 |

Activar una respuesta no presupone disponibilidad ilimitada. PM debe confirmar capacidad y fechas de los recursos adicionales antes de autorizar; si afecta un hito obligatorio, escala aunque el monto sea menor a USD 5.000. No sumar a esta tabla diferencias PERT ni costos ya comprometidos. RI-4/5/6/9/12/14 no tienen provisión incremental: su plan usa decisiones de negocio, escalamiento o obligaciones incluidas en M. Fechas anteriores al 27/10 son fechas del plan base; no se comprobó su ejecución. Verificar de inmediato RI-16 y contratos antes de usar este plan operativamente.


---



## 5. Justificación del Juicio de Experto y validación

La técnica usa conocimiento especializado para estimar y decidir cuando los datos históricos son insuficientes. Complementa el cálculo y no reemplaza al equipo (DPI11 pp.4-5 y 14). WorkHub combina configuración de producto comprado, APIs, datos VCA y una ventana crítica de balances; por eso una tarifa × esfuerzo no basta para establecer rangos, impacto o respuesta. No se inventan entrevistas: los rangos, puntajes, reservas y umbrales de esta entrega son hipótesis académicas del Grupo 1, pendientes de contraste con los perfiles indicados.

| Consulta propuesta | Decisión que sustenta | Evidencia necesaria / criterio de revisión |
| --- | --- | --- |
| PM + responsable comercial Tandem + Finanzas VCA | Tarifas, K-2 fijo, alcance de garantías y O/M/P; contingencia a cargo VCA. | Oferta y SOW revisados; matriz de exclusiones; estimaciones independientes por paquete, luego consenso documentado. |
| Integraciones + Tecnología VCA + fabricantes | Rangos clase C, RI-2/12/15/19 y cuotas sandbox. | Contratos API, ensayo técnico y supuestos de permisos/versiones; ajustar P/I y costos por evidencia. |
| QA + Seguridad + tercero independiente | Umbrales, aplicabilidad ASVS y RI-9/18/19. | Inventario de controles, informe de pruebas y capacidad del pipeline; revisar severidad sin ocultar bloqueos. |
| RR.HH. + SG + Sponsor | RI-1/3/4/5/7/8/11/13/17; costos y disponibilidad VCA. | Muestra de datos, agenda de UAT, disponibilidad de referentes, ventana de balances y capacidad de soporte. |

Protocolo propuesto: cada perfil estima primero de forma independiente, identifica causa y exclusiones, y explica O/M/P o P/I. El PM compara discrepancias; el equipo acuerda y registra rango, fecha, autor, fuente, desacuerdos y responsable de aprobación. Separar estimador proveedor de aceptante VCA reduce sesgo comercial y anclaje al presupuesto N1. Repetir ante nuevo contrato/API, evidencia de piloto, disparador o cambio relevante. Pendientes antes de uso operativo: cotizaciones, firma de contratos, disponibilidad de UAT/referentes, controles ASVS aplicables y calendario corporativo.

Cambio de prioridad frente a N3: RI-9 y RI-17 pasan de media a alta al puntuar I=5 por bloqueo de seguridad y afectación del go-live; RI-15 pasa de baja a media porque la regresión próxima al pase tiene I=4 aunque conserve probabilidad baja. La escala formal explica estos cambios; no son incidentes observados. Los riesgos ligados al software son RI-1/2/6/9/10/11/12/14/15/17/18/19; los restantes amplían el contexto operativo y de negocio.


### Fuentes y alcance de la verificación

Consigna N4, 27/10/2026, puntos 1-3. Devoluciones docentes N1 y N2 completas. N2 corregida PDF pp.7-9 y Excel original; N3 revisión 2 PDF pp.2-4 y 12-13. DPI5 pp.10-11 (estimación), 16-18 (reservas), 20-22 (curva); DPI6 pp.10-17 y 20-23 (EVM); DPI11 pp.4-5 y 14 (juicio experto). Colección GDP complementaria, numeración independiente: Incertidumbre pp.10-18 (escalas y matriz) y 19-21 (respuestas), Entrega/Calidad pp.3-6. Se inspeccionaron originales para fórmulas y formatos; no se atribuyen umbrales propios a las clases.

ISO/IEC 25010:2023, edición 2, ficha pública oficial: [iso.org/standard/78176.html](https://www.iso.org/standard/78176.html) (consulta 27/10/2026). Se usa el alcance público del modelo de producto, sin citar cláusulas no consultadas. OWASP ASVS 5.0.0, publicación 30/05/2025: [asvs.owasp.org](https://asvs.owasp.org/). Controles de autorización verificados en [fuente oficial etiquetada v5.0.0, V8](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x17-V8-Authorization.md) (consulta 27/10/2026). No se afirma verificación completa. ISO 9000:2000 figura como ejemplo en consigna; se elige un marco específico de calidad de producto software.
