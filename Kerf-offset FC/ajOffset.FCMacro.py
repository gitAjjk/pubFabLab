# -*- coding: utf-8 -*-
__Name__ = 'ajOffset.FCMacro.py'
__Comment__ = 'Creates offset contour lines for all selected objects, including pockets, to a TechDraw page'
__Author__ = 'AjjKoene'
__Version__ = '0.1.0'
__Date__ = '2024-11-06'
__License__ = 'LGPL-3.0-or-later'
__Web__ = 'https://TODO'
__Wiki__ = 'https://TODO'
__Icon__ = 'ajOffset.FCMacro.svg'
__Help__ = 'TODO'
__Status__ = 'PleaseImprove'
__Requires__ = 'FreeCAD >= v0.18'
__Communication__ = 'TODO'
__Files__ = 'ajOffset.FCMacro.py,ajOffset.FCMacro.svg'

#Debug with vsc
""" import ptvsd
print("Waiting for debugger attach")
ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
ptvsd.wait_for_attach()
 """
# TODO: 
#   auto orthogonal view ?
#   group tmp's in a part and delete afterwards?
#       Or set all invisible (visible clones are confusing)
#   Righty angle, otherwise change viewin WB techdraw?? Doubleclick view OR Adjust view > Data pane > Projection > Direction 
#   Rename view
#v   Keep circles, now small segments
#v       coarseview = false; can be toggled
#   face color
#v   clones en tmpOffsets hidden 

#Requester for kerf offset
from PySide2 import QtWidgets
def RequesterForOffset(default_value=0.2):
    # Prepare dialog
    dialog = QtWidgets.QInputDialog()
    dialog.setWindowTitle("Kerf offset")
    dialog.setLabelText("Enter OFFSET (= half kerf): ")
    dialog.setInputMode(QtWidgets.QInputDialog.DoubleInput)  # Stelt een numerieke invoer in
    dialog.setDoubleDecimals(2)  # Aantal decimalen voor de invoer
    dialog.setDoubleValue(default_value)  # Standaard ingevulde waarde instellen
    # Show dialog
    if dialog.exec_() == QtWidgets.QDialog.Accepted:
        input = dialog.doubleValue()
        return input
    else:
        return None

offset = RequesterForOffset(default_value=0.2)
kerf=2 * offset #if too large: .."null shape"??

import TechDraw
import FreeCAD
import FreeCADGui as gui
doc = FreeCAD.activeDocument()
if not doc:
    raise RuntimeError('No active document')

#Get selected shapes/objects:
selection = gui.Selection.getSelectionEx()
selectedObject = selection[0].Object
selectedObjects =[]
#selectedMisfit =[]
for selectedObject in selection:
#    if (hasattr(selectedObject, 'Shape')):
        selectedObjects.append(selectedObject.Object) 
#    else:
#        selectedMisfit.append(selectedObject.Object) 
        
if (selectedObjects.count == 0):
    print("whattado") #objects_to_export = [doc.ActiveObject]
else:
    #Create new TechDraw-page:
    templateTechdrawPage = doc.addObject("TechDraw::DrawSVGTemplate", "Template")
    templateTechdrawPage.Template = FreeCAD.getResourceDir() + "Mod\\TechDraw\\Templates\\Default_Template_A4_Landscape.svg"
    nameTechdrawPage = "TechdrawOffsetPage" #TODO
    pageTechdraw = doc.addObject("TechDraw::DrawPage", nameTechdrawPage)
    pageTechdraw.Template = templateTechdrawPage
    nameTechdrawPage = pageTechdraw.Name #Numbered if instance exists

#Create CrossSection for 2D offset:
import Part
from FreeCAD import Base
def CrossSection(shapesolid):
    wires=list()
    #shape=FreeCAD.getDocument("Assembly").Slice005_child2.Shape
    #TODO right normalaxis
    for i in shapesolid.slice(Base.Vector(0,1,0),4): #TODO: axis; 4 kerf?
        wires.append(i)

    comp=Part.Compound(wires)
    slice=FreeCAD.getDocument("Assembly").addObject("Part::Feature","Slice005_child2_cs")
    slice.Shape=comp
