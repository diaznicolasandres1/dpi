# DPI Knowledge Hub

Repositorio central de materiales, entregas y devoluciones de la materia DPI. Su propósito es conservar las fuentes originales y ofrecer versiones Markdown que agentes como Codex y Claude puedan buscar, relacionar y reutilizar al preparar nuevas entregas.

## Start here

1. Consultar [INDEX.md](INDEX.md) para navegar todo el contenido.
2. Leer [SUBMISSION_CRITERIA.md](SUBMISSION_CRITERIA.md) antes de preparar una entrega.
3. Revisar [DECISIONS.md](DECISIONS.md) y las devoluciones de entregas anteriores.
4. Usar [GLOSSARY.md](GLOSSARY.md) para fórmulas y conceptos recurrentes.

## Repository structure

- [`theory/`](theory/README.md): clases, material teórico y anexos de costos.
- [`submissions/`](submissions/README.md): entregas, archivos originales, versiones Markdown y correcciones.
- [`AI_GUIDE.md`](AI_GUIDE.md): instrucciones compartidas por todos los agentes.
- [`AGENTS.md`](AGENTS.md): punto de entrada para Codex.
- [`CLAUDE.md`](CLAUDE.md): punto de entrada para Claude.
- [`INDEX.md`](INDEX.md): índice navegable del hub.
- [`SUBMISSION_CRITERIA.md`](SUBMISSION_CRITERIA.md): checklist y requisitos consolidados.
- [`DECISIONS.md`](DECISIONS.md): decisiones, observaciones pendientes y aprendizajes acumulados.
- [`scripts/`](scripts/README.md): actualización y validación automatizada del hub.

## Source policy

- Los PDF, DOCX, XLSX, Draw.io e imágenes son las fuentes originales.
- Los archivos Markdown son una capa de consulta y búsqueda.
- Cuando una tabla, fórmula o diagrama sea decisivo, se debe verificar contra el archivo original.
- Antes de aplicar un término, método o formato de la materia, localizar la clase y página o diapositiva que lo define. Para diagramas y otros elementos visuales, comparar la clase original con el archivo final renderizado; el texto extraído en Markdown no alcanza para validar el diseño.
- Si falta la fuente o hay una contradicción, registrar la incertidumbre en vez de asumir una convención general o afirmar que fue validada.
- Las devoluciones docentes tienen prioridad para corregir las siguientes entregas.

## Working with AI agents

Las tareas nuevas deben iniciarse con este repositorio como proyecto o directorio de trabajo. Cada agente tiene un archivo de entrada que lo dirige a la guía compartida:

| Agent | Entry file | Shared rules |
|---|---|---|
| Codex | `AGENTS.md` | `AI_GUIDE.md` |
| Claude | `CLAUDE.md` | `AI_GUIDE.md` |

Si se utiliza otro agente, se le debe indicar explícitamente que lea `AI_GUIDE.md`. Un pedido recomendado es:

> Prepará la próxima entrega usando este repositorio como hub. Revisá primero la consigna, el material teórico relacionado, `SUBMISSION_CRITERIA.md`, `DECISIONS.md` y todas las devoluciones anteriores.

## Maintenance

Después de agregar o reemplazar material original:

```bash
make hub-update
make hub-check
```

Consultar [scripts/README.md](scripts/README.md) para agregar nuevas fuentes al manifiesto.

## Add a new class

1. Guardar el archivo original en `theory/course_material/`.
2. Mantener el nombre original del PDF, PowerPoint, Word o planilla.
3. Elegir para la versión Markdown un nombre descriptivo en inglés y `snake_case`, por ejemplo `09_risk_management.md`.
4. Agregar la relación entre fuente y salida en `hub_manifest.json`.
5. Ejecutar:

```bash
make hub-update
make hub-check
```

6. Agregar el nuevo Markdown a `INDEX.md` y a `theory/course_material/README.md`.
7. Si la clase modifica criterios utilizados en entregas anteriores, actualizar `GLOSSARY.md`, `SUBMISSION_CRITERIA.md` o `DECISIONS.md` según corresponda.

