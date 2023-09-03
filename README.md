# rope-tools
A set of tools for performing various calculations related to splicing rope. Currently built to accept imperial dimensions, but I plan on adding suport for metric in the future.

## Current calculations
### General
#### Fid length
Calculates the short and full fid lengths for a given diameter of rope. The short length differs slightly depending on the diamter of the rope.
 - For ropes up to 1/2", the short length is 37.5% of the full length.
 - For ropes from 1/2" to 3/4", the short length is 30% of the full length.
 - For ropes larger than 3/4", the short length is 25% of the full length.

Additionally, the following table shows the full and short section lengths for [Sampson tubular fids](https://www.samsonrope.com/docs/default-source/splice-instructions/tools_required_for_splicing_web.pdf?sfvrsn=e2e345e0_2).

|Rope dia.|Full length|Short section|
|---------|-----------|-------------|
|1/4"	  |5-1/2"	  |2-1/16"		|
|5/16"	  |6-3/4"	  |2-1/2"		|
|3/8"	  |7-3/4"	  |2-7/8"		|
|7/16"	  |9-1/2"	  |3-9/16"		|
|1/2"	  |11"	      |4-1/8"		|
|9/16"	  |12-1/4"	  |3-5/8"		|
|5/8"	  |14"	      |4-1/8"		|
|3/4"	  |16"	      |4-3/4"		|
|7/8"	  |19"	      |4-3/4"		|
|1"	      |21"	      |5-1/4"		|


### Twisted ropes
#### [Eye splice](https://www.animatedknots.com/eye-splice-knot)
Caluculates the length needed to form an eye of a given diameter with a given diameter of rope. Includes a correction to account for the diameter of the rope.

#### [Back splice](https://www.animatedknots.com/back-splice-knot)
Calculates the length needed to make back splice in a given diameter of rope. Uses a value of 15 rope diameters [^1] and assumes 3 tucks. 

#### [Chain splice](https://www.animatedknots.com/chain-splice-knot)
Calculates the length of rope needed to make a chain splice (attaches a rope to a chain link) in a given diameter of rope.

### Hollow braid ropes
#### [Eye splice](https://www.animatedknots.com/brummel-eye-splice-knot)
Caluculates the length needed to form an eye of a given diameter with a given diameter of rope. Includes a correction to account for the diameter of the rope. Uses the McDonald locked brummel method, requiring only one end of the rope.

#### [Chain splice](https://www.animatedknots.com/brummel-eye-splice-knot)
Calculates the length of rope needed to make a chain splice (attaches a rope to a chain link) in a given diameter of rope. In hollow braid, this is really just a varient of the eye splice with a different methodfor calculating the length needed for the eye.

#### [Grog sling](https://www.animatedknots.com/grog-sling-knot)
Calculates the lengths needed to create a [grog sling](https://www.animatedknots.com/grog-sling-knot) of a given size with a given diameter of rope.

## Disclaimer
The numbers given by this tool are intended as a guide only. If you plan on using any of the splices described here for lifting or life support appliations, it is your responsibility to make sure you are tying everything correctly and following all relevant laws where you live. There are a lot of variables with splices, and making a mistake with the wrong ones can seriously impact the strength of the final splice. If you doubt your skills at all, you should not be trusting your, or other people's, lives to your splices.

[^1]: This value was reached through trial and error while tying back splices in 23 x 100ft lengths of 5/8" rope.