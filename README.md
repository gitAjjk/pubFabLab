# pubFabLab
Here my **FreeCad** & **FabLab** experiences.  
Feel free to use this lifehacks and share your improvements & suggestions with me.

See [ajOffset.FCStd](https://github.com/gitAjjk/pubFabLab/blob/main/ajOffset.FCStd) for examples of dovetail-sliced polar patterns with pockets.

# [Freecad](https://www.freecad.org/)
Opensource replace for Fusion. Fullt parametric, python scripting (macro recording), construction history. I don't miss any features upto now, and it is still improving 😃!  
## Best practises:
  - For each piece: nest a 'body'(+sketch) in a 'part' and 'Transform' part for posioning.
  - Use (sub)shapebinders with care. (SSB are NOT intuitieve)
## **Kerf-offset** with macro '[ajOffset.FCMacro.py](https://github.com/gitAjjk/pubFabLab/blob/main/ajOffset.FCMacro.py)'
Creates user-set offset contour lines for all selected objects (including pockets!) to a TechDraw page.  
Usage:  
- Put ajOffset.FCMacro.py in you MACRO direcrory (menu > Edit > Preferences > Python > Macro > Macro path) 
- Select one ore more bodies/solids (try what works well).
- Macro-buttonbar > Macros ... > User Macros; Select this .py; Execute.
- Enter an offset. This is half the lasercutter kerf.
  - 0,17 for plywood
  - 0,2 for 2mm plexi
- In Model-tree, check generated TechdrawOffsetPage* and tmpOffset3D_*.
- Export to TechdrawOffsetPage*.dxf has somitimes lines removed. Use .svg or export manually. 
### ToDo with ajOffset.FCMacro.py :
  - Improve this manual ;-)
  - Export views in techdrawpage to .dxf doesn't work for all views.
  - Making offset with arc-corners with 2D approach (see macro code) doesn't work.
  - Auto cleanup afterwards, if necessary.
  - Test/debug other shapes.

# [InkScape](https://inkscape.org/)
Use for check & Post processing.  
Be aware that lines are double. There is a set of complex paths and a set of a lot of small paths.
- Select all
  - Ungroup, select parts & group
  - Select a small path, rclick > Select Same : ObjectType?   Delete, so only 'complex paths' remain  
  - Fill and Stroke [shift][ctrl][f] > Stroke Style > Width: hairline
- Take picture of material and use it as scaled background to arrange pieces to fit best  
- [ctrl][l] shows object-tree  
- Put text (CamBam_Stick) with a production-timestamp on every part (use duplicate [ctrl][d])
  - Adapt text-fonts to lines:
    - Select all, Menu > Extensions > Text > Hershey text
      - All fontst are single lined
- ! Beware of Double lines (also in hairline-fonts). For cutting face only is sufficient.
- File > Document properties
  - Resize to content
  - Checkboard
- Select all, Fill and Stroke [shift][ctrl][f] > Stroke Style > Width: 1 pixel
  - Don't use Hairline. Svg won't render fonts well. (A hairline can be a completely overlapping inner an outer strokes and will be cut twice.)
- **Kerf-offset** Can also be done with IS (See [InkScape Kerf offset EN.pdf](https://github.com/gitAjjk/pubFabLab/blob/main/InkScape%20Kerf%20offset%20EN%200.2.pdf))   

# Lasercutter
- Put 'Laser Cutting Masking Tape' at least on bottom. On top affects engraving  
- Remove stickerfilm and Leave cut pieces for one day degassing  
- Dont use 'Engrave' mode; it makes a face filled with lines and takes too much time  

## Speed / Power  
- carglass plexi 2mm. (protection film removed, LCM tape on bottom & top):  
	- 100 / 9  ±.1 mm deep: 'touched' OK  
	- 30 / 15   > 1mm  
	- 15 / 38  cut OK  
  - 15 / 35	OK	(quit slow cutting)
	- 350 / 10 brand 0,5 mm in (De speed is much lower in realtime; truncated?)  
	- 350 / 08 nothing  
		30/25 ±1 mm met smeltrand  
		30/10   
		40/10  
		50/10 ±.2? mm, geen smeltrand
  - Using protectionfilm, little cracks and a brim occur. Leave it for a while in a 70° C environment? 
- Birch Plywood 6mm
  - 14 / 70	OK
  - See fablab table  
