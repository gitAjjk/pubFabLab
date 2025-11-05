In FreeCad, create dynamic techdraw with all lines moved 1/2 kerf (= thickness laserbeam). Outerlines are moved to larger outside, inner lines to smaller inside.   
Put **ajOffset.FCMacro.py** in e.g. C:/Users/\<username\>/Dropbox/Freecad/MACROS/  
Usage:  
- select objects  
- menu > macro > Macros... > ajOffset.FCMacro.py
  - First time: set "User Macros Location" in "Execute Macro" window.
- Set kerf

Beware the kerf offset lines don't cross other lines. This happens when two lines have less than 'kerf' distance in sketch.  
