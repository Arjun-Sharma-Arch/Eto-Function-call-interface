#Logic Caller script
# Author : Arjun Sharma
# e-mail id = arjun.sharma.arch@gmail.com

# import .clr namespace from.net package
import clr
# AddReference methods in the clr module interop with .NET libraries.
clr.AddReference("Eto")
# import Rhino Libraries
import scriptcontext
import math



# from libraries import everything
from Rhino.UI import *


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
sticky = scriptcontext.sticky
# dialog box variable
dlg = None
resultLabel = None
result_Total_Lable = None
result_StraightCut_Lable = None
result_AngleCut_Lable = None


#Recompute Button Definition
def recompute_Click(sender, e):
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
    
    result_Total_Lable.Text = "Total number of insulation panels required: " + total.ToString()
    result_StraightCut_Lable.Text = "Number of straight cut pieces: " + straigh.ToString()
    result_AngleCut_Lable.Text = "Number of Angle cut pieces: " + angle.ToString()
    
# Dialog box initialisation
if dlg == None: 
def runScript_Validate():
    windowSill = sticky.get("mystuff-windowSill")
    windowLeft = sticky.get("mystuff-windowLeft")
    groundLine = sticky.get("mystuff-groundLine")
    
    
length = NumericUpDown(MaxValue = 10000, MinValue = 1, Value = 1000)
height = NumericUpDown(MaxValue = 10000, MinValue = 1, Value = 500)
thick = NumericUpDown(MaxValue = 10000, MinValue = 1, Value = 100)

sufaceSelected2 = CheckBox(Enabled = False, Text = "Selected")
# Definition for button 2
def button2_Click(sender, e): 
        
button2.Click += button2_Click
# Definition for button 3
def button3_Click(sender, e): 
        
button3.Click += button3_Click

Window_Left = CheckBox(Enabled = False, Text = "Selected")
# Definition for button 4
def button4_Click(sender, e): 
        
button4.Click += button4_Click


Ground_Line = CheckBox(Enabled = False, Text = "Selected")
# Definition for button 5
def button5_Click(sender, e): 
        
button5.Click += button5_Click

# Dialog box initialisation
if dlg == None: 


content = StackLayout(Spacing = 5, HorizontalContentAlignment = HorizontalAlignment.Stretch)
content.Items.Add(TableLayout.Horizontal(button3, None, Window_Sill))
content.Items.Add(TableLayout.Horizontal(button4, None, Window_Left))
content.Items.Add(TableLayout.Horizontal(button5, None, Ground_Line))



content.Items.Add(None)
content.Items.Add(None)
content.Items.Add(None)
content.Items.Add(None)
content.Items.Add(None)
dlg.Content = content



