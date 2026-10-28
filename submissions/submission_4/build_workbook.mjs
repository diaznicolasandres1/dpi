import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const dir=path.dirname(fileURLToPath(import.meta.url));
const d=JSON.parse(await fs.readFile(path.join(dir,'model_data.json'),'utf8'));
const wb=Workbook.create();
const names=['Resumen','Tareas','Mano de obra','Partidas','Línea base','EVM','Calidad','Riesgos','Matriz','Contingencia','Supuestos'];
const sh=Object.fromEntries(names.map(n=>[n,wb.worksheets.add(n)]));
const fmt='#,##0.00;(#,##0.00);"-"';
const money='#,##0;(#,##0);"-"';
const blue='#1D58A6',green='#167143',navy='#142E49';
function col(n){let s='';for(n++;n;n=Math.floor((n-1)/26))s=String.fromCharCode(65+(n-1)%26)+s;return s;}
function cells(s,r,c,rows){s.getRangeByIndexes(r-1,c-1,rows.length,rows[0].length).values=rows;}
function formula(s,cell,f){s.getRange(cell).formulas=[[f]];s.getRange(cell).format.font.color=f.includes('!')?green:'#192F44';}
function title(s,t,desc){cells(s,2,1,[[t]]);s.getRange('A2').format.font={name:'Arial',bold:true,size:15,color:navy};if(desc)cells(s,3,1,[[desc]]);}
function header(s,r,labels){cells(s,r,1,[labels]);s.getRange(`A${r}:${col(labels.length-1)}${r}`).format={fill:navy,font:{name:'Arial',bold:true,color:'#FFFFFF',size:10},rowHeight:32,wrapText:true,verticalAlignment:'center'};}
function base(s,lastCol,lastRow){s.showGridLines=false;s.getRange(`A1:${lastCol}${lastRow}`).format={font:{name:'Arial',size:10,color:'#192F44'},rowHeight:24,verticalAlignment:'center'};s.getRange(`A1:${lastCol}${lastRow}`).format.columnWidth=16;}
function widths(s,vs){vs.forEach((v,i)=>s.getRange(`${col(i)}:${col(i)}`).format.columnWidth=v);}
function inputs(s,r){s.getRange(r).format.font.color=blue;s.getRange(r).format.fill='#FFF6DA';}
function sum(s,r,lastCol){s.getRange(`A${r}:${lastCol}${r}`).format.fill='#E5EEF4';s.getRange(`A${r}:${lastCol}${r}`).format.font.bold=true;}
for(const s of Object.values(sh))base(s,'T',130);

