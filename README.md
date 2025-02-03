# pubFabLab
Here my **FreeCad** & **FabLab** experiences.  
Feel free to use this lifehacks and share your improvements & suggestions with me.

See [ajOffset.FCStd](https://github.com/gitAjjk/pubFabLab/blob/main/ajOffset.FCStd) for examples of dovetail-sliced polar patterns with pockets.

# [Freecad](https://www.freecad.org/)
Opensource replace for Fusion. Fullt parametric, python scripting, construction history. I don't miss any features upto now, and it is still improving 😃!  
## Best practises:
  - For each piece: nest a 'body'(+sketch) in a 'part' and 'Transform' part for posioning.
  - Try macrorecording for making your own extra nifty workflows.
  - 
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
- Export to TechdrawOffsetPage*.dxf doesn't work well. Perform export manually. 
### ToDo with ajOffset.FCMacro.py :
  - Improve this manual ;-)
  - Export views in techdrawpage to .dxf doesn't work for all views.
  - Making offset with arc-corners with 2D approach (see macro code) doesn't work.
  - Auto cleanup afterwards, if necessary.
  - Test/debug other shapes.

# [InkScape](https://inkscape.org/)
Use for check & Post processing.  
- Select all, Fill and Stroke [shift][ctrl][f] > Stroke Style > Width: hairline
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
  - Don't use Hairline. Svg won't render fonts well. A hairline can be a completely overlapping inner an outer strokes and will be cut twice.

## **Kerf-offset**  
Can also be done with IS (See [InkScape Kerf offset EN.pdf](https://github.com/gitAjjk/pubFabLab/blob/main/InkScape%20Kerf%20offset%20EN%200.2.pdf))  

# Lasercutter
- Put stickerfilm at least on bottom. On top affects engraving  
- Remove stickerfilm and Leave cut pieces for one day degassing  
- 'Engrave' mode makes face be filled with lines  

## Speed / Power  
- carglass plexi 2mm. met papier erop:  
	- 350 / 9 ±.1 mm diep (zonder folie) touch OK  
	- 30 / 15   > 1mm  
	- 15 / 45  cut OK  
  - 15 / 35	OK	speed 15 is wel traag bij cutten  
	- 350 / 10 brand 0,5 mm in (De speed lijkt lang niet zo hoog; waarsch truncate de machine het)  
	- 350 / 08 niks  
		30/25 ±1 mm met smeltrand  
		30/10   
		40/10  
		50/10 ±.2? mm, geen smeltrand  
Birch Plywood
