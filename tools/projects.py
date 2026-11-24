import sys; sys.path.insert(0, __file__.rsplit('/',1)[0])
from build_page import build
B='bilder/'; U='update-2027/'
build(dict(slug='steel-vehicle', title='Steel Vehicle', sub='Gravity racer from steel only',
  desc='Steel Vehicle: a gravity racer by Leonard Philp at San Francisco State University, every part made of steel, designed and welded in three weeks.',
  label='02 / Concept to working vehicle',
  tagline='A "Gravity Racer": an unpowered vehicle in which every part, from frame to axle, had to be made of steel.',
  cover=(B+'02-steel-cover.jpg','Steel gravity racer with blue wheels in front of the Golden Gate Bridge'),
  meta=[('Where','San Francisco State University'),('Duration','3 weeks'),('Methods','Sketching · CAD · Mock-ups · Welding'),('Software','Fusion')],
  sections=[
   dict(title='Brief', text=['Build a vehicle that travels as far and as straight as possible, using only steel as a material.']),
   dict(title='Sketching the gravity racer', images=[(B+'02-steel-sketch-variants.jpg','Variants on proportion & wheel position','Sketches of gravity racer variants with different proportions and wheel positions'),(B+'02-steel-sketch-form.jpg','Form exploration','Form exploration sketches of the steel vehicle'),(B+'02-steel-sketch-cog.jpg','Low centre of gravity, close wheels','Sketch showing a low centre of gravity and closely spaced wheels')]),
   dict(title='From drawing to welded frame', text=['Measured drawings, a CAD model and wood-and-dowel mock-ups tested proportions before any steel was cut; the frame was then welded in the SFSU workshop.'],
     images=[(U+'02-steel-vehicle/02-steel-measured-drawings.jpg','Measured drawings','Hand-drawn measured drawings of the frame'),(U+'02-steel-vehicle/02-steel-dimensioned-frame-drawing.jpg','Dimensioned frame drawing','Dimensioned technical drawing of the steel frame'),(U+'02-steel-vehicle/02-steel-frame-cad.jpg','Frame in CAD','CAD model of the steel frame in Fusion'),(U+'02-steel-vehicle/02-steel-wood-dowel-mockup.jpg','Wood & dowel mock-up','Wood and dowel mock-up of the vehicle'),(U+'02-steel-vehicle/02-steel-welded-frame.jpg','Welded steel frame','Welded steel frame of the gravity racer')]),
   dict(title='Render studies', images=[(B+'02-steel-renders.jpg','Render studies of the final frame','Render studies of the final steel frame')]),
   dict(title='From mock-up to welded frame', images=[(B+'02-steel-mockups.jpg','Wood & dowel mock-ups','Wood and dowel mock-ups'),(B+'02-steel-welding.jpg','Welding in the SFSU workshop','Welding the frame in the SFSU workshop'),(B+'02-steel-detail-1.jpg','Finished vehicle, detail','Detail of the finished steel vehicle'),(B+'02-steel-detail-2.jpg','Finished vehicle, detail','Second detail of the finished steel vehicle')]),
   dict(title='Outcome', text=['A rolling, fully welded steel vehicle, designed and built in three weeks. The project taught me to let material and manufacturing constraints drive form, and to test ideas quickly in cheap mock-ups before committing to metal.']),
  ], next=('03','Tableware for Construction Workers','../tableware/')))
