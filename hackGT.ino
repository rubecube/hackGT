 #include <Adafruit_NeoPixel.h>
int ledpin = 2;
#define PIN 6
// small led 73
// large led 116
int ledLenght = 75;
int timeLen = 100;

// Parameter 1 = number of pixels in strip
// Parameter 2 = pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(ledLenght, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(115200);
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
  //pinMode(ledpin,OUTPUT);
  randomSeed(analogRead(0));
}

void loop() {
  String state = Serial.readString();
  int randNumR = random(255);
  int randNumG = random(255);
  int randNumB = random(255);

  if (state=="G"){                       // wait for a second
  theaterChase(strip.Color(  0, 255, 0), timeLen); //green
  delay(500);
  }else if(state=="Y"){
  theaterChase(strip.Color(  255, 255, 0), timeLen); //yellow
  theaterChase(strip.Color(  255, 255, 0), timeLen); //yellow

  delay(500); 
  }else if(state=="B"){
  theaterChase(strip.Color(  0, 0, 255), timeLen); //blue
  theaterChase(strip.Color(  0, 0, 255), timeLen); //blue
  delay(500); 
  }else if(state=="R"){  
    theaterChase(strip.Color(randNumR, randNumG, randNumB), timeLen); //Random
  delay(500); 
  }else{
    theaterChase(strip.Color( 0,  0, 0), 1);//Off
  }
  
    
}


//Theatre-style crawling lights.
void theaterChase(uint32_t c, uint8_t wait) {
  for (int j=0; j<10; j++) {  //do 10 cycles of chasing
    for (int q=0; q < 3; q++) {
      for (int i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(i+q, c);    //turn every third pixel on
      }
      strip.show();
     
      delay(wait);
     
      for (int i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(i+q, 0);        //turn every third pixel off
      }
    }
  }
}


