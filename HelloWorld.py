import rhinoscriptsyntax

def HW(a,b,c,d):
    print a
    print b
    print c
    print d
    hw = "hello world"
    
    print hw
    
    return hw


def logic(surf,windowSill,windowLeft,groundLine,length,height,thick):
    print surf
    print windowSill
    print windowLeft
    print groundLine
    
    A = length + height
    B = height + thick
    C = thick + length
    
    return(A,B,C)
    