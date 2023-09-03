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
Caluculates the length needed to form an eye of a given diameter with a given diameter of rope. Includes a correction to account for the diameter of the rope.

#### Back splice
Calculates the length needed to make back splice in a given diameter of rope. Uses a value of 15 rope diameters [^1] and assumes 3 tucks. 

#### Chain splice
Calculates the length of rope needed to make a chain splice (attaches a rope to a chain link) in a given diameter of rope.

### Hollow braid ropes
#### Eye splice
Caluculates the length needed to form an eye of a given diameter with a given diameter of rope. Includes a correction to account for the diameter of the rope.

#### Chain splice
Calculates the length of rope needed to make a chain splice (attaches a rope to a chain link) in a given diameter of rope.

#### [Grog sling](https://www.animatedknots.com/grog-sling-knot)
Calculates the lengths needed to create a [grog sling](https://www.animatedknots.com/grog-sling-knot) of a given size with a given diameter of rope.

## Disclaimer
The numbers given by this tool are intended as a guide only. If you plan on using any of the splices described here for lifting or life support appliations, it is your responsibility to make sure you are tying everything correctly and following all relevant laws where you live. There are a lot of variables with splices, and making a mistake with the wrong ones can seriously impact the strength of the final splice. If you doubt your skills at all, you should not be trusting your, or other people's, lives to your splices.

[^1]: This value was reached through trial and error while tying back splices in 23 x 100ft lengths of 5/8" rope.