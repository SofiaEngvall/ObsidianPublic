
![[Images/Pasted image 20241229114356.png|600]]

4-way infrared sensor

- 1 x Infrared sensor logic converter module
- 4 x Infrared sensor pair module
- 12 x Female-to-female dupont jumper wire

"The 4-Channel Line Tracker sensor provides an easy way for line tracking. A line sensor is composed of a number cells and each cell is composed of a emitter and a receiver. The particularity of this emitter/receiver pair is that it sends light that shall be reflected by the line to be detected but not by the eventually opaque background surrounding this line. Any emitter/receiver pair that is able to make a difference between a line and the rest of ground (of a different color) can be used in a line sensor."

- Output type : Digital
- Logical IC : LM339
- Mounting hole : 3mm

Specifications:
Working voltage: DC 3.3V-5V
Working current: try to choose more than 1A power supply
Working temperature: - 10oC - +50oC
Mounting aperture: M3 screws
Detection range: 1mm to 60 CM adjustable,the closer the performance more stable,white reflects the farthest distance.
Size: in the control panel of 42mm * 38mm * 12mm (length * width * height)
Small forward 25mm * 12mm * 12mm (length * width * height)
Output interface: 6 wire interface (1234 to 4 signal output ends,+ positive power,- for the negative power is ground)
The output signal: TTL level (can be directly connected to I/0 microcontroller,infrared light reflected back to the sensor induction,the red indicator light,output low level; no infrared light,the indicator light does not shine,the output high.)
 
Applications:
A Smart car or a robot hunt ( including the black and white lines ),walking along the black line path,also known as tracing .
(2) smart car to avoid the cliff,anti- fall.
3 smart car to avoid obstacles