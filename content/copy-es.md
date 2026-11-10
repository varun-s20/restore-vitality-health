# Copy: Restore Vitality Health (Español)
Copywriter, 2026-11-10. Mirror of content/copy.md: same pages, same section names (kept in English so the build maps them one to one), same order. Written for Spanish speakers in the US, not translated word for word.

## How to read this file
- Same conventions as copy.md: headlines in sentence case (CSS sets capitals), `**bold**` for the 600 weight, no full stops in headlines, buttons in sentence case with the arrow.
- Register: "usted", the usual choice in US healthcare for a 45+ audience. Buttons use the infinitive (Comenzar, Ver más), which is shorter and avoids the choice entirely.
- "Shared" becomes "Para todos" (for men and women alike). "Compartidos" reads as "shared out" in Spanish.
- Product names stay exactly as in OpenLoop intake (English), because the intake screens and pharmacy labels use them. The description under each name is in Spanish.
- Placeholders are the same as in English, written in English so the client and the build see one list.
- Length: every button and headline is within about 20% of the English. Headlines that ran longer were rewritten, not shrunk.
- Font note: every accent (á é í ó ú ñ ¿ ¡) falls back to Albert Sans in the trial Carbona. The build checks headlines at 1440 and 390 (choices.md).

---

## Sitewide

### Header
- Menu pill: Menú
- Inline links (from 1280): Salud masculina / Salud femenina / Para todos
- Logo alt: Restore Vitality Health, inicio
- Language switch: EN / ES. Screen reader text on EN: (English). Group label: Idioma
- Portal link: Mi portal. Screen reader text: (se abre en una pestaña nueva)
- Header pill: Comenzar (goes to the quiz)

### Menu drawer
- Close pill: Cerrar
- Links: Salud masculina / Salud femenina / Tratamientos para todos / Cómo funciona / Precios / Nosotros / Preguntas / Recursos / Contacto
- Language and portal row: EN / ES, Mi portal
- Quiz block title: ¿No sabe por dónde empezar?
- Quiz block text: Responda dos preguntas breves y le indicamos el programa adecuado. No guardamos nada de lo que elija.
- Button: Hacer el cuestionario

### Safety line (under every treatment rail and on every treatment page)
Los medicamentos compuestos no están aprobados por la FDA. Se requiere receta, y un profesional de la salud con licencia decide si un tratamiento es adecuado para usted. Leer la información de seguridad
- Link text: Leer la información de seguridad (to /medications-safety-information)

### Credibility row (sitewide)
1. **Revisado por profesionales con licencia**
   Cada solicitud la revisa un profesional con licencia en el estado donde usted vive.
2. **Los 50 estados y DC**
   La disponibilidad de cada medicamento varía según el estado.
3. **Precios claros desde el inicio**
   Usted ve el precio y el periodo de cobro antes de empezar.
4. **[HIPAA wording: pending client]**
   [HIPAA supporting line: pending client]

Marquee at 390 reads the four headings in order, separated by spaces only.

### Closing CTA band (default)
- Headline: Vitalidad para **lo que viene**
- Line: Dos preguntas breves le indican el programa adecuado. Un profesional con licencia se encarga del resto.
- Button: Encontrar su programa
- Glyph alt: none (decorative, `aria-hidden`)

The English closes on the tagline, "Restored for what's next". A literal Spanish version needs a gendered adjective (restaurados, restauradas), so this line keeps the meaning and the brand's own word, vitality.

### Footer
- Email (first, 26px): support@rx.restorevitality.health
- Line under it: Atención al cliente en vivo de lunes a sábado, de 9 a. m. a 6 p. m., hora del Centro.
- Phone: [Phone number]
- Column heads and links:
  - **Tratamientos**: Salud masculina / Salud femenina / Tratamientos para todos / Precios / Hacer el cuestionario
  - **Empresa**: Nosotros / Cómo funciona / Preguntas / Recursos / Contacto / Mi portal
  - **Legal**: Política de privacidad / Términos del servicio / Información de seguridad de los medicamentos / Consentimiento de telesalud / Configuración de cookies / No vender ni compartir mi información personal
