# Principy tvorby softveru
### Zadanie ulohy

Program uchováva zoznam učastníkov a ich aktuálny stav bodov v sútaži.
Po spustení si program od užívateľa vypýta heslo. Potom program čaká na príkazy od užívateľa,
ktoré následne vykoná.

##### Zoznam príkazov:

`points <name> <number>`
*  Pridá hráčovi `<name> <number>` bodov. Číslo môže byť aj záporné.
*  Ak hráč `<name>` ešte nie je evidovaný pridá ho do zoznamu s <number> bodmi.

`reduce <number>`
*  Zníži počet bodov každého hráča o <number>%. Výsledok sa zaokrúhli na celé čísla nadol.

`junior <name>`
*  Označí, že hráč `<name>` je junior

`ranking` 
*  Vypíše celé poradie. Hráčov zoradíme podľa počtu bodov.

`ranking junior`
*  Vypíše poradie medzi juniormi.

`quit`
*  Ukončí program.


Ak užívateľ zadá príkazy points, reduce, junior, a quit systém si najprv vypýta password
a príkaz vykoná iba v prípade, že password je správny.





### Subory
Uloha sa zklada z nasledujucich suborov:
* main.py
* commands.py
* decorator.py
* login.py
* database.py
* database.db

Struktura programu:

![alt text](documentation/image.png)


### main.py
Toto je spustitelny subor, ktory loaduje moduly a parsuje vstup a podla toho vola Command triedy s parametramy.
Predtym vsak vytvory objekt login, kde si poprosi zadavacie heslo.


### commands.py
Module, ktory obsahuje jednoduchy navrhovy vzor command.
Abstraktna trieda zaobaluje referenciu na databazu z modulu ```database.py```. 
Obsahuje este triedu CommandHistory, ktora niakoniec vykonava Command objekt, ktory dostane a ulozi ho do historie


### decorator.py
Modul, ktory obsahuje jedniny triedu **login_decorator**. Pomocou tejto triedy dekorujeme triedy z ```commands.py```, ktore pri ich vykonani maju vypytat heslo. 


### login.py
Modul, ktory obsahuje triedy Login, ktora je typu singleton.
Dovod, je taky, ze pri jej inicializacii v ```main.py``` sa nastavy heslo, ktore chceme nastavit len raz.
Trieda Login sa vytvara v kazdom dekoratore, co bys sposobilo, ze pri kazdom novom prikaze, by sa vytvaralo nove heslo.


### database.py
Jednoducha trieda, ktora obaluje databazu ```database.db```.
Vyuziva modul [**sqlite3**](https://docs.python.org/3/library/sqlite3.html).

### database.db
Subor, ktory obsahuje samostatnu databazu.
