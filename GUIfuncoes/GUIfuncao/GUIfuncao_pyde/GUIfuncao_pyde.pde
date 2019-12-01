import controlP5.*;

ControlP5 cp5;
ControlTimer c;
PGraphics pg;
int numero_bolas = 1;
_Ball[] b = null;
boolean fullScreen = false;
void setup()
{
  //size(900, 900);
  fullScreen();
  
   pg = createGraphics(width, height);
   
   b = new _Ball[numero_bolas];
   
   for(int i = 0; i < numero_bolas; i++)
   {
     b[i] = new _Ball(15);
   }
   
   
   PFont font = createFont("arial", 20);
   cp5 = new ControlP5(this);
   cp5.addTextfield("Bolas")
      .setPosition(10, 10)
      .setSize(200, 40)
      .setText("")
      .setFocus(true)
      .setFont(createFont("arial",18))
      .setColor(color(255, 255, 255));
  
  textFont(font);
  cp5.get(Textfield.class,"Bolas").setText("");
  c = new ControlTimer();
  c.setSpeedOfTime(1);
}

void keyPressed()
{
  char k = str(key).toLowerCase().charAt(0);
  switch(k)
  {
    case 'r':
      numero_bolas = int(cp5.get(Textfield.class,"Bolas").getText());
      setup();
      break;
    case 's':
      setup();
      break;
    case 'f':
      fullScreen = !fullScreen;
      print("Botão da tela cheia apertado!");
    default:
      print("Não existe esse comando!");
  }
}

void draw()
{   
   if( int(c.second()) == 15)
   {
     c.reset();
     setup();
   }
   
   background(0);
   fill(0, 255, 0);
   text(c.toString(),width-100,30);
   fill(0, 0, 255);
   
   pushMatrix();
   image(pg, 0, 0);
   popMatrix(); 
   
   fill(255);
   
   pushMatrix();
   translate(width/2, height/2);
   bolas_display(b, false);
   pg.beginDraw();
   //pg.background(255);
   
   pg.strokeWeight(3);
   pg.pushMatrix();
   pg.translate(width/2, height/2);
   bolas_display(b, true);
   pg.popMatrix();
   //print(b.getPosx(), b.getPosy() + "\n");
   pg.endDraw();
   popMatrix();
   
   
}

void bolas_display(_Ball[] b, boolean t)
{
  if(!t)
  {
     for(int i = 0; i < numero_bolas; i++)
     {
       b[i].display();
       pushMatrix();
       translate(-width/2, -height/2 + 100);
       text("Bola "+i+"{ x: " + nf(b[i].getPosx(),0,4)+", y: "+nf(b[i].getPosy(),0,4)
           +", Variacoes:["+ b[i].getVariacaoS()+", "+b[i].getVariacaoC()+"] }", 10, 20 * i + 10);
       popMatrix();
     } 
  }
  else
  {
     for(int i = 0; i < numero_bolas; i++)
     {
       pg.stroke(b[i].getColorPoint());
       pg.point(b[i].getPosx(), b[i].getPosy());
     } 
  }
}

void textDisplay()
{
   textSize(19);
   /*
   text("x: "+      nf(b.getPosx(),0,4 ) 
   +"\ny: "+        nf(b.getPosy(),0,4) 
   +"\nVariação: "   +b.getVariacaoS()+", "+b.getVariacaoC()
   +"\nRaio de Giro:\n -"+b.getRaioGiroS()+"\n-"+b.getRaioGiroC(), 10, 30);
   */ 
  
}
