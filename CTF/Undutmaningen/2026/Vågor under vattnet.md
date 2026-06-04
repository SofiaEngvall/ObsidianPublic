
```
┌──(fixit42㉿kali)-[~/Downloads/undut/vagor]
└─$ ls -la
total 6052
drwxrwxr-x 2 fixit42 fixit42    4096 Mar 21 13:14 .
drwxrwxr-x 4 fixit42 fixit42    4096 Mar 21 13:14 ..
-rw-rw-r-- 1 fixit42 fixit42 6185040 Mar 21 13:12 capture.cfile
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut/vagor]
└─$ file capture.cfile       
capture.cfile: data


┌──(fixit42㉿kali)-[~/Downloads/undut/vagor]
└─$ which urh 
urh not found
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut/vagor]
└─$ pipx install urh       
  installed package urh 2.10.0, installed using Python 3.13.11
  These apps are now globally available
    - urh
    - urh_cli
done! ✨ 🌟 ✨
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/undut/vagor]
└─$ urh
Traceback (most recent call last):
  File "/home/fixit42/.local/share/pipx/venvs/urh/lib/python3.13/site-packages/urh/ui/actions/EditSignalAction.py", line 136, in redo
    self.signal.filter_range(self.start, self.end, self.dsp_filter)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/fixit42/.local/share/pipx/venvs/urh/lib/python3.13/site-packages/urh/signalprocessing/Signal.py", line 644, in filter_range
    self._qad[start:end] = signal_functions.afp_demod(
    ~~~~~~~~~^^^^^^^^^^^
ValueError: could not broadcast input array from shape (773130,) into shape (2,)
zsh: IOT instruction  urh

```