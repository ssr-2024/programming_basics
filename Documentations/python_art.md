# Paket "art Python" für VS Code
Um künstlerische Freiheiten in Python zu erlangen kann man das Paket `art` installieren.

## Installation
Um das wunderschöne Paket `art` zu installieren müssen Sie zu erst das Terminal in VS Code öffnen. Geben Sie in das Terminal `pip install art`ein. Anschliessend öffnen Sie über das Terminal Python. Geben Sie dafür folgendes ein im Terminal: `python`. Anschliessend müssen Sie noch dieses Paket importieren. Dies schaffen Sie wie folgt: geben Sie in das Terminal `from art import *` ein. Nun können Sie Ihre künstlerische Freiheiten nachgehen.

## Häufig gebrauchte Befehle
```python
Art=text2art("art") # Return ASCII text (default font) and default chr_ignore=True 
print(Art)
              _   
  __ _  _ __ | |_ 
 / _` || '__|| __|
| (_| || |   | |_ 
 \__,_||_|    \__|


#Oder

Art=text2art("art",font='block',chr_ignore=True) # Return ASCII text with block font
print(Art)


 .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. |
| |      __      | || |  _______     | || |  _________   | |
| |     /  \     | || | |_   __ \    | || | |  _   _  |  | |
| |    / /\ \    | || |   | |__) |   | || | |_/ | | \_|  | |
| |   / ____ \   | || |   |  __ /    | || |     | |      | |
| | _/ /    \ \_ | || |  _| |  \ \_  | || |    _| |_     | |
| ||____|  |____|| || | |____| |___| | || |   |_____|    | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'
```
Wie der Leser*in erkennen gibt es ganz viele tolle Möglichkeiten sich künstlerische zu betätigen. 

weitere Informationen finden Sie auf der [Homepage](https://pypi.org/project/art/). 