// Supuestos conserva entradas y fuentes junto a los recursos.
let s=sh.Supuestos;title(s,'Supuestos y fuentes','Entradas azules; fórmulas negras; vínculos verdes. Hipótesis académicas pendientes de validación.');
header(s,5,['Código','Recurso','USD/día','Fuente / límite']);
const roles=[...new Map(d.labor.map(x=>[x.role,x])).values()];
cells(s,6,1,roles.map(x=>[x.role,x.resource,x.rate,'N2 corregida, Recursos; tarifa supuesta, no cotización verificada.']));
inputs(s,'C6:C17');s.getRange('C6:C17').setNumberFormat(money);
header(s,20,['Clase','Hipótesis','Factor O','Factor P','Escenario']);
cells(s,21,1,Object.entries(d.classes).map(([k,v])=>[k,v.name,v.o,v.p,v.scenario]));inputs(s,'C21:D23');s.getRange('C21:D23').setNumberFormat('0.0%');
header(s,26,['Parámetro','Valor','Fuente / explicación']);
cells(s,27,1,[['Reserva gestión',.04,'N2 corregida, PDF p.9; fuera de línea base.'],['Techo Acta',420000,'N1/N3; margen no asignado no es reserva.'],['BAC criterio','M','DPI5 p.11 conserva M; PERT contraste técnico, K-2 precio fijo.'],['Día-persona',8,'Horas por día; duración en días hábiles ≠ esfuerzo.'],['Moneda','USD nominal','Sin inflación, impuestos ni FX adicionales; hipótesis pendiente de contrato.'],['Calendario','N2 corregida','Fechas/ponderaciones congeladas del calendario N2; no es motor de reprogramación.'],['Estado','Plan académico','Sin evidencia de contratos firmados, gastos reales, avance o consultas efectivamente realizadas.']]);inputs(s,'B27:B28');s.getRange('B27').setNumberFormat('0.0%');s.getRange('B28').setNumberFormat(money);
const sources=[
['Costos y trazabilidad','submissions/submission_2/corrected_review/Grupo 1_Entrega N2.pdf pp.7-9 y Excel original.'],
['Continuidad','submissions/submission_3/revisions/revision_2/Grupo 1_Entrega N3.pdf pp.2-4,12-13. Excel N3 original no presumido actualizado.'],
['Estimación/reservas','DPI5 pp.10-11,16-18,20-22. Se retiene M como ejemplo p.11.'],
['EVM','DPI6 pp.10-17,20-23. BAC operativo excluye reservas, reconciliado con línea base.'],
['Juicio experto','DPI11 pp.4-5,14. Consultas propuestas, no realizadas.'],
['Riesgos/calidad','GDP complementario Incertidumbre pp.10-21; Entrega/Calidad pp.3-6. Numeración independiente.'],
['ISO/IEC 25010:2023 ed.2','https://www.iso.org/standard/78176.html ; ficha pública consultada27/10/2026, sin cláusulas íntegras ni certificación.'],
['OWASP ASVS 5.0.0','https://asvs.owasp.org/ ; publicación 30/05/2025, consulta 27/10/2026. Marco general, sin afirmar nivel completo.'],
['ASVS autorización V8','https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x17-V8-Authorization.md ; controles v5.0.0-8.1.1,8.2.1,8.2.2,8.3.1 verificados.'],
['Costos no laborales','Cantidades/precios N2 como hipótesis de contrato; P-1 proviene de N1, sin cotización comercial adjunta comprobada.'],
['Devengo revisado','P-4b desde 30/10 conforme N3; P-3c logística30 sesiones después balances/UAT,22-30/03. Referentes replican: validar disponibilidad.'],
['Calendario de riesgos','Acciones con fecha anterior27/10 son plan base, no evidencia de ejecución. Estado: identificado/plan propuesto.'],
['No doble conteo','M incluye prevención/pruebas/retrabajo fijo K-2. Reserva solo incrementosVCA ante disparador. PERT no se suma a M ni a contingencia.']];
header(s,36,['Tema','Fuente y límite']);cells(s,37,1,sources);widths(s,[25,57,15,65,90]);s.getRange('A37:B49').format.wrapText=true;s.getRange('A37:B49').format.rowHeight=60;s.getRange('E21:E23').format.wrapText=true;s.getRange('A21:E23').format.rowHeight=64;

s=sh['Mano de obra'];title(s,'Mano de obra por recurso y tarea','N2 corregida. FTE × duración = días-persona. Tarifa del recurso en Supuestos.');
header(s,5,['EDT','Tarea','Rol','FTE','Duración d','Días-persona','USD/día','Costo USD']);
const lr=6,le=lr+d.labor.length-1;
cells(s,lr,1,d.labor.map(x=>[x.task,d.tasks.find(t=>t.id===x.task).name,x.role,x.fte,x.duration,null,null,null]));
d.labor.forEach((x,i)=>{const r=lr+i;formula(s,`E${r}`,`=Tareas!C${6+d.tasks.findIndex(t=>t.id===x.task)}`);formula(s,`F${r}`,`=D${r}*E${r}`);formula(s,`G${r}`,`='Supuestos'!C${6+roles.findIndex(k=>k.role===x.role)}`);formula(s,`H${r}`,`=F${r}*G${r}`);});
cells(s,le+1,1,[['Total']]);formula(s,`F${le+1}`,`=SUM(F${lr}:F${le})`);formula(s,`H${le+1}`,`=SUM(H${lr}:H${le})`);sum(s,le+1,'H');inputs(s,`D${lr}:D${le}`);s.getRange(`D${lr}:F${le+1}`).setNumberFormat('0.0');s.getRange(`D${lr}:D${le}`).setNumberFormat('0.000');s.getRange(`G${lr}:H${le+1}`).setNumberFormat(money);widths(s,[10,50,12,12,14,17,15,18]);s.freezePanes.freezeRows(5);s.freezePanes.freezeColumns(2);

