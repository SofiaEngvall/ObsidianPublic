
```sh
┌──(kali㉿kali)-[~]
└─$ cd thm          
                                                                                                                              
┌──(kali㉿kali)-[~/thm]
└─$ cd valley
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ ls -la
total 54664
drwxr-xr-x  2 kali kali    4096 May 16 18:30 .
drwxr-xr-x 20 kali kali    4096 May 16 18:23 ..
-rw-r--r--  1 kali kali 2473315 May 16 18:23 1.jpeg
-rw-r--r--  1 kali kali 2275927 May 16 18:24 10.jpeg
-rw-r--r--  1 kali kali  627909 May 16 18:24 11.jpeg
-rw-r--r--  1 kali kali 2203486 May 16 18:24 12.jpeg
-rw-r--r--  1 kali kali 3673497 May 16 18:28 13.jpeg
-rw-r--r--  1 kali kali 3838999 May 16 18:30 14.jpeg
-rw-r--r--  1 kali kali 3477315 May 16 18:30 15.jpeg
-rw-r--r--  1 kali kali 2468462 May 16 18:30 16.jpeg
-rw-r--r--  1 kali kali 3551807 May 16 18:30 17.jpeg
-rw-r--r--  1 kali kali 2036137 May 16 18:30 18.jpeg
-rw-r--r--  1 kali kali 3627113 May 16 18:24 2.jpeg
-rw-r--r--  1 kali kali  421858 May 16 18:24 3.jpeg
-rw-r--r--  1 kali kali 7389635 May 16 18:24 4.jpeg
-rw-r--r--  1 kali kali 1426557 May 16 18:24 5.jpeg
-rw-r--r--  1 kali kali 2115495 May 16 18:24 6.jpeg
-rw-r--r--  1 kali kali 5217844 May 16 18:24 7.jpeg
-rw-r--r--  1 kali kali 7919631 May 16 18:24 8.jpeg
-rw-r--r--  1 kali kali 1190575 May 16 18:24 9.jpeg
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ exiftool --help
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ exiftool 1.jpeg
ExifTool Version Number         : 12.76
File Name                       : 1.jpeg
Directory                       : .
File Size                       : 2.5 MB
File Modification Date/Time     : 2024:05:16 18:23:20+02:00
File Access Date/Time           : 2024:05:16 18:23:20+02:00
File Inode Change Date/Time     : 2024:05:16 18:23:50+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Little CMS
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2012:01:25 03:41:57
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : 
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Little CMS
Profile ID                      : 0
Profile Description             : c2
Profile Copyright               : IX
Media White Point               : 0.9642 1 0.82491
Media Black Point               : 0.01205 0.0125 0.01031
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Red Tone Reproduction Curve     : (Binary data 64 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 64 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 64 bytes, use -b option to extract)
Image Width                     : 3024
Image Height                    : 4032
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 3024x4032
Megapixels                      : 12.2
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ exiftool 2.jpeg
ExifTool Version Number         : 12.76
File Name                       : 2.jpeg
Directory                       : .
File Size                       : 3.6 MB
File Modification Date/Time     : 2024:05:16 18:24:01+02:00
File Access Date/Time           : 2024:05:16 18:24:01+02:00
File Inode Change Date/Time     : 2024:05:16 18:24:04+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Little CMS
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2012:01:25 03:41:57
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : 
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Little CMS
Profile ID                      : 0
Profile Description             : c2
Profile Copyright               : IX
Media White Point               : 0.9642 1 0.82491
Media Black Point               : 0.01205 0.0125 0.01031
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Red Tone Reproduction Curve     : (Binary data 64 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 64 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 64 bytes, use -b option to extract)
Image Width                     : 6000
Image Height                    : 4000
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 6000x4000
Megapixels                      : 24.0
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ exiftool 3.jpeg
ExifTool Version Number         : 12.76
File Name                       : 3.jpeg
Directory                       : .
File Size                       : 422 kB
File Modification Date/Time     : 2024:05:16 18:24:06+02:00
File Access Date/Time           : 2024:05:16 18:24:06+02:00
File Inode Change Date/Time     : 2024:05:16 18:24:07+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Little CMS
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2012:01:25 03:41:57
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : 
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Little CMS
Profile ID                      : 0
Profile Description             : c2
Profile Copyright               : IX
Media White Point               : 0.9642 1 0.82491
Media Black Point               : 0.01205 0.0125 0.01031
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Red Tone Reproduction Curve     : (Binary data 64 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 64 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 64 bytes, use -b option to extract)
Image Width                     : 2592
Image Height                    : 1936
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2592x1936
Megapixels                      : 5.0
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ exiftool 4.jpeg
ExifTool Version Number         : 12.76
File Name                       : 4.jpeg
Directory                       : .
File Size                       : 7.4 MB
File Modification Date/Time     : 2024:05:16 18:24:11+02:00
File Access Date/Time           : 2024:05:16 18:24:11+02:00
File Inode Change Date/Time     : 2024:05:16 18:24:13+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Little CMS
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2012:01:25 03:41:57
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : 
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Little CMS
Profile ID                      : 0
Profile Description             : c2
Profile Copyright               : IX
Media White Point               : 0.9642 1 0.82491
Media Black Point               : 0.01205 0.0125 0.01031
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Red Tone Reproduction Curve     : (Binary data 64 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 64 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 64 bytes, use -b option to extract)
Image Width                     : 6000
Image Height                    : 4000
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 6000x4000
Megapixels                      : 24.0
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ exiftool 5.jpeg
ExifTool Version Number         : 12.76
File Name                       : 5.jpeg
Directory                       : .
File Size                       : 1427 kB
File Modification Date/Time     : 2024:05:16 18:24:16+02:00
File Access Date/Time           : 2024:05:16 18:24:16+02:00
File Inode Change Date/Time     : 2024:05:16 18:24:18+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Little CMS
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2012:01:25 03:41:57
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : 
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Little CMS
Profile ID                      : 0
Profile Description             : c2
Profile Copyright               : IX
Media White Point               : 0.9642 1 0.82491
Media Black Point               : 0.01205 0.0125 0.01031
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Red Tone Reproduction Curve     : (Binary data 64 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 64 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 64 bytes, use -b option to extract)
Image Width                     : 6000
Image Height                    : 4000
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 6000x4000
Megapixels                      : 24.0
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ exiftool 6.jpeg
ExifTool Version Number         : 12.76
File Name                       : 6.jpeg
Directory                       : .
File Size                       : 2.1 MB
File Modification Date/Time     : 2024:05:16 18:24:21+02:00
File Access Date/Time           : 2024:05:16 18:24:21+02:00
File Inode Change Date/Time     : 2024:05:16 18:24:24+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Little CMS
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2012:01:25 03:41:57
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : 
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Little CMS
Profile ID                      : 0
Profile Description             : c2
Profile Copyright               : IX
Media White Point               : 0.9642 1 0.82491
Media Black Point               : 0.01205 0.0125 0.01031
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Red Tone Reproduction Curve     : (Binary data 64 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 64 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 64 bytes, use -b option to extract)
Image Width                     : 4032
Image Height                    : 3024
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4032x3024
Megapixels                      : 12.2
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ exiftool 7.jpeg
ExifTool Version Number         : 12.76
File Name                       : 7.jpeg
Directory                       : .
File Size                       : 5.2 MB
File Modification Date/Time     : 2024:05:16 18:24:29+02:00
File Access Date/Time           : 2024:05:16 18:24:28+02:00
File Inode Change Date/Time     : 2024:05:16 18:24:30+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Little CMS
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2012:01:25 03:41:57
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : 
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Little CMS
Profile ID                      : 0
Profile Description             : c2
Profile Copyright               : IX
Media White Point               : 0.9642 1 0.82491
Media Black Point               : 0.01205 0.0125 0.01031
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Red Tone Reproduction Curve     : (Binary data 64 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 64 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 64 bytes, use -b option to extract)
Image Width                     : 6000
Image Height                    : 4000
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 6000x4000
Megapixels                      : 24.0
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ exiftool 8.jpeg
ExifTool Version Number         : 12.76
File Name                       : 8.jpeg
Directory                       : .
File Size                       : 7.9 MB
File Modification Date/Time     : 2024:05:16 18:24:37+02:00
File Access Date/Time           : 2024:05:16 18:24:36+02:00
File Inode Change Date/Time     : 2024:05:16 18:24:38+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Little CMS
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2012:01:25 03:41:57
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : 
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Little CMS
Profile ID                      : 0
Profile Description             : c2
Profile Copyright               : IX
Media White Point               : 0.9642 1 0.82491
Media Black Point               : 0.01205 0.0125 0.01031
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Red Tone Reproduction Curve     : (Binary data 64 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 64 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 64 bytes, use -b option to extract)
Image Width                     : 6000
Image Height                    : 4000
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 6000x4000
Megapixels                      : 24.0
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ exiftool 9.jpeg
ExifTool Version Number         : 12.76
File Name                       : 9.jpeg
Directory                       : .
File Size                       : 1191 kB
File Modification Date/Time     : 2024:05:16 18:24:42+02:00
File Access Date/Time           : 2024:05:16 18:24:42+02:00
File Inode Change Date/Time     : 2024:05:16 18:24:44+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Little CMS
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2012:01:25 03:41:57
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : 
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Little CMS
Profile ID                      : 0
Profile Description             : c2
Profile Copyright               : IX
Media White Point               : 0.9642 1 0.82491
Media Black Point               : 0.01205 0.0125 0.01031
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Red Tone Reproduction Curve     : (Binary data 64 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 64 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 64 bytes, use -b option to extract)
Image Width                     : 4032
Image Height                    : 3024
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4032x3024
Megapixels                      : 12.2
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ exiftool 10.jpeg
ExifTool Version Number         : 12.76
File Name                       : 10.jpeg
Directory                       : .
File Size                       : 2.3 MB
File Modification Date/Time     : 2024:05:16 18:24:49+02:00
File Access Date/Time           : 2024:05:16 18:24:49+02:00
File Inode Change Date/Time     : 2024:05:16 18:24:51+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Little CMS
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2012:01:25 03:41:57
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : 
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Little CMS
Profile ID                      : 0
Profile Description             : c2
Profile Copyright               : IX
Media White Point               : 0.9642 1 0.82491
Media Black Point               : 0.01205 0.0125 0.01031
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Red Tone Reproduction Curve     : (Binary data 64 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 64 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 64 bytes, use -b option to extract)
Image Width                     : 4032
Image Height                    : 3024
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4032x3024
Megapixels                      : 12.2
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ exiftool 11.jpeg
ExifTool Version Number         : 12.76
File Name                       : 11.jpeg
Directory                       : .
File Size                       : 628 kB
File Modification Date/Time     : 2024:05:16 18:24:54+02:00
File Access Date/Time           : 2024:05:16 18:24:54+02:00
File Inode Change Date/Time     : 2024:05:16 18:24:56+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Little CMS
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2012:01:25 03:41:57
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : 
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Little CMS
Profile ID                      : 0
Profile Description             : c2
Profile Copyright               : IX
Media White Point               : 0.9642 1 0.82491
Media Black Point               : 0.01205 0.0125 0.01031
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Red Tone Reproduction Curve     : (Binary data 64 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 64 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 64 bytes, use -b option to extract)
Image Width                     : 3024
Image Height                    : 4032
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 3024x4032
Megapixels                      : 12.2
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ exiftool 12.jpeg
ExifTool Version Number         : 12.76
File Name                       : 12.jpeg
Directory                       : .
File Size                       : 2.2 MB
File Modification Date/Time     : 2024:05:16 18:24:59+02:00
File Access Date/Time           : 2024:05:16 18:24:59+02:00
File Inode Change Date/Time     : 2024:05:16 18:25:01+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Little CMS
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2012:01:25 03:41:57
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : 
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Little CMS
Profile ID                      : 0
Profile Description             : c2
Profile Copyright               : IX
Media White Point               : 0.9642 1 0.82491
Media Black Point               : 0.01205 0.0125 0.01031
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Red Tone Reproduction Curve     : (Binary data 64 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 64 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 64 bytes, use -b option to extract)
Image Width                     : 5770
Image Height                    : 3847
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 5770x3847
Megapixels                      : 22.2
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ exiftool 13.jpeg
ExifTool Version Number         : 12.76
File Name                       : 13.jpeg
Directory                       : .
File Size                       : 3.7 MB
File Modification Date/Time     : 2024:05:16 18:28:27+02:00
File Access Date/Time           : 2024:05:16 18:28:26+02:00
File Inode Change Date/Time     : 2024:05:16 18:29:59+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Little CMS
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2012:01:25 03:41:57
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : 
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Little CMS
Profile ID                      : 0
Profile Description             : c2
Profile Copyright               : IX
Media White Point               : 0.9642 1 0.82491
Media Black Point               : 0.01205 0.0125 0.01031
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Red Tone Reproduction Curve     : (Binary data 64 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 64 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 64 bytes, use -b option to extract)
Image Width                     : 6000
Image Height                    : 4000
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 6000x4000
Megapixels                      : 24.0
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ exiftool 14.jpeg
ExifTool Version Number         : 12.76
File Name                       : 14.jpeg
Directory                       : .
File Size                       : 3.8 MB
File Modification Date/Time     : 2024:05:16 18:30:04+02:00
File Access Date/Time           : 2024:05:16 18:30:03+02:00
File Inode Change Date/Time     : 2024:05:16 18:30:07+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Little CMS
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2012:01:25 03:41:57
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : 
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Little CMS
Profile ID                      : 0
Profile Description             : c2
Profile Copyright               : IX
Media White Point               : 0.9642 1 0.82491
Media Black Point               : 0.01205 0.0125 0.01031
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Red Tone Reproduction Curve     : (Binary data 64 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 64 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 64 bytes, use -b option to extract)
Image Width                     : 5799
Image Height                    : 3866
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 5799x3866
Megapixels                      : 22.4
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ exiftool 15.jpeg
ExifTool Version Number         : 12.76
File Name                       : 15.jpeg
Directory                       : .
File Size                       : 3.5 MB
File Modification Date/Time     : 2024:05:16 18:30:11+02:00
File Access Date/Time           : 2024:05:16 18:30:11+02:00
File Inode Change Date/Time     : 2024:05:16 18:30:13+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Little CMS
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2012:01:25 03:41:57
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : 
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Little CMS
Profile ID                      : 0
Profile Description             : c2
Profile Copyright               : IX
Media White Point               : 0.9642 1 0.82491
Media Black Point               : 0.01205 0.0125 0.01031
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Red Tone Reproduction Curve     : (Binary data 64 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 64 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 64 bytes, use -b option to extract)
Image Width                     : 6000
Image Height                    : 4000
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 6000x4000
Megapixels                      : 24.0
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ exiftool 16.jpeg
ExifTool Version Number         : 12.76
File Name                       : 16.jpeg
Directory                       : .
File Size                       : 2.5 MB
File Modification Date/Time     : 2024:05:16 18:30:25+02:00
File Access Date/Time           : 2024:05:16 18:30:25+02:00
File Inode Change Date/Time     : 2024:05:16 18:30:28+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Little CMS
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2012:01:25 03:41:57
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : 
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Little CMS
Profile ID                      : 0
Profile Description             : c2
Profile Copyright               : IX
Media White Point               : 0.9642 1 0.82491
Media Black Point               : 0.01205 0.0125 0.01031
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Red Tone Reproduction Curve     : (Binary data 64 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 64 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 64 bytes, use -b option to extract)
Image Width                     : 6000
Image Height                    : 4000
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 6000x4000
Megapixels                      : 24.0
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ exiftool 17.jpeg
ExifTool Version Number         : 12.76
File Name                       : 17.jpeg
Directory                       : .
File Size                       : 3.6 MB
File Modification Date/Time     : 2024:05:16 18:30:32+02:00
File Access Date/Time           : 2024:05:16 18:30:32+02:00
File Inode Change Date/Time     : 2024:05:16 18:30:34+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Little CMS
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2012:01:25 03:41:57
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : 
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Little CMS
Profile ID                      : 0
Profile Description             : c2
Profile Copyright               : IX
Media White Point               : 0.9642 1 0.82491
Media Black Point               : 0.01205 0.0125 0.01031
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Red Tone Reproduction Curve     : (Binary data 64 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 64 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 64 bytes, use -b option to extract)
Image Width                     : 5994
Image Height                    : 3996
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 5994x3996
Megapixels                      : 24.0
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ exiftool 18.jpeg
ExifTool Version Number         : 12.76
File Name                       : 18.jpeg
Directory                       : .
File Size                       : 2.0 MB
File Modification Date/Time     : 2024:05:16 18:30:36+02:00
File Access Date/Time           : 2024:05:16 18:30:36+02:00
File Inode Change Date/Time     : 2024:05:16 18:30:38+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Little CMS
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2012:01:25 03:41:57
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : 
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Little CMS
Profile ID                      : 0
Profile Description             : c2
Profile Copyright               : IX
Media White Point               : 0.9642 1 0.82491
Media Black Point               : 0.01205 0.0125 0.01031
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Red Tone Reproduction Curve     : (Binary data 64 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 64 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 64 bytes, use -b option to extract)
Image Width                     : 5743
Image Height                    : 3829
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 5743x3829
Megapixels                      : 22.0
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ ls -la          
total 54972
drwxr-xr-x  2 kali kali    4096 May 16 20:36 .
drwxr-xr-x 20 kali kali    4096 May 16 18:23 ..
-rw-r--r--  1 kali kali 2473315 May 16 18:23 1.jpeg
-rw-r--r--  1 kali kali 2275927 May 16 18:24 10.jpeg
-rw-r--r--  1 kali kali  627909 May 16 18:24 11.jpeg
-rw-r--r--  1 kali kali 2203486 May 16 18:24 12.jpeg
-rw-r--r--  1 kali kali 3673497 May 16 18:28 13.jpeg
-rw-r--r--  1 kali kali 3838999 May 16 18:30 14.jpeg
-rw-r--r--  1 kali kali 3477315 May 16 18:30 15.jpeg
-rw-r--r--  1 kali kali 2468462 May 16 18:30 16.jpeg
-rw-r--r--  1 kali kali 3551807 May 16 18:30 17.jpeg
-rw-r--r--  1 kali kali 2036137 May 16 18:30 18.jpeg
-rw-r--r--  1 kali kali 3627113 May 16 18:24 2.jpeg
-rw-r--r--  1 kali kali  421858 May 16 18:24 3.jpeg
-rw-r--r--  1 kali kali 7389635 May 16 18:24 4.jpeg
-rw-r--r--  1 kali kali 1426557 May 16 18:24 5.jpeg
-rw-r--r--  1 kali kali 2115495 May 16 18:24 6.jpeg
-rw-r--r--  1 kali kali 5217844 May 16 18:24 7.jpeg
-rw-r--r--  1 kali kali 7919631 May 16 18:24 8.jpeg
-rw-r--r--  1 kali kali 1190575 May 16 18:24 9.jpeg
-rw-r--r--  1 kali kali  314992 May 16 20:36 photo-1585640073714-8caeb6f11f66.avif
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ exiftool photo-1585640073714-8caeb6f11f66.avif 
ExifTool Version Number         : 12.76
File Name                       : photo-1585640073714-8caeb6f11f66.avif
Directory                       : .
File Size                       : 315 kB
File Modification Date/Time     : 2024:05:16 20:36:35+02:00
File Access Date/Time           : 2024:05:16 20:36:35+02:00
File Inode Change Date/Time     : 2024:05:16 20:36:35+02:00
File Permissions                : -rw-r--r--
File Type                       : AVIF
File Type Extension             : avif
MIME Type                       : image/avif
Major Brand                     : AV1 Image File Format (.AVIF)
Minor Version                   : 0.0.0
Compatible Brands               : avif, mif1, miaf, MA1B
Handler Type                    : Picture
Handler Description             : libavif
Primary Item Reference          : 1
Image Width                     : 2340
Image Height                    : 1560
Image Spatial Extent            : 2340x1560
Image Pixel Depth               : 8 8 8
AV1 Configuration Version       : 1
Chroma Format                   : YUV 4:2:0
Chroma Sample Position          : Unknown
Profile CMM Type                : Linotronic
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 1998:02:09 06:49:00
Profile File Signature          : acsp
Primary Platform                : Microsoft Corporation
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : Hewlett-Packard
Device Model                    : sRGB
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Hewlett-Packard
Profile ID                      : 0
Profile Copyright               : Copyright (c) 1998 Hewlett-Packard Company
Profile Description             : sRGB IEC61966-2.1
Media White Point               : 0.95045 1 1.08905
Media Black Point               : 0 0 0
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Device Mfg Desc                 : IEC http://www.iec.ch
Device Model Desc               : IEC 61966-2.1 Default RGB colour space - sRGB
Viewing Cond Desc               : Reference Viewing Condition in IEC61966-2.1
Viewing Cond Illuminant         : 19.6445 20.3718 16.8089
Viewing Cond Surround           : 3.92889 4.07439 3.36179
Viewing Cond Illuminant Type    : D50
Luminance                       : 76.03647 80 87.12462
Measurement Observer            : CIE 1931
Measurement Backing             : 0 0 0
Measurement Geometry            : Unknown
Measurement Flare               : 0.999%
Measurement Illuminant          : D65
Technology                      : Cathode Ray Tube Display
Red Tone Reproduction Curve     : (Binary data 2060 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 2060 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 2060 bytes, use -b option to extract)
Color Profiles                  : nclx
Color Primaries                 : BT.709
Transfer Characteristics        : sRGB or sYCC
Matrix Coefficients             : BT.601
Video Full Range Flag           : 1
Media Data Size                 : 311553
Media Data Offset               : 3439
Image Size                      : 2340x1560
Megapixels                      : 3.7
```
