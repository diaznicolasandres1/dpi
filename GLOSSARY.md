# Glossary and Formulas

## Project definition and scope

**Business Case:** justificación del proyecto basada en inversión, beneficios, riesgos y creación de valor.

**Project Charter / Acta de Constitución:** documento que autoriza formalmente el proyecto, identifica objetivos, autoridad, hitos y restricciones iniciales.

**SMART objective:** objetivo específico, medible, alcanzable, relevante y limitado en el tiempo.

**Scope statement / Declaración del Alcance:** definición del producto, entregables, límites, exclusiones y criterios de aceptación.

**WBS / EDT:** descomposición jerárquica del alcance en entregables y paquetes de trabajo.

**Acceptance criteria:** condiciones cuantitativas o verificables que debe cumplir un entregable para ser aceptado.

## Schedule

**AON network:** red de precedencias donde los nodos representan actividades y las flechas representan relaciones.

**ES / Inicio temprano:** primer momento en que puede comenzar una actividad.

**EF / Fin temprano:** primer momento en que puede terminar una actividad.

**LS / Inicio tardío:** último momento en que puede comenzar una actividad sin retrasar el proyecto.

**LF / Fin tardío:** último momento en que puede finalizar una actividad sin retrasar el proyecto.

**Total float / Holgura total:** margen disponible antes de afectar la fecha final. En el cálculo convencional: `LS - ES` o `LF - EF`.

**Critical path / Camino crítico:** secuencia que determina la duración del proyecto. Debe revisarse al incorporar calendarios, restricciones y recursos.

**Relationship types:** FS (fin a inicio), SS (inicio a inicio), FF (fin a fin) y SF (inicio a fin).

## Costs and reserves

**Activity estimate:** costo estimado de una actividad mediante técnicas como estimación análoga, paramétrica o PERT.

**Contingency reserve:** reserva para riesgos identificados. Forma parte de la línea base de costos.

**Management reserve:** reserva para trabajo imprevisto dentro del alcance. Se ubica fuera de la línea base de costos.

**Cost baseline:** estimación de actividades más reserva para contingencias.

**Total project budget:** línea base de costos más reserva de gestión.

**Bottom-up estimate:** estimación ascendente construida desde actividades o paquetes de trabajo. Debe validar la estimación descendente y no ajustarse artificialmente para igualarla.

**S-curve:** representación del costo planificado o real acumulado a lo largo del tiempo.

## Earned Value Management

**BAC — Budget at Completion:** presupuesto aprobado para el trabajo medido.

**PV — Planned Value:** valor presupuestado del trabajo planificado a la fecha de corte.

**EV — Earned Value:** valor presupuestado del trabajo realmente completado.

**AC — Actual Cost:** costo real del trabajo completado.

**CV — Cost Variance:** `EV - AC`. Un valor negativo indica sobrecosto.

**SV — Schedule Variance:** `EV - PV`. Se expresa en unidades monetarias, no directamente en días.

**CPI — Cost Performance Index:** `EV / AC`. Un valor inferior a 1 indica ineficiencia de costos.

**SPI — Schedule Performance Index:** `EV / PV`. Un valor inferior a 1 indica avance menor al planificado.

**EAC — Estimate at Completion:** pronóstico del costo total al cierre. La fórmula depende del supuesto de desempeño futuro.

**ETC — Estimate to Complete:** costo esperado del trabajo restante. En una formulación básica: `EAC - AC`.

**VAC — Variance at Completion:** `BAC - EAC`.

**TCPI — To Complete Performance Index:** desempeño de costos requerido para alcanzar una meta de cierre.

## Stakeholders and work

**Stakeholder:** persona, grupo u organización que puede afectar o ser afectada por el proyecto.

**Project work performance domain:** coordinación de procesos, recursos, aprendizaje, comunicación y cambios necesarios para producir los entregables.

## Known data issue

Los anexos de costos no son consistentes respecto del PV del día 15: una imagen indica USD 38.000 y otras dos indican USD 38.800. El valor debe verificarse antes de reutilizarlo.