s=sh.Partidas;title(s,'Partidas no laborales','Cantidad × precio. Cuenta EDT agrupa costo una sola vez; período propio conserva devengo del servicio.');header(s,5,['ID','Concepto','Cantidad','Unidad','USD/unidad','Costo USD','EDT','Desde','Hasta']);
cells(s,6,1,d.parts.map(x=>[x.id,x.name,x.quantity,x.unit,x.price,null,x.task,new Date(x.start+'T12:00:00Z'),new Date(x.end+'T12:00:00Z')]));
d.parts.forEach((x,i)=>formula(s,`F${i+6}`,`=C${i+6}*E${i+6}`));cells(s,18,1,[['Total']]);formula(s,'F18','=SUM(F6:F17)');sum(s,18,'I');inputs(s,'C6:E17');s.getRange('E6:F18').setNumberFormat(money);s.getRange('H6:I17').setNumberFormat('dd/mm/yyyy');widths(s,[12,62,14,18,17,18,10,17,17]);s.getRange('B6:B17').format.wrapText=true;s.getRange('A6:I17').format.rowHeight=48;s.freezePanes.freezeRows(5);

s=sh.Tareas;title(s,'Presupuesto por las 31 tareas EDT','M en línea base. O/M/P son USD para alcance constante; PERT=(O+4M+P)/6. NL fijo en los tres escenarios.');
header(s,5,['EDT','Tarea','Duración d','Clase','Labor USD','NL USD','O USD','M USD','P USD','PERT USD','Inicio','Fin']);
cells(s,6,1,d.tasks.map(t=>[t.id,t.name,t.duration,t.class,null,null,null,null,null,null,new Date(t.start+'T12:00:00Z'),new Date(t.end+'T12:00:00Z')]));
d.tasks.forEach((t,i)=>{let r=i+6;const cr=21+Object.keys(d.classes).indexOf(t.class);formula(s,`E${r}`,`=SUMIF('Mano de obra'!$A$${lr}:$A$${le},A${r},'Mano de obra'!$H$${lr}:$H$${le})`);formula(s,`F${r}`,`=SUMIF(Partidas!$G$6:$G$17,A${r},Partidas!$F$6:$F$17)`);formula(s,`G${r}`,`=E${r}*Supuestos!C${cr}+F${r}`);formula(s,`H${r}`,`=E${r}+F${r}`);formula(s,`I${r}`,`=E${r}*Supuestos!D${cr}+F${r}`);formula(s,`J${r}`,`=(G${r}+4*H${r}+I${r})/6`);});
cells(s,37,1,[['Total']]);for(let c=4;c<=9;c++)formula(s,`${col(c)}37`,`=SUM(${col(c)}6:${col(c)}36)`);sum(s,37,'L');s.getRange('E6:J37').setNumberFormat(money);s.getRange('K6:L36').setNumberFormat('dd/mm/yyyy');inputs(s,'C6:C36');widths(s,[10,50,15,12,17,17,17,17,17,18,17,17]);s.freezePanes.freezeRows(5);s.freezePanes.freezeColumns(2);

