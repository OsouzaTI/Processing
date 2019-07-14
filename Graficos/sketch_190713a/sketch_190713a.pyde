
#COR
cor = [color(255, 0, 0), color(0, 0, 255), color(0,255,0), color(255,255,255), color(255, 255, 102)] 
corB = [color(255, 163, 102), color(204, 0, 0), color(255, 0, 0)]

#POSIÇÂO
varZ = 5
z = [ [0,0] , [0,0] ]
pos = [ [0,0] , [0,0] ]
raio = [ [0, 0] , [0, 0] ]
raioBola = 50/2
raioMax = 0    
raioG = raioMax + 100
k = [0.01, 0.01]
vel = [1, 1]
posMax = [ [0,0] , [0,0] ]
varEixos = [ [0,0] , [0,0] ]
varEixosReset = False
varEixosRandom = False
varEixosRandomNumber = 0
varEixosRandomNumber_ = False
#TELA
w = 0
h = 0
layers = [0,0]

t = 120 * 5

timer = t

def setup():
    global pos, w, h, k, vel, posMax, z, raio, raioMax, raioG, varEixos, timer, varEixosRandomNumber
    #size(640,640)
    fullScreen()
    
    if(varEixosRandom):
        if varEixosRandomNumber_:
            varEixosRandomNumber = random(1.5)
            
        varEixos = [ [varEixosRandomNumber, varEixosRandomNumber] , [varEixosRandomNumber , varEixosRandomNumber] ]
        timer = t
    
    if varEixosReset:
        varEixos = [ [0, 0], [0, 0] ]
    
    k = [0.01, 0.01]
    vel = [1, 1]
    posMax = [ [0,0] , [0,0] ]
    pos = [ [width/2, height/2], [width/2, height/2] ]
    z = [ [random(1, varZ), random(1, varZ)] , [random(1, varZ), random(1, varZ)] ]
    raio = [ 
            [300 + random(varEixos[0][0]) * (100 + random(1) * 100)  , 300 + random(varEixos[0][1]) * (100 + random(1) * 100)],
            [300 + random(varEixos[1][0]) * (100 + random(1) * 100)  , 300 + random(varEixos[1][1]) * (100 + random(1) * 100)]
        ]
    raioMax = 0
    if(max(raio[0]) > max(raio[1])):
        raioMax = max(raio[0])
    else:
        raioMax = max(raio[1])
    raioG = raioMax + 100
        
    w = width/2
    h = height/2
 
    layers[0] = createGraphics(width, height)

def keyPressed():
    global vel, varEixosRandom, varEixosRandomNumber, varEixosReset, varEixosRandomNumber_
    if(key == "r"):
        setup()
    elif(keyCode == UP):
        vel[0] = vel[0] + 0.5
    elif(keyCode == DOWN):
        vel[0] = vel[0] - 0.5
    elif(keyCode == LEFT):
        vel[1] = vel[1] - 0.5
    elif(keyCode == RIGHT):
        vel[1] = vel[1] + 0.5
    elif(key == "1"):
        varEixos[0][0] = varEixos[0][0] + 0.1
    elif(key == "2"):
        varEixos[0][1] = varEixos[0][1] + 0.1
    elif(key == "3"):
        varEixos[1][0] = varEixos[1][0] + 0.1
    elif(key == "4"):
        varEixos[1][1] = varEixos[1][1] + 0.1
    elif(key == "q"):
        varEixos[0][0] = varEixos[0][0] - 0.1
    elif(key == "w"):
        varEixos[0][1] = varEixos[0][1] - 0.1
    elif(key == "e"):
        varEixos[1][0] = varEixos[1][0] - 0.1
    elif(key == "f"):
        varEixos[1][1] = varEixos[1][1] - 0.1
    elif(key == "u"):
        if(varEixosReset):
            varEixosReset = False
        else:
            varEixosReset = True
    elif(key == "p"):
        if(varEixosRandom):
            varEixosRandom = False
        else:
            varEixosRandom = True
    elif(key == "o"):
        if(varEixosRandom):
            varEixosRandomNumber = varEixosRandomNumber + 0.1
    elif(key == "i"):
        if(varEixosRandom):
            varEixosRandomNumber = varEixosRandomNumber - 0.1
    elif(key == "y"):
        if(varEixosRandom):
            if varEixosRandomNumber_:
                varEixosRandomNumber_ = False
            else:
                varEixosRandomNumber_ = True
            
         
