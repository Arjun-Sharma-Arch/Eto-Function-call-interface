#Logic Caller script
# Author : Arjun Sharma
# e-mail id = arjun.sharma.arch@gmail.com

# import .clr namespace from.net package
import clr
# AddReference methods in the clr module interop with .NET libraries.
clr.AddReference("Eto")clr.AddReference("Rhino.UI")
# import Rhino Libraries
import scriptcontextimport Rhinoimport rhinoscriptsyntax as rs
import math



# from libraries import everything
from Rhino.UI import *from Eto.Forms import * from Eto.Drawing import *


# EXTERNAL LOGIC CALLED IN WHEN RECOMPUTE IS PRESSED
def logic(surf,windowSill,windowLeft,groundLine,length,height,thick):
    print surf
    print windowSill
    print windowLeft
    print groundLine
    
    A = length + height
    B = height + thick
    C = thick + length
    
    return(A,B,C)



# sticky store temporary information and bring it also across components
sticky = scriptcontext.sticky#dlg = sticky.get("mystuff")
# dialog box variable
dlg = None# result lable variable
resultLabel = None
result_Total_Lable = None
result_StraightCut_Lable = None
result_AngleCut_Lable = None


#Recompute Button Definition
def recompute_Click(sender, e):    #print "Hello World"    
    #Logic = insulation_script_20161028.logic(surf,windowSill,windowLeft,groundLine,length,height,thick)
    
    # WHEN THE VALUES ARE TO BE CALCULATED BY A EXTERNAL FUCNTION, THE SCRIPT CRASHES!!!
    """
    Logic = logic(surf,windowSill,windowLeft,groundLine,length,height,thick)
    
    total = Logic[0]
    straigh = Logic[1]
    angle = Logic[2]
    """
    
    # WHEN THE VALUES ARE FIXED VALUES THE SCRIPT WORKS WELL
    total = 10
    straigh = 30
    angle = 50
        #resultLabel.Text = "Number of cut pieces: " + num.ToString()
    result_Total_Lable.Text = "Total number of insulation panels required: " + total.ToString()
    result_StraightCut_Lable.Text = "Number of straight cut pieces: " + straigh.ToString()
    result_AngleCut_Lable.Text = "Number of Angle cut pieces: " + angle.ToString()
    
# Dialog box initialisation
if dlg == None:     dlg = Form(Title = "Surface Insulation", Padding = Padding(10), ClientSize = Size(300, 500))        runScript = Button(Text = "Recompute", Enabled = False)    runScript.Click += recompute_Click;# get input surface 
def runScript_Validate():    #surf1 = sticky.get("mystuff-surf1")    surf = sticky.get("mystuff-surf")
    windowSill = sticky.get("mystuff-windowSill")
    windowLeft = sticky.get("mystuff-windowLeft")
    groundLine = sticky.get("mystuff-groundLine")
    
        #and surf2 != None and suf2[0] == Rhino.Commands.Result.Success)    if surf != None and windowSill != None and windowLeft != None and groundLine != None:        if surf[0] == Rhino.Commands.Result.Success and windowSill[0] == Rhino.Commands.Result.Success and windowLeft[0] == Rhino.Commands.Result.Success and groundLine[0] == Rhino.Commands.Result.Success:            runScript.Enabled = True        else:            runScript.Enabled = False    else:        runScript.Enabled = False        result_Total_Lable = Label(Text = "Not run yet!")result_StraightCut_Lable = Label(Text = "")result_AngleCut_Lable = Label(Text = "")
length = NumericUpDown(MaxValue = 10000, MinValue = 1, Value = 1000)
height = NumericUpDown(MaxValue = 10000, MinValue = 1, Value = 500)
thick = NumericUpDown(MaxValue = 10000, MinValue = 1, Value = 100)

sufaceSelected2 = CheckBox(Enabled = False, Text = "Selected")button2 = Button(Text = "Select surface to be insulated")
# Definition for button 2
def button2_Click(sender, e):     rs.UnselectAllObjects()    surf = Rhino.Input.RhinoGet.GetOneObject("Select the surface", False, Rhino.DocObjects.ObjectType.Surface)    if surf[0] == Rhino.Commands.Result.Success:        sticky.Add("mystuff-surf", surf)        sufaceSelected2.Checked = True        runScript_Validate()
        
