# Copy: Restore Vitality Health (English)
Copywriter, 2026-11-10. Built from brief.md, design/design-spec.md (section names as they stand during the art director's critic loop), prd/existing-site.md and the client's own terms in assets/legal/existing-site-legal.md. Spanish mirror: content/copy-es.md, same structure and section names.

## How to read this file
- Headlines are written in sentence case. The CSS sets them in capitals. `**bold**` marks the words set in the 600 weight; everything else in a headline is the 300 weight (spec 3, Varun's light + bold mix). No headline ends in a full stop.
- Buttons are sentence case with the small arrow (V9).
- Square brackets are client placeholders that Varun approved for this run: founder and partner names, any named clinician, reviews and outcomes, phone number, notification email, peptide names and prices, and the HIPAA wording. Each one is listed under Questions for the client. The build keeps them out of the live page and adds `<!-- CLIENT COPY REQUIRED -->` (spec 7). No other brackets appear in the copy.
- Brand name: the client writes "Restore Vitality Health" (three words) in its footer, terms and product copy, so the copy does too. The prototype's `<title>` says "RestoreVitality Health" and should change to match.
- Product names stay exactly as they appear in OpenLoop intake, because the intake screens and pharmacy labels use them.
- Font note: the trial Carbona has no `' ? ! $ :` and no Spanish accents. Display headlines avoid those characters where the line reads just as well without them. Where one is needed (questions, prices, "Men's health"), Albert Sans fills the gap, as choices.md says.

---

## Sitewide

### Header
- Menu pill: Menu
- Inline links (from 1280): Men's health / Women's health / Shared
- Logo alt: Restore Vitality Health, home
- Language switch: EN / ES. Screen reader text on ES: (Español). Group label: Language
- Portal link: My portal. Screen reader text: (opens in a new tab)
- Header pill: Get started (goes to the quiz)

### Menu drawer
- Close pill: Close
- Links: Men's health / Women's health / Shared treatments / How it works / Pricing / About / FAQ / Resources / Contact
- Language and portal row: EN / ES, My portal
- Quiz block title: Not sure where to start?
- Quiz block text: Answer two short questions and we point you to the program that fits. Nothing you choose is saved.
- Button: Take the quiz

### Safety line (under every treatment rail and on every treatment page)
Compounded medications are not FDA-approved. A prescription is required, and a licensed provider decides whether a treatment is right for you. Read the safety information
- Link text: Read the safety information (to /medications-safety-information)

### Credibility row (sitewide)
Four statements, 16px caps over one muted line.
1. **Reviewed by licensed providers**
   Every request is reviewed by a provider licensed in the state where you live.
2. **All 50 states and DC**
   Availability of each medication varies by state.
3. **Prices shown up front**
   You see the price and billing period before you start.
4. **[HIPAA wording: pending client]**
   [HIPAA supporting line: pending client]

Marquee at 390 reads the four headings in order, separated by spaces only (no dots, per anti-slop).

### Closing CTA band (default)
- Headline: Restored for **what's next**
- Line: Two short questions point you to the right program. A licensed provider takes it from there.
- Button: Find your program
- Glyph alt: none (decorative, `aria-hidden`)

The tagline lives here, at the close, not in the hero (choices.md keeps it out of the hero).

### Footer
- Email (first, 26px): support@rx.restorevitality.health
- Line under it: Live customer service Monday to Saturday, 9am to 6pm Central.
- Phone: [Phone number]
- Column heads and links:
  - **Treatments**: Men's health / Women's health / Shared treatments / Pricing / Take the quiz
  - **Company**: About / How it works / FAQ / Resources / Contact / My portal
  - **Legal**: Privacy policy / Terms of service / Medications safety information / Telehealth consent / Cookie settings / Do not sell or share my personal information
- Disclaimer paragraph (client's text, kept word for word):
  Compounded drug products are not FDA approved. FDA does not evaluate compounded products for safety, effectiveness, or quality. Prescription products require an online consultation with a healthcare provider who will determine if a prescription is appropriate. Please visit our website for full details, applicable restrictions, and important drug safety information.
  Restore Vitality Health does not manufacture compounded medications. Actual product appearance and labeling of the medication you receive will differ from website images.
  Results are not guaranteed and may vary by individual as part of a personalized weight loss and health program.
- Copyright: Copyright 2026 Restore Vitality Health. All rights reserved.
- Bottom row: EN / ES, Back to top, Created with love by Digital Heroes
- Closing lockup alt: Restore Vitality Health. Lived well. Restored for what's next.

### Sticky mobile CTA
- Pill: Find your program

### Cookie notice
- Text: We use essential cookies to run this site. With your permission we also use analytics and marketing cookies to see how the site is used. You can change your choice at any time in Cookie settings.
- Buttons: Accept / Settings

### Form messages (shared by every form)
- Required field: Please fill in this field.
- Email format: Please enter an email address, for example name@example.com.
- Phone format: Please enter a US phone number, including the area code.
- Sending: Sending
- Network error: That did not go through. Please try again, or email us at support@rx.restorevitality.health.

---

## Home

### Meta
- Title: Restore Vitality Health | Prescription care for midlife
- Description: Prescription programs for men and women in midlife: sexual health, menopause, weight loss and longevity. Reviewed online by a licensed provider, with prices shown up front.

### Hero
- Headline (3 rows at 390): Ready for / **the next / adventure**
- Lead: Prescription care for men and women in midlife: sexual health, menopause, weight loss and longevity, reviewed online by a licensed provider in your state.
- Button: Find your program (to the quiz)
- Fact chip: Plans from $96 per 4 weeks
- Scroll cue: Scroll to discover
- Media alt: none (wordmark is decorative, `aria-hidden`; the logo in the header carries the name)

The headline comes from the client's own words, "ready for life's next adventures". I recommend keeping it (spec decision 1).

### Treatments
- Screen reader h2: Treatments
- Tabs: Men's health / Women's health / Shared
- Cards: see Treatment data below. Each card shows title, two chips (format, frequency), the two-line card description, price with period, the gold pill and the text link.
- Card pill: Get started (to that product's OpenLoop intake link)
- Card link: Learn more (to the treatment page)
- Card media alt: none (vein crops are decorative; the card title names the product)
- Under the rail: Safety line (sitewide)

### Credibility row
Sitewide block, as above.

### How it works
- Heading: How it **works**
- Intro: From your first answers to your next refill, everything happens online. A provider licensed in your state reviews your history and decides what, if anything, to prescribe. You always know what you are paying and when.
- Five step cards. Step name (13px caps beside the chip), title, body:
  1. **Consult**
     Title: Tell us **about you**
     Body: Choose a program and complete a short online intake about your health and goals. A licensed provider reviews it, by video, by phone or by message.
  2. **Labs**
     Title: Labs, **if needed**
     Body: Some treatments call for lab results first. If yours does, your provider will tell you what is needed, and with your consent existing results can be added to your record.
  3. **Plan**
     Title: Your **plan**
     Body: Your provider decides whether a prescription is right for you, and at what dose. If it is not, they may suggest another option, and you are refunded in full.
  4. **Delivery**
     Title: Sent **to your door**
     Body: A licensed partner pharmacy fills your prescription and ships it to you. You get updates by text or email as it moves.
  5. **Follow-up**
     Title: Ongoing **care**
     Body: Your plan renews each billing period, with refill reminders by text or email. Manage your account in My portal, and cancel at any time.
- Step illustration alt: none (decorative; the card text carries the meaning)

### Quiz entry band
- Heading: Where would you **like to start?**
- Routing rows (each row is one link):
  - Men's **health**, chip: From $96 per 4 weeks (to Men's health)
  - Women's **health**, chip: From $237 per 12 weeks (to Women's health)
  - **Shared**, chip: From $145 per 4 weeks (to Shared treatments)
- Quiz row: **Not sure? Take the two-question quiz** (to the quiz)
- Media alt: none (decorative)

The spec's working line had "two-minute quiz"; the quiz below has two questions, so the row says that instead of a time.

### Real results
Built only when the client sends real reviews (spec). Copy for when they arrive:
- Heading: In their **own words**
- Ring arrows: Previous / Next (screen reader labels)
- Cards (three to start):
  - Initials: [Reviewer initials: pending client]. Date: [Review date: pending client]
  - Quote: [Review: pending client]
  - Product row: [Product reviewed: pending client]
- Note under the rail: Reviews are from real patients. Individual results vary.

### Pricing tease
- Heading: Clear prices, **no surprises**
- Intro: Each program has one price for each billing period, shown before you start. The price covers your provider's review, your medication if it is prescribed, and online support.
- Cards:
  1. Pill: Men's health. Group name: **Men's** health. Blurb: Seven treatments for erectile dysfunction, as tablets or liposomal vials. From: $96 per 4 weeks. Button: See men's treatments
  2. Pill: Women's health. Group name: **Women's** health. Blurb: Menopause care, with hormone and non-hormonal options. From: $237 per 12 weeks. Button: See women's treatments
  3. Pill: Shared. Group name: **Shared**. Blurb: Weight loss, GLP-1 microdosing and longevity, for men and women. From: $145 per 4 weeks. Button: See shared treatments
- "Every plan includes" list (same on all three cards):
  - Review by a provider licensed in your state
  - Your medication, if your provider prescribes it
  - Online support through My portal
- Under the cards: See every price (to Pricing)

The list uses the client's own terms: "The Subscription Services include access to providers, medications where appropriate, and online support."

### FAQ
- Heading: Questions, **answered**
- Tabs and questions: the first two questions of each theme from the FAQ page (Getting started, Prescriptions and safety, Billing, Privacy).
- Link under the answers: See all questions (to FAQ)

### Resources rail
Until articles exist the band shows the newsletter capture only (spec).
- Heading: Hear from **us** (pass 8b; was: Notes for **what's next**)
- Line: Plain-language notes on our programs and new treatments as they arrive. No spam, and you can unsubscribe at any time.
- Field label: Email address
- Button: Sign up
- Success: Thank you. You are on the list.

When articles exist:
- Heading: **Resources**
- Card link: Read the article
- Link at the end: All resources

### Closing CTA band
Default, as in Sitewide.

---

## Treatment data (cards and treatment pages)
Each entry: title / chips / card description (two lines) / price / page paragraph / benefits (three) / ingredients / intake link.
Benefits are the client's own lines from its program pages, kept as written. Page paragraphs are built only from the client's facts.

### Men's health: Erectile dysfunction (billed every 4 weeks)

**Daily Boost Pill**
- Chips: Oral / Take as needed
- Card: Tadalafil in one simple tablet, taken when you need it.
- Price: $112 per 4 weeks
- Page: One simple tablet with a single active, tadalafil, taken when you need it. It is a compounded prescription, so a licensed provider reviews your health history first and decides whether it suits you and at what dose. If it is prescribed, a partner pharmacy fills it and ships it to you.
- Benefits: Enhances penile blood flow / Promotes smooth muscle relaxation / Boosts response to stimulation
- Ingredients: Tadalafil
- Intake: productId UHJvZHVjdDoxNjg=, program erectile_dysfunction

**Double Powered Liposomal**
- Chips: Oral / Take as needed
- Card: Sildenafil and tadalafil together, in one simple vial.
- Price: $99 per 4 weeks
- Page: Two actives, sildenafil and tadalafil, combined in one liposomal vial you take by mouth when you need it. Liposomal means the actives are carried in a fine lipid layer. Your provider reviews your history and current medications and decides whether it is a fit.
- Benefits: Encourages spontaneous readiness / Enhances sexual response / Supports stronger activity
- Ingredients: Sildenafil, Tadalafil
- Intake: productId UHJvZHVjdDoxNjM=

**Double Powered Pill**
- Chips: Oral / Take as needed
- Card: Sildenafil and tadalafil together, in one simple tablet.
- Price: $96 per 4 weeks
- Page: The same two actives as the liposomal, sildenafil and tadalafil, in one tablet taken when you need it. It is our lowest-priced treatment for erectile dysfunction. A licensed provider reviews your health history and decides whether it is right for you, and at what dose.
- Benefits: Boosts readiness for activity / Enhances response intensity / Improves sexual activity
- Ingredients: Sildenafil, Tadalafil
- Intake: productId UHJvZHVjdDoxNjU=

**Quadruple Powered Liposomal**
- Chips: Oral / Take as needed
- Card: Our most complete formula, with four actives in one vial.
- Price: $119 per 4 weeks
- Page: Four actives in one liposomal vial: sildenafil, tadalafil, apomorphine and L-citrulline. It is the most complete formula in the range, taken by mouth when you need it. Because it combines several medications, your provider looks closely at your history and other prescriptions before deciding whether it suits you.
- Benefits: Comprehensive ED support / Accelerated absorption rate / Physical and mental arousal
- Ingredients: Sildenafil, L-Citrulline, Tadalafil, Apomorphine
- Intake: productId UHJvZHVjdDoxOTY=

**Triple Powered Liposomal**
- Chips: Oral / Take as needed
- Card: Sildenafil, tadalafil and vardenafil, in one simple vial.
- Price: $109 per 4 weeks
- Page: Three actives, sildenafil, tadalafil and vardenafil, in one liposomal vial taken by mouth when you need it. A licensed provider reviews your health history and current medications and decides whether it is right for you. If it is prescribed, a partner pharmacy fills it and ships it to you.
- Benefits: Quick onset of action / Extended duration benefits / Reliable multi-ingredient formula
- Ingredients: Sildenafil, Tadalafil, Vardenafil
- Intake: productId UHJvZHVjdDoxNjE=

**Triple Powered Pill**
- Chips: Oral / Take as needed
- Card: Sildenafil, tadalafil and apomorphine, in one simple tablet.
- Price: $102 per 4 weeks
- Page: Three actives, sildenafil, tadalafil and apomorphine, in one tablet taken when you need it. A licensed provider reviews your history and current medications first and decides whether it is a fit, and at what dose. If it is prescribed, a partner pharmacy fills it and ships it to you.
- Benefits: Rapid arousal response / Prolonged effectiveness / Central arousal enhancement
- Ingredients: Sildenafil, Tadalafil, Apomorphine
- Intake: productId UHJvZHVjdDoxNjQ=

**Triple Powered Up Liposomal**
- Chips: Oral / Take as needed
- Card: Sildenafil, tadalafil and apomorphine, in one simple vial.
- Price: $109 per 4 weeks
- Page: The same three actives as the Triple Powered Pill, sildenafil, tadalafil and apomorphine, in a liposomal vial taken by mouth when you need it. Your provider reviews your health history and decides whether this form or the tablet suits you better.
- Benefits: Fast-acting liposomal formula / Prolonged supporting effects / Enhances central arousal
- Ingredients: Sildenafil, Tadalafil, Apomorphine
- Intake: productId UHJvZHVjdDoxNjI=

### Women's health: Menopause hormone therapy (billed every 12 weeks)

**Estradiol cream + Progesterone**
- Chips: Cream / Daily
- Card: Estradiol and progesterone, one simple application a day.
- Price: $237 per 12 weeks
- Page: Estradiol applied as a cream once a day, prescribed together with progesterone. It is one of three hormone options in the program, and the choice between cream, patch and tablet is one you make with your provider. Billing is every 12 weeks, so you are not reordering every month.
- Benefits: Relieves menopause symptoms / Supports bone health / Enhances overall well-being
- Ingredients: Estradiol, Progesterone
- Intake: productId UHJvZHVjdDoxOTI=, program whrt

**Estradiol patch + Progesterone**
- Chips: Patch / Twice weekly
- Card: Estradiol and progesterone, one simple patch twice a week.
- Price: $237 per 12 weeks
- Page: Estradiol as a patch you change twice a week, prescribed together with progesterone. It contains the same hormones as the cream and the tablet, in a form you only think about twice a week. Your provider reviews your history and symptoms and decides which form and dose suit you.
- Benefits: Eases menopause discomfort / Improves mood and sleep / Maintains bone density
- Ingredients: Estradiol, Progesterone
- Intake: productId UHJvZHVjdDoxOTE=

**Estradiol Tablet**
- Chips: Oral / Daily
- Card: Estradiol with progesterone, one simple tablet a day.
- Price: $237 per 12 weeks
- Page: Estradiol taken as a tablet once a day, with progesterone. Like the cream and the patch, it is billed every 12 weeks. A licensed provider reviews your health history and decides whether hormone therapy is right for you, and in which form.
- Benefits: Reduces hot flashes / Protects bone strength / Supports hormone therapy
- Ingredients: Estradiol, Progesterone
- Intake: productId UHJvZHVjdDoxOTA=

**Oral Paroxetine**
- Chips: Oral / Daily
- Card: A non-hormonal option, one simple tablet a day.
- Price: $237 per 12 weeks
- Page: For women who cannot take hormones, or would rather not. One tablet a day of paroxetine or desvenlafaxine, both non-hormonal. Your provider reviews your history and decides which, if either, is right for you.
- Benefits: Non-hormonal for hot flashes / Alleviates mood swings / Improves sleep quality
- Ingredients: Paroxetine or Desvenlafaxine
- Intake: productId UHJvZHVjdDoxOTM=

### Shared: Medical weight loss (billed every 4 weeks)

**Oral Semaglutide**
- Chips: Oral / Daily
- Card: Semaglutide in one dissolvable tablet a day.
- Price: $279 per 4 weeks
- Page: Semaglutide, a GLP-1 medication, as one dissolvable tablet a day, for people who would rather not inject. Your provider reviews your health history and decides whether it is right for you and how the dose should change over time.
- Benefits: Stimulates insulin release / Controls blood sugar spikes / Curbs appetite effectively
- Ingredients: Semaglutide
- Intake: productId UHJvZHVjdDoxNDQ=, program macro_dosing_glp

**Semaglutide Injections**
- Chips: Injection / Weekly
- Card: Semaglutide in one simple injection a week.
- Price: $249 per 4 weeks
- Page: Semaglutide as one injection a week, with written and video instructions for doing it yourself at home. Your provider sets your starting dose after reviewing your health history and adjusts it with you over time.
- Benefits: Enhances insulin response / Prolongs gastric fullness / Reduces calorie intake
- Ingredients: Semaglutide
- Intake: productId UHJvZHVjdDoxNDI=

**Tirzepatide Injections**
- Chips: Injection / Weekly
- Card: Tirzepatide in one simple injection a week.
- Price: $339 per 4 weeks
- Page: Tirzepatide, which acts on two appetite pathways, as one injection a week. It comes with written and video instructions for injecting at home. Your provider reviews your history and decides whether it is right for you, and at what dose.
- Benefits: Increases insulin efficiency / Prolongs stomach fullness / Promotes appetite suppression
- Ingredients: Tirzepatide
- Intake: productId UHJvZHVjdDoxNDM=

### Shared: GLP-1 microdosing (billed every 4 weeks)

**Semaglutide Microdose Injection**
- Chips: Injection / Weekly
- Card: Low-dose semaglutide for steady, gentle progress.
- Price: $179 per 4 weeks
- Page: A lower dose of semaglutide, once a week, for steady and gentle progress rather than fast change. The dose is set for you by your provider after reviewing your health history, and it can be adjusted to your goals.
- Benefits: Supports smooth metabolism / Reduces appetite gently / Customizable for personal goals
- Ingredients: Semaglutide
- Intake: productId UHJvZHVjdDoxOTQ=, program microdosing_glp

**Tirzepatide Microdose Injection**
- Chips: Injection / Weekly
- Card: Our most powerful low-dose option for steady results.
- Price: $179 per 4 weeks
- Page: A lower dose of tirzepatide, which acts on two appetite pathways, once a week. It is the stronger of the two microdose options, at the same price. Your provider reviews your health history and decides whether it suits you, and at what dose.
- Benefits: Dual pathway hunger control / Smooth and sustainable results / Personalized ingredient customization
- Ingredients: Tirzepatide
- Intake: productId UHJvZHVjdDoxOTU=

### Shared: Longevity (billed every 4 weeks)
The client's longevity cards have descriptions instead of three short benefits. The benefits below are taken from those descriptions, not added to them.

**Metabolism Boost Injection (B12 + MIC)**
- Chips: Injection / Weekly
- Card: B12 with methionine, inositol and choline, once a week.
- Price: $145 per 4 weeks
- Page: A B12 and MIC injection (methionine, inositol, choline) that pairs B12 energy support with lipotropic compounds that help your body process and metabolize fat. A popular add-on for energy, metabolism and weight-management support.
- Benefits: B12 for energy support / Lipotropic compounds to help process fat / A popular add-on to a weight-management plan
- Ingredients: B12, Methionine, Inositol, Choline
- Intake: productId UHJvZHVjdDoxNzg=, program nad_sermorelin

**Cellular Recharge Injection (NAD+)**
- Chips: Injection / Twice weekly
- Card: NAD+ delivered directly, in one injection twice a week.
- Price: $199 per 4 weeks
- Page: A NAD+ injection that delivers this essential coenzyme straight into your system, supporting the cellular energy production, DNA repair and metabolism that naturally decline with age. Injection offers high, direct absorption, a foundational option for energy, focus and recovery.
- Benefits: Supports cellular energy production / Supports DNA repair and metabolism / High, direct absorption
- Ingredients: NAD+
- Intake: productId UHJvZHVjdDoxNzQ=

**Peak Recovery Injection (Sermorelin)**
- Chips: Injection
- Card: Sermorelin, which supports natural growth hormone production.
- Price: $229 per 4 weeks
- Page: A sermorelin injection that may support lean muscle maintenance, healthy aging, deeper sleep and steady energy. Typically taken before bed to align with your natural overnight cycle.
- Benefits: Supports natural growth hormone production / May support lean muscle and deeper sleep / Taken before bed, with your overnight cycle
- Ingredients: Sermorelin
- Intake: productId UHJvZHVjdDoxNzc=

**Cellular Recharge Nasal Spray (NAD+)**
- Chips: Nasal / Daily
- Card: NAD+ without needles, in one simple spray a day.
- Price: $229 per 4 weeks
- Page: A NAD+ nasal spray that absorbs through the nasal lining for a convenient, needle-free way to support cellular energy, focus and recovery. An easy daily option for maintaining NAD+ levels between or instead of injections.
- Benefits: Needle-free / Supports cellular energy, focus and recovery / Use between or instead of injections
- Ingredients: NAD+
- Intake: productId UHJvZHVjdDoxNzU=

**Cellular Recharge Liposomal (NAD+, Next-Gen)**
- Chips: Oral / Daily
- Card: Liposomal NAD+, taken by mouth once a day.
- Price: $229 per 4 weeks
- Page: A next-gen liposomal NAD+ that wraps the molecule in a protective lipid layer so more survives digestion and reaches your cells than with a standard oral. Supports cellular energy, metabolism and repair in a simple, needle-free daily form.
- Benefits: Protective lipid layer / Supports cellular energy, metabolism and repair / Needle-free, once a day
- Ingredients: NAD+
- Intake: productId UHJvZHVjdDoxNzY=

### Shared: Peptides (only when the client confirms them)
- Card titles: [Peptide name: pending client], six cards
- Prices: [Peptide price: pending client]
- No chips, descriptions or benefits until the client supplies them with intake links.

---

## Men's health (category page)

### Meta
- Title: Men's health | Restore Vitality Health
- Description: Seven prescription treatments for erectile dysfunction, as tablets or liposomal vials, from $96 per 4 weeks. Reviewed online by a licensed provider in your state.

### Compact banner
- Title: Men's **health**
- Line: Seven treatments for erectile dysfunction, prescribed online by a licensed provider, from $96 per 4 weeks.
- Media alt: none (decorative)

### Treatment rail
Seven Men's health cards (Treatment data). Safety line under the grid.

### Who it is for
- Heading: Erectile **dysfunction**
- Body: For men who want dependable help with erections, without a waiting room. Choose between tablets and liposomal vials, with one to four actives. Tell us about your health and any medications you take, and a licensed provider decides which option suits you, and at what dose. Every option is billed every 4 weeks, and you can cancel at any time.

### Quiz entry row
- **Not sure which one? Take the two-question quiz**

### FAQ
- Heading: Men's health **questions**
- Questions:
  - **What is the difference between a pill and a liposomal vial?** Both are taken by mouth when you need them. A pill is a tablet. A liposomal vial is a liquid in which the actives are carried in a fine lipid layer. Your provider can help you choose.
  - **Why do some treatments have more than one active?** Each active works in its own way, and some formulas combine two, three or four of them. Your provider looks at your health history and other medications before recommending one.
  - **Do I need a prescription?** Yes. Every treatment here is a compounded prescription medication. A licensed provider reviews your intake and decides whether it is right for you.
  - **What does it cost?** From $96 to $119 every 4 weeks, depending on the treatment. You see the price before you start.

### Closing CTA band
Default.

---

## Women's health (category page)

### Meta
- Title: Women's health | Restore Vitality Health
- Description: Menopause care online: estradiol cream, patch or tablet with progesterone, or a non-hormonal option. $237 per 12 weeks, reviewed by a licensed provider.

### Compact banner
- Title: Women's **health**
- Line: Menopause care with hormone and non-hormonal options, prescribed online, at $237 per 12 weeks.
- Media alt: none (decorative)

### Treatment rail
Four Women's health cards (Treatment data). Safety line under the grid.

### Who it is for
- Heading: Menopause **care**
- Body: For women in menopause who want relief from symptoms such as hot flashes, broken sleep and mood swings. Hormone therapy pairs estradiol, as a cream, a patch or a tablet, with progesterone. If hormones are not for you, there is a non-hormonal tablet. A licensed provider reviews your history and decides with you what fits. Every option is $237, billed every 12 weeks.

### Quiz entry row
- **Not sure which one? Take the two-question quiz**

### FAQ
- Heading: Women's health **questions**
- Questions:
  - **How do I choose between cream, patch and tablet?** They contain the same hormones in different forms. The cream is applied once a day, the patch is changed twice a week and the tablet is taken once a day. Your provider helps you decide.
  - **Is there an option without hormones?** Yes. Oral paroxetine (or desvenlafaxine) is a non-hormonal tablet taken once a day.
  - **Why is it billed every 12 weeks?** The menopause program is priced in 12-week periods, so you are billed and resupplied less often. The price is $237 for each period.
  - **Do I need a prescription?** Yes. A licensed provider reviews your intake and decides whether a treatment is right for you.

### Closing CTA band
Default.

---

## Shared treatments (category page)

### Meta
- Title: Shared treatments | Restore Vitality Health
- Description: Medical weight loss, GLP-1 microdosing and longevity treatments for men and women, from $145 per 4 weeks. Prescribed online by a licensed provider.

### Compact banner
- Title: **Shared** treatments
- Line: Weight loss, GLP-1 microdosing and longevity, for men and women alike, from $145 per 4 weeks.
- Media alt: none (decorative)

### Treatment rail
Ten Shared cards (Treatment data), grouped by program with the program name as a small label above each group: Medical weight loss / GLP-1 microdosing / Longevity. Safety line under the grid.

### Who it is for
Three Margaux intros, one per program:
- Heading: Medical **weight loss**
  Body: For adults who want a medical approach to losing weight, with a provider who adjusts the plan with them. Choose semaglutide as a daily tablet or a weekly injection, or tirzepatide as a weekly injection. Your provider reviews your health history and sets your dose. From $249 every 4 weeks.
- Heading: GLP-1 **microdosing**
  Body: For people who want steady, gentle progress rather than fast change. Semaglutide or tirzepatide at a lower dose, once a week, set by your provider and adjusted to your goals. Both options are $179 every 4 weeks.
- Heading: **Longevity**
  Body: For adults who feel well and want to keep their energy, focus and recovery as the years go on. Choose NAD+ as an injection, a nasal spray or a liposomal taken by mouth, sermorelin taken before bed, or a weekly B12 injection. From $145 every 4 weeks.
- Heading (only when the client confirms them): **Peptides**
  Body: [Peptide names: pending client]. [Peptide prices: pending client].

### Quiz entry row
- **Not sure which one? Take the two-question quiz**

### FAQ
- Heading: Shared treatment **questions**
- Questions:
  - **What is the difference between the weight loss program and microdosing?** Both use semaglutide or tirzepatide. Microdosing uses a lower dose for slower, gentler progress, and costs $179 every 4 weeks. The full program starts at $249.
  - **Do I have to inject?** Not always. Semaglutide comes as a daily tablet, and NAD+ comes as a nasal spray or a liposomal taken by mouth. Injections come with written and video instructions.
  - **Can I combine treatments?** Some patients add the B12 injection to a weight-management plan. Whether two treatments can be combined is your provider's decision.
  - **Do I need a prescription?** Yes. A licensed provider reviews your intake and decides whether a treatment is right for you.

### Closing CTA band
Default.

---

## Treatment detail template
One page per product. The product's own copy is in Treatment data.

### Meta (pattern)
- Title: {Product name} | Restore Vitality Health
- Description: {Card description} {Price}. Prescribed online by a licensed provider in your state.
  Example: Daily Boost Pill | Restore Vitality Health / Tadalafil in one simple tablet, taken when you need it. $112 per 4 weeks. Prescribed online by a licensed provider in your state.

### Info column
- H1: {Product name}
- Chips: {format} / {frequency}
- Price: {price} per {4 or 12} weeks
- Paragraph: {Page paragraph}
- Button: Start your consult (to the product's intake link)
- Line under the button: You are charged only when you complete your intake, and refunded in full if a provider finds the treatment is not right for you.
- Safety line (sitewide)
- Ingredients label: Ingredients
- Media alt: none (decorative vein crop)

### Benefits band
- Heading: What it **is for**
- List: the product's three benefits, each as one row with a hairline.
- Note under the list: Results are not guaranteed and vary from person to person.

### Safety information block
- Heading: Safety **information**
- Body: This is a compounded medication. Compounded drug products are not FDA-approved, and the FDA does not evaluate them for safety, effectiveness or quality. They are prepared by licensed pharmacies that must meet state and federal quality standards. How to take it, and what to watch for, is set out in the medications safety information.
- Link: Read the full medications safety information

### FAQ
The FAQ of the product's category page.

### You may also consider
- Heading: You may **also consider**
- Three cards from the same program (or the same group when the program has fewer than four products).

### Closing CTA band
- Headline: Restored for **what's next**
- Line: Start your consult online. A licensed provider takes it from there.
- Button: Start your consult (to this product's intake link)

---

## How it works (page)

### Meta
- Title: How it works | Restore Vitality Health
- Description: Consult, labs if needed, your plan, delivery and follow-up, all online. See each step of care with Restore Vitality Health, from first answers to refills.

### Compact banner
- Title: How it **works**
- Line: Five steps, all online, with a licensed provider deciding at every point that matters.

### Steps
Card titles and step names as on Home. Long copy for this page:
1. **Consult**: Tell us **about you**
   Choose the program you are interested in and complete the online intake. It asks about your health, your history and any medications you take, so your provider has the full picture. A provider licensed in the state where you live reviews it. Depending on your needs, that happens by video, by phone or by secure message. You are charged for your first period when you complete the intake.
2. **Labs**: Labs, **if needed**
   Some treatments need lab results before a provider can prescribe them. If yours does, your provider will tell you what is needed. With your consent, existing records such as recent lab results can be added to your file, so you are not repeating tests you already have. Some plans include lab services; where an outside lab is used, it may bill separately.
3. **Plan**: Your **plan**
   Using their own professional judgment, your provider decides whether a prescription is right for you, which treatment and at what dose. Sometimes the answer is a different option, or a visit in person. If you are not a fit for medical reasons, you receive a full refund.
4. **Delivery**: Sent **to your door**
   Your prescription goes to one of our licensed partner pharmacies, which prepares it and ships it to you. You get updates by text or email as your order moves, and injections come with written and video instructions.
5. **Follow-up**: Ongoing **care**
   Your plan renews each billing period until you cancel, and you get refill reminders by text or email. Sign in to My portal to manage your account. To cancel, email support or use your account at least 72 hours before your next billing date.

### Timeline (vertical list at 390)
- Consult: online intake, reviewed by a licensed provider
- Labs: only if your treatment needs them
- Plan: your provider decides what fits
- Delivery: filled by a licensed pharmacy, shipped to you
- Follow-up: refill reminders and support in My portal

### FAQ
- Heading: Questions about **the process**
- Questions (from the FAQ page): How do I start? / Who is my provider? / Will I need a video visit? / What if I am not a fit? / How do I cancel?

### Closing CTA band
Default.

---

## Pricing (page)

### Meta
- Title: Pricing | Restore Vitality Health
- Description: Every Restore Vitality Health price in one place, from $96 per 4 weeks. One price per billing period covers your provider review, medication if prescribed, and support.

### Compact banner
- Title: **Pricing**
- Line: One price for each billing period, shown before you start, for every program we offer.

### Program cards
The three cards from the Home pricing tease (Men's health, Women's health, Shared), with each card listing its programs and price ranges:
- Men's health: Erectile dysfunction, $96 to $119 per 4 weeks
- Women's health: Menopause hormone therapy, $237 per 12 weeks. Non-hormonal option, $237 per 12 weeks
- Shared: Medical weight loss, $249 to $339 per 4 weeks. GLP-1 microdosing, $179 per 4 weeks. Longevity, $145 to $229 per 4 weeks
- "Every plan includes" list as on Home.

### What is included
- Heading: What your price **covers**
- Body: Your price is one bundled amount for each billing period. It covers a review by a provider licensed in your state, your medication if it is prescribed, and online support. Depending on your plan and medical eligibility, it may also include follow-up consultations, care coordination, lab services and access to a 24/7 patient support line.
- Not included list:
  - Shipping and processing fees, which are shown before you complete your order
  - Services from outside companies, such as a separate lab, which may bill you directly
  - Insurance billing: our plans are paid privately

### How billing works
- Heading: How billing **works**
- Four short rows:
  - **When you are charged**: when you complete your intake, for your first billing period.
  - **Renewal**: your plan renews automatically every 4 or 12 weeks, at the price shown when you enrolled, until you cancel.
  - **Cancelling**: at any time, by email or in your account, at least 72 hours before your next billing date.
  - **Refunds**: a full refund if a provider finds you are not a fit for medical reasons, or if you cancel within 72 hours and have not received any services. Prescription medications cannot be returned once ordered.

### Compare programs
- Heading: Compare **programs**
- Table columns: Program / Group / Forms / Billed every / From
- Rows:
  - Erectile dysfunction / Men's health / Tablet, liposomal vial / 4 weeks / $96
  - Menopause care / Women's health / Cream, patch, tablet / 12 weeks / $237
  - Medical weight loss / Shared / Tablet, weekly injection / 4 weeks / $249
  - GLP-1 microdosing / Shared / Weekly injection / 4 weeks / $179
  - Longevity / Shared / Injection, nasal spray, liposomal / 4 weeks / $145
- Row link (last cell on desktop, button on mobile): See treatments
- Caption (screen readers): Restore Vitality Health programs compared by group, forms, billing period and starting price

### FAQ
- Heading: Billing **questions**
- Questions: the Billing tab of the FAQ page.

### Closing CTA band
Default.

---

## About (page)

### Meta
- Title: About | Restore Vitality Health
- Description: Restore Vitality Health is an independent telehealth brand from Texas offering prescription care for midlife, through licensed providers and licensed pharmacies.

### Compact banner
- Title: About **us**
- Line: An independent telehealth brand from Texas, built for adults in midlife who feel well and want to stay that way.

### Who we are
- Heading: Lived **well**
- Body: Restore Vitality Health opened in October 2026, started in Texas by [Founder name] and [Partner name]. We built it for men and women in midlife who are healthy, active and ready for what comes next, and who want straightforward access to modern prescription care. That means clear prices, plain language, and a licensed provider making every medical decision.

### Clinical standards
- Heading: Clinical **standards**
- Body: We are not a medical practice ourselves, and we never make treatment decisions. Care is provided through OpenLoop Healthcare Partners and its affiliated medical groups, whose providers are licensed in the state where you live. Your provider may be a physician, a nurse practitioner or a physician assistant, and decides in their own professional judgment whether to prescribe. Prescriptions are filled by licensed partner pharmacies: Red Rock Compounding Pharmacy, Health Warehouse, Precision Medicine and Triad Rx.

### Privacy
- Heading: Your **privacy**
- Body: [HIPAA wording: pending client]. What you share in your intake goes to your provider and the pharmacy filling your prescription so they can care for you. We do not sell your personal information. Our website forms, like the callback request, are kept apart from your medical intake, so please keep health details for your consult.
- Link: Read our privacy policy

### Clinical team
Held until the client names real people (spec). Copy for when they do:
- Heading: The people **behind it**
- Cards:
  - [Founder name], [Founder role: pending client]. [Founder bio: pending client]
  - [Partner name], [Partner role: pending client]. [Partner bio: pending client]
  - [Clinician name], [Clinician credentials: pending client]. [Clinician bio: pending client]
- Portrait alt pattern: Portrait of {name}, {role}

### Closing CTA band
Default.

---

## FAQ (page)

### Meta
- Title: FAQ | Restore Vitality Health
- Description: Answers about prescriptions, providers, compounded medications, billing, cancelling, refunds and privacy at Restore Vitality Health.

### Compact banner
- Title: **Questions**, answered
- Line: If yours is not here, email support@rx.restorevitality.health and we will help.

### FAQ
- Tabs: Getting started / Prescriptions and safety / Billing / Privacy
- Open and close labels for screen readers: Show answer / Hide answer

**Getting started**
- **Who is Restore Vitality Health for?** Adults in midlife, men and women, who want prescription care for sexual health, menopause, weight or healthy aging, handled online. You must be at least 18 and live in the United States.
- **Where do you offer care?** In all 50 states and Washington DC. Some medications are not available in every state, and the intake tells you if that affects you.
- **How do I start?** Choose a program, or take the two-question quiz if you are not sure, then complete the online intake for the treatment you want.
- **Will I need a video visit?** Not always. Depending on your needs, your provider may review your intake by message, or ask to speak by phone or video.

"How quickly will a provider review my intake?" is left out until the client gives a review time (Questions for the client, 8).

**Prescriptions and safety**
- **Who is my provider?** A provider licensed in your state, who may be a physician, a nurse practitioner or a physician assistant, working with OpenLoop Healthcare Partners and its affiliated medical groups.
- **What are compounded medications?** Medications prepared by a licensed pharmacy for an individual patient. They are not FDA-approved, and the FDA does not review them for safety, effectiveness or quality. Compounding pharmacies are licensed and must follow state and federal rules.
- **What if I am not a fit?** Your provider may suggest a different option or a visit in person. If you are not a fit for medical reasons, you receive a full refund.
- **How will my medication arrive?** A licensed partner pharmacy prepares it and ships it to you, with updates by text or email.
- **Are results guaranteed?** No. Results vary from person to person, and no treatment can promise an outcome.

**Billing**
- **How much does it cost?** From $96 every 4 weeks, depending on the treatment. Every price is on our Pricing page and shown again before you pay.
- **When am I charged?** When you complete your intake, for your first billing period. After that your plan renews automatically until you cancel.
- **How do I cancel?** Email support@rx.restorevitality.health or use your account, at least 72 hours before your next billing date. You keep your service until the end of the period you have paid for.
- **Can I get a refund?** Yes, in full, if a provider finds you are not a fit for medical reasons, or if you cancel within 72 hours of signing up and have not received any services. Medications cannot be returned once ordered.
- **Do you take insurance?** Our plans are paid privately, so insurance is not billed for them. Keep your existing coverage for everything else.

**Privacy**
- **Is my information private?** [HIPAA wording: pending client]. Your intake information is shared with your provider and pharmacy so they can care for you, and we do not sell your personal information.
- **Does the quiz save my answers?** No. The quiz only points you to a program. Nothing you choose is stored or sent.
- **How do I manage cookies?** Use Cookie settings in the footer at any time. You can also opt out of non-essential data sharing on our Do Not Sell page.

### Closing CTA band
Default.

---

## Contact (page)

### Meta
- Title: Contact | Restore Vitality Health
- Description: Email support@rx.restorevitality.health or request a callback. Live customer service Monday to Saturday, 9am to 6pm Central.

### Glass panel (left)
- Heading: Talk to **us**
- Line: Questions about a program, your order or your account. We are glad to help.
- Email label: Email
- Email: support@rx.restorevitality.health
- Phone label: Phone
- Phone: [Phone number]
- Hours label: Live customer service
- Hours: Monday to Saturday, 9am to 6pm Central
- Line: Already a patient? Sign in to My portal.
- Media alt: none (decorative)

### Callback form (right)
- Heading: Request a **callback**
- Intro: Leave your number and a good time to call, and a member of our team will call you during service hours.
- Fields:
  - Name (required)
  - Email (required)
  - Phone (required). Hint: US number, with area code
  - Best time to call. Options: Morning (9am to 12pm Central) / Afternoon (12pm to 3pm Central) / Late afternoon (3pm to 6pm Central)
  - Message (optional). Hint: Please do not include health details here. Your provider will ask about those in your consult.
- Consent checkbox: I agree to be contacted by phone or email about my request.
- Button: Request a callback
- Success (only if the endpoint answers): Thank you. We have your request and will call you during service hours.
- Error: Form messages (sitewide)
- Build note: the form sends to [Notification email].

### Closing CTA band
Default.

---

## Quiz (page)

### Meta
- Title: Find your program | Restore Vitality Health
- Description: Two short questions point you to the Restore Vitality Health program that fits. Nothing you choose is saved or sent.

### Intro screen
- Heading: Find your **program**
- Line: Two short questions. Nothing you choose is saved or sent: this only points you to the right program, and a licensed provider makes the medical decisions.
- Button: Start
- Progress label (screen readers): Question {n} of 2

### Question 1
- Question: What would you **like help with?**
- Answers:
  - Erectile dysfunction (to Result: Erectile dysfunction)
  - Menopause symptoms (to Question 2: Menopause)
  - Weight (to Question 2: Weight)
  - Energy and healthy aging (to Result: Longevity)
  - I am not sure yet (to Result: Not sure)

### Question 2: Menopause
- Question: Would you consider **hormone therapy?**
- Answers:
  - Yes, hormone therapy (to Result: Menopause care, hormone options highlighted)
  - I would rather avoid hormones (to Result: Menopause care, non-hormonal option highlighted)
  - Not sure, I would like advice (to Result: Menopause care)

### Question 2: Weight
- Question: What pace **suits you?**
- Answers:
  - A full program, with my provider setting the dose (to Result: Medical weight loss)
  - A lower dose, for steady and gentle progress (to Result: GLP-1 microdosing)
  - Not sure, I would like advice (to Result: Medical weight loss)

### Navigation
- Back: Back
- Restart: Start again

### Results
Each result: program name, "from" price, one paragraph, gold pill, text link.
- **Erectile dysfunction**. From $96 per 4 weeks.
  Seven treatments, as tablets or liposomal vials, with one to four actives. Your provider reviews your history and suggests the one that fits.
  Button: See the treatments (Men's health). Link: Start again
- **Menopause care**. $237 per 12 weeks.
  Estradiol as a cream, patch or tablet with progesterone, or a non-hormonal tablet. Your provider helps you choose.
  Button: See the treatments (Women's health). Link: Start again
- **Medical weight loss**. From $249 per 4 weeks.
  Semaglutide as a daily tablet or weekly injection, or tirzepatide as a weekly injection, with your dose set by your provider.
  Button: See the treatments (Shared, weight loss). Link: Start again
- **GLP-1 microdosing**. $179 per 4 weeks.
  A lower weekly dose of semaglutide or tirzepatide, for steady and gentle progress.
  Button: See the treatments (Shared, microdosing). Link: Start again
- **Longevity**. From $145 per 4 weeks.
  NAD+ as an injection, nasal spray or liposomal, sermorelin, or a weekly B12 injection, for energy, focus and recovery.
  Button: See the treatments (Shared, longevity). Link: Start again
- **Not sure yet**.
  That is fine. Browse every program and price in one place, or ask us and we will point you in the right direction.
  Button: See all prices (Pricing). Link: Contact us

Under every result: A licensed provider makes the final decision after your consult.

---

## Resources index and article

### Meta (index)
- Title: Resources | Restore Vitality Health
- Description: Plain-language notes on midlife health, our programs and new treatments from Restore Vitality Health.

### Index
- H1: **Resources**
- Standfirst: Plain-language notes on midlife health, our programs and new treatments as they arrive.
- Empty state (until articles exist): Our first articles are on the way. Sign up below and we will let you know when they are published.
- Newsletter: as in the Home resources rail.
- Category chip on cards: {category}
- Card link: Read the article

### Article template
- Meta title: {Article title} | Restore Vitality Health
- Meta description: {Standfirst, up to 155 characters}
- Labels: Published {date} / {n} min read
- Footer of the article: This article is for general information and is not medical advice. Talk to a licensed provider about your own health.
- Next link: Next article
- Back link: All resources

---

## Legal pages
The client's text is placed word for word from assets/legal/existing-site-legal.md, between the ```text fences of each section. Nothing is rewritten. The build copies it from that file rather than from this one, so nothing is lost in a retyping. The site's header, footer and safety line wrap each page as usual.

| Page | URL | H1 (client's) | Source lines | Meta description |
|---|---|---|---|---|
| Privacy policy | /privacy | Privacy Policy | 17 to 191 | How Restore Vitality Health collects, uses and protects information when you use this website. |
| Terms of service | /terms | Terms & Conditions | 203 to 533 | The terms that govern your use of the Restore Vitality Health website and services. |
| Medications safety information | /medications-safety-information | Medications Safety Information | 545 to 1609 | Safety information for the compounded medications prescribed through Restore Vitality Health. |
| Telehealth consent | /telehealth-and-medical-info | Telehealth and Medical Information | 1621 to 1891 | Consent to telehealth, treatment, communications and use of your medical information. |
| Do not sell or share | /do-not-sell | Do Not Sell or Share My Personal Information | 1903 to 1938 | How to opt out of the sale or sharing of your personal information. |

- Meta title pattern: {H1} | Restore Vitality Health
- The client's text already starts with the H1; the build uses that line as the page's H1 and does not repeat it.
- "Opt-Out Now" on /do-not-sell opens Cookie settings.
- The client's text contains 5 dashes (em or en). Per Varun's note they stay as written; see Notes for Varun.

---

## 404

### Meta
- Title: Page not found | Restore Vitality Health
- Description: This page has moved or no longer exists.

### Content
- Headline: This page has **moved on**
- Line: The link may be old, or the address mistyped. Everything else is where you left it.
- Button: Back to home
- Text link: Find your program

---

## Questions for the client
For Varun to forward. Placeholder items first, as he asked, then everything else the copy had to write around.

### Placeholders in the copy
1. **[Founder name]** and **[Partner name]**, with roles, short bios and portraits (About: Who we are, Clinical team).
2. **[Clinician name]**, credentials and bio: is there a medical director or lead clinician we can name (About: Clinical team)?
3. **[Review: pending client]**, with initials, date and product: do you have real patient reviews or outcomes you have permission to publish (Home: Real results)?
4. **[Phone number]**: which number should appear on Contact and in the footer?
5. **[Notification email]**: which address should receive callback and contact form messages?
6. **[Peptide name: pending client]** and **[Peptide price: pending client]**: names, prices, formats, frequencies, descriptions and OpenLoop intake links for the six peptides (Shared treatments). Has OpenLoop confirmed its pharmacies can supply them?
7. **[HIPAA wording: pending client]**: the exact privacy statement you want in the credibility row, About and FAQ. Your terms say Restore Vitality Health is "not a Covered Entity under HIPAA" and that consultations run on "a secure platform that complies with the privacy and security standards" of HIPAA. A line like "Consults on a HIPAA-compliant platform" needs your and OpenLoop's approval.

### Other things the copy wrote around
8. **Review time**: how quickly does a provider usually review a new intake? The FAQ question waits for this, and a "we reply within" line for Contact and the footer waits for a support reply time.
9. **Men, Women, Shared**: we put ED under Men's health, menopause under Women's health, and weight loss, microdosing and longevity under Shared. Is that the grouping you want?
10. **Naming OpenLoop**: About and FAQ name OpenLoop Healthcare Partners and your four partner pharmacies, as your terms do. Are you happy to show them on the marketing pages?
11. **Founding facts**: we say Restore Vitality Health opened in October 2026 and was started in Texas. Correct?
12. **Benefit claims**: product benefits are your own lines from the current site (for example "Instant sexual readiness" on the home page, "Accelerated absorption rate"). Has a prescriber or OpenLoop's compliance team approved them? We used the program-page versions, which are slightly milder.
13. **Estradiol Tablet**: the home page lists "Supports gender-affirming therapy"; the menopause page lists "Supports hormone therapy". We used the second. Which do you want?
14. **Sermorelin frequency**: the card has no frequency. How often is it taken?
15. **Insurance**: your terms say prescription plans are paid privately, but the telehealth consent also authorizes insurance billing. Can we say "Our plans are paid privately"?
16. **Shipping**: are shipping and processing fees charged, and how much? Is packaging discreet? We say nothing about packaging yet.
17. **Labs**: which programs need lab work, and how do patients get it done (home kit, local lab)?
18. **Newsletter**: which provider, and how often will you send it?
19. **Spanish**: do OpenLoop's intake and patient portal run in Spanish? If not, the Spanish site should warn visitors before they reach an English intake. Who supplies Spanish legal text, and can you approve our Spanish versions of the footer disclaimers and the safety line? Can your team return callbacks in Spanish? Should real reviews be translated or shown as written?

## Notes for Varun
- **Button wording**: the spec has "Find your protocol". The client's own site, and every product page, says "program", so the copy says "Find your program" everywhere, sticky pill included. If you want "protocol", it is a find-and-replace on the button labels.
- **Hero**: I kept "Ready for the next adventure" (spec decision 1). The tagline closes the site in the closing CTA band instead.
- **Legal text and em dashes**: the client's legal text has 5 em or en dashes. Anti-slop says rewrite even client copy, but your note for this run says legal text stays verbatim. I left them. Your call.
- **Client copy with em dashes outside legal**: two product descriptions (Quadruple Powered Liposomal and Cellular Recharge Injection) had em dashes. I rewrote those sentences without them. Nothing else in them changed.
- **Legal pages are pointers, not pasted text**: about 210,000 characters already sit verbatim in assets/legal/existing-site-legal.md. Retyping them here would only risk changing them, so this file gives the exact line ranges.
- **What I left out**: "Community Support", "Dynamic Platform", "Care Coaching" and the old "Take Our Quiz" step text from the template. Nothing in the client's material shows those services exist.
- **Spec working lines changed**: quiz row "two-minute quiz" became "two-question quiz", to match the quiz as written. The credibility statement "Prescribed by licensed providers" became "Reviewed by licensed providers", because a provider may decide not to prescribe.