// La distribución mensual cambia con los importes, manteniendo ponderaciones de calendario N2 explícitas.
s=sh['Línea base'];title(s,'Línea base de costos por mes','USD devengados. Trabajo + reserva no distribuida. Ponderaciones por días hábiles del calendario N2, conservadas como entradas.');
header(s,5,['Mes','Trabajo USD','Contingencia USD','Línea base USD','Acumulada USD','Trabajo acumulado USD']);
cells(s,6,1,d.monthkeys.map(m=>[new Date(m+'-01T12:00:00Z'),null,null,null,null,null]));
header(s,20,['Componente','Tipo','Importe USD',...d.monthkeys]);
const ar=21,ae=ar+d.alloc.length-1;
cells(s,ar,1,d.alloc.map(a=>[a.id,a.kind,null,...a.weights]));
d.alloc.forEach((a,i)=>{const r=ar+i;const ref=a.kind==='Labor'?`Tareas!E${6+d.tasks.findIndex(t=>t.id===a.id)}`:`Partidas!F${6+d.parts.findIndex(p=>p.id===a.id)}`;formula(s,`C${r}`,`=${ref}`);});
for(let i=0;i<7;i++){const r=6+i;formula(s,`B${r}`,`=SUMPRODUCT($C$${ar}:$C$${ae},${col(3+i)}${ar}:${col(3+i)}${ae})`);formula(s,`C${r}`,`=SUMIF(Riesgos!$N$6:$N$24,"${d.monthkeys[i]}",Riesgos!$M$6:$M$24)`);formula(s,`D${r}`,`=B${r}+C${r}`);formula(s,`E${r}`,`=SUM($D$6:D${r})`);formula(s,`F${r}`,`=SUM($B$6:B${r})`);}
cells(s,13,1,[['Total']]);for(const c of ['B','C','D'])formula(s,`${c}13`,`=SUM(${c}6:${c}12)`);formula(s,'E13','=E12');formula(s,'F13','=F12');sum(s,13,'F');s.getRange('A6:A12').setNumberFormat('mmm-yy');s.getRange('B6:F13').setNumberFormat(money);s.getRange(`C${ar}:C${ae}`).setNumberFormat(money);s.getRange(`D${ar}:J${ae}`).setNumberFormat('0.0%');widths(s,[17,20,22,22,22,24,17,17,17,17,17,17,17,17,17]);
// Rango auxiliar contiguo con meses de texto y vínculo al dato calculado.
cells(s,16,18,[['Mes','Línea base acumulada USD']]);
for(let i=0;i<7;i++){cells(s,17+i,18,[[d.monthkeys[i]]]);formula(s,`S${17+i}`,`=E${6+i}`);}
const chart=s.charts.add('line',s.getRange('R16:S23'));chart.title='Línea base acumulada (USD)';chart.hasLegend=false;chart.series.items[0].line={fill:'#007A78',style:'solid',width:2};chart.setPosition('H5','P17');chart.yAxis={numberFormatCode:'#,##0',numberFormatSourceLinked:false};chart.xAxis={axisType:'textAxis'};
cells(s,16,1,[['BAC operativo 372.700 + contingencia 22.000 = línea base 394.700. La reserva no gana EV por tiempo.']]);cells(s,17,1,[['Trabajo acumulado es costo lineal; validar hitos/componentes antes de cargar PV al reporte EVM.']]);

s=sh.Riesgos;title(s,'Registro de riesgos y respuestas','P/I inherentes1-5; residual es meta pendiente. Estado: identificado / plan propuesto. Reserva incremental VCA, sin duplicar K-2/K-5.');
header(s,5,['ID','Causa, evento y efecto','EDT','P','I','P×I','Prioridad','Dueño','Estrategia','P residual','I residual','R residual','Reserva USD','Mes exposición','Prevención','Disparador y respuesta','Monitoreo / evidencia']);
cells(s,6,1,d.risks.map(r=>[r[0],r[1],r[2],r[3],r[4],null,null,r[5],r[6],r[10],r[11],null,r[12],r[13],r[7],r[8],r[9]]));
d.risks.forEach((x,i)=>{const r=i+6;formula(s,`F${r}`,`=D${r}*E${r}`);formula(s,`G${r}`,`=IF(F${r}>=15,"Alta",IF(F${r}>=6,"Media","Baja"))`);formula(s,`L${r}`,`=J${r}*K${r}`);formula(s,`M${r}`,`=SUMIF(Contingencia!$A$6:$A$26,A${r},Contingencia!$E$6:$E$26)`);});
cells(s,25,1,[['Total reserva']]);formula(s,'M25','=SUM(M6:M24)');sum(s,25,'Q');s.getRange('M6:M25').setNumberFormat(money);inputs(s,'D6:E24');inputs(s,'J6:K24');inputs(s,'N6:N24');s.dataValidations.add({range:'D6:E24',rule:{type:'whole',operator:'between',formula1:1,formula2:5}});s.dataValidations.add({range:'J6:K24',rule:{type:'whole',operator:'between',formula1:1,formula2:5}});s.getRange('F6:F24').conditionalFormats.add('cellIs',{operator:'greaterThanOrEqual',formula:15,format:{fill:'#F2B5AA',font:{color:'#8D2119',bold:true}}});
widths(s,[12,68,20,8,8,10,13,27,21,12,12,12,20,19,65,78,68]);s.getRange('A6:Q24').format.wrapText=true;s.getRange('A6:Q24').format.rowHeight=90;s.freezePanes.freezeRows(5);s.freezePanes.freezeColumns(2);