#    slice.purgeTouched()
    del comp,wires
    return slice

# Add view to techdraw page
def AddViewToTechdrawpage( pageTechdraw, source, nameView, lineWidth):
    try: #<Exception> GeometryObject::projectShapeWithPolygonAlgo - OCC error
        view = doc.addObject("TechDraw::DrawViewPart", nameView) #TechDraw::DrawProjGroupItem
        doc.recompute()
        view.CoarseView = False
        view.ViewObject.LineWidth = lineWidth
        view.Source = source
        #view.Direction = Vector(0, 0, 1)
        view.ScaleType = u'Custom'
        view.Scale = 1.00
        #view.CoarseView = True #Not yet here! Otherwise "GO::projectShapeWithPolygonAlgo - OCC error - NCollection_Array1::Create - while projecting shape" & "<Exception> GeometryObject::projectShapeWithPolygonAlgo - OCC error"
    except Exception as ex:
        FreeCAD.Console.PrintError('\nView for ' + nameView + ' cannot be created ! ')
        FreeCAD.Console.PrintError(ex)
    pageTechdraw.addView(view)
    gui.runCommand('TechDraw_ToggleFrame',1) #page.ShowFrame = False
    doc.recompute() #Essential! Otherwise "GO::projectShapeWithPolygonAlgo - OCC error - NCollection_Array1::Create - while projecting shape" & "<Exception> GeometryObject::projectShapeWithPolygonAlgo - OCC error"
    #Some post adjustments:
    view.CoarseView = False #True gives segments insteadof curves
    view.ViewObject.FaceColor=(170,170,255) #Distinguish face color for postprocessing separation from curves&lines 
    view.recompute()

#Create offset shapes for all selected:
import Draft
for obj in selectedObjects:
    # Prepare offset shape:
    clone = Draft.make_clone(obj)
    clone.Fuse = True
    doc.recompute()
    
    """ # Create 2D offset shape: NOT OK. No pocket offset. Usage clone? To be improved
    tmpNameOffset = "tmpOffset2D_"+ obj.Name
    shape=FreeCAD.getDocument("Assembly").getObject(clone.Name).Shape #This is NOT clone.Shape
    crosssection = CrossSection( shape) #shape=FreeCAD.getDocument("Assembly").Slice005_child2.Shape
    newOffset2D = FreeCAD.ActiveDocument.addObject("Part::Offset2D",tmpNameOffset) #If tmpName exists, a number is added/increased eg: Pipo001
    newOffset2D.Source = crosssection
    newOffset2D.Value = offset
    newOffset2D.Join = u"Arc"
    #AddViewToTechdrawpage(pageTechdraw, newOffset2D, "tmpOffset2D_"+ obj.Name, kerf) """

    # Create 3D offset shape:
    tmpNameOffset = "tmpOffset3D_" + str(kerf/2).replace('.', ',') + "_" + obj.Name
    newOffset3D = FreeCAD.ActiveDocument.addObject("Part::Offset",tmpNameOffset) #If tmpName exists, a number is added/increased eg: Pipo001
    newOffset3D.Source = clone
    newOffset3D.Value = offset
    newOffset3D.Join = u"Intersection" #Arc
    newOffset3D.Visibility = False
    clone.Visibility = False

    doc.recompute()
    AddViewToTechdrawpage(pageTechdraw, newOffset3D, tmpNameOffset, kerf)

#Export offset shapes to .dxf in .FCstd directory:
import os
directory = os.path.dirname(doc.FileName)
fullpathTechdrawExport = directory + "/" + nameTechdrawPage + ".dxf"
doc.recompute()
fl = TechDraw.writeDXFPage(pageTechdraw, fullpathTechdrawExport)

print("Check result in: " + fullpathTechdrawExport + ". Perhaps export manually")
