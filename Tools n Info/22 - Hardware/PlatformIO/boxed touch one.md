
esp32 wroom 32u pinout
clk d0 d1 15 2 0 4 14 17 5 18 19 gnd 21 rx tx 22 23 gnd
5v cmd d3 d2 13 gnd 12 14 27 26 25 33 32 35 34 un up en 3v3


### **TFT Display Pins:**

TFT_CS   → GPIO 5     (Labeled "5")  
TFT_DC   → GPIO 2     (Labeled "2")
TFT_RST  → GPIO 15    (Labeled "15") 
TFT_SCK  → GPIO 18    (Labeled "18")
TFT_MOSI → GPIO 23    (Labeled "23")
TFT_MISO → GPIO 19    (Labeled "19")
LED      → 3.3V       (Backlight power) or 
     TFT LED → GPIO 12 (PWM capable) + 100Ω resistor or
     
TFT VCC  → ESP32 3.3V  
TFT GND  → ESP32 GND

### **Touch Screen Pins:**

T_CS     → GPIO 14    (Labeled "14")  
T_IRQ    → GPIO 17    (Labeled "17")
T_CLK  → GPIO 18 (SCK) - shared with TFT
T_DIN   → GPIO 23 (MOSI) - shared with TFT  
T_DO   → GPIO 19 (MISO) - shared with TFT

### **Navigation Buttons:**

BTN_UP     → GPIO 27    (Labeled "27")
BTN_DOWN   → GPIO 26    (Labeled "26")  
BTN_SELECT → GPIO 25    (Labeled "25")
BTN_BACK   → GPIO 33    (Labeled "33")

### **SD Card (Future):**

SD_CS    → GPIO 13    (Labeled "13")
SD_SCK   → GPIO 18    (Shared)
SD_MOSI  → GPIO 23    (Shared)  
SD_MISO  → GPIO 19    (Shared)

### **RFID/RF Modules (Future):**

NRF24_CS → GPIO 12    (Labeled "12")
RFID_CS  → GPIO 32    (Labeled "32")

## **Available for Future Use:**

**GPIO 0, 4** - Available (careful with GPIO 0 - boot mode)
**GPIO 21, 22** - Available (I2C capable)
**GPIO 34, 35** - Input only (good for sensors)
**GPIO 36, 39** - Input only (touch capable)

## **Pins to Avoid:**

**GPIO 6-11** - Used for flash memory
**GPIO 1, 3** - Serial TX/RX (unless you need them)
**GPIO 0** - Boot mode pin (use carefully)


## **TFT Power Considerations:**

The 2.8" TFT can draw **200-400mA** at full brightness
ESP32-WROOM-32U 3.3V regulator can supply **~500mA**
**Recommendation**: Add a **1000μF capacitor** between 3.3V and GND near the TFT to handle current spikes


