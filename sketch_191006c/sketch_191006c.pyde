def setup():
    size(480, 480) #creates window x pixels wide and y pixels high
    
def draw():
    if mousePressed:
        fill(0)
        ellipse(mouseX, mouseY, 80, 80)
    
    
