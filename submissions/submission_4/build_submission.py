"""Fuentes de datos, Markdown y PDF de N4. Ejecutar con Python bundled de Codex."""
from pathlib import Path
import json, calendar, re
from datetime import datetime
from collections import defaultdict
import openpyxl
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.graphics.shapes import Drawing, Line, String, Rect, PolyLine

ROOT=Path(__file__).resolve().parent
SRC=ROOT.parent/'submission_2/corrected_review/Grupo 1_Entrega N2.xlsx'
w=openpyxl.load_workbook(SRC,data_only=True)
tasks=[]; labor=[]; parts=[]
for row in list(w['Tareas'].values)[5:]:
    if isinstance(row[0],str) and re.match(r'^\d\.\d$',row[0]):
        tasks.append(dict(id=row[0],name=row[1],duration=row[3],start=row[12].strftime('%Y-%m-%d'),end=row[13].strftime('%Y-%m-%d')))
for row in list(w['Costos'].values)[4:]:
    if row[0] in [t['id'] for t in tasks] and row[2]:
        labor.append(dict(task=row[0],role=row[2],resource=row[3],fte=row[4],duration=row[5],effort=row[6],rate=row[7],cost=row[8],category=row[9]))
mapping=['1.1','5.1','5.1','5.4','5.1','5.1','4.3','4.4','4.4','4.1','3.4','3.2']
for n,row in enumerate(list(w['Partidas'].values)[4:16]):
    start,end=row[9].strftime('%Y-%m-%d'),row[10].strftime('%Y-%m-%d')
    if row[0]=='P-3c':start,end='2027-03-22','2027-03-30'
    if row[0]=='P-4b':start,end='2026-10-30','2026-11-12'
    parts.append(dict(id=row[0],name=row[1],quantity=row[3],unit=row[4],price=row[5],cost=row[6],task=mapping[n],start=start,end=end))
classes={
 'A':dict(o=.9,p=1.1,name='Gestión y validación acotada',scenario='O: documentación disponible y una ronda; M: dedicación N2; P: ronda adicional de revisión. Rango técnico ±10 % de mano de obra.'),
 'B':dict(o=.85,p=1.3,name='Configuración y adopción',scenario='O: reglas, planos y materiales reutilizables; M: configuración prevista; P: ajustes de interfaces o materiales dentro del alcance. Mano de obra -15 % / +30 %.'),
 'C':dict(o=.8,p=1.4,name='Integración y verificación compleja',scenario='O: contratos API y datos válidos al primer ensayo; M: pruebas planificadas; P: diagnóstico y una iteración adicional, sin cambiar alcance. Mano de obra -20 % / +40 %.'),
}
for t in tasks:
    t['class']='A' if t['id'].startswith('1.') else ('C' if t['id'].startswith('3.') or t['id'] in ['2.5','2.8','5.2','5.3','5.4'] else 'B')
    t['labor']=sum(x['cost'] for x in labor if x['task']==t['id'])
    t['nonlabor']=sum(x['cost'] for x in parts if x['task']==t['id'])
    t['M']=t['labor']+t['nonlabor']; c=classes[t['class']]
    t['O']=t['labor']*c['o']+t['nonlabor'];t['P']=t['labor']*c['p']+t['nonlabor'];t['PERT']=(t['O']+4*t['M']+t['P'])/6
    t['basis']='; '.join(f"{x['role']} {x['effort']:g} × {x['rate']:g}" for x in labor if x['task']==t['id'])