s=sh.Matriz;title(s,'Matriz de riesgos inherentes','Eje vertical P, horizontal I. Baja1-5; media6-12; alta15-25. Riesgo de seguridad/hito obligatorio escala aunque el producto sea medio.');header(s,5,['P / I',1,2,3,4,5]);
cells(s,6,1,[[5],[4],[3],[2],[1]]);
for(let rr=6;rr<=10;rr++)for(let cc=1;cc<=5;cc++){const addr=`${col(cc)}${rr}`;const terms=d.risks.map((r,i)=>`IF(AND(Riesgos!$D$${i+6}=$A${rr},Riesgos!$E$${i+6}=${col(cc)}$5),Riesgos!$A$${i+6}&" ","")`);formula(s,addr,'='+terms.join('&'));let score=(11-rr)*cc;s.getRange(addr).format.fill=score>=15?'#F2B5AA':score>=6?'#F6DDA6':'#CFE5D5';}
widths(s,[13,24,24,24,30,33]);s.getRange('A6:F10').format.rowHeight=65;s.getRange('B6:F10').format.wrapText=true;
cells(s,13,1,[['P:1≤10%;2>10-30%;3>30-50%;4>50-80%;5>80-<100%. Son hipótesis, no frecuencia observada.']]);
cells(s,15,1,[['I','Costo adicional USD','Plazo','Calidad / aceptación']]);
cells(s,16,1,[[1,'≤1.000','≤1 día','Menor sin criterio afectado'],[2,'>1.000-3.000','>1-3 días','Secundario con alternativa'],[3,'>3.000-8.000','>3-5 días','Retrabajo recuperable antes hito'],[4,'>8.000-15.000','>5-10 días o H-3 en riesgo','Módulo principal comprometido'],[5,'>15.000','>10 días o desvío H-5/H-6/H-7','Bloqueo seguridad/integridad/beneficio']]);s.getRange('A15:D20').format.wrapText=true;s.getRange('A15:D20').format.rowHeight=42;

s=sh.Calidad;title(s,'Plan de calidad y controles','Umbrales nuevos son decisiones del equipo; marcos ISO/IEC 25010:2023 ed.2 y OWASP ASVS 5.0.0, sin certificación ni nivel completo.');header(s,5,['ID','Dimensión','Umbral y alcance','Método / evidencia','Responsable','Momento y acción','EDT','Origen']);
cells(s,6,1,d.quality);widths(s,[10,27,65,85,45,72,22,37]);s.getRange('A6:H13').format.wrapText=true;s.getRange('A6:H13').format.rowHeight=125;s.freezePanes.freezeRows(5);s.freezePanes.freezeColumns(2);

s=sh.Contingencia;title(s,'Contingencia: cálculo por respuesta','Provisión heredada 22.000 USD. Paquetes incrementales propuestos; no valor esperado ni cotizaciones. Reestimar si necesidades exceden provisión.');
header(s,5,['Riesgo','Cantidad incremental','Unidad','USD/unidad','Reserva USD','Exclusión / fundamento']);
cells(s,6,1,d.reserve_items.map(x=>[x[0],x[1],x[2],x[3],null,x[4]]));
d.reserve_items.forEach((x,i)=>formula(s,`E${i+6}`,`=B${i+6}*D${i+6}`));
cells(s,27,1,[['Total']]);formula(s,'E27','=SUM(E6:E26)');sum(s,27,'F');inputs(s,'B6:B26');inputs(s,'D6:D26');s.getRange('D6:E27').setNumberFormat(money);widths(s,[12,20,38,18,20,90]);s.getRange('C6:F26').format.wrapText=true;s.getRange('A6:F26').format.rowHeight=48;s.freezePanes.freezeRows(5);

