# Python Random Password Generator

**This program will generate a password with the given parameters given 
by the user from the command line. The parameters are:**

- ***length***: the length of the password

- ***uppercase***: if the password will have uppercase

- ***lowercase***: if the password will have lowercase

- ***number***: if the password will have numbers

- ***symbol***: if the password will have symbols

  

**The script can catch the following exceptions:**

- ***ValueError***: if the length is not an integer

- ***IndexError***: if the length not passed from the command line

- ***KeybordInterrupt***: if the user press Ctrl+C

  

**This script can be run from the command line with the following command:**
    

```bash
$ python main.py 10
```
Where 10 is the length of the password


**main.py use the following libraries:**

- random
- sys
 
 

**Formatted with black 🍰**