build(dict(slug='tableware', title='Tableware for Construction Workers', sub='User-centred product design',
  desc='Tableware for Construction Workers: a robust, vacuum-formed lunch set in safety yellow by Leonard Philp, designed at San Francisco State University.',
  label='03 / User-centred product design',
  tagline='A robust lunch set designed around the day of a construction worker: durable, easy to carry and as tough-looking as the tools around it.',
  cover=(B+'03-tableware-cover.jpg','Safety-yellow lunch trays, bowl and cup on a workbench next to a hard hat'),
  meta=[('Where','San Francisco State University'),('Duration','4 weeks'),('Methods','Research · Sketching · CAD · Vacuum forming'),('Software','Fusion')],
  sections=[
   dict(title='Process', text=['The project started from a persona: Bob, a construction worker whose lunch break happens on the tailgate of a pick-up. Sketches tested stacking, grip and size; the final shapes were modelled in CAD, milled as wooden moulds, vacuum-formed and spray-finished in safety yellow.']),
   dict(title='Ideation & prototypes', images=[(B+'03-tableware-sketches.jpg','Sketches & mood','Sketches and mood board for the tableware'),(B+'03-tableware-cardboard.jpg','Cardboard prototypes','Cardboard prototypes of trays and bowls'),(B+'03-tableware-foam.jpg','Foam prototypes','Foam prototypes of the tableware')]),
   dict(title='CAD & manufacturing', images=[(B+'03-tableware-cad.jpg','CAD with dimensions','CAD model with dimensions'),(U+'03-tableware/03-tableware-cad-tray.jpg','CAD with dimensions (tray)','Dimensioned CAD drawing of the tray'),(U+'03-tableware/03-tableware-cad-bowl.jpg','CAD with dimensions (bowl)','Dimensioned CAD drawing of the bowl'),(U+'03-tableware/03-tableware-wooden-moulds.jpg','Wooden moulds','Milled wooden moulds for vacuum forming'),(B+'03-tableware-vacuum-forming.jpg','Vacuum forming','Vacuum forming plastic over a wooden mould'),(B+'03-tableware-spray.jpg','Spray finish','Spray finishing the parts in safety yellow')]),
  ], next=('04','Hybrid Yoga Box','../hybrid-yoga-box/')))
W='weitere-projekte/'; A='auto-skizzen/06-sketch-'
build(dict(slug='hybrid-yoga-box', title='Hybrid Yoga Box', sub='Cork, wood & sound',
  desc='Hybrid Yoga Box by Leonard Philp (HTW Berlin): a CNC-milled wooden yoga block in cork with a built-in Bluetooth speaker and a companion box.',
  label='04 / Product design', tagline='A dual-use yoga block that merges natural craftsmanship with technology.',
  cover=(B+'04-yoga-box-joined.jpg','Cork yoga block and companion box being joined by hand'),
  meta=[('Where','HTW Berlin'),('Duration','1 month'),('Materials','Wood · Cork · Electronics'),('Methods','CNC milling · Model making')],
  sections=[
   dict(title='Concept', text=['A precision CNC-milled wooden core wrapped in high-grip, sustainable cork houses an integrated Bluetooth speaker for immersive sound during practice. A companion box stores a water bottle, and a Velcro system snaps both units together for maximum stability.']),
   dict(title='Making & details', images=[(U+'04-yoga-box/04-yoga-milling-wooden-core.jpg','Milling the wooden core','CNC milling the wooden core of the yoga block'),(U+'04-yoga-box/04-yoga-cork-block-three-openings.jpg','Cork block with three openings','Cork yoga block with three speaker openings'),(B+'04-yoga-box-companion.jpg','Companion box','Cork companion box for a water bottle'),(B+'04-yoga-box-joined.jpg','Block & box joined','Yoga block and companion box joined with Velcro')]),
  ], next=('05','BRUSH_D','../brush-d/')))
