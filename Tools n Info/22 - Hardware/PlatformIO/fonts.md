
  // Fill screen with grey so we can see the effect of printing with and without 
  // a background colour defined
  tft.fillScreen(TFT_GREY);
  
  // Set "cursor" at top left corner of display (0,0) and select font 2
  // (cursor will move to next line automatically during printing with 'tft.println'
  //  or stay on the line is there is room for the text with tft.print)
  tft.setCursor(0, 0, 2);

menu font?
```cpp
tft.setTextColor(TFT_GREEN,TFT_BLACK);
tft.setTextFont(4);
tft.println("Hello!");
```


font size 1
![[Images/Pasted image 20250830011236.png]]

Font size 2
![[Images/Pasted image 20250830011533.png]]




