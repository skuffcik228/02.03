x=600
y=600
def setup():
    size(600,400)
def draw():
    global x,y
    background(0)
    fill(random(0,255),random(0,255),random(0,255))

    ellipse(300,200,x,y)
    x=x-5
    y=y-5
    if x==10 and y==10:
        noLoop()
