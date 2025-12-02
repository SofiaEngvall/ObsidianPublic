
We get a file to download

![[Images/Pasted image 20251017145026.png]]

![[Images/Pasted image 20251017145154.png]]

Oh, we have a .net executable with a .dll file!

Let's download, extract and run [ILSpy_binaries_9.1.0.7988-x64.zip](https://github.com/icsharpcode/ILSpy/releases/download/v9.1/ILSpy_binaries_9.1.0.7988-x64.zip)
And open the ELF file (shown by typing *)

There's a menu
```c#
public static Choice RunMenu()  
{  
    Console.WriteLine("1. List Ingredients");  
    Console.WriteLine("2. Display Current Recipe");  
    Console.WriteLine("3. Add Ingredient");  
    Console.WriteLine("4. Brew Spell");  
    Console.WriteLine("5. Clear Recipe");  
    Console.WriteLine("6. Quit");  
    Console.Write("> ");  
    while (true)  
    {  
        if (int.TryParse(Console.ReadLine(), out var result))  
        {  
            switch (result)  
            {  
            case 1:  
                return Choice.ListIngredients;  
            case 2:  
                return Choice.DisplayRecipe;  
            case 3:  
                return Choice.AddIngredient;  
            case 4:  
                return Choice.BrewSpell;  
            case 5:  
                return Choice.ClearRecipe;  
            case 6:  
                Environment.Exit(0);  
                continue;  
            }  
            Console.Write($"Unknown option `{result}`\n> ");  
        }  
    }  
}
```

A list of the correct ingredients:
```c#
private static readonly string[] correct = new string[36]
{
	"Phantom Firefly Wing", "Ghastly Gourd", "Hocus Pocus Powder", "Spider Sling Silk", "Goblin's Gold", "Wraith's Tear", "Werewolf Whisker", "Ghoulish Goblet", "Cursed Skull", "Dragon's Scale Shimmer",
	"Raven Feather", "Dragon's Scale Shimmer", "Ghoulish Goblet", "Cursed Skull", "Raven Feather", "Spectral Spectacles", "Dragon's Scale Shimmer", "Haunted Hay Bale", "Wraith's Tear", "Zombie Zest Zest",
	"Serpent Scale", "Wraith's Tear", "Cursed Crypt Key", "Dragon's Scale Shimmer", "Salamander's Tail", "Raven Feather", "Wolfsbane", "Frankenstein's Lab Liquid", "Zombie Zest Zest", "Cursed Skull",
	"Ghoulish Goblet", "Dragon's Scale Shimmer", "Cursed Crypt Key", "Wraith's Tear", "Black Cat's Meow", "Wraith Whisper"
};
```

And a check for showing the flag:
```c#
private static void BrewSpell()  
{  
    if (recipe.Count < 1)  
    {  
        Console.WriteLine("You can't brew with an empty cauldron");  
        return;  
    }  
    byte[] bytes = recipe.Select((Ingredient ing) => (byte)(Array.IndexOf(IngredientNames, ing.ToString()) + 32)).ToArray();  
    if (recipe.SequenceEqual(correct.Select((string name) => new Ingredient(name))))  
    {  
        Console.WriteLine("The spell is complete - your flag is: " + Encoding.ASCII.GetString(bytes));  
        Environment.Exit(0);  
    }  
    else  
    {  
        Console.WriteLine("The cauldron bubbles as your ingredients melt away. Try another recipe.");  
    }  
}
```

All the spells in the correct spells list needs to be entered in the correct order.

It's quite a lot to enter manually so let's make a python script using pwntools:
```python
#!/usr/bin/env python3
from pwn import *

#path = "~/Downloads/rev_spellbrewery/SpellBrewery"
path = "SpellBrewery"

correct = [
    "Phantom Firefly Wing", "Ghastly Gourd", "Hocus Pocus Powder", "Spider Sling Silk", "Goblin's Gold", "Wraith's Tear", "Werewolf Whisker", "Ghoulish Goblet", "Cursed Skull", "Dragon's Scale Shimmer",
    "Raven Feather", "Dragon's Scale Shimmer", "Ghoulish Goblet", "Cursed Skull", "Raven Feather", "Spectral Spectacles", "Dragon's Scale Shimmer", "Haunted Hay Bale", "Wraith's Tear", "Zombie Zest Zest",
    "Serpent Scale", "Wraith's Tear", "Cursed Crypt Key", "Dragon's Scale Shimmer", "Salamander's Tail", "Raven Feather", "Wolfsbane", "Frankenstein's Lab Liquid", "Zombie Zest Zest", "Cursed Skull",
    "Ghoulish Goblet", "Dragon's Scale Shimmer", "Cursed Crypt Key", "Wraith's Tear", "Black Cat's Meow", "Wraith Whisper"
]

conn = process(path)
#conn = remote(host, port, timeout=5)

#conn.recv(timeout=10)

#loop through and send all ingredients
for ingredient in correct:
    print(conn.recvuntil([b'> '], timeout=5))
    conn.sendline(b'3') #option to add ingredient
    print(conn.recvuntil([b'?'], timeout=5))
    conn.sendline(ingredient) #send ingredient name

#brew
print(conn.recvuntil([b'> '], timeout=5))
conn.sendline(b'4') #option to brew
print(conn.readall())
```