// EVM real vacío y ejemplo enteramente separado. Cada componente con costo propio.
s=sh.EVM;title(s,'Valor Ganado: reporte por completar','Sin datos reales verificados. Cargar plan, avance aceptado y costo incurrido por 43 componentes; cero explícito significa ningún avance/costo.');
header(s,5,['Indicador real','Valor','Regla','Ejemplo ilustrativo','Valor ficticio']);
const er=26,ee=er+d.alloc.length-1;
cells(s,6,1,[['Fecha de corte',null,'Entrada obligatoria; mismo corte para PV, EV y AC.','Fecha ficticia',new Date('2026-11-30T12:00:00Z')],['BAC operativo',null,'Excluye reserva no distribuida.','BAC',null],['PV',null,'Plan autorizado por componente.','PV',200000],['EV',null,'Trabajo aceptado, no gasto ni porcentaje subjetivo.','EV',180000],['AC',null,'Devengado conciliado, no calculado de avance.','AC',195000],['CV',null,'EV−AC en USD.','CV',null],['SV',null,'EV−PV en USD, no días.','SV',null],['CPI',null,'EV/AC si AC>0.','CPI',null],['SPI',null,'EV/PV si PV>0.','SPI',null],['EAC',null,'BAC/CPI si CPI>0; hipótesis eficiencia persistente.','EAC',null],['ETC',null,'EAC−AC.','ETC',null],['VAC',null,'BAC−EAC.','VAC',null],['TCPI',null,'(BAC−EV)/(BAC−AC) si denominador>0.','TCPI',null],['Estado real',null,'No informar estado hasta completar corte y 43 componentes.','Estado ejemplo','ILUSTRATIVO, sin datos reales']]);
formula(s,'B7','=Tareas!H37');formula(s,'E7','=Tareas!H37');
const invalid=`OR(COUNTIF(D${er}:E${ee},"<0")>0,COUNTIF(D${er}:E${ee},">1")>0,COUNTIF(F${er}:F${ee},"<0")>0)`;
const complete=`AND(COUNT(D${er}:F${ee})=${d.alloc.length*3},ISNUMBER(B6),NOT(${invalid}))`;
for(const [dest,range] of [['B8',`G${er}:G${ee}`],['B9',`H${er}:H${ee}`],['B10',`F${er}:F${ee}`]])formula(s,dest,`=IF(${complete},SUM(${range}),"")`);
const realf={B11:'B9-B10',B12:'B9-B8',B13:'IF(B10>0,B9/B10,"No calculable")',B14:'IF(B8>0,B9/B8,"No calculable")',B15:'IF(AND(ISNUMBER(B13),B13>0),B7/B13,"No calculable")',B16:'IF(ISNUMBER(B15),B15-B10,"No calculable")',B17:'IF(ISNUMBER(B15),B7-B15,"No calculable")',B18:'IF(B7-B10>0,(B7-B9)/(B7-B10),"No calculable")'};
for(const [cell,exp] of Object.entries(realf))formula(s,cell,`=IF(${complete},${exp},"")`);
formula(s,'B19',`=IF(${invalid},"Dato inválido: avance 0..1 y AC>=0",IF(${complete},IF(OR(B8=0,B10=0,B9=0,B7-B10<=0),"Completo; hay índices no calculables","Completo para analizar"),"Pendiente de datos reales"))`);
const demof={E11:'E9-E10',E12:'E9-E8',E13:'IF(E10>0,E9/E10,"No calculable")',E14:'IF(E8>0,E9/E8,"No calculable")',E15:'IF(AND(ISNUMBER(E13),E13>0),E7/E13,"No calculable")',E16:'IF(ISNUMBER(E15),E15-E10,"No calculable")',E17:'IF(ISNUMBER(E15),E7-E15,"No calculable")',E18:'IF(E7-E10>0,(E7-E9)/(E7-E10),"No calculable")'};for(const [c,f] of Object.entries(demof))formula(s,c,'='+f);
inputs(s,'B6');inputs(s,'E8:E10');s.getRange('B6').setNumberFormat('dd/mm/yyyy');s.getRange('E6').setNumberFormat('dd/mm/yyyy');s.getRange('B7:B17').setNumberFormat(money);s.getRange('E7:E17').setNumberFormat(money);for(const r of [13,14,18]){s.getRange(`B${r}`).setNumberFormat('0.0000');s.getRange(`E${r}`).setNumberFormat('0.0000');}
cells(s,21,1,[['PV requiere plan físico por componente. 20 % diseño, 50 % integrado/revisado, 30 % aceptación para módulos;0/100 documentos breves.']]);
cells(s,22,1,[['LOE 1.5 gana por gestión prestada. Partidas: avance según servicio disponible/aceptado, sin ganar7 meses por alta del ambiente.']]);
cells(s,23,1,[['Al activar reserva, transferir presupuesto a componente con plan futuro. Mantener BAC operativo + reserva = línea base.']]);
header(s,25,['Componente','Tipo / tarea','BAC USD','Plan físico','Avance aceptado','AC USD','PV USD','EV USD']);
cells(s,er,1,d.alloc.map(a=>[a.id,a.kind==='Labor'?d.tasks.find(t=>t.id===a.id).name:d.parts.find(p=>p.id===a.id).name,null,null,null,null,null,null]));
d.alloc.forEach((a,i)=>{const r=er+i;formula(s,`C${r}`,`='Línea base'!C${ar+i}`);formula(s,`G${r}`,`=IF(ISNUMBER(D${r}),C${r}*D${r},"")`);formula(s,`H${r}`,`=IF(ISNUMBER(E${r}),C${r}*E${r},"")`);});
inputs(s,`D${er}:F${ee}`);s.getRange(`D${er}:E${ee}`).setNumberFormat('0.0%');s.getRange(`C${er}:C${ee}`).setNumberFormat(money);s.getRange(`F${er}:H${ee}`).setNumberFormat(money);s.dataValidations.add({range:`D${er}:E${ee}`,rule:{type:'decimal',operator:'between',formula1:0,formula2:1}});s.dataValidations.add({range:`F${er}:F${ee}`,rule:{type:'decimal',operator:'greaterThanOrEqual',formula1:0}});widths(s,[25,62,65,35,40,20,20,20]);s.getRange('C6:C19').format.wrapText=true;s.getRange('A6:E19').format.rowHeight=32;s.getRange('B26:B68').format.wrapText=true;s.getRange('A26:H68').format.rowHeight=42;