def Texto():
    fill(cor[3])
    textSize(20)
    #fnt = loadFont("BodoniMT-481.vlw")
    #textFont(fnt, 28)
    text("Limite das bolas : B1(%d, %d), B2(%d, %d)"%( posMax[0][0] ,posMax[0][1], posMax[1][0],posMax[1][1] ), 10, 20)  
    text("Velocidades : B1 = %.2f, B2 = %.2f"%(vel[0], vel[1]), 10, 40) 
    text("Limite do Grafico: %d"%(raioG), 10, 60)      
    text("XB1: %.2f * sen( (2PI/%.2f) * %.2f"%(raio[0][0], z[0][0], k[0]), 10, 80)
    text("YB1: %.2f * cos( (2PI/%.2f) * %.2f"%(raio[0][1], z[0][1], k[0]), 10, 100)
    text("="*10, 10, 120)
    text("XB2: %.2f * cos( (2PI/%.2f) * %.2f"%(raio[1][0], z[1][0], k[1]), 10, 140)
    text("YB2: %.2f * sen( (2PI/%.2f) * %.2f"%(raio[1][1], z[1][1], k[1]), 10, 160)
    text("="*10, 10, 180)
    text("Limite de variacao do multiplicador\ndos raios de atuacao dos eixos", 10, 200)
    if not varEixosRandom:
        text("\nX1 = %.3f"%(varEixos[0][0]), 10, 230)
        text("\nY1 = %.3f"%(varEixos[0][1]), 10, 250)
        text("\nX2 = %.3f"%(varEixos[1][0]), 10, 270)
        text("\nY2 = %.3f"%(varEixos[1][1]), 10, 290)       
    text("\nVariacao Aleatoria: %s"%(varEixosRandom), 10, 310)
    text("\nLimite da variacao aleatoria: %.3f"%(varEixosRandomNumber), 10, 330)
    if varEixosRandom:
        text("\nTimer: %d"%(timer), 10, 350)
    text("\nEixos Reset: %s"%(varEixosReset), 10, 370)
    text("\nNumero aleatorio: %s"%(varEixosRandomNumber_), 10, 390)
    
    
def _timer():
    global timer
    
    if varEixosRandom:
        timer = timer - 0.1   
        if(timer <= 0):
            setup()
            print("setup Timer")      
            
def draw():
    global pos, k, posMax
    _timer()
    
    background(0)
    stroke(cor[1])
    strokeWeight(5)
    line(w, h - raioG, w, h + raioG)
    line(w - raioG, h, w + raioG, h)
    Texto()
    
    layers[0].beginDraw()


    # BOLA
    pushMatrix()
    translate(width/2, height/2) 
    text("X = {0:.3f}, Y = {1:.3f}".format(pos[0][0],pos[0][1]), pos[0][0] - 100, pos[0][1]- 50)
    text("X = {0:.3f}, Y = {1:.3f}".format(pos[1][0],pos[1][1]), pos[1][0] - 100, pos[1][1]- 50)       
    noStroke()
    fill(corB[2])
    circle(pos[0][0], pos[0][1], raioBola)
    fill(corB[1])
    circle(pos[1][0], pos[1][1], raioBola)  
    
    popMatrix()
    
    pushMatrix()
    translate(0, 0) 
    #layers[0].background(255)
    image(layers[0], 0, 0)
    popMatrix()
    
    pushMatrix()    
    
    layers[0].translate(w, h)
    layers[0].stroke(cor[4])
    layers[0].strokeWeight(5)
    layers[0].point(pos[0][0], pos[0][1])
    layers[0].stroke(cor[2])
    layers[0].point(pos[1][0], pos[1][1])
    
    popMatrix()
    
    
    layers[0].endDraw()

    k[0] = k[0] + (0.01 * vel[0])
    k[1] = k[1] + (0.01 * vel[1]) 

    pos[0][0] = (raio[0][0] * cos(TWO_PI/z[0][0] * k[0])) 
    pos[0][1] = (raio[0][1] * cos(TWO_PI/z[0][1] * k[0]))
    
    pos[1][0] = (raio[1][0] * sin(TWO_PI/z[1][0] * k[1])) 
    pos[1][1] = (raio[1][1] * sin(TWO_PI/z[1][1] * k[1]))
    
        
    if(pos[0][0] > posMax[0][0]): posMax[0][0] = pos[0][0]
    if(pos[0][1] > posMax[0][1]): posMax[0][1] = pos[0][1]
    
    if(pos[1][0] > posMax[1][0]): posMax[1][0] = pos[1][0]
    if(pos[1][1] > posMax[1][1]): posMax[1][1] = pos[1][1]
    
    
    
    