build(dict(slug='brush-d', title='BRUSH_D', sub='Modular dish brush',
  desc='BRUSH_D by Leonard Philp: a modular dish brush with integrated soap tank, replaceable heads and a drying stand, designed at HTW Berlin with Berliner Besen und Bürsten.',
  label='05 / Product design', tagline='The modular dish brush: a kitchen accessory worth leaving out, with an integrated soap tank, replaceable heads and its own drying stand.',
  cover=(U+'05-brushd/05-brushd-kitchen-hero.jpg','Copper BRUSH_D dish brush in its stand next to a kitchen sink'),
  meta=[('Where','HTW Berlin, Prof. S. Feucht'),('Project','BBB, Berliner Besen und Bürsten'),('Duration','1.5 months · Summer 2026'),('Software','Rhino, Blender')],
  sections=[
   dict(title='Problem', text=['Dish brushes lie in the wet sink, collect food residue and start to smell, while plastic detergent bottles bring advertising into otherwise calm kitchens.']),
   dict(title='Sketching the form', images=[(B+'05-brushd-sketch-1.jpg','Grip, head & dispenser ideas','Sketches of grip, head and dispenser ideas'),(B+'05-brushd-sketch-2.jpg','Handle silhouettes','Sketches of handle silhouettes'),(B+'05-brushd-sketch-3.jpg','Modular heads & storage','Sketches of modular heads and storage'),(U+'05-brushd/05-brushd-sketch-4.jpg','Form sketch','Further form sketch of the brush')]),
   dict(title='Integrated soap dispenser', text=['A detergent tank in the handle replaces the plastic bottle. Round portholes show the fill level, and a button releases just the right amount of soap.'], images=[(B+'05-brushd-soap.jpg','','Handle with integrated soap tank and fill-level portholes')]),
   dict(title='Modular heads', text=['Individually replaceable brush heads snap into place, so the handle lasts and only the worn part is changed.'], images=[(B+'05-brushd-heads.jpg','','Replaceable brush heads')]),
   dict(title='Smart drying stand', text=['The stand holds the brush upside down, protects the bristles and lets water drain straight into the sink.'], images=[(B+'05-brushd-stand.jpg','','Brush standing upside down in its drying stand')]),
   dict(title='Three versions, one modular system', images=[(U+'05-brushd/05-brushd-three-versions.jpg','','Three versions of BRUSH_D in one modular system')]),
  ], next=('06','Nilu 27 & Sketch Gallery','../nilu-27/')))
sk=[('01','BMW 8 Series coupé, marker rendering','bmw-8er-coupe'),('02','Front detail study, marker','bmw-front-detail'),('03','Mercedes-Benz S-Class cabriolet, marker','mercedes-s-cabrio'),('04','Interior concept, marker','mercedes-interior'),('05','BMW X5 concept, marker','bmw-x5-concept'),('06','Coupé side view, pencil','bmw-coupe-pencil'),('07','Detail studies, pencil & colour','mercedes-pencil-details'),('08','Bentley Continental GT Speed study, marker','bentley-continental'),('09','Mercedes-Benz SUV, marker','mercedes-gle'),('10','Sedan side view, digital','mercedes-digital-side-red'),('11','Sports SUV, digital line sketch','digital-sketch-red-suv'),('12','Electric SUV, digital','mercedes-eqa-digital'),('13','Sports car rear view, digital','mercedes-rear-digital'),('14','Luxury sedan, digital','mercedes-sedan-digital'),('15','Front, rear & side views, digital','mercedes-views-digital'),('16','BMW concept, digital rendering','bmw-vision-digital')]
skimg=lambda r:[(f'{A}{n}-{f}.jpg',c,'Car sketch by Leonard Philp: '+c) for n,c,f in r]
build(dict(slug='nilu-27', title='Nilu 27 & Sketch Gallery', sub='Full-scale tape rendering & car sketches',
  desc='Nilu 27: a full-scale automotive tape rendering of a sports car side view, plus a gallery of car sketches in marker, pencil and digital by Leonard Philp.',
  label='06 / Automotive design techniques', tagline='"nilu 27", a sports car side view as full-scale tape rendering, built layer by layer on stretched paper: every surface, shadow and highlight is laid by hand with tape in different widths and tones, then refined line by line to capture the light and form of the car.',
  cover=('bilder/00-hero-nilu27-tape-rendering.jpg','Full-scale tape rendering of the sports car Nilu 27'),
  meta=[('Technique','Full-scale tape rendering'),('Team','Team of three, with Alp Ömer Özbek & Carl Schüring'),('Course','Rendering seminar, Prof. Gerhard Friedrich, Summer 2025'),('Duration','1 week')],
  sections=[
   dict(title='Side view', images=[(U+'06-nilu-27/06-nilu27-side-view-cutout.png','','Cut-out side view of the Nilu 27 tape rendering on black')]),
   dict(title='Sketch gallery', text=['Car sketches from recent years, drawn digitally and by hand: studies of proportion, stance, surfaces and light signatures. Media: digital, marker, pencil (Photoshop, Procreate).']),
   dict(title='Marker & pencil sketches', images=skimg(sk[:9])),
   dict(title='Digital sketches', images=skimg(sk[9:])),
  ], next=('07','Yellow Superpress','../yellow-superpress/')))