button2.Click += button2_ClickWindow_Sill = CheckBox(Enabled = False, Text = "Selected")button3 = Button(Text = "Select Window Sill Line")
# Definition for button 3
def button3_Click(sender, e):     rs.UnselectAllObjects()    windowSill = Rhino.Input.RhinoGet.GetOneObject("Select the Window Sill Line", False, Rhino.DocObjects.ObjectType.EdgeFilter)    if windowSill[0] == Rhino.Commands.Result.Success:        sticky.Add("mystuff-windowSill", windowSill)        Window_Sill.Checked = True        runScript_Validate()
        
button3.Click += button3_Click

Window_Left = CheckBox(Enabled = False, Text = "Selected")button4 = Button(Text = "Select Window Left Line")
# Definition for button 4
def button4_Click(sender, e):     rs.UnselectAllObjects()    windowLeft = Rhino.Input.RhinoGet.GetOneObject("Select the Window Left Line", False, Rhino.DocObjects.ObjectType.EdgeFilter)    if windowLeft[0] == Rhino.Commands.Result.Success:        sticky.Add("mystuff-windowLeft", windowLeft)        Window_Left.Checked = True        runScript_Validate()
        
button4.Click += button4_Click


Ground_Line = CheckBox(Enabled = False, Text = "Selected")button5 = Button(Text = "Select Ground Line")
# Definition for button 5
def button5_Click(sender, e):     rs.UnselectAllObjects()    groundLine = Rhino.Input.RhinoGet.GetOneObject("Select the Ground Line", False, Rhino.DocObjects.ObjectType.EdgeFilter)    if groundLine[0] == Rhino.Commands.Result.Success:        sticky.Add("mystuff-groundLine", groundLine)        Ground_Line.Checked = True        runScript_Validate()
        
button5.Click += button5_Click

# Dialog box initialisation
if dlg == None:     dlg = Form(Title = "Surface Insulation", Padding = Padding(10), ClientSize = Size(300, 500))        runScript = Button(Text = "Recompute", Enabled = False)    runScript.Click += recompute_Click;


content = StackLayout(Spacing = 5, HorizontalContentAlignment = HorizontalAlignment.Stretch)#content.Items.Add(checkBox)content.Items.Add(None)#content.Items.Add(TableLayout.Horizontal(button1, None, sufaceSelected1))content.Items.Add(TableLayout.Horizontal(button2, None, sufaceSelected2))
content.Items.Add(TableLayout.Horizontal(button3, None, Window_Sill))
content.Items.Add(TableLayout.Horizontal(button4, None, Window_Left))
content.Items.Add(TableLayout.Horizontal(button5, None, Ground_Line))


content.Items.Add(None)#content.Items.Add(StackLayoutItem(Control = TableLayout.Horizontal("Width", width), HorizontalAlignment = HorizontalAlignment.Center))#content.Items.Add(None)content.Items.Add(StackLayoutItem(Control = TableLayout.Horizontal("Length", length), HorizontalAlignment = HorizontalAlignment.Center))
content.Items.Add(None)content.Items.Add(StackLayoutItem(Control = TableLayout.Horizontal("Height", height), HorizontalAlignment = HorizontalAlignment.Center))
content.Items.Add(None)content.Items.Add(StackLayoutItem(Control = TableLayout.Horizontal("Thickness", thick), HorizontalAlignment = HorizontalAlignment.Center))
content.Items.Add(None)#content.Items.Add(resultLabel)
content.Items.Add(None)content.Items.Add(result_Total_Lable)content.Items.Add(None)content.Items.Add(result_StraightCut_Lable)content.Items.Add(None)content.Items.Add(result_AngleCut_Lable)
content.Items.Add(None)content.Items.Add(TableLayout.Horizontal(None, runScript))
dlg.Content = contentdlg.Owner = RhinoEtoApp.MainWindowsticky.Add("mystuff", dlg)dlg.Show()




