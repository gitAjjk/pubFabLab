# pubFabLab
Here my **FreeCad** & **FabLab** experiences.  
Feel free to use this lifehacks and share your improvements & suggestions with me.

See [ajOffset.FCStd](https://github.com/gitAjjk/pubFabLab/blob/main/ajOffset.FCStd) for examples of dovetail-sliced polar patterns with pockets.

# [Freecad](https://www.freecad.org/)
Opensource replace for Fusion. Fullt parametric, python scripting, construction history. I don't miss any features upto now, and it is still improving 😃!  
## Best practises:
  - For each piece: nest a 'body'(+sketch) in a 'part' and 'Transform' part for posioning.
  - Try macrorecording for making your own extra nifty workflows.
## **Kerf-offset** with macro '[ajOffset.FCMacro.py](https://github.com/gitAjjk/pubFabLab/blob/main/ajOffset.FCMacro.py)'
Creates user-set offset contour lines for all selected objects (including pockets!) to a TechDraw page.  
Usage:  
- Put ajOffset.FCMacro.py in you MACRO direcrory (menu > Edit > Preferences > Python > Macro > Macro path) 
- Select one ore more bodies/solids (try what works well).
- Macro-buttonbar > Macros ... > User Macros; Select this .py; Execute.
- Enter an offset. This is half the lasercutter kerf.
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
- [ctrl][l] shows object-tree  
- Put text (CamBam_Stick) with a production-timestamp on every part (use duplicate [ctrl][d])
  - Adapt text-fonts to lines:
    - Select all, Menu > Extensions > Text > Hershey text
      - All fontst are single lined
- Beware of Double lines (also in hairline-fonts).
- Select all, Fill and Stroke [shift][ctrl][f] > Stroke Style > Width: 1 pixel
  - Don't use Hairline. Svg won't render fonts well. A hairline can be a completely overlapping inner an outer strokes and will be cut twice.

## **Kerf-offset** 
Can also be done with IS (See [InkScape Kerf offset EN.pdf](https://github.com/gitAjjk/pubFabLab/blob/main/InkScape%20Kerf%20offset%20EN%200.2.pdf))
