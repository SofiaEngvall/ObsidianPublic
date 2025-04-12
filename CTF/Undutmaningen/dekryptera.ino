/*
 * Denna kod utför dekryptering med RSA-nycklar. Dvs (c**d mod n) där c är
 * skiffertext, d är den privata exponenten och n är det publika modulus.
 *
 * Implementationen bygger på "square and multiply", även känd som "binary left-to-right" algoritmen.
 *
 * Denna fil kan öppnas direkt i Arduino IDE och kan köras på en Arduino UNO
 * med en 8-bitars Atmega328 mikrokontroller.
 */

#include <stdint.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>

#define BIGINT_BITS 512

// Definera en 528-bit integer-typ (33 uint16_t's) för att möjliggöra
// aritmetiska operationer med 512-bitars heltal.
typedef struct {
  uint16_t data[(BIGINT_BITS / 16) + 1];
} BigInt;

void BigInt_modexp(BigInt *base, BigInt *exp, BigInt *mod, BigInt *result);
void BigInt_mul(BigInt *a, BigInt *b, BigInt *mod, BigInt *result);
void BigInt_add(BigInt *a, BigInt *b, BigInt *result);
void BigInt_sub(BigInt *a, BigInt *b, BigInt *result);
void BigInt_shl(BigInt *a);
uint8_t BigInt_greater_or_equal(BigInt *a, BigInt *b);
void print_BigInt(BigInt num);

// Funktion för att utföra exponentiering med modulus: (base**exp) % mod
void BigInt_modexp(BigInt *base, BigInt *exp, BigInt *mod, BigInt *result) {
  
  // Initialilisera result till 1
  memset(result, 0, sizeof(BigInt));
  result->data[0] = 0x1;

  // Skapa en etta som bigint
  BigInt always_one = { 0x1 };

  // För varje bit i exponenten, från vänster till höger
  for (uint16_t i = BIGINT_BITS + 15; i >= 0; i--) {

    // Skriv ut hur långt vi kommit
    // TODO: Ta bort detta. Det tar tid och är ett avbrott i beräkningen
    Serial.print("Progress: ");
    Serial.print(uint8_t(floor(i*100/(BIGINT_BITS+15))));
    Serial.println("%");
    
    // Utför kvadrering (skippa om result=1)
    if (!BigInt_greater_or_equal(&always_one, result)) {
      BigInt_mul(result, result, mod, result);
    }

    // Utför multiplikation OM nuvarande bit av exponenten är 1
    if ((exp->data[i / 16] >> i % 16) & 1) {
      BigInt_mul(base, result, mod, result);
    }
    if (i == 0) {
      break;
    }
  }
}

// Funktion för att utföra multiplikation av två bigints
// Denna är supersnabb om b är liten
void BigInt_mul(BigInt *a, BigInt *b, BigInt *mod, BigInt *result) {
  BigInt a_copy, b_copy;
  memcpy(&a_copy, a, sizeof(BigInt));
  memcpy(&b_copy, b, sizeof(BigInt));
  memset(result, 0, sizeof(BigInt));

  for (uint16_t i = 0; i < BIGINT_BITS + 16; i++) {
    if ((b_copy.data[i / 16] >> (i % 16)) & 1) {
      BigInt_add(&a_copy, result, result);
      if (BigInt_greater_or_equal(result, mod)) {
        BigInt_sub(result, mod, result);
      }
    }
    BigInt_shl(&a_copy);
    if (BigInt_greater_or_equal(&a_copy, mod)) {
      BigInt_sub(&a_copy, mod, &a_copy);
    }
  }
}

// Funktion för att utföra addition av två bigints
void BigInt_add(BigInt *a, BigInt *b, BigInt *result) {
  BigInt a_copy, b_copy;
  memcpy(&a_copy, a, sizeof(BigInt));
  memcpy(&b_copy, b, sizeof(BigInt));
  memset(result, 0, sizeof(BigInt));

  uint8_t carry = 0;
  for (uint16_t i = 0; i < (BIGINT_BITS / 16) + 1; i++) {
    uint16_t sum = a_copy.data[i] + b_copy.data[i] + carry;
    result->data[i] = sum;
    if (carry) {
      carry = (sum <= a_copy.data[i]) || (sum <= b_copy.data[i]);
    }
    else {
      carry = (sum < a_copy.data[i]) || (sum < b_copy.data[i]);
    }
  }
}

