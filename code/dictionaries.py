from typing import *

def print_result(name: str,percentage: Union[int,float]) -> None:
   """prints the name and corresponding percentage value in a nicely formatted format.
   
   Parameters
   ----------

   name: str,char
        name of the individual or test case to be displayed
   percentage: int, float
        percentage score to be visualized as asterisks

   Returns
   -------
        none
   """
   print(f"{name}: {'*'*(int(percentage)//10)}")


successful_tests = {
    'Janis':44,
    'Matthieu': 55,
    'Jonathan':63,
    'Robin':68,
    'Nicolas':72,
    'Eliane':77,
    'Johanna':82,
    'Nicolas':87.8,
    'Elias':93
}

for name,percentage in successful_tests.items():
    success = print_result(name,percentage)
    

name1 = "test"
name2 = 33

print_result(name1,name2)