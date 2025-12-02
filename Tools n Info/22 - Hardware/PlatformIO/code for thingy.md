
deepseek, not actual ex, have better link
```cpp
void wifiDeauthAttack() {
  // Simple deauth frame broadcast
  wifi_set_channel(6);
  for(int i=0; i<100; i++) {
    sendDeauthFrame("FF:FF:FF:FF:FF:FF"); // Broadcast
    delay(100);
    updateProgressBar(i);
  }
}
```