s=sh.Resumen;title(s,'WorkHub · Entrega N4 · Grupo 1','VCA Catalinas / Tandem. Plan académico para 31/10/2026; USD. Solo PDF y Excel como archivos de entrega.');
header(s,5,['Presupuesto','USD','Criterio']);
const summary=[['Mano de obra',null,'Incluye Tandem 216.888 y horas VCA 19.038.'],['Partidas no laborales',null,'Licencia 108.000 y otras partidas 28.774.'],['Actividades M / BAC operativo',null,'Suma 31 tareas; M en línea base, PERT como contraste.'],['Contingencia',null,'Asignada a 19 riesgos; dentro línea base.'],['Línea base',null,'Trabajo + contingencia.'],['Reserva de gestión',null,'4 % de línea base, fuera de ella.'],['Presupuesto total',null,'Línea base + gestión.'],['Techo Acta',null,'No equivale al presupuesto estimado.'],['Margen sin asignar',null,'No reserva ni obligación de gasto.'],['PERT técnico agregado',null,'No incrementa precio fijo K-2 automáticamente.'],['Diferencia PERT−M',null,'No se suma a contingencia.'],['Diferencia contra N1 398.000',null,'M ascendente valida, no fuerza total N1.']];cells(s,6,1,summary);
const sf={B6:"='Mano de obra'!H"+(le+1),B7:'=Partidas!F18',B8:'=Tareas!H37',B9:'=Riesgos!M25',B10:'=B8+B9',B11:'=B10*Supuestos!B27',B12:'=B10+B11',B13:'=Supuestos!B28',B14:'=B13-B12',B15:'=Tareas!J37',B16:'=B15-B8',B17:'=B8-398000'};for(const [c,f]of Object.entries(sf))formula(s,c,f);s.getRange('B6:B17').setNumberFormat(money);sum(s,10,'C');sum(s,12,'C');
header(s,20,['Conciliación','Diferencia USD','Tolerancia monetaria 0,01 USD']);cells(s,21,1,[['Labor + no laboral = M'],['Mensual línea base = total'],['Reserva versus provisión heredada'],['31 paquetes / tareas']]);formula(s,'B21','=B6+B7-B8');formula(s,'B22',"=ROUND('Línea base'!D13-B10,2)");formula(s,'B23','=B9-22000');formula(s,'B24','=COUNTA(Tareas!A6:A36)-31');s.getRange('B21:B24').setNumberFormat('0.00;(0.00);0.00');s.getRange('B21:B24').conditionalFormats.addCustom('ABS(B21)>0.01',{fill:'#F7C7BD',font:{bold:true,color:'#942A24'}});
cells(s,27,1,[['Uso','Detalle']]);cells(s,28,1,[['Tareas / Mano de obra / Partidas','Base y escenarios; tarifas en Supuestos.'],['Línea base','Curva S y distribución con reserva por mes de riesgo.'],['EVM','Plantilla real vacía, 43 componentes y ejemplo separado.'],['Calidad','8 criterios, medición, responsables y bloqueo.'],['Riesgos / Matriz','19 riesgos con planes y monitoreo; 17 heredados + 2 de software nuevos.'],['Límite','No se verificó comportamiento en Microsoft Excel nativo; fórmulas calculadas en Artifact Tool.']]);widths(s,[42,24,85]);s.getRange('A6:C17').format.rowHeight=30;s.getRange('C6:C17').format.wrapText=true;s.tabColor=navy;