// Funktion för att utföra subtraktion av två bigints
// För a >= b
void BigInt_sub(BigInt *a, BigInt *b, BigInt *result) {
  BigInt a_copy, b_copy;
  memcpy(&a_copy, a, sizeof(BigInt));
  memcpy(&b_copy, b, sizeof(BigInt));
  memset(result, 0, sizeof(BigInt));
  uint16_t diff;

  uint8_t borrow = 0;
  for (uint16_t i = 0; i < (BIGINT_BITS / 16) + 1; i++) {
    if (a_copy.data[i] > b_copy.data[i]) {
      diff = a_copy.data[i] - b_copy.data[i] - borrow;
      result->data[i] = diff;
      borrow = (diff > a_copy.data[i]);
    }
    else if (b_copy.data[i] > a_copy.data[i]) {
      diff = a_copy.data[i] - b_copy.data[i] - borrow;
      result->data[i] = diff;
      borrow = (diff >= a_copy.data[i]);
    }
    else {
      diff = -borrow;
      result->data[i] = diff;
    }
  }
}

// Funktion för att utföra vänsterskift av en BigInt
void BigInt_shl(BigInt *a) {
  for (int16_t i = (BIGINT_BITS / 16); i > 0; i--) {
    a->data[i] = (a->data[i] << 1) | (a->data[i - 1] >> 15);
  }
  a->data[0] = (a->data[0] << 1);
}

// Funktion för att avgöra om bigint a är större eller lika med bigint b
uint8_t BigInt_greater_or_equal(BigInt *a, BigInt *b) {
  for (int16_t i = (BIGINT_BITS / 16); i >= 0; i--) {
    if (a->data[i] > b->data[i]) {
      return true;
    }
    if (a->data[i] < b->data[i]) {
      return false;
    }
  }
  return true;
}

// Funktion för att skriva ut en BigInt
void print_BigInt(BigInt num) {

  // Iterera över hela listan från slutet till början för att skriva
  // ut de mest signifikanta 16 bitarna först
  for (int16_t i = (BIGINT_BITS / 16); i >= 0; i--) {
    Serial.print(num.data[i], HEX);

  }
  Serial.print("\n");
}

// Denna funktion är den första som körs. Den kör endast en gång.
void setup() {
  //Initialisera seriell kommunikation
  Serial.begin(9600);
  Serial.println("Decrypt:");

  BigInt mod = { 0xb41b, 0xc782, 0xd6ee, 0x4666, 0xcd25, 0x7081, 0xb572, 0x2bad, 0x330e, 0x4d75, 0xde36, 0x7b20, 0x47a6, 0x3e1b, 0xcac0, 0x7c99, 0xfab5, 0x162b, 0x4c7c, 0x97b6, 0xe1bd, 0x1088, 0x5bfd, 0x6689, 0xbd5c, 0x836b, 0x4db4, 0x6c24, 0xb871, 0x72e8, 0x8ec4, 0x8339 };
  BigInt exp = { }; // NOTE: Den privata nyckelns exponent fylls i här
  // base är den krypterade flaggan (samma som i flagga.enc)
  BigInt base = { 0xad91, 0x4665, 0xfdcc, 0x0f59, 0xc5c9, 0x5489, 0x2d6c, 0x9d89, 0x7577, 0xd2c1, 0x031a, 0x7ed4, 0x44ff, 0xfc18, 0x0152, 0x967a, 0x49ac, 0x4ad7, 0x7801, 0x3eaf, 0xb112, 0xafdf, 0x8b01, 0x9f18, 0xfbd6, 0x917d, 0xec04, 0x7ea2, 0xb47f, 0x53c5, 0x6179, 0x1856 };
  BigInt result = { 0x0 };

  print_BigInt(base);
  print_BigInt(exp);
  print_BigInt(mod);

  // Dekryptera genom exponentiering med modulo
  BigInt_modexp(&base, &exp, &mod, &result);

  print_BigInt(result);
  
}

// Efter setup körs denna funktion repetitivt
void loop() {
}