build(dict(slug='yellow-superpress', title='Yellow Superpress', sub='Lemon press for bars',
  desc='Yellow Superpress by Leonard Philp (HTW Berlin): a mechanical citrus press for professional bars that presses sideways, one-handed and without electricity.',
  label='07 / Product design', tagline='A mechanical citrus press for professional bars. Instead of pressing down, it presses sideways, so lemons are squeezed with much less force: one-handed and without electricity.',
  cover=(W+'07-superpress-cover.jpg','White model of the Yellow Superpress with a glass and two lemons'),
  meta=[('Where','HTW Berlin, Design Basics 3'),('Supervision','Prof. Franziska Schuh · Dipl.-Des. Peggy Truxa · Prof. Jan Vietze'),('Semester','Summer 2025'),('Methods','Sketching · CAD (Rhino) · Rendering · Model making')],
  sections=[
   dict(title='Concept', text=['The glass stands directly beneath the press for clean, fast work, and a small inlet holds a second glass for seeds and pulp. Sketches explored containers, cones and stools; three CAD variants traced the form from a small table on legs to one continuous curved surface.']),
   dict(title='Ideation', images=[(W+'07-superpress-sketch-1.jpg','Early concepts','Early concept sketches of the lemon press'),(W+'07-superpress-sketch-2.jpg','Form exploration','Form exploration sketches')]),
   dict(title='CAD & rendering', images=[(W+'07-superpress-cad-variants.jpg','Variants in Rhino','Three CAD variants in Rhino'),(W+'07-superpress-render-detail.jpg','Curved tray with drainage holes','Render detail of the curved tray with drainage holes'),(W+'07-superpress-render-bar.jpg','In context on the bar counter','Rendering of the press on a bar counter')]),
   dict(title='Model', images=[(U+'07-superpress/07-superpress-model-cocktail-glass.jpg','Model with cocktail glass','Model of the press with a cocktail glass'),(U+'07-superpress/07-superpress-model-bar-counter.jpg','At the bar counter','Model on a bar counter'),(U+'07-superpress/07-superpress-model-kitchen.jpg','Kitchen','Model in a kitchen')]),
  ], next=('08','Perfect Connections','../perfect-connections/')))
build(dict(slug='perfect-connections', title='Perfect Connections', sub='Organic joint for beech rods',
  desc='Perfect Connections by Leonard Philp (HTW Berlin): a Grasshopper-generated, 3D-printed organic connector for beech dowels in versions for two and three rods.',
  label='08 / Form & process', tagline='A connector for beech dowels, generated in Grasshopper to wrap the dowels with only the material it needs. The result is an organic, grown-looking lattice, in versions for two and three dowels.',
  cover=(W+'08-connections-cover.jpg','3D-printed organic lattice joint connecting beech dowels'),
  meta=[('Where','HTW Berlin, Design Basics 3'),('Dowels','Beech, Ø 20 mm'),('Methods','Sketching · Grasshopper · 3D printing · Model making')],
  sections=[
   dict(title='Approach', images=[(W+'08-connections-sketches.jpg','Construction ideas, pencil','Pencil sketches of construction ideas'),(W+'08-connections-marker-sketch.jpg','Joint concepts, marker','Marker sketches of joint concepts'),(W+'08-connections-early-model.jpg','Early functional model','Early functional model of the joint')]),
   dict(title='Result', images=[(W+'08-connections-two-variants.jpg','Two-rod and three-rod variants','Two-rod and three-rod connector variants'),(W+'08-connections-detail-2-rods.jpg','Two-rod joint','Two-rod joint'),(W+'08-connections-detail-3-rods.jpg','Three-rod joint','Three-rod joint'),(W+'08-connections-detail-close.jpg','Organic lattice, close-up','Close-up of the organic lattice')]),
  ], next=('09','Masseo','../masseo/')))