- Disclaimer paragraph (our Spanish version of the client's text; the client must approve it, Questions 19):
  Los medicamentos compuestos no están aprobados por la FDA. La FDA no evalúa la seguridad, eficacia ni calidad de los productos compuestos. Los productos con receta requieren una consulta en línea con un profesional de la salud, quien determinará si una receta es apropiada. Visite nuestro sitio web para ver todos los detalles, las restricciones aplicables y la información importante sobre la seguridad de los medicamentos.
  Restore Vitality Health no fabrica medicamentos compuestos. La apariencia y el etiquetado reales del medicamento que reciba serán distintos de las imágenes del sitio web.
  Los resultados no están garantizados y pueden variar según la persona, como parte de un programa personalizado de pérdida de peso y salud.
- Copyright: Copyright 2026 Restore Vitality Health. Todos los derechos reservados.
- Bottom row: EN / ES, Volver arriba, Creado con cariño por Digital Heroes
- Closing lockup alt: Restore Vitality Health. Lived well. Restored for what's next.

The lockup alt stays in English because the tagline in the logo image is in English.

### Sticky mobile CTA
- Pill: Encontrar su programa

### Cookie notice
- Text: Usamos cookies esenciales para que este sitio funcione. Con su permiso, también usamos cookies de análisis y de marketing para entender cómo se usa el sitio. Puede cambiar su elección en cualquier momento en Configuración de cookies.
- Buttons: Aceptar / Configurar

### Form messages (shared by every form)
- Required field: Complete este campo.
- Email format: Escriba un correo electrónico, por ejemplo nombre@ejemplo.com.
- Phone format: Escriba un número de teléfono de EE. UU., con el código de área.
- Sending: Enviando
- Network error: No se pudo enviar. Inténtelo de nuevo o escríbanos a support@rx.restorevitality.health.

---

## Home

### Meta
- Title: Restore Vitality Health | Atención con receta en la mediana edad
- Description: Programas con receta para hombres y mujeres en la mediana edad: salud sexual, menopausia, pérdida de peso y longevidad. Revisados en línea por un profesional con licencia.

### Hero
- Headline (3 rows at 390): Rumbo a / **su próxima / aventura**
- Lead: Atención con receta para hombres y mujeres en la mediana edad: salud sexual, menopausia, pérdida de peso y longevidad, revisada en línea por un profesional con licencia en su estado.
- Button: Encontrar su programa (to the quiz)
- Fact chip: Planes desde $96 cada 4 semanas
- Scroll cue: Desplácese para descubrir
- Media alt: none (decorative, `aria-hidden`)

"Listos para la próxima aventura" would be the literal line, but "listos" is gendered. "Rumbo a su próxima aventura" (heading for your next adventure) keeps the client's idea for everyone.

### Treatments
- Screen reader h2: Tratamientos
- Tabs: Salud masculina / Salud femenina / Para todos
- Cards: see Treatment data below.
- Card pill: Comenzar (to that product's OpenLoop intake link)
- Card link: Ver más (to the treatment page)
- Card media alt: none (decorative)
- Under the rail: Safety line (sitewide)

### Credibility row
Sitewide block, as above.

### How it works
- Heading: Cómo **funciona**
- Intro: Desde sus primeras respuestas hasta su próximo resurtido, todo sucede en línea. Un profesional con licencia en su estado revisa su historial y decide qué recetar, si corresponde. Siempre sabe cuánto paga y cuándo.
- Five step cards. Step name, title, body:
  1. **Consulta**
     Title: Cuéntenos **sobre usted**
     Body: Elija un programa y complete un breve formulario en línea sobre su salud y sus metas. Un profesional con licencia lo revisa por video, por teléfono o por mensaje.
  2. **Análisis**
     Title: Análisis, **si hacen falta**
     Body: Algunos tratamientos requieren resultados de laboratorio. Si es su caso, su profesional le dirá qué necesita y, con su consentimiento, se pueden añadir resultados que ya tenga.
  3. **Plan**
     Title: Su **plan**
     Body: Su profesional decide si una receta es adecuada para usted y en qué dosis. Si no lo es, puede sugerirle otra opción, y se le reembolsa el total.
  4. **Envío**
     Title: Hasta **su puerta**
     Body: Una farmacia asociada con licencia prepara su receta y se la envía. Recibe avisos por mensaje de texto o correo electrónico durante el envío.
  5. **Seguimiento**
     Title: Atención **continua**
     Body: Su plan se renueva cada periodo, con recordatorios de resurtido por mensaje o correo. Administre su cuenta en Mi portal y cancele cuando quiera.
- Step illustration alt: none (decorative)

### Quiz entry band
- Heading: ¿Por dónde **quiere empezar?**
- Routing rows:
  - Salud **masculina**, chip: Desde $96 cada 4 semanas (to Men's health)
  - Salud **femenina**, chip: Desde $237 cada 12 semanas (to Women's health)
  - **Para todos**, chip: Desde $145 cada 4 semanas (to Shared treatments)
- Quiz row: **¿No está seguro? Responda dos preguntas** (to the quiz)
- Media alt: none (decorative)

### Real results
Built only when the client sends real reviews. Copy for when they arrive:
- Heading: En sus **propias palabras**
- Ring arrows: Anterior / Siguiente (screen reader labels)
- Cards (three to start):
  - Initials: [Reviewer initials: pending client]. Date: [Review date: pending client]
  - Quote: [Review: pending client]
  - Product row: [Product reviewed: pending client]
- Note under the rail: Opiniones de pacientes reales. Los resultados varían según la persona.

Reviews arrive in English; whether to translate them, or show them as written with a note, is in Questions 19.

### Pricing tease
- Heading: Precios claros, **sin sorpresas**
- Intro: Cada programa tiene un precio por periodo de cobro, visible antes de empezar. Incluye la revisión de su profesional, su medicamento si se lo recetan y apoyo en línea.
- Cards:
  1. Pill: Salud masculina. Group name: Salud **masculina**. Blurb: Siete tratamientos para la disfunción eréctil, en tabletas o viales liposomales. From: $96 cada 4 semanas. Button: Ver tratamientos
  2. Pill: Salud femenina. Group name: Salud **femenina**. Blurb: Atención para la menopausia, con opciones hormonales y no hormonales. From: $237 cada 12 semanas. Button: Ver tratamientos
  3. Pill: Para todos. Group name: **Para todos**. Blurb: Pérdida de peso, microdosis de GLP-1 y longevidad, para hombres y mujeres. From: $145 cada 4 semanas. Button: Ver tratamientos
- "Every plan includes" list (heading: Todos los planes incluyen):
  - Revisión de un profesional con licencia en su estado
  - Su medicamento, si su profesional se lo receta
  - Apoyo en línea a través de Mi portal
- Under the cards: Ver todos los precios (to Pricing)

The three English buttons name their group ("See men's treatments"); in Spanish the group is already the card's title, so one short label fits the pill.

### FAQ
- Heading: Preguntas **frecuentes**
- Tabs and questions: the first two questions of each theme from the FAQ page.
- Link under the answers: Ver todas las preguntas (to FAQ)

### Resources rail
Until articles exist the band shows the newsletter capture only.
- Heading: Sepa de **nosotros** (pass 8b; was: Notas para **lo que viene**)
- Line: Notas en lenguaje sencillo sobre nuestros programas y los nuevos tratamientos a medida que lleguen. Sin spam, y puede darse de baja cuando quiera.
- Field label: Correo electrónico
- Button: Suscribirse
- Success: Gracias. Ya está en la lista.

When articles exist:
- Heading: **Recursos**
- Card link: Leer el artículo
- Link at the end: Todos los recursos

### Closing CTA band
Default, as in Sitewide.

---

## Treatment data (cards and treatment pages)
Same products, prices and intake links as copy.md. Benefits are our Spanish versions of the client's own lines.
Chips: Oral / Crema / Parche / Inyección / Nasal. Frequencies: Según necesidad / Diario / Semanal / Dos veces por semana.

### Men's health: Erectile dysfunction (billed every 4 weeks)

**Daily Boost Pill**
- Chips: Oral / Según necesidad
- Card: Tadalafil en una tableta sencilla, cuando la necesite.
- Price: $112 cada 4 semanas
- Page: Una tableta sencilla con un solo activo, tadalafil, que se toma cuando la necesite. Es un medicamento compuesto con receta, así que un profesional con licencia revisa primero su historial de salud y decide si le conviene y en qué dosis. Si se lo recetan, una farmacia asociada lo prepara y se lo envía.
- Benefits: Mejora el flujo sanguíneo del pene / Favorece la relajación del músculo liso / Aumenta la respuesta a la estimulación
- Ingredients: Tadalafil
- Intake: productId UHJvZHVjdDoxNjg=

**Double Powered Liposomal**
- Chips: Oral / Según necesidad
- Card: Sildenafil y tadalafil juntos, en un vial sencillo.
- Price: $99 cada 4 semanas
- Page: Dos activos, sildenafil y tadalafil, combinados en un vial liposomal que se toma por vía oral cuando lo necesite. Liposomal significa que los activos van dentro de una fina capa de lípidos. Su profesional revisa su historial y sus medicamentos actuales y decide si es adecuado para usted.
- Benefits: Favorece la disposición espontánea / Mejora la respuesta sexual / Apoya una actividad más firme
- Ingredients: Sildenafil, Tadalafil
- Intake: productId UHJvZHVjdDoxNjM=

**Double Powered Pill**
- Chips: Oral / Según necesidad
- Card: Sildenafil y tadalafil juntos, en una tableta sencilla.
- Price: $96 cada 4 semanas
- Page: Los mismos dos activos que el liposomal, sildenafil y tadalafil, en una tableta que se toma cuando la necesite. Es nuestro tratamiento de menor precio para la disfunción eréctil. Un profesional con licencia revisa su historial de salud y decide si es adecuado para usted y en qué dosis.
- Benefits: Aumenta la disposición para la actividad / Intensifica la respuesta / Mejora la actividad sexual
- Ingredients: Sildenafil, Tadalafil
- Intake: productId UHJvZHVjdDoxNjU=

**Quadruple Powered Liposomal**
- Chips: Oral / Según necesidad
- Card: Nuestra fórmula más completa, con cuatro activos en un vial.
- Price: $119 cada 4 semanas
- Page: Cuatro activos en un vial liposomal: sildenafil, tadalafil, apomorfina y L-citrulina. Es la fórmula más completa de la línea y se toma por vía oral cuando la necesite. Como combina varios medicamentos, su profesional revisa con atención su historial y sus otras recetas antes de decidir si le conviene.
- Benefits: Apoyo integral para la disfunción eréctil / Absorción más rápida / Excitación física y mental
- Ingredients: Sildenafil, L-Citrulina, Tadalafil, Apomorfina
- Intake: productId UHJvZHVjdDoxOTY=

**Triple Powered Liposomal**
- Chips: Oral / Según necesidad
- Card: Sildenafil, tadalafil y vardenafil, en un vial sencillo.
- Price: $109 cada 4 semanas
- Page: Tres activos, sildenafil, tadalafil y vardenafil, en un vial liposomal que se toma por vía oral cuando lo necesite. Un profesional con licencia revisa su historial de salud y sus medicamentos actuales y decide si es adecuado para usted. Si se lo recetan, una farmacia asociada lo prepara y se lo envía.
- Benefits: Acción rápida / Efecto más duradero / Fórmula confiable de varios ingredientes
- Ingredients: Sildenafil, Tadalafil, Vardenafil
- Intake: productId UHJvZHVjdDoxNjE=

**Triple Powered Pill**
- Chips: Oral / Según necesidad
- Card: Sildenafil, tadalafil y apomorfina, en una tableta sencilla.
- Price: $102 cada 4 semanas
- Page: Tres activos, sildenafil, tadalafil y apomorfina, en una tableta que se toma cuando la necesite. Un profesional con licencia revisa primero su historial y sus medicamentos actuales y decide si le conviene y en qué dosis. Si se lo recetan, una farmacia asociada lo prepara y se lo envía.
- Benefits: Respuesta de excitación rápida / Efecto prolongado / Mayor excitación central
- Ingredients: Sildenafil, Tadalafil, Apomorfina
- Intake: productId UHJvZHVjdDoxNjQ=

**Triple Powered Up Liposomal**
- Chips: Oral / Según necesidad
- Card: Sildenafil, tadalafil y apomorfina, en un vial sencillo.
- Price: $109 cada 4 semanas
- Page: Los mismos tres activos que la Triple Powered Pill, sildenafil, tadalafil y apomorfina, en un vial liposomal que se toma por vía oral cuando lo necesite. Su profesional revisa su historial de salud y decide si le conviene más esta forma o la tableta.
- Benefits: Fórmula liposomal de acción rápida / Efectos de apoyo prolongados / Mejora la excitación central
- Ingredients: Sildenafil, Tadalafil, Apomorfina
- Intake: productId UHJvZHVjdDoxNjI=

### Women's health: Menopause hormone therapy (billed every 12 weeks)

**Estradiol cream + Progesterone**
- Chips: Crema / Diario
- Card: Estradiol y progesterona, una aplicación sencilla al día.
- Price: $237 cada 12 semanas
- Page: Estradiol en crema, que se aplica una vez al día, recetado junto con progesterona. Es una de las tres opciones hormonales del programa, y la elección entre crema, parche y tableta la toma usted con su profesional. Se cobra cada 12 semanas, así que no tiene que volver a pedir cada mes.
- Benefits: Alivia los síntomas de la menopausia / Apoya la salud de los huesos / Mejora el bienestar general
- Ingredients: Estradiol, Progesterona
- Intake: productId UHJvZHVjdDoxOTI=

**Estradiol patch + Progesterone**
- Chips: Parche / Dos veces por semana
- Card: Estradiol y progesterona, un parche sencillo dos veces por semana.
- Price: $237 cada 12 semanas
- Page: Estradiol en un parche que se cambia dos veces por semana, recetado junto con progesterona. Contiene las mismas hormonas que la crema y la tableta, en una forma en la que solo piensa dos veces por semana. Su profesional revisa su historial y sus síntomas y decide qué forma y qué dosis le convienen.
- Benefits: Alivia las molestias de la menopausia / Mejora el ánimo y el sueño / Mantiene la densidad ósea
- Ingredients: Estradiol, Progesterona
- Intake: productId UHJvZHVjdDoxOTE=

**Estradiol Tablet**
- Chips: Oral / Diario
- Card: Estradiol con progesterona, una tableta sencilla al día.
- Price: $237 cada 12 semanas
- Page: Estradiol en tableta, una vez al día, con progesterona. Como la crema y el parche, se cobra cada 12 semanas. Un profesional con licencia revisa su historial de salud y decide si la terapia hormonal es adecuada para usted y en qué forma.
- Benefits: Reduce los bochornos / Protege la fuerza de los huesos / Apoya la terapia hormonal
- Ingredients: Estradiol, Progesterona
- Intake: productId UHJvZHVjdDoxOTA=

**Oral Paroxetine**
- Chips: Oral / Diario
- Card: Una opción no hormonal, una tableta sencilla al día.
- Price: $237 cada 12 semanas
- Page: Para mujeres que no pueden tomar hormonas o prefieren no hacerlo. Una tableta al día de paroxetina o desvenlafaxina, ambas no hormonales. Su profesional revisa su historial y decide cuál es adecuada para usted, si alguna lo es.
- Benefits: No hormonal, para los bochornos / Alivia los cambios de humor / Mejora la calidad del sueño
- Ingredients: Paroxetina o Desvenlafaxina
- Intake: productId UHJvZHVjdDoxOTM=

### Shared: Medical weight loss (billed every 4 weeks)

**Oral Semaglutide**
- Chips: Oral / Diario
- Card: Semaglutida en una tableta soluble al día.
- Price: $279 cada 4 semanas
- Page: Semaglutida, un medicamento GLP-1, en una tableta soluble al día, para quienes prefieren no inyectarse. Su profesional revisa su historial de salud y decide si es adecuada para usted y cómo ajustar la dosis con el tiempo.
- Benefits: Estimula la liberación de insulina / Controla los picos de azúcar en la sangre / Reduce el apetito de forma eficaz
- Ingredients: Semaglutida
- Intake: productId UHJvZHVjdDoxNDQ=

**Semaglutide Injections**
- Chips: Inyección / Semanal
- Card: Semaglutida en una inyección sencilla a la semana.
- Price: $249 cada 4 semanas
- Page: Semaglutida en una inyección a la semana, con instrucciones escritas y en video para aplicarla usted en casa. Su profesional fija la dosis inicial después de revisar su historial de salud y la ajusta con usted con el tiempo.
- Benefits: Mejora la respuesta a la insulina / Prolonga la sensación de saciedad / Reduce el consumo de calorías
- Ingredients: Semaglutida
- Intake: productId UHJvZHVjdDoxNDI=

**Tirzepatide Injections**
- Chips: Inyección / Semanal
- Card: Tirzepatida en una inyección sencilla a la semana.
- Price: $339 cada 4 semanas
- Page: Tirzepatida, que actúa sobre dos vías del apetito, en una inyección a la semana. Incluye instrucciones escritas y en video para aplicarla en casa. Su profesional revisa su historial y decide si es adecuada para usted y en qué dosis.
- Benefits: Aumenta la eficacia de la insulina / Prolonga la saciedad / Ayuda a reducir el apetito
- Ingredients: Tirzepatida
- Intake: productId UHJvZHVjdDoxNDM=

### Shared: GLP-1 microdosing (billed every 4 weeks)

**Semaglutide Microdose Injection**
- Chips: Inyección / Semanal
- Card: Semaglutida en dosis baja, para un progreso constante y suave.
- Price: $179 cada 4 semanas
- Page: Una dosis más baja de semaglutida, una vez por semana, para un progreso constante y suave en lugar de un cambio rápido. Su profesional fija la dosis después de revisar su historial de salud y puede ajustarla a sus metas.
- Benefits: Apoya un metabolismo estable / Reduce el apetito con suavidad / Se adapta a sus metas personales
- Ingredients: Semaglutida
- Intake: productId UHJvZHVjdDoxOTQ=

**Tirzepatide Microdose Injection**
- Chips: Inyección / Semanal
- Card: Nuestra opción de dosis baja más potente, para resultados constantes.
- Price: $179 cada 4 semanas
- Page: Una dosis más baja de tirzepatida, que actúa sobre dos vías del apetito, una vez por semana. Es la más potente de las dos opciones de microdosis, al mismo precio. Su profesional revisa su historial de salud y decide si le conviene y en qué dosis.
- Benefits: Control del hambre por dos vías / Resultados suaves y sostenibles / Formulación personalizada
- Ingredients: Tirzepatida
- Intake: productId UHJvZHVjdDoxOTU=

### Shared: Longevity (billed every 4 weeks)

**Metabolism Boost Injection (B12 + MIC)**
- Chips: Inyección / Semanal
- Card: B12 con metionina, inositol y colina, una vez por semana.
- Price: $145 cada 4 semanas
- Page: Una inyección de B12 y MIC (metionina, inositol, colina) que combina el apoyo energético de la B12 con compuestos lipotrópicos que ayudan al cuerpo a procesar y metabolizar la grasa. Un complemento popular para apoyar la energía, el metabolismo y el control del peso.
- Benefits: B12 para apoyar la energía / Compuestos lipotrópicos que ayudan a procesar la grasa / Un complemento popular para un plan de control de peso
- Ingredients: B12, Metionina, Inositol, Colina
- Intake: productId UHJvZHVjdDoxNzg=

**Cellular Recharge Injection (NAD+)**
- Chips: Inyección / Dos veces por semana
- Card: NAD+ de forma directa, en una inyección dos veces por semana.
- Price: $199 cada 4 semanas
- Page: Una inyección de NAD+ que lleva esta coenzima esencial directamente a su organismo y apoya la producción de energía celular, la reparación del ADN y el metabolismo, que disminuyen de forma natural con la edad. La inyección ofrece una absorción alta y directa, una opción básica para la energía, la concentración y la recuperación.
- Benefits: Apoya la producción de energía celular / Apoya la reparación del ADN y el metabolismo / Absorción alta y directa
- Ingredients: NAD+
- Intake: productId UHJvZHVjdDoxNzQ=

**Peak Recovery Injection (Sermorelin)**
- Chips: Inyección
- Card: Sermorelina, que apoya la producción natural de la hormona del crecimiento.
- Price: $229 cada 4 semanas
- Page: Una inyección de sermorelina que puede apoyar el mantenimiento de la masa muscular magra, un envejecimiento saludable, un sueño más profundo y una energía estable. Suele aplicarse antes de dormir, en sintonía con su ciclo natural nocturno.
- Benefits: Apoya la producción natural de la hormona del crecimiento / Puede apoyar la masa muscular magra y un sueño más profundo / Se aplica antes de dormir, con su ciclo nocturno
- Ingredients: Sermorelina
- Intake: productId UHJvZHVjdDoxNzc=

**Cellular Recharge Nasal Spray (NAD+)**
- Chips: Nasal / Diario
- Card: NAD+ sin agujas, en un aerosol sencillo al día.
- Price: $229 cada 4 semanas
- Page: Un aerosol nasal de NAD+ que se absorbe a través de la mucosa nasal, una forma cómoda y sin agujas de apoyar la energía celular, la concentración y la recuperación. Una opción diaria fácil para mantener sus niveles de NAD+ entre inyecciones o en lugar de ellas.
- Benefits: Sin agujas / Apoya la energía celular, la concentración y la recuperación / Entre inyecciones o en lugar de ellas
- Ingredients: NAD+
- Intake: productId UHJvZHVjdDoxNzU=

**Cellular Recharge Liposomal (NAD+, Next-Gen)**
- Chips: Oral / Diario
- Card: NAD+ liposomal, por vía oral una vez al día.
- Price: $229 cada 4 semanas
- Page: Un NAD+ liposomal de nueva generación que envuelve la molécula en una capa protectora de lípidos, para que más cantidad resista la digestión y llegue a sus células que con un oral común. Apoya la energía celular, el metabolismo y la reparación en una forma diaria sencilla y sin agujas.
- Benefits: Capa protectora de lípidos / Apoya la energía celular, el metabolismo y la reparación / Sin agujas, una vez al día
- Ingredients: NAD+
- Intake: productId UHJvZHVjdDoxNzY=

### Shared: Peptides (only when the client confirms them)
- Card titles: [Peptide name: pending client], six cards
- Prices: [Peptide price: pending client]
- No chips, descriptions or benefits until the client supplies them with intake links.

---

## Men's health (category page)

### Meta
- Title: Salud masculina | Restore Vitality Health
- Description: Siete tratamientos con receta para la disfunción eréctil, en tabletas o viales liposomales, desde $96 cada 4 semanas. Revisados en línea por un profesional con licencia.

### Compact banner
- Title: Salud **masculina**
- Line: Siete tratamientos para la disfunción eréctil, recetados en línea por un profesional con licencia, desde $96 cada 4 semanas.
- Media alt: none (decorative)

### Treatment rail
Seven Men's health cards. Safety line under the grid.

### Who it is for
- Heading: Disfunción **eréctil**
- Body: Para hombres que buscan una ayuda confiable con la erección, sin sala de espera. Elija entre tabletas y viales liposomales, con uno a cuatro activos. Cuéntenos sobre su salud y los medicamentos que toma, y un profesional con licencia decide qué opción le conviene y en qué dosis. Todas se cobran cada 4 semanas y puede cancelar cuando quiera.

### Quiz entry row
- **¿No sabe cuál elegir? Responda dos preguntas**

### FAQ
- Heading: Preguntas sobre **salud masculina**
- Questions:
  - **¿Qué diferencia hay entre una tableta y un vial liposomal?** Ambos se toman por vía oral cuando los necesita. La tableta es una pastilla. El vial liposomal es un líquido en el que los activos van dentro de una fina capa de lípidos. Su profesional puede ayudarle a elegir.
  - **¿Por qué algunos tratamientos tienen más de un activo?** Cada activo actúa a su manera, y algunas fórmulas combinan dos, tres o cuatro. Su profesional revisa su historial de salud y sus otros medicamentos antes de recomendar uno.
  - **¿Necesito receta?** Sí. Todos estos tratamientos son medicamentos compuestos con receta. Un profesional con licencia revisa su formulario y decide si son adecuados para usted.
  - **¿Cuánto cuesta?** De $96 a $119 cada 4 semanas, según el tratamiento. Usted ve el precio antes de empezar.

### Closing CTA band
Default.

---

## Women's health (category page)

### Meta
- Title: Salud femenina | Restore Vitality Health
- Description: Atención para la menopausia en línea: estradiol en crema, parche o tableta con progesterona, o una opción no hormonal. $237 cada 12 semanas.

### Compact banner
- Title: Salud **femenina**
- Line: Atención para la menopausia con opciones hormonales y no hormonales, recetadas en línea, por $237 cada 12 semanas.
- Media alt: none (decorative)

### Treatment rail
Four Women's health cards. Safety line under the grid.

### Who it is for
- Heading: Atención para **la menopausia**
- Body: Para mujeres en la menopausia que buscan alivio de síntomas como los bochornos, el sueño interrumpido y los cambios de humor. La terapia hormonal combina estradiol, en crema, parche o tableta, con progesterona. Si las hormonas no son para usted, hay una tableta no hormonal. Un profesional con licencia revisa su historial y decide con usted la mejor opción. Todas cuestan $237 cada 12 semanas.

### Quiz entry row
- **¿No sabe cuál elegir? Responda dos preguntas**

### FAQ
- Heading: Preguntas sobre **salud femenina**
- Questions:
  - **¿Cómo elijo entre crema, parche y tableta?** Contienen las mismas hormonas en distintas formas. La crema se aplica una vez al día, el parche se cambia dos veces por semana y la tableta se toma una vez al día. Su profesional le ayuda a decidir.
  - **¿Hay una opción sin hormonas?** Sí. La paroxetina oral (o desvenlafaxina) es una tableta no hormonal que se toma una vez al día.
  - **¿Por qué se cobra cada 12 semanas?** El programa de menopausia tiene precio por periodos de 12 semanas, así que se le cobra y se le resurte con menos frecuencia. Cuesta $237 por periodo.
  - **¿Necesito receta?** Sí. Un profesional con licencia revisa su formulario y decide si un tratamiento es adecuado para usted.

### Closing CTA band
Default.

---

## Shared treatments (category page)

### Meta
- Title: Tratamientos para todos | Restore Vitality Health
- Description: Pérdida de peso, microdosis de GLP-1 y longevidad para hombres y mujeres, desde $145 cada 4 semanas. Recetados en línea por un profesional con licencia.

### Compact banner
- Title: Tratamientos **para todos**
- Line: Pérdida de peso, microdosis de GLP-1 y longevidad, para hombres y mujeres, desde $145 cada 4 semanas.
- Media alt: none (decorative)

### Treatment rail
Ten Shared cards, grouped with a small label above each group: Pérdida de peso médica / Microdosis de GLP-1 / Longevidad. Safety line under the grid.

### Who it is for
- Heading: Pérdida de **peso médica**
  Body: Para adultos que quieren bajar de peso con un enfoque médico y un profesional que ajusta el plan con ellos. Elija semaglutida en tableta diaria o inyección semanal, o tirzepatida en inyección semanal. Su profesional revisa su historial de salud y fija la dosis. Desde $249 cada 4 semanas.
- Heading: Microdosis **de GLP-1**
  Body: Para quienes prefieren un progreso constante y suave en lugar de un cambio rápido. Semaglutida o tirzepatida en dosis más baja, una vez por semana, fijada por su profesional y ajustada a sus metas. Ambas opciones cuestan $179 cada 4 semanas.
- Heading: **Longevidad**
  Body: Para adultos que se sienten bien y quieren conservar su energía, su concentración y su recuperación con los años. Elija NAD+ en inyección, aerosol nasal o liposomal oral, sermorelina antes de dormir o una inyección semanal de B12. Desde $145 cada 4 semanas.
- Heading (only when the client confirms them): **Péptidos**
  Body: [Peptide names: pending client]. [Peptide prices: pending client].

### Quiz entry row
- **¿No sabe cuál elegir? Responda dos preguntas**

### FAQ
- Heading: Preguntas sobre **estos tratamientos**
- Questions:
  - **¿Qué diferencia hay entre el programa de pérdida de peso y la microdosis?** Ambos usan semaglutida o tirzepatida. La microdosis usa una dosis más baja para un progreso más lento y suave, y cuesta $179 cada 4 semanas. El programa completo empieza en $249.
  - **¿Tengo que inyectarme?** No siempre. La semaglutida existe en tableta diaria, y el NAD+ en aerosol nasal o liposomal oral. Las inyecciones incluyen instrucciones escritas y en video.
  - **¿Puedo combinar tratamientos?** Algunos pacientes añaden la inyección de B12 a un plan de control de peso. Si se pueden combinar dos tratamientos lo decide su profesional.
  - **¿Necesito receta?** Sí. Un profesional con licencia revisa su formulario y decide si un tratamiento es adecuado para usted.

### Closing CTA band
Default.

---

## Treatment detail template

### Meta (pattern)
- Title: {Product name} | Restore Vitality Health
- Description: {Card description} {Price}. Recetado en línea por un profesional con licencia en su estado.

### Info column
- H1: {Product name}
- Chips: {format} / {frequency}
- Price: {price} cada {4 or 12} semanas
- Paragraph: {Page paragraph}
- Button: Iniciar su consulta (to the product's intake link)
- Line under the button: Solo se le cobra al completar su formulario, y se le reembolsa el total si un profesional determina que el tratamiento no es adecuado para usted.
- Safety line (sitewide)
- Ingredients label: Ingredientes
- Media alt: none (decorative)

### Benefits band
- Heading: Para qué **sirve**
- List: the product's three benefits.
- Note under the list: Los resultados no están garantizados y varían según la persona.

### Safety information block
- Heading: Información **de seguridad**
- Body: Este es un medicamento compuesto. Los medicamentos compuestos no están aprobados por la FDA, y la FDA no evalúa su seguridad, eficacia ni calidad. Los preparan farmacias con licencia que deben cumplir normas de calidad estatales y federales. Cómo tomarlo, y a qué estar atento, se explica en la información de seguridad de los medicamentos.
- Link: Leer la información de seguridad completa

The linked safety page is in English until the client supplies Spanish legal text.

### FAQ
The FAQ of the product's category page.

### You may also consider
- Heading: También **le puede interesar**
- Three cards from the same program or group.

### Closing CTA band
- Headline: Vitalidad para **lo que viene**
- Line: Inicie su consulta en línea. Un profesional con licencia se encarga del resto.
- Button: Iniciar su consulta (to this product's intake link)

---

## How it works (page)

### Meta
- Title: Cómo funciona | Restore Vitality Health
- Description: Consulta, análisis si hacen falta, su plan, el envío y el seguimiento, todo en línea. Conozca cada paso de la atención con Restore Vitality Health.

### Compact banner
- Title: Cómo **funciona**
- Line: Cinco pasos, todos en línea, con un profesional con licencia que decide en cada momento importante.

### Steps
1. **Consulta**: Cuéntenos **sobre usted**
   Elija el programa que le interesa y complete el formulario en línea. Le pregunta sobre su salud, sus antecedentes y los medicamentos que toma, para que su profesional tenga el panorama completo. Lo revisa un profesional con licencia en el estado donde usted vive, por video, por teléfono o por mensaje seguro, según lo que necesite. Se le cobra el primer periodo al completar el formulario.
2. **Análisis**: Análisis, **si hacen falta**
   Algunos tratamientos requieren resultados de laboratorio antes de poder recetarse. Si es su caso, su profesional le dirá qué necesita. Con su consentimiento, se pueden añadir a su expediente registros que ya tenga, como análisis recientes, para no repetir pruebas. Algunos planes incluyen servicios de laboratorio; si interviene un laboratorio externo, puede cobrar por separado.
3. **Plan**: Su **plan**
   Con su propio criterio profesional, su profesional decide si una receta es adecuada para usted, qué tratamiento y en qué dosis. A veces la respuesta es otra opción o una visita en persona. Si no es candidato por razones médicas, recibe un reembolso total.
4. **Envío**: Hasta **su puerta**
   Su receta va a una de nuestras farmacias asociadas con licencia, que la prepara y se la envía. Recibe avisos por mensaje de texto o correo electrónico durante el envío, y las inyecciones incluyen instrucciones escritas y en video.
5. **Seguimiento**: Atención **continua**
   Su plan se renueva cada periodo de cobro hasta que cancele, y recibe recordatorios de resurtido por mensaje o correo. Entre a Mi portal para administrar su cuenta. Para cancelar, escriba a soporte o use su cuenta al menos 72 horas antes de su próxima fecha de cobro.

### Timeline (vertical list at 390)
- Consulta: formulario en línea, revisado por un profesional con licencia
- Análisis: solo si su tratamiento los requiere
- Plan: su profesional decide qué le conviene
- Envío: preparado por una farmacia con licencia y enviado a usted
- Seguimiento: recordatorios de resurtido y apoyo en Mi portal

### FAQ
- Heading: Preguntas sobre **el proceso**
- Questions (from the FAQ page): ¿Cómo empiezo? / ¿Quién es mi profesional? / ¿Necesitaré una videollamada? / ¿Y si no soy candidato? / ¿Cómo cancelo?

### Closing CTA band
Default.

---

## Pricing (page)

### Meta
- Title: Precios | Restore Vitality Health
- Description: Todos los precios de Restore Vitality Health en un solo lugar, desde $96 cada 4 semanas. Un precio por periodo incluye la revisión, el medicamento si se receta y el apoyo.

### Compact banner
- Title: **Precios**
- Line: Un precio por periodo de cobro, visible antes de empezar, en cada programa que ofrecemos.

### Program cards
- Salud masculina: Disfunción eréctil, de $96 a $119 cada 4 semanas
- Salud femenina: Terapia hormonal para la menopausia, $237 cada 12 semanas. Opción no hormonal, $237 cada 12 semanas
- Para todos: Pérdida de peso médica, de $249 a $339 cada 4 semanas. Microdosis de GLP-1, $179 cada 4 semanas. Longevidad, de $145 a $229 cada 4 semanas
- "Every plan includes" list as on Home.

### What is included
- Heading: Qué incluye **su precio**
- Body: Su precio es un solo monto por cada periodo de cobro. Incluye la revisión de un profesional con licencia en su estado, su medicamento si se lo recetan y apoyo en línea. Según su plan y su elegibilidad médica, también puede incluir consultas de seguimiento, coordinación de la atención, servicios de laboratorio y acceso a una línea de apoyo al paciente las 24 horas.
- Not included list (heading: No incluye):
  - Los cargos de envío y procesamiento, que se muestran antes de completar su pedido
  - Servicios de empresas externas, como un laboratorio aparte, que pueden cobrarle directamente
  - Facturación al seguro: nuestros planes se pagan de forma privada

### How billing works
- Heading: Cómo **se cobra**
- Four short rows:
  - **Cuándo se le cobra**: al completar su formulario, por su primer periodo de cobro.
  - **Renovación**: su plan se renueva automáticamente cada 4 o 12 semanas, al precio que vio al inscribirse, hasta que cancele.
  - **Cancelación**: en cualquier momento, por correo o en su cuenta, al menos 72 horas antes de su próxima fecha de cobro.
  - **Reembolsos**: reembolso total si un profesional determina que no es candidato por razones médicas, o si cancela dentro de las primeras 72 horas sin haber recibido ningún servicio. Los medicamentos con receta no se pueden devolver una vez pedidos.

### Compare programs
- Heading: Compare **los programas**
- Table columns: Programa / Grupo / Formas / Se cobra cada / Desde
- Rows:
  - Disfunción eréctil / Salud masculina / Tableta, vial liposomal / 4 semanas / $96
  - Menopausia / Salud femenina / Crema, parche, tableta / 12 semanas / $237
  - Pérdida de peso médica / Para todos / Tableta, inyección semanal / 4 semanas / $249
  - Microdosis de GLP-1 / Para todos / Inyección semanal / 4 semanas / $179
  - Longevidad / Para todos / Inyección, aerosol nasal, liposomal / 4 semanas / $145
- Row link: Ver tratamientos
- Caption (screen readers): Programas de Restore Vitality Health comparados por grupo, formas, periodo de cobro y precio inicial

### FAQ
- Heading: Preguntas sobre **pagos**
- Questions: the Billing tab of the FAQ page.

### Closing CTA band
Default.

---

## About (page)

### Meta
- Title: Nosotros | Restore Vitality Health
- Description: Restore Vitality Health es una marca independiente de telesalud de Texas que ofrece atención con receta para la mediana edad, con profesionales y farmacias con licencia.

### Compact banner
- Title: **Nosotros**
- Line: Una marca independiente de telesalud de Texas, creada para adultos en la mediana edad que se sienten bien y quieren seguir así.

### Who we are
- Heading: Una vida **bien vivida**
- Body: Restore Vitality Health abrió en octubre de 2026, fundada en Texas por [Founder name] y [Partner name]. La creamos para hombres y mujeres en la mediana edad que están sanos, activos y listos para lo que viene, y que quieren acceso sencillo a la atención médica moderna con receta. Eso significa precios claros, lenguaje sencillo y un profesional con licencia que toma cada decisión médica.

### Clinical standards
- Heading: Normas **clínicas**
- Body: No somos una práctica médica ni tomamos decisiones de tratamiento. La atención la brindan OpenLoop Healthcare Partners y sus grupos médicos afiliados, cuyos profesionales tienen licencia en el estado donde usted vive. Su profesional puede ser un médico, un enfermero practicante o un asistente médico, y decide con su propio criterio profesional si recetar. Las recetas las preparan farmacias asociadas con licencia: Red Rock Compounding Pharmacy, Health Warehouse, Precision Medicine y Triad Rx.

### Privacy
- Heading: Su **privacidad**
- Body: [HIPAA wording: pending client]. Lo que comparte en su formulario llega a su profesional y a la farmacia que prepara su receta, para que puedan atenderle. No vendemos su información personal. Los formularios del sitio web, como la solicitud de llamada, están separados de su formulario médico, así que guarde los detalles de salud para su consulta.
- Link: Leer nuestra política de privacidad

### Clinical team
Held until the client names real people. Copy for when they do:
- Heading: Las personas **detrás**
- Cards:
  - [Founder name], [Founder role: pending client]. [Founder bio: pending client]
  - [Partner name], [Partner role: pending client]. [Partner bio: pending client]
  - [Clinician name], [Clinician credentials: pending client]. [Clinician bio: pending client]
- Portrait alt pattern: Retrato de {name}, {role}

### Closing CTA band
Default.

---

## FAQ (page)

### Meta
- Title: Preguntas frecuentes | Restore Vitality Health
- Description: Respuestas sobre recetas, profesionales, medicamentos compuestos, pagos, cancelaciones, reembolsos y privacidad en Restore Vitality Health.

### Compact banner
- Title: **Preguntas** frecuentes
- Line: Si la suya no está aquí, escriba a support@rx.restorevitality.health y le ayudamos.

### FAQ
- Tabs: Primeros pasos / Recetas y seguridad / Pagos / Privacidad
- Open and close labels for screen readers: Mostrar respuesta / Ocultar respuesta

**Getting started**
- **¿Para quién es Restore Vitality Health?** Para adultos en la mediana edad, hombres y mujeres, que quieren atención con receta para la salud sexual, la menopausia, el peso o un envejecimiento saludable, todo en línea. Debe tener al menos 18 años y vivir en Estados Unidos.
- **¿Dónde ofrecen atención?** En los 50 estados y Washington DC. Algunos medicamentos no están disponibles en todos los estados, y el formulario le indica si eso le afecta.
- **¿Cómo empiezo?** Elija un programa, o responda las dos preguntas del cuestionario si no está seguro, y luego complete el formulario en línea del tratamiento que desea.
- **¿Necesitaré una videollamada?** No siempre. Según lo que necesite, su profesional puede revisar su formulario por mensaje, o pedirle hablar por teléfono o por video.

"¿Cuánto tarda la revisión de mi formulario?" is left out until the client gives a review time (Questions for the client, 8).

**Prescriptions and safety**
- **¿Quién es mi profesional?** Un profesional con licencia en su estado, que puede ser un médico, un enfermero practicante o un asistente médico, y que trabaja con OpenLoop Healthcare Partners y sus grupos médicos afiliados.
- **¿Qué son los medicamentos compuestos?** Medicamentos que una farmacia con licencia prepara para un paciente en particular. No están aprobados por la FDA, y la FDA no revisa su seguridad, eficacia ni calidad. Las farmacias de compuestos tienen licencia y deben cumplir normas estatales y federales.
- **¿Y si no soy candidato?** Su profesional puede sugerirle otra opción o una visita en persona. Si no es candidato por razones médicas, recibe un reembolso total.
- **¿Cómo me llega el medicamento?** Una farmacia asociada con licencia lo prepara y se lo envía, con avisos por mensaje de texto o correo electrónico.
- **¿Los resultados están garantizados?** No. Los resultados varían según la persona, y ningún tratamiento puede prometer un resultado.

**Billing**
- **¿Cuánto cuesta?** Desde $96 cada 4 semanas, según el tratamiento. Todos los precios están en nuestra página de Precios y se muestran de nuevo antes de pagar.
- **¿Cuándo se me cobra?** Al completar su formulario, por su primer periodo de cobro. Después, su plan se renueva automáticamente hasta que cancele.
- **¿Cómo cancelo?** Escriba a support@rx.restorevitality.health o use su cuenta, al menos 72 horas antes de su próxima fecha de cobro. Conserva el servicio hasta el final del periodo que ya pagó.
- **¿Puedo recibir un reembolso?** Sí, total, si un profesional determina que no es candidato por razones médicas, o si cancela dentro de las 72 horas siguientes a su inscripción sin haber recibido ningún servicio. Los medicamentos no se pueden devolver una vez pedidos.
- **¿Aceptan seguro médico?** Nuestros planes se pagan de forma privada, así que no se facturan al seguro. Conserve su seguro actual para todo lo demás.

**Privacy**
- **¿Mi información es privada?** [HIPAA wording: pending client]. La información de su formulario se comparte con su profesional y su farmacia para que puedan atenderle, y no vendemos su información personal.
- **¿El cuestionario guarda mis respuestas?** No. El cuestionario solo le indica un programa. Nada de lo que elija se guarda ni se envía.
- **¿Cómo administro las cookies?** Use Configuración de cookies en el pie de página cuando quiera. También puede excluirse del intercambio de datos no esenciales en nuestra página No vender ni compartir.

### Closing CTA band
Default.

---

## Contact (page)

### Meta
- Title: Contacto | Restore Vitality Health
- Description: Escriba a support@rx.restorevitality.health o pida una llamada. Atención al cliente en vivo de lunes a sábado, de 9 a. m. a 6 p. m., hora del Centro.

### Glass panel (left)
- Heading: Hable **con nosotros**
- Line: Preguntas sobre un programa, su pedido o su cuenta. Con gusto le ayudamos.
- Email label: Correo electrónico
- Email: support@rx.restorevitality.health
- Phone label: Teléfono
- Phone: [Phone number]
- Hours label: Atención al cliente en vivo
- Hours: Lunes a sábado, de 9 a. m. a 6 p. m., hora del Centro
- Line: ¿Ya es paciente? Entre a Mi portal.
- Media alt: none (decorative)

### Callback form (right)
- Heading: Pida **una llamada**
- Intro: Déjenos su número y el mejor momento para llamarle, y alguien de nuestro equipo le llamará en horario de atención.
- Fields:
  - Nombre (obligatorio)
  - Correo electrónico (obligatorio)
  - Teléfono (obligatorio). Hint: Número de EE. UU., con código de área
  - Mejor momento para llamar. Options: Mañana (de 9 a. m. a 12 p. m., hora del Centro) / Tarde (de 12 p. m. a 3 p. m., hora del Centro) / Final de la tarde (de 3 p. m. a 6 p. m., hora del Centro)
  - Mensaje (opcional). Hint: No incluya detalles de salud aquí. Su profesional le preguntará sobre eso en la consulta.
- Consent checkbox: Acepto que me contacten por teléfono o correo electrónico sobre mi solicitud.
- Button: Pedir una llamada
- Success (only if the endpoint answers): Gracias. Recibimos su solicitud y le llamaremos en horario de atención.
- Error: Form messages (sitewide)
- Build note: the form sends to [Notification email]. Spanish requests should be flagged as Spanish in the notification, so the team knows to call back in Spanish (Questions 19).

### Closing CTA band
Default.

---

## Quiz (page)

### Meta
- Title: Encuentre su programa | Restore Vitality Health
- Description: Dos preguntas breves le indican el programa de Restore Vitality Health adecuado para usted. Nada de lo que elija se guarda ni se envía.

### Intro screen
- Heading: Encuentre **su programa**
- Line: Dos preguntas breves. Nada de lo que elija se guarda ni se envía: solo le indica el programa adecuado, y un profesional con licencia toma las decisiones médicas.
- Button: Empezar
- Progress label (screen readers): Pregunta {n} de 2

### Question 1
- Question: ¿En qué **le podemos ayudar?**
- Answers:
  - Disfunción eréctil (to Result: Erectile dysfunction)
  - Síntomas de la menopausia (to Question 2: Menopause)
  - Peso (to Question 2: Weight)
  - Energía y envejecimiento saludable (to Result: Longevity)
  - Todavía no lo sé (to Result: Not sure)

### Question 2: Menopause
- Question: ¿Consideraría la **terapia hormonal?**
- Answers:
  - Sí, terapia hormonal (to Result: Menopause care, hormone options highlighted)
  - Prefiero evitar las hormonas (to Result: Menopause care, non-hormonal option highlighted)
  - No lo sé, quiero un consejo (to Result: Menopause care)

### Question 2: Weight
- Question: ¿Qué ritmo **le conviene?**
- Answers:
  - Un programa completo, con la dosis que fije mi profesional (to Result: Medical weight loss)
  - Una dosis más baja, para un progreso constante y suave (to Result: GLP-1 microdosing)
  - No lo sé, quiero un consejo (to Result: Medical weight loss)

### Navigation
- Back: Atrás
- Restart: Empezar de nuevo

### Results
- **Disfunción eréctil**. Desde $96 cada 4 semanas.
  Siete tratamientos, en tabletas o viales liposomales, con uno a cuatro activos. Su profesional revisa su historial y le sugiere el adecuado.
  Button: Ver tratamientos (Men's health). Link: Empezar de nuevo
- **Atención para la menopausia**. $237 cada 12 semanas.
  Estradiol en crema, parche o tableta con progesterona, o una tableta no hormonal. Su profesional le ayuda a elegir.
  Button: Ver tratamientos (Women's health). Link: Empezar de nuevo
- **Pérdida de peso médica**. Desde $249 cada 4 semanas.
  Semaglutida en tableta diaria o inyección semanal, o tirzepatida en inyección semanal, con la dosis que fije su profesional.
  Button: Ver tratamientos (Shared, weight loss). Link: Empezar de nuevo
- **Microdosis de GLP-1**. $179 cada 4 semanas.
  Una dosis semanal más baja de semaglutida o tirzepatida, para un progreso constante y suave.
  Button: Ver tratamientos (Shared, microdosing). Link: Empezar de nuevo
- **Longevidad**. Desde $145 cada 4 semanas.
  NAD+ en inyección, aerosol nasal o liposomal, sermorelina o una inyección semanal de B12, para la energía, la concentración y la recuperación.
  Button: Ver tratamientos (Shared, longevity). Link: Empezar de nuevo
- **Todavía no lo sé**.
  No hay problema. Vea todos los programas y precios en un solo lugar, o escríbanos y le orientamos.
  Button: Ver todos los precios (Pricing). Link: Contáctenos

Under every result: Un profesional con licencia toma la decisión final después de su consulta.

---

## Resources index and article

### Meta (index)
- Title: Recursos | Restore Vitality Health
- Description: Notas en lenguaje sencillo sobre la salud en la mediana edad, nuestros programas y los nuevos tratamientos de Restore Vitality Health.

### Index
- H1: **Recursos**
- Standfirst: Notas en lenguaje sencillo sobre la salud en la mediana edad, nuestros programas y los nuevos tratamientos a medida que lleguen.
- Empty state: Nuestros primeros artículos están en camino. Suscríbase abajo y le avisaremos cuando se publiquen.
- Newsletter: as in the Home resources rail.
- Category chip on cards: {category}
- Card link: Leer el artículo

### Article template
- Meta title: {Article title} | Restore Vitality Health
- Meta description: {Standfirst, up to 155 characters}
- Labels: Publicado el {date} / {n} min de lectura
- Footer of the article: Este artículo es informativo y no sustituye el consejo médico. Hable con un profesional con licencia sobre su propia salud.
- Next link: Siguiente artículo
- Back link: Todos los recursos

---

## Legal pages
[Spanish legal text: pending client]

Per Varun's note, the legal pages are not translated. Until the client supplies Spanish text, each Spanish legal URL shows the English page with a short Spanish line above it, and the H1 stays in English with `lang="en"` on the legal body.

| Page | URL (es) | H1 | Body | Meta description |
|---|---|---|---|---|
| Privacy policy | /es/privacy | Privacy Policy | [Spanish legal text: pending client] | Cómo Restore Vitality Health recopila, usa y protege la información cuando usted usa este sitio web. |
| Terms of service | /es/terms | Terms & Conditions | [Spanish legal text: pending client] | Los términos que rigen el uso del sitio web y los servicios de Restore Vitality Health. |
| Medications safety information | /es/medications-safety-information | Medications Safety Information | [Spanish legal text: pending client] | Información de seguridad sobre los medicamentos compuestos recetados a través de Restore Vitality Health. |
| Telehealth consent | /es/telehealth-and-medical-info | Telehealth and Medical Information | [Spanish legal text: pending client] | Consentimiento para la telesalud, el tratamiento, las comunicaciones y el uso de su información médica. |
| Do not sell or share | /es/do-not-sell | Do Not Sell or Share My Personal Information | [Spanish legal text: pending client] | Cómo excluirse de la venta o el intercambio de su información personal. |

- Meta title pattern: {Spanish page name} | Restore Vitality Health. Names: Política de privacidad / Términos del servicio / Información de seguridad de los medicamentos / Consentimiento de telesalud / No vender ni compartir mi información personal
- Line above the English text: Este documento legal está disponible solo en inglés por ahora. Si tiene preguntas, escríbanos a support@rx.restorevitality.health.

---

## 404

### Meta
- Title: Página no encontrada | Restore Vitality Health
- Description: Esta página cambió de lugar o ya no existe.

### Content
- Headline: Esta página **ya no está aquí**
- Line: Puede que el enlace sea antiguo o que la dirección tenga un error. Todo lo demás sigue en su lugar.
- Button: Volver al inicio
- Text link: Encontrar su programa

---

## Questions for the client
The full list is in copy.md, Questions for the client (1 to 19).

### Placeholders in the copy
The same seven items as copy.md, items 1 to 7: founder and partner names, clinician, reviews, phone number, notification email, peptide names and prices, HIPAA wording.

### Other things the copy wrote around
Items 8 to 18 in copy.md apply to both languages. Spanish-specific points, also in item 19 there:
- Do OpenLoop's intake and patient portal run in Spanish? If not, every Comenzar and Iniciar su consulta button lands on an English form, and the Spanish site should say so before the click. Suggested line under intake buttons, once confirmed: "El formulario médico está en inglés."
- Who supplies the Spanish legal text?
- Can the client approve our Spanish versions of the footer disclaimers and the safety line?
- Can the team call back in Spanish? The callback form promises a call; if no Spanish speaker is available, the Spanish contact page should say calls are in English.
- Should real reviews be translated, or shown in the language they were written in?

## Notes for Varun
- Section names match copy.md exactly, in English, so the Developer can build both languages from one structure.
- "Para todos" replaces "Shared" in Spanish navigation, tabs and pills. The URL can stay shared-treatments.
- The hero and closing lines are not literal translations (see the notes under Hero and Closing CTA band), to avoid gendered adjectives for a mixed audience.
- "Hot flashes" is "bochornos", the term most US Spanish speakers of Mexican and Central American origin use; "sofocos" is the usual term in Spain.
