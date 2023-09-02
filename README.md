# rope-tools
A set of tools for performing various calculations related to splicing rope. Currently built to accept imperial dimensions, but I plan on adding suport for metric in the future.

## Current calculations
### General
#### Fid length
Calculates the full fid length and the short section length for a given diameter of rope. The short section length differs slightly depending on the diamter of the rope.
 - For ropes up to 1/2", the short section is 37.5% of the full length.
 - For ropes from 1/2" to 3/4", the short section is 30% of the full length.
 - For ropes larger than 3/4", the short section is 25% of the full length.

Short section length is based off the Sampson tubular fid sizes.

### Twisted ropes
#### Eye splice
Caluculates the length needed to form an eye of a given diameter with a given diameter of rope.

#### Back splice
Calculates the length needed to make back splice in a given diameter of rope. Uses a value of 15 rope diameters [^1] and assumes 3 tucks. 

#### Chain splice
Calculates the length of rope needed to make a chain splice (attaches a rope to a chain link) in a given diameter of rope.

### Hollow braid ropes
#### Eye splice
Caluculates the length needed to form an eye of a given diameter with a given diameter of rope.

#### Chain splice
Calculates the length of rope needed to make a chain splice (attaches a rope to a chain link) in a given diameter of rope.

## Disclaimer
The numbers given by this tool are intended as a guide only. If you plan on using any of the splices described here for lifting or life support appliations, PLEASE DO YOUR OWN RESEARCH on how to properly tie these splices and how much length you really need.

[^1]: This value was reached through trial and error while tying back splices in 23 x 100ft lengths of 5/8" rope.