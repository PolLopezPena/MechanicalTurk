#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
#include <SoftwareSerial.h>

// Definir pines para SoftwareSerial
SoftwareSerial mySerial(10, 11); // RX, TX

Adafruit_PWMServoDriver servos = Adafruit_PWMServoDriver(0x40);

unsigned int pos0=152; // ancho de pulso en cuentas para pocicion 0°
unsigned int pos180=545; // ancho de pulso en cuentas para la pocicion 180°
char dato;

void setup() {
  // put your setup code here, to run once:
  servos.begin();  
  servos.setPWMFreq(60);

  Serial.begin(9600);
  mySerial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    // Lee el dato del puerto serial
    dato = Serial.read();

    mySerial.write(dato);

    // Acciones
    switch (dato) {
      case '1':
        // ENFADADO
        servos.setPWM(8,0,pos180);
        servos.setPWM(0,0,pos0);
        servos.setPWM(4,0,pos0);
        servos.setPWM(12,0,pos0 + 280);
        break;
      case '2':
        // SERIO
        servos.setPWM(8,0,pos0 + 196);
        servos.setPWM(0,0,pos0 + 196);
        servos.setPWM(4,0,pos0);
        servos.setPWM(12,0,pos0 + 280);
        break;
        case '3':
        // PREOCUPADO
        servos.setPWM(8,0,pos0 + 196);
        servos.setPWM(0,0,pos0 + 196);
        servos.setPWM(4,0,pos0 + 650);
        servos.setPWM(12,0,pos0 -60);
        break;
        case '4':
        // ARQUEADO IZQUIERDA
        servos.setPWM(0,0,pos0 + 196);
        servos.setPWM(8,0,pos180);
        servos.setPWM(4,0,pos0);
        servos.setPWM(12,0,pos0 + 280);
        break;
        case '5':
        // ARQUEADO DERECHA
        servos.setPWM(0,0,pos0);
        servos.setPWM(8,0,pos0 + 196);
        servos.setPWM(4,0,pos0);
        servos.setPWM(12,0,pos0 + 280);
        break;
      default:
        // Si se presiona una tecla no reconocida, no hace nada
        break;
    }
  }
}