---

To run the exec we needed to install .net 7. To do this we added the debian sources to `/etc/apt/sources.list`
```sh
deb http://deb.debian.org/debian bookworm main non-free-firmware
deb http://deb.debian.org/debian bookworm-updates main non-free-firmware
```

---

Script output:
```sh
┌──(rev_spellbrewery)─(fixit42㉿kali)-[~/Downloads/rev_spellbrewery]
└─$ ~/py-tools/reveng/spellbrewery.py
[!] Could not find executable 'SpellBrewery' in $PATH, using './SpellBrewery' instead
[+] Starting local process './SpellBrewery': pid 43838
b'\x1b[?1h\x1b=1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> '
b'What ingredient would you like to add?'
/home/fixit42/py-tools/reveng/spellbrewery.py:24: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  conn.sendline(ingredient) #send ingredient name
b" The cauldron fizzes as you toss in a 'Phantom Firefly Wing'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Ghastly Gourd'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Hocus Pocus Powder'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Spider Sling Silk'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Goblin's Gold'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Wraith's Tear'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Werewolf Whisker'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Ghoulish Goblet'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Cursed Skull'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Dragon's Scale Shimmer'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Raven Feather'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Dragon's Scale Shimmer'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Ghoulish Goblet'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Cursed Skull'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Raven Feather'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Spectral Spectacles'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Dragon's Scale Shimmer'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Haunted Hay Bale'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Wraith's Tear'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Zombie Zest Zest'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Serpent Scale'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Wraith's Tear'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Cursed Crypt Key'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Dragon's Scale Shimmer'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Salamander's Tail'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Raven Feather'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Wolfsbane'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Frankenstein's Lab Liquid'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Zombie Zest Zest'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Cursed Skull'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Ghoulish Goblet'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Dragon's Scale Shimmer'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Cursed Crypt Key'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Wraith's Tear'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Black Cat's Meow'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
b'What ingredient would you like to add?'
b" The cauldron fizzes as you toss in a 'Wraith Whisper'...\n1. List Ingredients\n2. Display Current Recipe\n3. Add Ingredient\n4. Brew Spell\n5. Clear Recipe\n6. Quit\n> "
[+] Receiving all data: Done (75B)
[*] Process './SpellBrewery' stopped with exit code 0 (pid 43838)
b'The spell is complete - your flag is: HTB{y0ur3_4_r34l_p0t10n_m45st3r_n0w}\n'
```

