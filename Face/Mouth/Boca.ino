#include <Adafruit_GFX.h>
#include <Adafruit_NeoMatrix.h>
#include "patterns.h"  // Incluir el archivo de patrones

#define PIN 6             // Pin donde están conectados los NeoPixels
#define MATRIX_WIDTH 32
#define MATRIX_HEIGHT 8

Adafruit_NeoPixel strip = Adafruit_NeoPixel(256, PIN, NEO_GRB+ NEO_KHZ800);
char dato;

int xyToIndex(int x, int y) {
  // Calcula el índice en la tira horizontal de NeoPixel con zigzag
  int index;
  if (y % 2 == 0) {
    // Filas pares (0, 2, 4, ...): avanzan de izquierda a derecha
    index = y * 8 + x;
  } else {
    // Filas impares (1, 3, 5, ...): avanzan de derecha a izquierda
    index = y * 8 + (7 - x);
  }
  return index;
}

uint8_t getBit(const uint8_t pattern[MATRIX_HEIGHT][(MATRIX_WIDTH + 7) / 8], int row, int col) {
  return (pattern[row][col / 8] >> (7 - (col % 8))) & 1;
}

void drawPattern(const uint8_t pattern[MATRIX_HEIGHT][(MATRIX_WIDTH + 7) / 8]) {
  for (int y = 0; y < MATRIX_HEIGHT; y++) {
    for (int x = 0; x < MATRIX_WIDTH; x++) {
      uint8_t bit = getBit(pattern, y, x);
      if (bit) {
        int index = xyToIndex(y, x);
        strip.setPixelColor(index, strip.Color(25, 25, 25));
      }
    }
  }
}

void setup() {
  Serial.begin(9600);
  strip.begin();
  strip.show(); // Inicializa todos los píxeles a 'apagado'
}

// Función para establecer un bit en la matriz
void setBit(uint8_t pattern[MATRIX_HEIGHT][(MATRIX_WIDTH + 7) / 8], int row, int col, uint8_t value) {
  if (value)
    pattern[row][col / 8] |= (1 << (7 - (col % 8)));
  else
    pattern[row][col / 8] &= ~(1 << (7 - (col % 8)));
}

void loop() {
  if (Serial.available() > 0) {
    // Lee el dato del puerto serial
    dato = Serial.read();
    switch (dato) {
      case '1':
        // ENFADADO
        strip.clear();
        drawPattern(pattern3);
        strip.show();
        break;
      case '2':
        // SERIO
        strip.clear();
        drawPattern(pattern5);
        strip.show();
        break;
      case '3':
        // PREOCUPADO
        strip.clear();
        drawPattern(pattern4);
        strip.show();
        break;
      case '4':
        // ARQUEADO IZQUIERDA
        strip.clear();
        drawPattern(pattern5);
        strip.show();
        break;
      case '5':
        // ARQUEADO DERECHA
        strip.clear();
        drawPattern(pattern5);
        strip.show();
        break;
      default:
        // Si se presiona una tecla no reconocida, no hace nada
        break;
    }
    
  } // Muestra el nuevo patrón
}