Si el material es una imagen o un escaneo sin texto extraíble, debe registrarse como conversión manual en `hub_manifest.json` y transcribirse con revisión visual.

## Create a new submission

Para crear la estructura de la próxima entrega:

```bash
make new-submission N=4
```

El comando crea:

```text
submissions/submission_4/
├── README.md
├── source/
└── revisions/
```

Después:

1. Guardar la consigna y los archivos de trabajo originales en `source/`.
2. Agregar al manifiesto los archivos que necesiten una versión Markdown reutilizable.
3. Ejecutar `make hub-update`.
4. Actualizar `INDEX.md` y `submissions/README.md`.
5. Preparar la entrega revisando obligatoriamente `AI_GUIDE.md`, el archivo de entrada del agente, `SUBMISSION_CRITERIA.md`, `DECISIONS.md` y todas las devoluciones anteriores.
6. Conservar una copia exacta de lo entregado. No sobrescribirla durante revisiones posteriores.

## Add instructor feedback

Cuando llegue una corrección docente:

1. Guardarla como `submissions/submission_N/feedback.md`.
2. Si existen varias rondas, usar `feedback_round_1.md`, `feedback_round_2.md`, etc.
3. Copiar a `DECISIONS.md` únicamente los aprendizajes y reglas que afecten entregas futuras.
4. Actualizar el README de la entrega y `INDEX.md`.
5. Ejecutar `make hub-check`.

La devolución debe conservarse textual. Las interpretaciones o decisiones derivadas deben registrarse por separado en `DECISIONS.md`.

## Generate a corrected version with an agent

La tarea debe abrirse usando este repositorio como proyecto o directorio de trabajo. Codex debe partir de `AGENTS.md`, Claude de `CLAUDE.md` y cualquier otro agente de `AI_GUIDE.md`. Usar un pedido como el siguiente:

```text
Trabajá sobre submissions/submission_N usando este repositorio como hub.

Antes de editar:
1. Leé AI_GUIDE.md, el archivo de entrada correspondiente a tu agente, INDEX.md, SUBMISSION_CRITERIA.md y DECISIONS.md.
2. Leé la consigna de la entrega, todos los archivos de source/ y feedback.md.
3. Leé las devoluciones de todas las entregas anteriores.
4. Identificá la clase y página o diapositiva original para cada método, término, fórmula y formato relevante. Usá el Markdown para buscar, pero verificá los detalles y los ejemplos visuales en el PDF o PowerPoint original.
5. Compará cada observación docente con el documento, la planilla y los diagramas originales.

Creá una versión corregida en revisions/revision_1/ sin sobrescribir los archivos entregados.
Incluí revision_notes.md con una tabla que relacione cada observación, el cambio realizado, el archivo afectado y la verificación aplicada.
Anotá en revision_notes.md qué clases y páginas o diapositivas originales usaste para validar los cambios; si algo no pudo validarse, indicá la limitación.
Reconciliá alcance, EDT, tareas, red, Gantt, recursos y costos.
Señalá cualquier contradicción que no pueda resolverse con las fuentes disponibles.
Actualizá el README de la entrega, DECISIONS.md e INDEX.md cuando corresponda.
Al finalizar, ejecutá make hub-check.
Antes de dar por terminada la versión, abrí y compará los archivos finales renderizados con las clases originales a tamaño de lectura normal. No des por cumplido un molde solo porque los datos coinciden.
```

Para una segunda corrección, cambiar la salida a `revisions/revision_2/` y usar como base la revisión anterior sin modificarla.

## Definition of done for the hub

Antes de considerar actualizado el hub:

- todos los originales están preservados;
- los archivos reutilizables tienen una versión Markdown;
- las carpetas y Markdown tienen nombres en inglés;
- `INDEX.md` enlaza el contenido nuevo;
- la devolución docente está preservada;
- `DECISIONS.md` contiene los aprendizajes aplicables al futuro;
- las revisiones no sobrescriben versiones anteriores;
- Codex y Claude utilizan las mismas reglas compartidas de `AI_GUIDE.md`;
- `make hub-check` finaliza sin errores ni advertencias relevantes.
