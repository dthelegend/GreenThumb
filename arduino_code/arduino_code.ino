//www.elegoo.com
//2018.10.25

#include "LedControl.h"
#include <stdlib.h>
#include <dht_nonblocking.h>
#define DHT_SENSOR_TYPE DHT_TYPE_11
#define MESSAGE_BUFFER_SIZE 512
#include <LiquidCrystal.h>

LedControl lc = LedControl(12,10,11,1);
LiquidCrystal lcd(3, 9, 4, 5, 6, 7);

unsigned long delaytime1=200;
unsigned long delaytime2=30;

static const int DHT_TMPHMD_PIN = 2;
DHT_nonblocking dht_sensor( DHT_TMPHMD_PIN, DHT_SENSOR_TYPE );

const int LIGHT_id = 1;
const int WTRLVL_id = 0;

int facing = 1;
int time = 0;

int sentiment = 2;

char messageBuffer[512];

char printBuffer[250];

/*
 * Initialize the serial port.
 */
void setup()
{
  Serial.begin(9600);

  lcd.begin(16,2);
  lcd.noCursor();

  /*
  The MAX72XX is in power-saving mode on startup,
  we have to do a wakeup call
  */
  lc.shutdown(0,false);
  /* Set the brightness to a medium values */
  lc.setIntensity(0,6);
  /* and clear the display */
  lc.clearDisplay(0);
  
  strcpy(printBuffer,"Hello World! I am a Plant!\0");
}

void write(char* tex){
  lcd.write(tex);
}

void chill(){
  byte c[8] = {B00011110, 
               B00100010, 
               B00111010,
               B00111010, 
               B00111000, 
               B00100000,
               B00000010,
               B00011100};
  transposeBytes(c);
  eye(c);
}

void left(){
  byte left[8] = { B00111100, 
                   B01000100, 
                   B01110100,
                   B01110100, 
                   B01110000, 
                   B01000000,
                   B00000100,
                   B00111000};
  transposeBytes(left);
  eye(left);  
}

void right(){
  byte right[8] = { B00011110, 
                    B00010001, 
                    B00010111,
                    B00010111, 
                    B00000111, 
                    B00000001,
                    B00010000,
                    B00001110 };
  transposeBytes(right);
  eye(right);
}

void heart(){
  byte clos[8] = { B00000000, 
                   B00010100,
                   B00111110, 
                   B00111110, 
                   B00011100,
                   B00001000,
                   B00000000,
                   B00000000};
  transposeBytes(clos);
  eye(clos);
}

void sad(){
  byte clos[8] = { B00000100, 
                   B00011000,
                   B00000000, 
                   B00101100, 
                   B00101100,
                   B00100000,
                   B00000010,
                   B00011100};
  transposeBytes(clos);
  eye(clos);
}

void sadb(){
  byte clos[8] = { B00000100, 
                   B00011000,
                   B00000000, 
                   B00000000, 
                   B00100010,
                   B00011100,
                   B00000000,
                   B00000000};
  transposeBytes(clos);
  eye(clos);
}

void close(){
  byte clos[8] = { B00000000, 
                   B00000000, 
                   B00000000,
                   B00111110, 
                   B01111110, 
                   B00111100,
                   B00000000,
                   B00000000 };
  transposeBytes(clos);
  eye(clos);
}

void annoyed(){
  byte clos[8] = { B00000000, 
                   B00000000, 
                   B00000000,
                   B01111100, 
                   B00000000, 
                   B01111100,
                   B01111100,
                   B00000000 };
  transposeBytes(clos);
  eye(clos);
}

void dead(){
  byte clos[8] = { B00000000, 
                   B00100100, 
                   B00100100,
                   B00011000, 
                   B00011000, 
                   B00100100,
                   B00100100,
                   B00000000 };
  transposeBytes(clos);
  eye(clos);
}

void transposeBytes(byte arr[8]) {
  byte transposed[8];
  for (int i = 0; i < 8; i++) {
    transposed[i] = 0;
    for (int j = 0; j < 8; j++) {
      transposed[i] |= ((arr[j] >> i) & 1) << (7 - j);
    }
  }
  for (int i = 0; i < 8; i++) {
    arr[i] = transposed[i];
  }
}

void eye(byte code []){

  for (int i=0;i<8;i++){
    lc.setRow(0,i,code[i]);
  }
  delay(delaytime1);
}

/*
 * Poll for a measurement, keeping the state machine alive.  Returns
 * true if a measurement is available.
 */
static bool measure_environment( float *temperature, float *humidity )
{
  static unsigned long measurement_timestamp = millis( );

  /* Measure once every four seconds. */
  if( millis( ) - measurement_timestamp > 5000ul )
  {
    if( dht_sensor.measure( temperature, humidity ) == true )
    {
      measurement_timestamp = millis( );
      return( true );
    }
  }

  return( false );
}


void heartPulse(){
  heart();
  if (time % 30 == 0){
    close();
  } else if (time % 8 == 0){
    lc.setIntensity(0,15);
  } else if (time % 8 == 4){
    lc.setIntensity(0,4);
  }
}

void blink(){
  lc.setIntensity(0,4);

  if (time % 30 == 0){
    close();
  } else {

    int r = rand() % 80;
    if (r == 10){
      facing += 1;
      facing = facing % 4;
    }

    if (facing == 1) {
      right();
     } else if (facing == 2) {
      chill();
    } else if (facing == 3) {
      left();
    } else {
      chill();
    }
  }
}

void annBlink(){
  lc.setIntensity(0,4);
  if (time % 30 == 0){
    close();
  } else {
    annoyed();
  }
}

/*
 * Main program loop.
 */
void loop( )
{
  float temperature;
  float humidity;
  int waterlvl;
  int lightlvl;

  time += 1;

  if (sentiment < 1) {
    heartPulse();
  } else if (sentiment < 3) {
    blink();
  } else if (sentiment < 5) {
    annBlink();
  } else if (sentiment < 7) {
    sadb();
  } else {
    dead();
  }

  /* Measure temperature and humidity.  If the functions returns
     true, then a measurement is available. */
  if( measure_environment( &temperature, &humidity ) == true )
  {

    waterlvl = analogRead(WTRLVL_id);
    lightlvl = analogRead(LIGHT_id)-320;

    Serial.print("{\"temperature\": ");
    Serial.print(temperature, 1);
    Serial.print(", \"humidity\": ");
    Serial.print(humidity, 1);
    Serial.print(", \"water_level\": ");
    Serial.print(waterlvl, 1);
    Serial.print(", \"light_level\": ");
    Serial.print(lightlvl, 1);
    Serial.print("}\n");
  }

  
  Serial.flush();

  int nbits = Serial.available();
  if (nbits > 0) {
    sentiment = Serial.read();
    
    int i = 0;
    for (i; i < MESSAGE_BUFFER_SIZE; i++) {
      int messageByte = Serial.read();

      if (messageByte == -1) {
        break;
      }

      messageBuffer[i] = messageByte;

      if (messageByte == NULL) {
        break;
      }
    }
    messageBuffer[i+1] = '\0';

    lcd.clear();

    lcd.print(messageBuffer);
  }

}