# ID, causa-evento-efecto, paquetes, P, I, dueño, estrategia, prevención, disparador/respuesta, monitor, residualP/I, reserva, mes
risks=[
['RI-1','Omisión de check-in o geocerca imprecisa produce registros de ocupación inexactos y una discrepancia >5 % que invalida la recomendación de planta 4.','2.5,5.4,5.6',3,5,'PO / Servicios Generales','Mitigar','Activar recordatorios y liberación automática. Validar QR y conteo manual en piloto.','Si discrepancia >5 % en dos muestras: congelar informe, ampliar conteo manual y corregir reglas.','Semanal en piloto y estabilización; SG concilia registros con muestra estratificada por planta.',2,4,2000,'2027-04'],
['RI-2','Permisos insuficientes, límites o incompatibilidad de Entra ID, HRIS o Graph bloquean conectores y requieren retrabajo.','3.1-3.5,5.2',3,4,'Tecnología VCA','Mitigar','Probar autenticación, cuotas y contratos API en sandbox antes de integrar.','Si error de permisos persiste >1 día: escalar al fabricante y habilitar cuota/entorno adicional autorizado.','Semanal C-4 y diario durante integración; log de fallos y bloqueos.',2,3,2400,'2026-11'],
['RI-3','Temor al control de presentismo y pérdida del puesto fijo genera resistencia y adopción inferior al 70 %.','4.1-4.5,5.3',4,4,'RR.HH. VCA','Mitigar','Comunicar uso agregado de datos, política y referentes. Medir intención antes del piloto.','Si intención <70 % o UAT <9: sesiones focalizadas y piezas aclaratorias antes del lanzamiento.','Quincenal C-13/C-15; encuestas y motivos de rechazo.',3,3,1800,'2027-03'],
['RI-4','Pico de demanda o cláusula de alquiler impide devolver planta 4 aunque WorkHub funcione.','5.6',2,5,'Sponsor / Servicios Generales','Aceptar pasiva','No se presupone devolución ni ahorro realizado. El informe conserva escenarios de ocupación.','Si demanda excede capacidad o contrato impide salida: Sponsor revisa el caso de negocio, sin gasto automático del proyecto.','Mensual al Comité; informe de demanda y revisión contractual.',2,5,0,'2027-04'],
['RI-5','Extensión del cierre de balances más allá del 15/03 bloquea UAT crítica y desplaza hitos.','5.3,5.4,1.6',3,5,'Sponsor','Aceptar activa','Reservar ventana y participantes por escrito. Preparar casos y ambiente sin despliegue masivo durante balances.','Si al 08/03 no se confirma 16/03: escalar al Sponsor en 48 h y tramitar cambio de hitos. No comprar una fecha ficticia.','Semanal desde febrero y diario al 15/03; confirmación de Finanzas.',3,5,0,'2027-03'],
['RI-6','Solape SS+5 inicia escritorios antes de cerrar reglas y cambios tardíos generan retrabajo que amenaza H-3.','2.1,2.3,5.2',3,3,'PO','Mitigar','Validar reglas críticas en primera semana y versionar decisiones.','Si regla cambia después de diseño: analizar impacto, corregir dentro de K-2; cambio de alcance solo por comité.','Semanal; registro de cambios y holgura restante del piloto.',2,3,0,'2026-11'],
['RI-7','Vacaciones y feriados reducen participación de 300 usuarios del piloto y ponen H-3 del 19/12 en riesgo.','5.2',4,4,'PO','Mitigar','Confirmar participantes y suplentes antes del 18/11; distribuir casos por sesión.','Si ejecución <90 % de casos programados en weekly: recuperar sesiones VCA antes del 18/12; si no alcanza, escalar H-3.','Diario C-2 durante piloto; asistencia y casos ejecutados.',2,4,1500,'2026-12'],
['RI-8','UAT concentrada en cuatro días y 120 usuarios deja sesiones incompletas o puntaje <9 y demora el go-live.','5.3,5.4',3,5,'QA / RR.HH.','Mitigar','Confirmar 120 usuarios y suplentes, datos y casos listos al 15/03; sesiones paralelas de 90 min.','Si al segundo día se ejecutó <50 % de casos o nota proyectada <9: recuperar sesiones y ampliar dedicación VCA autorizada; no omitir aceptación.','Diario 16-19/03; tablero de casos, defectos y puntajes.',2,5,2500,'2027-03'],
['RI-9','Vulnerabilidades de configuración o bot producen hallazgos críticos/altos e impiden RA-2.','3.4,2.8,2.9',3,5,'Seguridad VCA / Integraciones','Transferir','Exigir en K-2 corrección de defectos y en K-5 prueba independiente y re-test incluidos; criterios Q-4.','Hallazgo crítico/alto: bloquear pase y exigir corrección y re-test al proveedor. Transferencia propuesta por contrato, sin suponer contrato firmado.','Semanal desde 13/11; informe del tercero y cierre validado por Seguridad.',2,5,0,'2026-12'],
['RI-10','Consulta de planos y dimensionamiento insuficiente no alcanzan p95<500 ms a 300 usuarios y exige capacidad extra.','3.5,5.1,5.4',3,4,'DevOps','Mitigar','Ejecutar carga representativa y perfilar consultas antes de UAT.','Si p95≥500 ms a 300 concurrentes o ≥800 ms a 500: optimizar en K-2 y habilitar capacidad Azure adicional por consumo, con tope autorizado.','Cada build candidato y durante estabilización; p95, errores y costo diario.',2,3,2000,'2027-03'],
['RI-11','Datos HRIS o planos desactualizados causan errores de sincronización >0,5 % o inventario >1 % y reservas inválidas.','2.2,3.2',3,4,'Tecnología / Servicios Generales','Mitigar','Perfilar datos, validar inventario y hacer carga de ensayo con conciliación.','Si se excede umbral: detener importación, corregir fuente VCA y repetir conciliación antes de habilitar.','Por importación y semanal en piloto; conteo esperado versus recibido.',2,3,1800,'2026-11'],
['RI-12','Reservas simultáneas WorkHub/Exchange producen dobles reservas y violan CE-2.','2.4,3.3',3,4,'Integraciones','Mitigar','Pruebas de concurrencia, idempotencia, reintento y conciliación bidireccional.','Un solapamiento confirmado: bloquear conector afectado, aplicar corrección K-2 y repetir casos de carrera.','Cada despliegue y diario en piloto; alertas de duplicados.',2,4,0,'2026-12'],
['RI-13','Ausencia de referentes VCA con dedicación limitada o rotación de Tandem demora validaciones y pierde conocimiento.','2.1,5.2,5.3',3,4,'PM','Mitigar','Nombrar suplentes y mantener runbooks y revisión cruzada dentro de tareas existentes.','Ausencia >2 días en ruta sensible: activar suplente; financiar solo transferencia adicional VCA, reemplazo Tandem a cargo K-2.','Weekly; disponibilidad confirmada dos semanas hacia adelante.',2,3,1500,'2027-03'],
['RI-14','Geocerca sin conformidad de Legal o Seguridad impide su uso y requiere rediseño del check-in.','2.5,4.2',3,4,'Seguridad / RR.HH.','Evitar','Impedir activación de geocerca hasta aprobación formal; usar QR ya previsto en entorno de prueba.','Si se rechaza geocerca: tramitar decisión de alcance y comunicación; no remover requisito unilateralmente ni recolectar ubicación.','Antes de piloto y cada cambio de tratamiento de datos; acta de aprobación.',1,4,0,'2026-11'],
['RI-15','Actualización de WorkHub o API del bot genera regresiones y repetición de pruebas cerca del go-live.','2.x,3.x,5.4',2,4,'PO','Mitigar','Fijar versión soportada, congelar cambios y mantener regresión automatizada.','Aviso de versión incompatible: analizar en sandbox y postergar actualización; entorno de pruebas extendido si no es posible.','Semanal; avisos fabricante y resultados de regresión.',1,4,1000,'2027-03'],
['RI-16','Demora de cotizaciones o firma K-5/K-7 impide sandbox y pentest a tiempo.','3.2-3.4,4.4',3,3,'PM','Mitigar','Preparar alcance y aprobaciones antes de fechas N3: sandbox 23/10, pentest 06/11.','Si no se adjudica a fecha objetivo: escalar a Sponsor y activar proveedor alternativo aprobado; solo costo administrativo adicional de VCA.','Dos veces por semana hasta adjudicar; orden y fecha comprometida.',2,3,500,'2026-11'],
['RI-17','Defectos y dudas al corte simultáneo superan mesa de ayuda y degradan disponibilidad <99,5 %.','4.5,5.4',3,5,'DevOps / Tecnología VCA','Aceptar activa','Reservar guardia VCA adicional y ensayar reversión con runbook. K-2 mantiene corrección de defectos.','Si incidente crítico o cola >20 tickets por 2 h: activar guardia, priorizar incidente y ejecutar rollback si integridad está comprometida.','Diario primera semana y weekly de estabilización; disponibilidad y cola.',2,4,3000,'2027-04'],
['RI-18','Error de pipeline, secreto o configuración despliega una versión no aprobada y causa caída o acceso indebido.','5.1,5.4',3,5,'DevOps','Mitigar','Separar ambientes y credenciales; aprobación de dos personas, artefacto firmado y ensayo de rollback.','Build sin evidencia o diferencia de configuración: detener pase; recuperar secretos/tenant con soporte externo si excede capacidad VCA.','Cada despliegue; auditoría de pipeline y prueba de restauración.',1,5,1000,'2027-03'],
['RI-19','Dependencia vulnerable o sin soporte aparece en análisis de componentes y obliga a detener liberación.','2.8,2.9,3.4',3,4,'Integraciones / Seguridad','Mitigar','Inventariar componentes y versiones, analizar dependencias en CI y revisar avisos semanales.','Hallazgo alto/crítico: bloquear release; proveedor corrige bajo K-2; financiar solo evaluación independiente de alternativa de tercero si se requiere.','Por build y semanal; inventario y reporte de composición.',2,4,1000,'2026-12'],
]
assert sum(r[12] for r in risks)==22000
reserve_items=[
['RI-1',8,'días SG',170,'Conteo manual adicional VCA; no corrección de software K-2'],['RI-1',4,'días RH',160,'Validación adicional de muestra VCA'],
['RI-2',2,'entornos adicionales',1200,'Dos entornos extra por incompatibilidad, además de los dos sandbox iniciales P-4b; precio unitario supuesto'],
['RI-3',4,'piezas adicionales',300,'Ampliación focalizada de campaña, fuera de 12 piezas P-3a'],['RI-3',5,'sesiones adicionales',120,'Logística extra a las 30 sesiones P-3c'],
['RI-7',10,'días-persona USR',150,'Recuperación extraordinaria de piloto; no horas ya planificadas'],
['RI-8',10,'días-persona USR',150,'Sesiones adicionales a 22,5 días-persona UAT base'],['RI-8',4,'días SG',170,'Apoyo adicional UAT'],['RI-8',2,'días RH',160,'Coordinación adicional UAT'],
['RI-10',2,'meses capacidad adicional',1000,'Incremento cloud marzo/abril, fuera de P-2c; capacidad y precio por validar'],
['RI-11',5,'días SG',170,'Corrección adicional de fuente de inventario VCA'],['RI-11',5,'días TEC',190,'Corrección adicional de fuente HRIS VCA'],
['RI-13',2,'días TEC',190,'Transferencia extraordinaria VCA; sustitución Tandem cubierta K-2'],['RI-13',7,'días RH',160,'Inducción adicional de referente VCA'],
['RI-15',1,'extensión sandbox',1000,'Extensión extraordinaria de prueba de nueva versión, distinta de P-4b inicial; precio supuesto'],
['RI-16',2,'días Compras/Legal VCA',250,'Costo interno adicional supuesto; no PM Tandem ya incluido'],
['RI-17',8,'días TEC',190,'Guardia VCA extra primera semana; no corrección de defectos K-2'],['RI-17',4,'días SG',170,'Guardia VCA adicional'],['RI-17',5,'días RH',160,'Guardia adicional de referentes'],
['RI-18',1,'servicio recuperación tenant',1000,'Soporte externo extraordinario a VCA; no retrabajo de pipeline contratado K-2'],
['RI-19',2,'días especialista independiente',500,'Evaluación adicional de alternativa de tercero; no corrección propia ni re-test K-5']]
assert sum(x[1]*x[3] for x in reserve_items)==22000
for r in risks:assert sum(x[1]*x[3] for x in reserve_items if x[0]==r[0])==r[12]
quality=[
['Q-1','Revisión por pares','100 % de cambios propios de código, scripts, infraestructura y configuración versionable aprobados por al menos un par distinto del autor.','PR aprobados / PR integrados ×100; checklist y trazabilidad a requisito. Excluir binarios del fabricante; revisar su configuración y versión.','DEV/INT/OPS ejecutan, PO controla','En cada PR; ramas protegidas. Si falta aprobación, no integrar.','2.x,3.x,5.1','Nuevo umbral del equipo'],
['Q-2','Pruebas unitarias','≥80 % de líneas y ≥70 % de ramas del código propio; 100 % de reglas críticas de reserva, permisos e idempotencia con casos positivos y negativos.','Informe CI; cobertura sobre código ejecutable propio; exclusiones generadas/documentadas aprobadas por QA. Casos críticos pasados / inventario crítico =100 %.','DEV/INT ejecutan, QA verifica','En cada build; si incumple, bloquear candidato y añadir pruebas.','2.3-2.9,3.1-3.3','Nuevo umbral del equipo'],
['Q-3','Conformidad funcional','100 % de casos críticos de extremo a extremo aprobados; cero solapamientos de reservas; error de sincronización ≤0,5 %.','Suite con SSO, altas/bajas, reserva/cancelación, check-in y doble reserva. Errores / registros procesados ×100. Evidencia de datos y logs.','QA e Integraciones; Tecnología acepta','Cada integración y antes de piloto/UAT. Fallo crítico impide pase.','2.4,2.5,3.1-3.5','CE-2 y aceptación N1/N3; 100 % equipo'],
['Q-4','Seguridad','Cero hallazgos críticos o altos abiertos. ASVS v5.0.0-8.1.1: permisos documentados; 8.2.1: función con permiso explícito; 8.2.2: autorización por objeto; 8.3.1: control en servicio confiable.','Prueba independiente K-5; usuario A no cancela reserva B; rol sin permiso no administra salas; acceso directo a API tampoco elude control. Análisis estático/dependencias y re-test. No se afirma nivel ASVS completo.','Tercero prueba; Seguridad VCA acepta','Antes de piloto: controles de acceso y revisión preliminar; informe final al 04/12, re-test antes de UAT. Si falla, bloquear.','3.4,2.8,2.9','RA-2 + OWASP ASVS5.0.0'],
['Q-5','Rendimiento','p95<500 ms a 300 concurrentes (CE-3), y p95<800 ms a 500 concurrentes (aceptación 3.0); error técnico <1 % en cada escenario.','Carga 30 min tras 5 min de calentamiento, mezcla reproducible reserva/búsqueda/cancelación; mismo tamaño de datos y topología prevista. p95 sobre solicitudes exitosas y errores por separado.','QA mide; DevOps ajusta; Tecnología acepta','3.5 y candidato final. Repetir tras cambio de consulta, configuración o capacidad.','3.5,5.1,5.4','CE-3; duración y error propuestos'],
['Q-6','Confiabilidad y resiliencia','Disponibilidad ≥99,5 % durante estabilización; recuperación ≤4 h y pérdida de datos ≤24 h en ensayo de restauración.','Disponibilidad=(minutos acordados−indisponibilidad no planificada)/minutos acordados. Ventana24×7, sin excluir incidentes propios. Logs y prueba de restauración en staging.','DevOps; Tecnología VCA acepta','Monitoreo diario; ensayo antes de go-live. Incumplimiento genera incidente y plan correctivo.','5.1,5.4','99,5 % N3; recuperación propuesta'],
['Q-7','Datos e inventario','Discrepancia inventario ≤1 % y ocupación real versus sistema ≤5 %.','Inventario: diferencias / puestos relevados. Ocupación: diferencia absoluta / conteo manual, por planta y franja; al menos 5 días de muestra. Cero manual se informa aparte.','Servicios Generales; PO concilia','Inventario antes de piloto; ocupación semanal en piloto y estabilización. No emitir recomendación con muestra insuficiente.','2.2,2.5,5.6','RA-4 y aceptación N3; muestra equipo'],
['Q-8','Aceptación y usabilidad','UAT ≥9,0/10 con al menos 120 usuarios; mediana de reserva + check-in ≤2 min; 100 % de escenarios críticos ejecutados; cero defectos bloqueantes.','Puntaje medio de cuestionario aprobado por RR.HH.; lista de participantes y evidencia por caso. No sustituir ejecución por satisfacción.','QA coordina, RR.HH. verifica; Sponsor firma','16-19/03; evaluación diaria. Si falla, corregir, repetir casos y gestionar impacto en H-5.','5.3','N2/N3; cobertura crítica equipo'],
]
monthkeys=['2026-10','2026-11','2026-12','2027-01','2027-02','2027-03','2027-04']
cal=[r[1] for r in list(w['Calendario'].values)[2:] if isinstance(r[1],datetime)]
alloc=[]
for t in tasks:alloc.append(dict(id=t['id'],kind='Labor',cost=t['labor'],start=t['start'],end=t['end']))
for p in parts:alloc.append(dict(id=p['id'],kind='Partida',cost=p['cost'],start=p['start'],end=p['end']))
for a in alloc:
    dates=[d for d in cal if a['start']<=d.strftime('%Y-%m-%d')<=a['end']]
    if not dates:raise ValueError(a)
    a['weights']=[sum(d.strftime('%Y-%m')==m for d in dates)/len(dates) for m in monthkeys]
