
- Inside, there’s a disk with contacts and two “channels” (A and B) offset 90° apart.
- As you rotate, the contacts open/close in a repeating pattern, producing **square waves**.
- The two signals are slightly out of phase (called **quadrature**). This lets the ESP32 detect **both movement and direction**:
    - If A changes before B → rotation is clockwise.
    - If B changes before A → rotation is counterclockwise.
- Each step (detent) typically gives 1–4 signal changes, depending on encoder design.


standard **5-pin mechanical rotary encoder with push button**. The layout is usually like this:
**Three pins (encoder side):**
- **Left pin** → Channel A (signal A)
- **Middle pin** → Common (GND)
- **Right pin** → Channel B (signal B)

**Two pins (button side):**
- One side of the button → Common (GND, same as middle pin of the encoder side)
- Other side of the button → Switch output (goes LOW when pressed)


