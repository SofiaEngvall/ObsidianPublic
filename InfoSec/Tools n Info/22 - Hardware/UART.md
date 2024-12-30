
https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter

Universal Asynchronous Receiver / Transmitter

![[Images/UART_block_diagram.svg.png|500]]

Sends data bits one by one, from the least significant to the most significant, framed by start and stop bits

Common signal levels are RS-232, RS-485, and raw TTL for short debugging links


![[Images/UART-signal.png]]

A UART frame:
- Idle (logic high (1))
- Start bit (logic low (0)): the start bit signals to the receiver that a new character is coming.
- Data bits: the next five to nine bits, depending on the code set employed, represent the character.
- Parity bit: if a parity bit is used, it would be placed after all of the data bits. The parity bit is a way for the receiving UART to tell if any data has changed during transmission.
- Stop (logic high (1)): the next one or two bits are always in the **mark** (logic high, i.e., '1') condition and called the stop bit(s). They signal to the receiver that the character is complete. Since the start bit is logic low (0) and the stop bit is logic high (1) there are always at least two guaranteed signal changes between characters. If the line is held in the logic low condition for longer than a character time, this is a break condition that can be detected by the UART.

