def setup():
    size(400,400)
    stroke(225)
    background(192, 64, 0)    
    
def draw():
    line(200, 200, mouseX, mouseY)
    
def mousePressed():
    
    saveFrame("Output.png")
