# steganoCracker  
## _open source steganography tool to hide information inside pictures_  

steganoCracker is a cross-platform steganography tool written in Python, with its GUI designed in PyQt6.  
It's main purpose is to hide and reveal text in image files.  
I created this application for my own use, as it is very useful in many of CTF competitions that I participate in.  

## Features  

- Two modes - writing and reading to/from image files  
- Supports all six possible subpixel layouts (RGB, RBG, GRB, GBR, BRG, BGR)  
- Works in three different patterns (horizontal, vertical, diagonal)  
- You select pixels order, from lowest to highest or the other way around  


## Screenshots  
Down below you can see, that my application successfully recovered flags from both BCACTF-4.0 and MSHP 2023 CTF image files:  
![bcactf](https://raw.githubusercontent.com/tTargiel/steganoCracker/main/_resources/bcactf.png?raw=true)  
![mshp](https://raw.githubusercontent.com/tTargiel/steganoCracker/main/_resources/mshp.png?raw=true)  


## Installation  

steganoCracker requires [PIL] and [PyQt6] to run.  

Clone the [repository][git-repo-url], install dependencies in Python's virtual environment and run application (./main.py).  

```sh  
git clone https://github.com/tTargiel/steganoCracker.git  
cd steganoCracker/  
python3 -m venv venv
source venv/bin/activate
python3 -m pip install Pillow PyQt6 
python3 main.py
```  

## Dependencies  

steganoCracker is currently extended with the following Python dependencies.  

| Name | Link |  
| ------ | ------ |  
| PIL | [Python Package Index][PIL] |  
| PyQt6 | [Python Package Index][PyQt6] |  

## License  

LGPL-3.0  

**Free Software, Hell Yeah!**  

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)  

[steganoCracker]: <https://github.com/tTargiel/steganoCracker>  
[git-repo-url]: <ttps://github.com/tTargiel/steganoCracker.git>  
[PIL]: <https://pypi.org/project/Pillow/>  
[PyQt6]: <https://pypi.org/project/PyQt6/>  
