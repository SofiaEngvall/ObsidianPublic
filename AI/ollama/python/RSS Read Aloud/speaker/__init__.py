# __init__.py - Library to simplify use of the TTS on Windows and Linux
# version 1.0
# by Sofia Engvall - FixIt42, 2023-10-22, added linux support 2025-05-04

import os

if os.name == 'nt':
    from .win_speaker import Speaker
elif os.name == 'posix':
    from .linux_speaker import Speaker
else:
    raise NotImplementedError("Unsupported OS for TTS.")