just making it a bit prettier ;D
```sh
┌──(rev_spellbrewery)─(fixit42㉿kali)-[~/Downloads/rev_spellbrewery]
└─$ ~/py-tools/reveng/spellbrewery.py
[+] Starting local process './SpellBrewery': pid 49800
\x1b[?1h\x1b=1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
/home/fixit42/py-tools/reveng/spellbrewery.py:25: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  conn.sendline(ingredient) #send ingredient name
Phantom Firefly Wing

 The cauldron fizzes as you toss in a 'Phantom Firefly Wing'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Ghastly Gourd

 The cauldron fizzes as you toss in a 'Ghastly Gourd'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Hocus Pocus Powder

 The cauldron fizzes as you toss in a 'Hocus Pocus Powder'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Spider Sling Silk

 The cauldron fizzes as you toss in a 'Spider Sling Silk'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Goblin's Gold

 The cauldron fizzes as you toss in a 'Goblin's Gold'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Wraith's Tear

 The cauldron fizzes as you toss in a 'Wraith's Tear'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Werewolf Whisker

 The cauldron fizzes as you toss in a 'Werewolf Whisker'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Ghoulish Goblet

 The cauldron fizzes as you toss in a 'Ghoulish Goblet'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Cursed Skull

 The cauldron fizzes as you toss in a 'Cursed Skull'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Dragon's Scale Shimmer

 The cauldron fizzes as you toss in a 'Dragon's Scale Shimmer'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Raven Feather

 The cauldron fizzes as you toss in a 'Raven Feather'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Dragon's Scale Shimmer

 The cauldron fizzes as you toss in a 'Dragon's Scale Shimmer'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Ghoulish Goblet

 The cauldron fizzes as you toss in a 'Ghoulish Goblet'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Cursed Skull

 The cauldron fizzes as you toss in a 'Cursed Skull'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Raven Feather

 The cauldron fizzes as you toss in a 'Raven Feather'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Spectral Spectacles

 The cauldron fizzes as you toss in a 'Spectral Spectacles'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Dragon's Scale Shimmer

 The cauldron fizzes as you toss in a 'Dragon's Scale Shimmer'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Haunted Hay Bale

 The cauldron fizzes as you toss in a 'Haunted Hay Bale'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Wraith's Tear

 The cauldron fizzes as you toss in a 'Wraith's Tear'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Zombie Zest Zest

 The cauldron fizzes as you toss in a 'Zombie Zest Zest'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Serpent Scale

 The cauldron fizzes as you toss in a 'Serpent Scale'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Wraith's Tear

 The cauldron fizzes as you toss in a 'Wraith's Tear'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Cursed Crypt Key

 The cauldron fizzes as you toss in a 'Cursed Crypt Key'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Dragon's Scale Shimmer

 The cauldron fizzes as you toss in a 'Dragon's Scale Shimmer'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Salamander's Tail

 The cauldron fizzes as you toss in a 'Salamander's Tail'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Raven Feather

 The cauldron fizzes as you toss in a 'Raven Feather'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Wolfsbane

 The cauldron fizzes as you toss in a 'Wolfsbane'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Frankenstein's Lab Liquid

 The cauldron fizzes as you toss in a 'Frankenstein's Lab Liquid'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Zombie Zest Zest

 The cauldron fizzes as you toss in a 'Zombie Zest Zest'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Cursed Skull

 The cauldron fizzes as you toss in a 'Cursed Skull'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Ghoulish Goblet

 The cauldron fizzes as you toss in a 'Ghoulish Goblet'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Dragon's Scale Shimmer

 The cauldron fizzes as you toss in a 'Dragon's Scale Shimmer'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Cursed Crypt Key

 The cauldron fizzes as you toss in a 'Cursed Crypt Key'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Wraith's Tear

 The cauldron fizzes as you toss in a 'Wraith's Tear'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Black Cat's Meow

 The cauldron fizzes as you toss in a 'Black Cat's Meow'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 3

What ingredient would you like to add?
Wraith Whisper

 The cauldron fizzes as you toss in a 'Wraith Whisper'...
1. List Ingredients
2. Display Current Recipe
3. Add Ingredient
4. Brew Spell
5. Clear Recipe
6. Quit
> 4

[+] Receiving all data: Done (75B)
[*] Process './SpellBrewery' stopped with exit code 0 (pid 49800)
The spell is complete - your flag is: HTB{y0ur3_4_r34l_p0t10n_m45st3r_n0w}
```

pretty python
```python
#!/usr/bin/env python3
from pwn import *

#path = "~/Downloads/rev_spellbrewery/SpellBrewery"
path = "./SpellBrewery"

correct = [
    "Phantom Firefly Wing", "Ghastly Gourd", "Hocus Pocus Powder", "Spider Sling Silk", "Goblin's Gold", "Wraith's Tear", "Werewolf Whisker", "Ghoulish Goblet", "Cursed Skull", "Dragon's Scale Shimmer",
    "Raven Feather", "Dragon's Scale Shimmer", "Ghoulish Goblet", "Cursed Skull", "Raven Feather", "Spectral Spectacles", "Dragon's Scale Shimmer", "Haunted Hay Bale", "Wraith's Tear", "Zombie Zest Zest",
    "Serpent Scale", "Wraith's Tear", "Cursed Crypt Key", "Dragon's Scale Shimmer", "Salamander's Tail", "Raven Feather", "Wolfsbane", "Frankenstein's Lab Liquid", "Zombie Zest Zest", "Cursed Skull",
    "Ghoulish Goblet", "Dragon's Scale Shimmer", "Cursed Crypt Key", "Wraith's Tear", "Black Cat's Meow", "Wraith Whisper"
]

conn = process(path)
#conn = remote(host, port, timeout=5)

#conn.recv(timeout=10)

#loop through and send all ingredients
for ingredient in correct:
    print(conn.recvuntil([b'> '], timeout=5).decode("utf-8"),end="")
    conn.sendline(b'3') #option to add ingredient
    print("3\n")
    print(conn.recvuntil([b'?'], timeout=5).decode("utf-8"))
    conn.sendline(ingredient) #send ingredient name
    print(ingredient+"\n")

#brew
print(conn.recvuntil([b'> '], timeout=5).decode("utf-8"),end="")
conn.sendline(b'4') #option to brew
print("4\n")
print(conn.readall().decode("utf-8"))
```