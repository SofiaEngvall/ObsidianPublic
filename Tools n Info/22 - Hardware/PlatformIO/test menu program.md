
```cpp
#include <Arduino.h>
#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>
#include <SPI.h>

// TFT Pins
#define TFT_CS   5
#define TFT_DC   2
#define TFT_RST  4

// Button Pins (using your ESP32-WROOM layout)
#define BTN_UP     13   // Right side, near GND
#define BTN_DOWN   12   // Right side, near GND  
#define BTN_SELECT 14   // Right side, near GND
#define BTN_BACK   27   // Right side, near 3.3V

Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_RST);

// Menu system variables
int currentSelection = 0;
int currentMenuLevel = 0; // 0=Main, 1=Submenu
String mainMenu[] = {"Play Video", "View Images", "Settings", "System Info"};
String settingsMenu[] = {"Brightness", "Contrast", "Language", "Back"};
int mainMenuSize = 4;
int settingsMenuSize = 4;

// Simulated file lists (replace with SD card later)
String videoFiles[] = {"video1.mp4", "video2.avi", "test.mov"};
String imageFiles[] = {"image1.jpg", "photo.png", "art.bmp"};
int videoCount = 3;
int imageCount = 3;

void drawMainMenu();
void drawSettingsMenu();
void drawFileMenu(String title, String files[], int count);
void showMessage(String message);
void handleSelect();

void setup() {
  Serial.begin(115200);
  
  // Initialize TFT
  tft.initR(INITR_BLACKTAB);
  delay(150);
  tft.setRotation(0);
  tft.fillScreen(ST7735_BLACK);
  
  // Initialize buttons with internal pull-ups
  pinMode(BTN_UP, INPUT_PULLUP);
  pinMode(BTN_DOWN, INPUT_PULLUP);
  pinMode(BTN_SELECT, INPUT_PULLUP);
  pinMode(BTN_BACK, INPUT_PULLUP);
  
  // Welcome message
  tft.setTextSize(2);
  tft.setTextColor(ST7735_GREEN);
  tft.setCursor(20, 40);
  tft.println("MENU SYSTEM");
  tft.setTextSize(1);
  tft.setCursor(30, 70);
  tft.setTextColor(ST7735_YELLOW);
  tft.println("Ready!");
  delay(1500);
  
  drawMainMenu();
}

void drawMainMenu() {
  currentMenuLevel = 0;
  tft.fillScreen(ST7735_BLACK);
  tft.setTextSize(1);
  
  for(int i = 0; i < mainMenuSize; i++) {
    tft.setCursor(10, 15 + i*20);
    if(i == currentSelection) {
      tft.setTextColor(ST7735_YELLOW);
      tft.print("> ");
    } else {
      tft.setTextColor(ST7735_WHITE);
      tft.print("  ");
    }
    tft.println(mainMenu[i]);
  }
  
  // Footer
  tft.setTextColor(ST7735_BLUE);
  tft.setCursor(10, 110);
  tft.println("Use buttons to navigate");
}

void drawSettingsMenu() {
  currentMenuLevel = 1;
  tft.fillScreen(ST7735_BLACK);
  tft.setTextSize(1);
  
  for(int i = 0; i < settingsMenuSize; i++) {
    tft.setCursor(10, 15 + i*20);
    if(i == currentSelection) {
      tft.setTextColor(ST7735_CYAN);
      tft.print("> ");
    } else {
      tft.setTextColor(ST7735_WHITE);
      tft.print("  ");
    }
    tft.println(settingsMenu[i]);
  }
}

void drawFileMenu(String title, String files[], int count) {
  tft.fillScreen(ST7735_BLACK);
  tft.setTextSize(1);
  tft.setTextColor(ST7735_GREEN);
  tft.setCursor(40, 5);
  tft.println(title);
  
  for(int i = 0; i < count; i++) {
    tft.setCursor(20, 25 + i*20);
    if(i == currentSelection) {
      tft.setTextColor(ST7735_YELLOW);
      tft.print("> ");
    } else {
      tft.setTextColor(ST7735_WHITE);
      tft.print("  ");
    }
    tft.println(files[i]);
  }
}

void showMessage(String message) {
  tft.fillScreen(ST7735_BLACK);
  tft.setTextSize(1);
  tft.setTextColor(ST7735_MAGENTA);
  tft.setCursor(10, 50);
  tft.println(message);
  delay(2000);
  drawMainMenu();
}

void loop() {
  // Read buttons with debouncing
  static unsigned long lastButtonPress = 0;
  
  if(millis() - lastButtonPress > 200) { // Debounce delay
    if(digitalRead(BTN_UP) == LOW) {
      currentSelection = (currentSelection - 1);
      if(currentSelection < 0) currentSelection = 0;
      if(currentMenuLevel == 0) drawMainMenu();
      else if(currentMenuLevel == 1) drawSettingsMenu();
      lastButtonPress = millis();
    }
    
    if(digitalRead(BTN_DOWN) == LOW) {
      int maxItems = (currentMenuLevel == 0) ? mainMenuSize - 1 : settingsMenuSize - 1;
      currentSelection = (currentSelection + 1);
      if(currentSelection > maxItems) currentSelection = maxItems;
      if(currentMenuLevel == 0) drawMainMenu();
      else if(currentMenuLevel == 1) drawSettingsMenu();
      lastButtonPress = millis();
    }
    
    if(digitalRead(BTN_SELECT) == LOW) {
      handleSelect();
      lastButtonPress = millis();
    }
    
    if(digitalRead(BTN_BACK) == LOW) {
      if(currentMenuLevel > 0) {
        currentMenuLevel = 0;
        currentSelection = 0;
        drawMainMenu();
      }
      lastButtonPress = millis();
    }
  }
  
  delay(10);
}

void handleSelect() {
  if(currentMenuLevel == 0) { // Main menu
    switch(currentSelection) {
      case 0: // Play Video
        drawFileMenu("VIDEOS", videoFiles, videoCount);
        break;
      case 1: // View Images
        drawFileMenu("IMAGES", imageFiles, imageCount);
        break;
      case 2: // Settings
        currentSelection = 0;
        drawSettingsMenu();
        break;
      case 3: // System Info
        showMessage("ESP32-WROOM\n128x160 TFT\n4-Button Menu");
        break;
    }
  } else if(currentMenuLevel == 1) { // Settings menu
    switch(currentSelection) {
      case 0: // Brightness
        showMessage("Brightness Control\nUse potentiometer!");
        break;
      case 1: // Contrast
        showMessage("Adjust contrast\nin settings");
        break;
      case 2: // Language
        showMessage("Language selection\nNot implemented");
        break;
      case 3: // Back
        currentSelection = 2; // Return to Settings in main menu
        drawMainMenu();
        break;
    }
  }
}

```