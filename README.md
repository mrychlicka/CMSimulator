=== COFFEE MACHINE SIMULATOR ===

The purpose of this project is to create a model of fully functional automatic coffee machine. 

=== HOW IT WORKS ===
1. In first step user chooses in which mode wants to run program. 
    There are two modes:
    a. ASCII art mode - here steps of preparing coffe are visualized by ascii drawings and progres bars. 
    b. Debug mode - here uascii drawings are not visible, but text describing in details each step of working coffee machine. 
2. After choosing running mode user types which coffee he want to be made and how strong coffee should be. 
There are three coffee drinks to choose from: espresso, cappucino and latte macchiato.
3. Then preparing coffee machine is starting - it is checked if there are enough of ingredients: coffee beans, water, 
free space for grounds and optional - milk. 
If there is not enough of ingredient, user have to refill or empty container. 
4. When there are enough of ingredients, coffee drink are preparing. 
5. When coffee is prepared user can make another coffee or turn off coffee machine. 

Important thing while making this project was to make simulator which can be easily extended in functionality - like adding next 
types of coffee drinks. 

=== GETTING STARTED ===

I. PREREQUISITES
  Project was made in Python in 2.7 version. 

II. INSTALLING

  To run project there is needed to install several packages from pip: 
  1. time
  2. console_progressbar
  3. termcolor
  4. pyfiglet
  5. mock
  
III. RUNNING 
To run program, run Main.py file
  
=== AUTHOR === 
Malgorzata Rychlicka

=== OTHER === 
ASCII dwarings taken from:
1. www.asciiart.eu and
2. www.ascii.co.uk