M=U+'09-masseo/09-masseo-'
build(dict(slug='masseo', title='Masseo', sub='Bruxism add-on for in-ears',
  desc='Masseo by Leonard Philp: an add-on for wireless in-ears that turns a bruxism guard into a lifestyle product, designed at HTW Berlin with the Charité dental clinic.',
  label='09 / Design Project 2 · Charité', tagline='An add-on for wireless in-ears that turns a bruxism guard into a lifestyle product.',
  cover=(M+'cover-pad-docked.jpg','Masseo cheek pad docked to a wireless in-ear'),
  meta=[('Where','HTW Berlin, with Charité dental clinic'),('Supervision','Prof. Pelin Celik'),('Semester','Summer 2026'),('Methods','Research · Sketching · 3D modelling · Rendering')],
  sections=[
   dict(title='Brief', text=['A medical silicone pad on the cheek reads the masseter muscle via EMG and relaxes it with short bursts of heat and vibration. It draws power from the earbud through a flexible cable; at night a magnetic range-extender battery takes over, and an iOS app logs the clenching.']),
   dict(title='Concept', images=[(M+'cover-pad-docked.jpg','Cheek pad docked to the in-ear','Cheek pad docked to the in-ear'),(M+'wearing.jpg','Wearing Masseo','Person wearing Masseo'),(M+'night-mode-battery.jpg','Night mode with battery','Masseo in night mode with range-extender battery'),(M+'exploded-view.jpg','Exploded view: pad, heating foil, board, case','Exploded view of Masseo')]),
   dict(title='Form & fit', images=[(M+'form-studies.jpg','Form studies','Form studies of the cheek pad'),(M+'pad-position.jpg','Pad position on the masseter','Pad position on the masseter muscle')]),
  ], next=('10','Product Analysis: Detail Sander','../detail-sander/')))
S=U+'10-detail-sander/10-sander-'
build(dict(slug='detail-sander', title='Product Analysis: Detail Sander', sub='Repairability analysis',
  desc='Product analysis of a detail sander by Leonard Philp and Konstantin Weilinger (HTW Berlin): every part analysed for repairability, materials and manufacturing.',
  label='10 / Sustainable Design 2', tagline='Every part of a detail sander, analysed for repairability, materials and manufacturing.',
  cover=(S+'cover-board-detail.jpg','Findings laser-engraved into the frame of a presentation board'),
  meta=[('Where','HTW Berlin'),('Team','with Konstantin Weilinger'),('Course','Sustainable Design 2')],
  sections=[
   dict(title='Brief', text=['Together with Konstantin Weilinger, I took a detail sander apart and analysed every part for repairability, materials and manufacturing. The findings were laser-engraved into the frame of two presentation boards with a vacuum-formed inlay.']),
   dict(title='Boards', images=[(S+'cover-board-detail.jpg','Findings engraved into the frame','Findings laser-engraved into the board frame'),(S+'two-boards.jpg','Two boards with the disassembled sander','Two presentation boards with the disassembled sander'),(S+'vacuum-formed-inlay.jpg','Vacuum-formed inlay','Vacuum-formed inlay holding the sander parts')]),
  ], next=('01','Scorp.ion','../scorpion/')))