monthly=[]; cum=0
for j,m in enumerate(monthkeys):
    base=sum(a['cost']*a['weights'][j] for a in alloc);reserve=sum(r[12] for r in risks if r[13]==m);cum+=base+reserve
    monthly.append(dict(month=m,base=base,reserve=reserve,total=base+reserve,cumulative=cum))
assert len(tasks)==31 and abs(sum(t['M'] for t in tasks)-372700)<.001
assert sum(r[12] for r in risks)==22000 and abs(cum-394700)<.001
data=dict(tasks=tasks,labor=labor,parts=parts,classes=classes,risks=risks,reserve_items=reserve_items,quality=quality,monthly=monthly,alloc=alloc,monthkeys=monthkeys)
(ROOT/'model_data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))

def money(n):return f'{n:,.0f}'.replace(',','.')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyN4',fontName='Helvetica',fontSize=9,leading=12,spaceAfter=7,textColor=colors.HexColor('#22354A')))
styles.add(ParagraphStyle(name='CellN4',fontName='Helvetica',fontSize=7.8,leading=10))
styles.add(ParagraphStyle(name='SmallN4',fontName='Helvetica',fontSize=8,leading=10,spaceAfter=5))
styles['Title'].fontName='Helvetica-Bold';styles['Title'].textColor=colors.HexColor('#142E49');styles['Title'].fontSize=27
styles['Heading1'].fontSize=19;styles['Heading1'].textColor=colors.HexColor('#142E49')
styles['Heading2'].fontSize=12;styles['Heading2'].textColor=colors.HexColor('#007A78')
story=[]; md=[]
def p(txt,style='BodyN4'):
    story.append(Paragraph(txt,styles[style]));md.append(txt.replace('<b>','**').replace('</b>','**'))
def title(txt):story.append(Paragraph(txt,styles['Heading1']));md.append('\n## '+txt)
def sub(txt):story.append(Paragraph(txt,styles['Heading2']));md.append('\n### '+txt)
def page():story.append(PageBreak());md.append('\n---\n')
def table(headers,rows,widths=None,small=7.8):
    headstyle=ParagraphStyle('head',parent=styles['CellN4'],textColor=colors.white,fontName='Helvetica-Bold')
    content=[[Paragraph(str(x),headstyle) for x in headers]]+[[Paragraph(str(x).replace('\n','<br/>'),styles['CellN4']) for x in row] for row in rows]
    tb=Table(content,colWidths=widths,repeatRows=1,hAlign='LEFT')
    tb.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#142E49')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('VALIGN',(0,0),(-1,-1),'TOP'),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F0F4F7')]),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('LINEBELOW',(0,0),(-1,0),.8,colors.HexColor('#007A78'))]))
    story.append(tb);story.append(Spacer(1,8))
    md.append('| '+' | '.join(headers)+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+'\n'.join('| '+' | '.join(str(x).replace('\n','; ') for x in row)+' |' for row in rows))

p('UADE · Dirección de Proyectos Informáticos · 2026','SmallN4')
story.append(Spacer(1,20));p('WorkHub · Entrega N4','Title')
p('Costos detallados, control de gestión, calidad y riesgos','Heading2')
p('<b>Grupo 1</b> · Abosch, Nicolás (líder) · Jeandet · Diaz · Garcia · Gonzalez<br/>Docente: Mag. Ezequiel Pietracupa<br/>VCA, sede Catalinas · proveedor Tandem · Proyecto WKH-2026<br/>Fecha de entrega: 31 de octubre de 2026')
sub('Decisión de presupuesto')
p('Se mantiene como propuesta de control la línea base de <b>USD 394.700</b> de la N2 corregida, citada por la última N3 confirmada. La estimación multipunto aporta rangos y contraste PERT a las 31 tareas. El precio fijo de implementación no aumenta por la variabilidad técnica del proveedor. Esta entrega es un plan académico: no acredita gastos, avance real, contratos firmados ni aprobaciones nuevas.')
table(['Componente','USD','Criterio'],[['Actividades y partidas (M)',money(372700),'235.926 de mano de obra + 136.774 no laborales'],['Contingencia',money(22000),'Dentro de la línea base; asignada a acciones residuales identificadas'],['Línea base de costos',money(394700),'372.700 + 22.000'],['Reserva de gestión (4 %)',money(15788),'Fuera de la línea base; libera el Comité'],['Presupuesto total',money(410488),'Línea base + gestión'],['Techo del Acta / margen no asignado','420.000 / 9.512','El margen no es una reserva adicional']],[190,95,480])
p('El documento concentra la N4. El Excel permite auditar recursos, tarifas, esfuerzo, partidas, escenarios, distribución mensual, controles de calidad y los 19 riesgos. Los 17 riesgos de la N3 se conservan; RI-18 y RI-19 amplían riesgos propios del software. Se requieren cotizaciones, revisión de expertos y ratificación del plan antes de su uso operativo.','SmallN4')

page();title('1. Base de estimación y continuidad')
p('Fuente de continuidad: N2 corregida, PDF pp. 7-9 y Excel, y N3 revisión 2, PDF pp. 2-4 y 12-13. No se toma el presupuesto de USD 398.000 del Markdown N2 original como la versión corregida. Las 31 tareas conservan identificadores de la Estructura de Desglose del Trabajo (EDT), duraciones y recursos. La externalidad R-3, ventana de balances, no es un paquete ni una tarea con costo propio.')
sub('Recursos, esfuerzo y precios')
table(['Recurso','USD/día','Recurso','USD/día','Regla'],[['PM / PO','520 / 480','UX / DEV','420 / 440','Día-persona de 8 horas; esfuerzo = FTE × duración'],['QA / INT','360 / 480','OPS / CAM','460 / 400','FTE = dedicación equivalente a tiempo completo'],['TEC / SG','190 / 170','RH / USR','160 / 150','Horas VCA a costo interno cargado; Tandem a tarifa de venta']],[105,80,100,80,400])
p('PM: dirección de proyecto; PO: responsable de producto; UX: diseño de experiencia de usuario; DEV: desarrollo; QA: aseguramiento de calidad; INT: integraciones; OPS: DevOps; CAM: gestión del cambio; TEC: Tecnología VCA; SG: Servicios Generales; RH: RR.HH.; USR: usuarios de prueba.','SmallN4')
p('Las tarifas y precios heredados son supuestos de simulación, no precios de mercado verificados. La licencia de USD 108.000 proviene del caso N1, sin adjuntar una cotización comercial comprobada. No se suman impuestos, inflación ni tipo de cambio: moneda USD nominal y tarifa constante, supuesto académico pendiente de contrato. El modelo mide costo del proyecto VCA, incluyendo costo de oportunidad de sus horas. No confundir esfuerzo con duración: dos recursos durante 10 días pueden producir 20 días-persona.')
sub('Técnica multipunto y decisión de línea base')
p('O es costo optimista, M el más probable y P el pesimista, todos en USD y para el mismo alcance. PERT (técnica de evaluación y revisión de programas) calcula (O + 4 × M + P) / 6. Se aplica a la mano de obra con tres clases de incertidumbre; las partidas no laborales se conservan en O=M=P por precio/cantidad contractual supuestos. No se inventan históricos para llamarlo estimación análoga.')
table(['Clase','Escenario que explica O/M/P'],[[k+' · '+v['name'],v['scenario']] for k,v in classes.items()],[190,575])
pert=sum(t['PERT'] for t in tasks)
p(f'Las bandas son hipótesis académicas iniciales, no probabilidades ni intervalos de confianza. PERT agregado: <b>USD {money(pert)}</b>, diferencia de USD {money(pert-372700)} frente a M. Siguiendo DPI5 p. 11 se mantiene M en la línea base y PERT como contraste. K-2 de N3 fija USD 216.888 de Tandem; su retrabajo dentro del alcance se cubre con ese precio. Cambios aprobados o mayores obligaciones de VCA requieren decisión expresa, no un incremento automático por PERT. La suma de extremos no constituye un pronóstico probabilístico del proyecto.','SmallN4')

for i,(start,end) in enumerate([(0,16),(16,31)]):
    page();title(f'1.{i+1} Costos por tarea · '+('gestión y plataforma' if i==0 else 'integración, adopción y cierre'))
    p('USD. Base de mano de obra = días-persona × tarifa diaria. NL = partidas no laborales asignadas una sola vez. M = mano de obra + NL. O/P solo varían mano de obra según clase A/B/C. PERT se muestra redondeado; el Excel conserva precisión.','SmallN4')
    rows=[]
    for t in tasks[start:end]:rows.append([t['id']+' '+t['name'],str(t['duration'])+' d / '+t['class'],t['basis'],money(t['nonlabor']),money(t['O']),money(t['M']),money(t['P']),money(t['PERT'])])
    table(['EDT / tarea','Dur./clase','Días-persona × USD/día','NL','O','M','P','PERT'],rows,[160,52,235,52,65,65,65,65])
    if i==1:p('Control: 31 paquetes, USD 235.926 laborales + USD 136.774 no laborales = USD 372.700. PM de seguimiento: 132 días × 0,5 FTE × USD 520 = USD 34.320. R-3 no agrega horas. No se reducen duraciones ni se promete capacidad adicional. Para ejecutar el escenario P debe revalidarse carga y calendario; no autoriza recortes de plazo.','SmallN4')

page();title('1.3 Partidas no laborales y trazabilidad contractual')
table(['Partida / concepto','Cantidad × USD/unidad','USD','EDT','Período de devengo N4'],[[x['id']+' '+x['name'],f"{x['quantity']:g} {x['unit']} × {x['price']:g}",money(x['cost']),x['task'],x['start']+' a '+x['end']] for x in parts],[330,140,70,50,175])
p('Asignación presupuestaria: ambientes y herramientas comunes se cargan a 5.1 para evitar duplicación por cada módulo, conservando su devengo real por período. P-4b se asigna a 3.2 como cuenta agrupadora para ambos conectores; el registro de partidas conserva su alcance. Producción usa 422 USD/mes redondeados de la hipótesis N1; se retiene el precio unitario N2 para reproducir sus USD 844.')
p('Conciliación: K-1/K-3 a K-9 (no laborales) USD 136.774 + K-2 Tandem USD 216.888 + horas VCA USD 19.038 = USD 372.700. El precio fijo y las garantías se tratan como condiciones contractuales propuestas en N3, sin afirmar firma o transferencia efectiva. La contingencia no paga defectos ya incluidos en K-2/K-5.')
p('Ajustes de calendario de costos: sandbox se devenga desde 30/10, coherente con necesidad de N3 (N2 partidas usaba 14/10); los USD 3.600 de logística de las 30 sesiones masivas se devengan del 22 al 30/03, después de balances y de UAT. Las piezas y formación de referentes permanecen antes. Las sesiones se replican por referentes formados, supuesto N3; su disponibilidad debe validarse. No cambia ningún total ni hito, pero se corrige la distribución mensual respecto de N2. La fecha de pago contractual no determina por sí sola el avance ganado.','SmallN4')

page();title('1.4 Línea base distribuida y reservas')
p('La línea base integra USD 372.700 de trabajo planificado y USD 22.000 de contingencia. Las actividades laborales se devengan linealmente en días hábiles de N2; las partidas se distribuyen en su período explícito. Es una aproximación del costo devengado, no un cronograma de pagos. La contingencia ahora se ubica en el mes de exposición del riesgo y no se prorratea como N2.')
table(['Mes','Actividades USD','Contingencia USD','Línea base mensual USD','Acumulada USD'],[[x['month'],money(x['base']),money(x['reserve']),money(x['total']),money(x['cumulative'])] for x in monthly]+[['Total','372.700','22.000','394.700','394.700']],[110,160,160,175,159])
chart=Drawing(740,170);chart.add(Line(55,28,710,28,strokeColor=colors.HexColor('#8293A4')))
for v in [0,100000,200000,300000,400000]:
    y=28+v/400000*120;chart.add(Line(55,y,710,y,strokeColor=colors.HexColor('#DEE5EB')));chart.add(String(0,y-3,str(v//1000),fontSize=8))
pts=[]
for i,x in enumerate(monthly):
    xx=90+i*100;yy=28+x['cumulative']/400000*120;pts.extend([xx,yy]);chart.add(String(xx-18,12,x['month'],fontSize=8));chart.add(String(xx-10,yy+7,str(round(x['cumulative']/1000)),fontSize=8))
chart.add(PolyLine(pts,strokeColor=colors.HexColor('#007A78'),strokeWidth=2));chart.add(String(0,160,'Miles de USD acumulados · línea base de costos',fontSize=9));story.append(chart)
p('Control de reservas: USD 22.000 es una provisión agregada para acciones residuales concretas del registro, no la suma de pérdidas máximas ni P×I monetizado. La asignación es una propuesta de juicio experto pendiente de validar. Si el evento no ocurre, se libera saldo. PM puede autorizar hasta USD 5.000 por evento; más de ese monto va al Sponsor. Cambiar línea base, alcance o cierre, o impacto >5 %, requiere Comité. Gestión: USD 15.788 fuera de línea base; no se gana valor por mantenerla disponible.','SmallN4')

page();title('2. Control de gestión mediante Valor Ganado')
p('EVM, Earned Value Management (gestión del valor ganado), compara trabajo previsto, trabajo aceptado y costo incurrido a una misma fecha. No hay datos reales comprobados de avance o gasto de WorkHub en estas fuentes. El Excel separa entradas reales vacías de un ejemplo numérico rotulado ilustrativo.')
table(['Indicador / unidad','Definición y cálculo','Uso'],[['PV · USD','Valor planificado: suma del presupuesto de cada tarea × avance previsto a la fecha.','Se calcula con períodos y criterios de medición aprobados; no con facturas pagadas.'],['EV · USD','Valor ganado: suma del presupuesto de cada tarea × avance físico aceptado.','0/100 para entregables breves; hitos ponderados para módulos e integraciones; LOE de 1.5 solo por servicio de gestión prestado.'],['AC · USD','Costo real incurrido: horas valorizadas, facturas y provisiones devengadas por tarea.','Conciliar con Contabilidad, mismo alcance/corte; no inferir AC a partir de EV.'],['CV / SV · USD','Variación de costo CV=EV−AC; variación de cronograma SV=EV−PV.','Negativo es desfavorable. SV expresa dinero de trabajo pendiente, no días de atraso.'],['CPI / SPI · razón','Índice de costo CPI=EV/AC; índice de cronograma SPI=EV/PV.','<1 desfavorable; ≥1 requiere interpretar calidad y camino crítico, no solo gasto.'],['BAC / EAC / ETC / VAC · USD','BAC: presupuesto hasta la conclusión; EAC: estimación a la conclusión = BAC/CPI; ETC: costo estimado para completar = EAC−AC; VAC: variación a la conclusión = BAC−EAC.','Pronóstico por eficiencia pasada, útil si es representativa. Complementar estimación ascendente cuando cambia el contexto.'],['TCPI · razón','Índice de desempeño requerido para cumplir BAC: (BAC−EV)/(BAC−AC).','Solo si BAC−AC>0; si no, informar objetivo inviable y revisar EAC.']],[130,360,275])
p('<b>Convención BAC:</b> se sigue DPI6 p.20: BAC operativo = USD 372.700 (trabajo de las 31 tareas). Contingencia USD 22.000 permanece en línea base como reserva no distribuida; BAC operativo + reserva = USD 394.700. La curva anterior muestra línea base completa; para PV/EV usar solo trabajo distribuido, excluyendo reserva aún no autorizada. No se gana valor por el paso del tiempo sobre una reserva. Al activar respuesta, transferir presupuesto desde contingencia a tarea/paquete, con plan futuro y evidencia, sin alterar línea base total salvo cambio aprobado. Así BAC operativo aumenta y reserva disminuye por igual.','SmallN4')
sub('Método de medición y evidencia')
p('Antes de cada módulo 2.3-2.9 o conector 3.1-3.3: acordar hitos 20 % diseño aprobado, 50 % configuración/código integrado y revisión completa, 30 % pruebas de aceptación del paquete aprobadas. No acreditar porcentajes subjetivos. Para tareas de documentos y servicios breves, EV=0 hasta aceptación y 100 % al cerrar. Licencia gana valor cuando está habilitada y aceptada, no por anticipo. En tareas con partidas comunes, medir por separado disponibilidad del servicio y entregable laboral; el costo asignado a 5.1 no implica ganar siete meses de nube al crear el ambiente.','SmallN4')

page();title('2.1 Cortes, alertas y escenario ilustrativo')
p('El plan temporal por día hábil permite distribuir costos; para usarlo como PV de hitos discretos debe acordarse y cargar la fecha de aceptación planificada por componente. La hoja EVM recibe PV validado del plan por componente, EV aceptado y AC conciliado. No usa automáticamente el gasto mensual de la línea base completa como PV. El reporte operativo queda pendiente hasta cargar esa evidencia.','SmallN4')
table(['Control','Responsable / frecuencia','Umbral propuesto y acción'],[['Cierre de estado','PM + QA + Contabilidad; viernes semanal y cierre mensual','QA confirma entregables, PM congela corte, Contabilidad concilia incurridos. Informe C-8 y mensual C-10.'],['Alerta de desempeño','PM; cada corte','CPI o SPI <0,95: analizar causas y plan en 2 días hábiles. <0,90: Sponsor en 48 h. Umbrales del equipo, no exigencia normativa.'],['Pronóstico y reservas','PM / Sponsor; mensual','EAC operativo + reserva residual >410.488: elevar al Comité. Cualquier cambio de línea base o hito se aprueba, no se oculta con reserva.'],['Cronograma crítico','PM; weekly y diario en UAT','Verificar R-3→5.3→5.4→5.5/5.6→1.6 y H-3; SPI no sustituye camino crítico ni calendario.'],['Calidad y cierre','QA / Sponsor; cada entrega','No ganar valor por código rechazado, trabajo rehacer ni porcentaje de gasto. Bloqueos de calidad prevalecen sobre semáforo EVM.']],[145,260,360])
sub('Ejemplo de cálculo, sin datos reales de WorkHub')
B=372700;PV=200000;EV=180000;AC=195000;CPI=EV/AC
table(['Entrada ilustrativa','Valor','Resultado calculado','Valor'],[['BAC operativo','372.700','CPI / SPI',f'{CPI:.4f} / {EV/PV:.4f}'],['PV / EV / AC','200.000 / 180.000 / 195.000','CV / SV USD','−15.000 / −20.000'],['Reserva no distribuida / gestión','22.000 / 15.788','EAC / ETC USD',f'{money(B/CPI)} / {money(B/CPI-AC)}'],['Fecha de corte del ejemplo','30/11/2026 (ficticia)','VAC USD / TCPI',f'{money(B-B/CPI)} / {(B-EV)/(B-AC):.4f}']],[185,170,200,210])
p(f'Interpretación ilustrativa: el trabajo ganado equivale a 90 % de lo previsto y cada USD gastado gana USD {CPI:.4f} presupuestados. Si esa eficiencia persistiera, EAC operativo sería USD {money(B/CPI)}; sumando una reserva residual hipotética intacta de USD 22.000, la necesidad sería USD {money(B/CPI+22000)}, superior al presupuesto total de USD 410.488. Se requeriría decisión del Comité. Esta suma conservadora no aplica si el EAC ya incorpora las respuestas; evitar doble conteo. No equivale a afirmar un atraso de 20.000 días ni una fecha final nueva.')

page();title('3. Plan de gestión de calidad del software')
p('Calidad significa cumplir requisitos y expectativas de uso. El plan combina prevención en proceso y verificación de entregables (GDP Calidad pp.3-6). El objetivo es liberar reservas e integraciones seguras, datos confiables y una plataforma operable para 1.200 usuarios. Las dimensiones técnicas se organizan con ISO/IEC 25010:2023, edición 2, modelo de calidad de producto, y OWASP ASVS 5.0.0 como marco de verificación de seguridad web. No se afirma certificación, auditoría de norma íntegra ni cumplimiento de un nivel ASVS completo.')
sub('Prevención, control y responsabilidad')
table(['Etapa / momento','Mecanismo y evidencia','Responsabilidad y salida'],[['Diseño · 2.1/2.7 y 3.1','Vincular requisito→EDT→caso de prueba→aceptación. Revisar reglas, arquitectura, flujos de datos y amenazas. Registro de observaciones y cierre.','PO y QA con Tecnología/Seguridad; diseño aprobado antes de construir componente.'],['Construcción · cada cambio','Revisión por pares distinta del autor, rama protegida, CI (integración continua), pruebas unitarias, análisis estático y de dependencias. Versionar configuración e infraestructura.','DEV/INT/OPS corrigen; par aprueba; QA audita semanalmente muestra de PR y excepciones.'],['Integración · 3.4/3.5','Pruebas de contrato, punta a punta, concurrencia, carga y seguridad independientes. Ambiente equivalente a producción y datos sintéticos/desidentificados autorizados.','QA coordina, tercero K-5 prueba seguridad y Tecnología valida resultados.'],['Piloto y UAT · 5.2/5.3','300 usuarios piloto; UAT 120 usuarios. Casos y encuestas versionados, defectos con severidad, evidencia y repetición.','RR.HH./SG validan uso; QA verifica criterios; Sponsor firma aceptación UAT.'],['Pase y estabilización · 5.4','Checklist de versión, aprobaciones, respaldo, restauración, observabilidad, mesa N1 y reversión. Comparar métricas con umbrales.','DevOps prepara; Tecnología autoriza pase; Sponsor acepta cierre con evidencia.']],[155,390,220])
p('Tratamiento de defectos: bloqueante impide función crítica o compromete integridad/seguridad; alto afecta criterio sin alternativa aceptable; medio tiene alternativa; bajo es cosmético sin pérdida funcional. QA clasifica con PO y Seguridad. Bloqueantes y altos deben cerrarse y repetir pruebas antes del pase. Medios/bajos solo con aceptación escrita, responsable y fecha; nunca exceptuar un requisito crítico. Registrar hallazgo, versión, caso, severidad, dueño, vencimiento y evidencia de re-test.')
p('Presupuesto de calidad: revisiones y pruebas están en días DEV/QA/INT de cada tarea, pruebas integradas en 3.4/3.5 y K-5 USD 7.500; herramientas en P-2e y observabilidad P-2d. No agregar nuevamente estos costos como reserva. Auditoría semanal de proceso por QA: verificar evidencia de PR, trazabilidad de casos y cierres; el PM sigue acciones, sin suponer que esas auditorías ya ocurrieron.','SmallN4')

page();title('3.1 Métricas y puertas de aceptación')
p('Los porcentajes 100 % de revisión, 80 % de líneas, 70 % de ramas y demás métodos nuevos son decisiones propuestas del equipo por criticidad e integraciones; no porcentajes impuestos por ISO ni por la clase. Las metas heredadas se identifican. Los valores se validarán con VCA y Tandem antes de ejecutar.','SmallN4')
table(['ID / dimensión','Umbral y alcance','Medición / evidencia','Quién y cuándo / incumplimiento'],[[q[0]+' '+q[1],q[2],q[3],q[4]+'. '+q[5]] for q in quality],[100,220,245,200])

page();title('4. Riesgos: escalas, prioridad y mapa')
p('Se conservan RI-1 a RI-17 de N3 y se agregan RI-18/19. Riesgo inherente = exposición antes de las respuestas N4. Probabilidad P e impacto I se valoran de 1 a 5 para todo el horizonte hasta 30/04/2027. Las probabilidades son juicio académico, no frecuencias observadas. N3 alta se lleva a P4, media a P3 y baja a P2; se revalidarán con evidencia. No se usa P5 para eventos ya ocurridos.','SmallN4')
table(['Valor','Probabilidad orientativa','Impacto: tomar máximo en costo, plazo o calidad'],[['1','Muy baja: ≤10 %','Costo adicional ≤1.000 USD; demora ≤1 día; defecto menor sin criterio de aceptación afectado.'],['2','Baja: >10 a 30 %','>1.000 a 3.000 USD; >1 a 3 días; componente secundario con alternativa operativa.'],['3','Media: >30 a 50 %','>3.000 a 8.000 USD; >3 a 5 días; retrabajo de módulo recuperable antes del hito.'],['4','Alta: >50 a 80 %','>8.000 a 15.000 USD; >5 a 10 días o riesgo de H-3; aceptación de módulo principal comprometida.'],['5','Muy alta: >80 a <100 %','>15.000 USD; >10 días o cualquier desvío H-5/H-6/H-7; bloqueo de seguridad, integridad o beneficio principal.']],[45,160,560])
p('Prioridad = P×I: baja 1-5 (seguimiento mensual), media 6-12 (semanal), alta 15-25 (semanal con Sponsor; diaria ante disparador). Las celdas 13/14 no son posibles con enteros 1-5. Una consecuencia crítica de seguridad o un hito obligatorio se escala aunque el producto sea medio. P e I residuales son metas posteriores a respuesta, no evidencia de reducción ya lograda. Los USD de reserva son límites de acción, no equivalentes al puntaje.','SmallN4')
matrix=[]
for pp in range(5,0,-1):
    matrix.append([f'P={pp}']+[f"{pp*ii}\n"+', '.join(r[0] for r in risks if r[3]==pp and r[4]==ii) for ii in range(1,6)])
content=[['P / I','I=1','I=2','I=3','I=4','I=5']]+matrix
tb=Table([[Paragraph(c.replace('\n','<br/>'),styles['CellN4']) for c in row] for row in content],colWidths=[65]+[140]*5,rowHeights=[23]+[38]*5)
commands=[('VALIGN',(0,0),(-1,-1),'MIDDLE'),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#DCE5ED')),('GRID',(0,0),(-1,-1),.5,colors.white)]
for yy in range(1,6):
    for xx in range(1,6):
        score=(6-yy)*xx; commands.append(('BACKGROUND',(xx,yy),(xx,yy),colors.HexColor('#F2B5AA' if score>=15 else '#F6DDA6' if score>=6 else '#CFE5D5')))
tb.setStyle(TableStyle(commands));story.append(tb)
md.append('\n### Matriz inherente\n\n| '+' | '.join(content[0])+' |\n| '+' | '.join(['---']*6)+' |\n'+'\n'.join('| '+' | '.join(x.replace('\n','; ') for x in row)+' |' for row in content[1:]))
p('Verde: baja · ámbar: media · rojo: alta. Eje vertical: probabilidad creciente hacia arriba; horizontal: impacto creciente hacia la derecha. Se adapta el artefacto GDP Incertidumbre pp.10-18 a la escala 1-5 exigida por N4. La estrategia se decide por causa y capacidad de respuesta; el cuadrante no impone automáticamente una estrategia.','SmallN4')

for block in range(4):
    page();title(f'4.{block+1} Registro y respuestas · RI-{block*5+1} a RI-{min(block*5+5,19)}')
    p('Estado de todos: identificado / plan propuesto, pendiente de validación. P/I son inherentes; R=P×I; residual=P/I meta. Los montos son límites incrementales de contingencia VCA. La prevención habitual ya está en M; el gasto residual solo se autoriza ante disparador y no duplica obligación del proveedor.','SmallN4')
    for r in risks[block*5:block*5+5]:
        sub(f'{r[0]} · P{r[3]} / I{r[4]} / R{r[3]*r[4]} · {r[6]} · residual {r[10]}/{r[11]} · reserva USD {money(r[12])}')
        p(f'<b>Causa, evento y efecto:</b> {r[1]} <b>EDT:</b> {r[2]}. <b>Dueño:</b> {r[5]}.','SmallN4')
        p(f'<b>Plan preventivo:</b> {r[7]} <b>Disparador y respuesta:</b> {r[8]}','SmallN4')
        p(f'<b>Monitoreo y evidencia:</b> {r[9]} <b>Mes de exposición:</b> {r[13]}.','SmallN4')
    if block==3:p('Suma de asignaciones: USD 22.000. RI-5 tiene aceptación activa con plan de contingencia de fecha y escalamiento, sin reserva monetaria específica: dinero no elimina el bloqueo de balances. RI-4 es aceptación pasiva del beneficio, vigilada por el Sponsor. La transferencia RI-9 reduce exposición económica propuesta, conserva riesgo de calidad y responsabilidad de aceptación en VCA.','SmallN4')

page();title('4.5 Base de cálculo de la contingencia')
p('Los USD 22.000 conservan el techo de provisión heredado y se desagregan en una propuesta inicial de paquetes de respuesta. Cada cantidad es capacidad incremental condicionada al disparador, sin evidencia de gasto ni cotización. Las tarifas de roles existentes son las de N2; los servicios y perfiles nuevos son hipótesis explícitas. Esta suma no constituye valor monetario esperado ni demuestra suficiencia estadística. Reestimar de forma independiente al validar los riesgos; si el costo necesario supera la provisión, elevar cambio, sin forzar el resultado a USD 22.000.','SmallN4')
rr=[]
for r in risks:
    items=[x for x in reserve_items if x[0]==r[0]]
    if items:rr.append([r[0],'; '.join(f'{x[1]:g} {x[2]} × USD {x[3]:g}' for x in items),money(r[12]),'; '.join(x[4] for x in items)])
table(['Riesgo','Cantidad incremental × tarifa/precio','USD','Exclusión y fundamento'],rr,[60,235,65,405])
p('Activar una respuesta no presupone disponibilidad ilimitada. PM debe confirmar capacidad y fechas de los recursos adicionales antes de autorizar; si afecta un hito obligatorio, escala aunque el monto sea menor a USD 5.000. No sumar a esta tabla diferencias PERT ni costos ya comprometidos. RI-4/5/6/9/12/14 no tienen provisión incremental: su plan usa decisiones de negocio, escalamiento o obligaciones incluidas en M. Fechas anteriores al 27/10 son fechas del plan base; no se comprobó su ejecución. Verificar de inmediato RI-16 y contratos antes de usar este plan operativamente.','SmallN4')

page();title('5. Justificación del Juicio de Experto y validación')
p('La técnica usa conocimiento especializado para estimar y decidir cuando los datos históricos son insuficientes. Complementa el cálculo y no reemplaza al equipo (DPI11 pp.4-5 y 14). WorkHub combina configuración de producto comprado, APIs, datos VCA y una ventana crítica de balances; por eso una tarifa × esfuerzo no basta para establecer rangos, impacto o respuesta. No se inventan entrevistas: los rangos, puntajes, reservas y umbrales de esta entrega son hipótesis académicas del Grupo 1, pendientes de contraste con los perfiles indicados.')
table(['Consulta propuesta','Decisión que sustenta','Evidencia necesaria / criterio de revisión'],[['PM + responsable comercial Tandem + Finanzas VCA','Tarifas, K-2 fijo, alcance de garantías y O/M/P; contingencia a cargo VCA.','Oferta y SOW revisados; matriz de exclusiones; estimaciones independientes por paquete, luego consenso documentado.'],['Integraciones + Tecnología VCA + fabricantes','Rangos clase C, RI-2/12/15/19 y cuotas sandbox.','Contratos API, ensayo técnico y supuestos de permisos/versiones; ajustar P/I y costos por evidencia.'],['QA + Seguridad + tercero independiente','Umbrales, aplicabilidad ASVS y RI-9/18/19.','Inventario de controles, informe de pruebas y capacidad del pipeline; revisar severidad sin ocultar bloqueos.'],['RR.HH. + SG + Sponsor','RI-1/3/4/5/7/8/11/13/17; costos y disponibilidad VCA.','Muestra de datos, agenda de UAT, disponibilidad de referentes, ventana de balances y capacidad de soporte.']],[225,255,285])
p('Protocolo propuesto: cada perfil estima primero de forma independiente, identifica causa y exclusiones, y explica O/M/P o P/I. El PM compara discrepancias; el equipo acuerda y registra rango, fecha, autor, fuente, desacuerdos y responsable de aprobación. Separar estimador proveedor de aceptante VCA reduce sesgo comercial y anclaje al presupuesto N1. Repetir ante nuevo contrato/API, evidencia de piloto, disparador o cambio relevante. Pendientes antes de uso operativo: cotizaciones, firma de contratos, disponibilidad de UAT/referentes, controles ASVS aplicables y calendario corporativo.')
p('Cambio de prioridad frente a N3: RI-9 y RI-17 pasan de media a alta al puntuar I=5 por bloqueo de seguridad y afectación del go-live; RI-15 pasa de baja a media porque la regresión próxima al pase tiene I=4 aunque conserve probabilidad baja. La escala formal explica estos cambios; no son incidentes observados. Los riesgos ligados al software son RI-1/2/6/9/10/11/12/14/15/17/18/19; los restantes amplían el contexto operativo y de negocio.','SmallN4')
sub('Fuentes y alcance de la verificación')
p('Consigna N4, 27/10/2026, puntos 1-3. Devoluciones docentes N1 y N2 completas. N2 corregida PDF pp.7-9 y Excel original; N3 revisión 2 PDF pp.2-4 y 12-13. DPI5 pp.10-11 (estimación), 16-18 (reservas), 20-22 (curva); DPI6 pp.10-17 y 20-23 (EVM); DPI11 pp.4-5 y 14 (juicio experto). Colección GDP complementaria, numeración independiente: Incertidumbre pp.10-18 (escalas y matriz) y 19-21 (respuestas), Entrega/Calidad pp.3-6. Se inspeccionaron originales para fórmulas y formatos; no se atribuyen umbrales propios a las clases.','SmallN4')
p('ISO/IEC 25010:2023, edición 2, ficha pública oficial: <link href="https://www.iso.org/standard/78176.html">iso.org/standard/78176.html</link> (consulta 27/10/2026). Se usa el alcance público del modelo de producto, sin citar cláusulas no consultadas. OWASP ASVS 5.0.0, publicación 30/05/2025: <link href="https://asvs.owasp.org/">asvs.owasp.org</link>. Controles de autorización verificados en <link href="https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x17-V8-Authorization.md">fuente oficial etiquetada v5.0.0, V8</link> (consulta 27/10/2026). No se afirma verificación completa. ISO 9000:2000 figura como ejemplo en consigna; se elige un marco específico de calidad de producto software.','SmallN4')

def footer(canvas,doc):
    canvas.setStrokeColor(colors.HexColor('#D6DFE6'));canvas.line(35,29,807,29)
    canvas.setFont('Helvetica',8);canvas.setFillColor(colors.HexColor('#526577'));canvas.drawString(35,18,'Grupo 1 · WorkHub VCA Catalinas · Entrega N4 · 31/10/2026');canvas.drawRightString(807,18,f'Página {doc.page}')
doc=SimpleDocTemplate(str(ROOT/'Grupo 1_Entrega N4.pdf'),pagesize=landscape(A4),leftMargin=35,rightMargin=35,topMargin=30,bottomMargin=40,title='Grupo 1 - Entrega N4 - WorkHub',author='Grupo 1')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
mdtext='# Grupo 1 · Entrega N4\n\n'+'\n\n'.join(md)+'\n'
mdtext=re.sub(r'<link href="([^"]+)">([^<]+)</link>',r'[\2](\1)',mdtext)
(ROOT/'submission.md').write_text(mdtext)
print(json.dumps(dict(tasks=len(tasks),labor=sum(t['labor'] for t in tasks),nonlabor=sum(t['nonlabor'] for t in tasks),M=sum(t['M'] for t in tasks),PERT=pert,reserve=sum(r[12] for r in risks),baseline=cum),indent=2))
