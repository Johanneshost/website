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
  ], next=('04','Hybrid Yoga Box','../../#work')))