wb.recalculate();
const result=await wb.inspect({kind:'table',range:'Resumen!A5:C24',include:'values,formulas',tableMaxRows:22,tableMaxCols:3,maxChars:7000});
console.log(result.ndjson);
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:30},summary:'Errores finales',maxChars:4000})).ndjson);
// Ensayo de sensibilidad sobre entrada y restauración antes del guardado.
const old=sh.Supuestos.getRange('C6').values[0][0];const oldM=sh.Resumen.getRange('B8').values[0][0];sh.Supuestos.getRange('C6').values=[[old+10]];wb.recalculate();const newM=sh.Resumen.getRange('B8').values[0][0];if(!(newM>oldM))throw new Error('No recalcula tarifa PM');sh.Supuestos.getRange('C6').values=[[old]];
// P1:I1 cambia ubicación deRI-1 y la matriz debe reaccionar.
const before=sh.Matriz.getRange('F8').values[0][0];sh.Riesgos.getRange('D6').values=[[1]];wb.recalculate();const after=sh.Matriz.getRange('F8').values[0][0];if(before===after)throw new Error('Matriz no reacciona aP');sh.Riesgos.getRange('D6').values=[[3]];
const evm=sh.EVM;
evm.getRange('D26').values=[[1.1]];wb.recalculate();const invalidStatus=evm.getRange('B19').values[0][0];if(!invalidStatus.includes('inválido'))throw new Error('No detecta avance inválido');evm.getRange('D26').values=[[null]];
evm.getRange('B6').values=[[new Date('2026-11-30T12:00:00Z')]];
evm.getRange(`D${er}:F${ee}`).values=Array.from({length:d.alloc.length},()=>[0,0,0]);wb.recalculate();const zeroCPI=evm.getRange('B13').values[0][0];const zeroEAC=evm.getRange('B15').values[0][0];if(zeroCPI!=='No calculable'||zeroEAC!=='No calculable')throw new Error('Cero no controla divisores');
evm.getRange('F26').values=[[-1]];wb.recalculate();const negativeStatus=evm.getRange('B19').values[0][0];if(!negativeStatus.includes('inválido'))throw new Error('No detecta AC negativo');
evm.getRange(`D${er}:F${ee}`).values=Array.from({length:d.alloc.length},()=>[null,null,null]);evm.getRange('B6').values=[[null]];
wb.recalculate();
const validation={oldM,newM,restoredM:sh.Resumen.getRange('B8').values[0][0],invalidStatus,negativeStatus,zeroCPI,zeroEAC,EVMRealStatus:sh.EVM.getRange('B19').values[0][0],demo:sh.EVM.getRange('D7:E18').values};
await fs.writeFile(path.join(dir,'workbook_validation.json'),JSON.stringify(validation,null,2));
await fs.mkdir(path.join(dir,'work'),{recursive:true});
const views=[['Resumen','A1:C33'],['Tareas','A2:J15'],['Mano de obra','A2:H17'],['Partidas','A2:I18'],['Línea base','A2:P17'],['EVM','A2:E19'],['Calidad','A2:F9'],['Riesgos','A2:N10'],['Riesgos','O5:Q10'],['Matriz','A2:F20'],['Supuestos','A2:E23'],['Contingencia','A2:F27']];
for(let i=0;i<views.length;i++){const [sheetName,range]=views[i];const img=await wb.render({sheetName,range,scale:1,format:'png'});await fs.writeFile(path.join(dir,'work',`sheet_${i+1}.png`),new Uint8Array(await img.arrayBuffer()));}
const output=await SpreadsheetFile.exportXlsx(wb);await output.save(path.join(dir,'Grupo 1_Entrega N4.xlsx'));
console.log('Exportado Excel y11vistas');
