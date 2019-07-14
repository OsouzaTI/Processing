x = y = r = theta = n = max_ = 0
inicio_ = False
def setup():
    global x,y,r,theta,n,max_,inicio_
    x = [0,0,0,0,0,0,0,0,0,0]
    y = [0,0,0,0,0,0,0,0,0,0]
    r = [10,20,30,40,50,60,70,80,90,random(100,150),200,300,400]
    theta = [0,0,0,0,0,0,0,0,0,0]
    n = random(10)
    max_ = [[random(n),random(n)],[random(n),random(n)],[random(n),random(n)],[random(n),random(n)]]
    background(0)
    #size(640 , 640)
    fullScreen()
    
def keyPressed():
    global inicio_
    if(key == ENTER):
        print("Enter pressionado")
        if(inicio_):
            background(0)
            inicio_ = False
        else:
            inicio_ = True
            setup()
            background(0)
    
    

def inicio():
    textSize(36)
    text("Press enter to start",width/2 - 150, height/2)
    
def parametros(n, max_):
    textSize(26)
    text("n = " + str(n),10,20)
    text("p1 : ("+ str(max_[0][0])+",\t" + str(max_[0][1]) +")" ,10,45)
    text("p2 : ("+ str(max_[1][0])+",\t" + str(max_[1][1]) +")" ,10,70)
    text("p3 : ("+ str(max_[2][0])+",\t" + str(max_[2][1]) +")" ,10,95)
    text("p4 : ("+ str(max_[3][0])+",\t" + str(max_[3][1]) +")" ,10,120)
    text("Press enter to reset",10,145)
def draw():
    if inicio_:
        global x,y,theta,max_
        parametros(n, max_)
        #background(0)
        stroke(255)
        noFill() 
        strokeWeight(1);
        circle(width/2,height/2,200)
        fill(255)
        circle(width/2,height/2,3)    
        strokeWeight(10)
        translate(width/2, height/2)
        
        strokeWeight(1)
        #pontos Dentro
        point(x[4], y[4])
        theta[4] = theta[4] + 0.01    
        x[4] = r[1] * cos( TWO_PI * theta[4])
        y[4] = r[1] * sin( TWO_PI * theta[4])
        
        strokeWeight(1)
        #pontos fora 
        point(x[0], y[0])
        point(x[1], y[1])
        point(x[2], y[2])
        point(x[3], y[3])
        
        theta[0] = theta[0] + 0.01    
        x[0] = r[12] * cos( (3.14 + (0.1 * max_[0][0] )) * theta[0])
        y[0] = r[12] * sin( (3.14 + (0.1 * max_[0][1] )) * theta[0])
        
        theta[1] = theta[1] + 0.01    
        x[1] = r[11] * sin( (3.14 + (0.1 * max_[1][0] )) * theta[1])
        y[1] = r[11] * cos( (3.14 + (0.1 * max_[1][1] )) * theta[1])
        
        theta[2] = theta[2] + 0.01    
        x[2] = r[10] * cos( (3.14 + (0.1 * max_[2][0] )) * theta[2])
        y[2] = r[10] * sin( (3.14 + (0.1 * max_[2][1] )) * theta[2])
        
        theta[3] = theta[3] + 0.01    
        x[3] = r[11] * sin( (3.14 + (0.1 * max_[3][0] )) * theta[3])
        y[3] = r[11] * cos( (3.14 + (0.1 * max_[3][1] )) * theta[3])
    else:
        inicio()


        
        
        
        
        
        
        
        
        
        
        
