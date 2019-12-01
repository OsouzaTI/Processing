class _Ball
{
  
  int raio;
  float posx = 0.0;
  float posy = 0.0;
  boolean colorTrigger = false;
  int colorIndex = 0;
  color Point = 0;
  color[] myColor = {
    color(0,255,0),
    color(0,0,255),
    color(255,255,0),
    color(255,0,255),
    color(0,128,0),
    color(128,0,128),
    color(0,128,128),
    color(255,20,147),
    color(205,92,92),
    color(255,215,0),
    color(218,165,32),
    color(255,255,0),
    color(0,128,128),
    color(0,255,255)
  };
  float[] variacao = {PrecisionFloat(random(.05)+0.01),
                      PrecisionFloat(random(.05)+0.01)};
  float[] variacao_div = {floor(random(4)), floor(random(4))};
  float[] raio_giro = {random(width/3)+50, random(height/3)+50};
  _Ball(int _raio)
  {
    
    raio = _raio;
    print(variacao[0], variacao[1]+ "\n");
    print(raio_giro[0], raio_giro[1]+ "\n");
    print(variacao_div[0], variacao_div[1]+ "\n");
    
  }
  
  void move()
  {
    posx = 
    raio_giro[0] * (sin( -PI + frameCount * variacao[0]));
    
    posy =
    raio_giro[1] * (cos( -PI + frameCount * variacao[1]));
      
    for(int i = 0; i < 2; i++)
    {
       //variacao[i] += .1 ;
    }
    //print(variacao[0], variacao[1]+ "\n");
  }
  
  void display()
  {
    move();
    if(!colorTrigger)
    {
      colorIndex = floor( random(0, myColor.length -1 ) );
      Point = myColor[ colorIndex ];
      colorTrigger = !colorTrigger;
    }
    fill( myColor[ colorIndex ] );
    circle(posx, posy, raio);
  }
  
  float getPosx()
  {
     return posx; 
  }
  float getPosy()
  {
     return posy; 
  }
  float getVariacaoS()
  {
     return variacao[1]; 
  }
  float getVariacaoC()
  {
     return variacao[0]; 
  }
  
  float getRaioGiroS()
  {
     return raio_giro[1]; 
  }
  float getRaioGiroC()
  {
     return raio_giro[0]; 
  }
  int getColorPoint()
  {
    return Point;
  }  
  float PrecisionFloat(float n)
  {
     float m = float(String.format("%.2f\n", n).replace(",",".")) ;
     return m;
  }
 
}
