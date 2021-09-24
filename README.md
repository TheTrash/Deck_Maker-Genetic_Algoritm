# Il progetto
Lo scopo del progetto è quello di implementare un deck-builder di un proto-gioco di carte tramite un algoritmo genetico.

Si prende una popolazione di _N_ deck e si fanno evolvere gli elementi della popolazione.\
Ogni deck è un individuo della popolazione e ogni carta è il suo _cercare_

## inizializzazione della popolazione
Si creano gli n a partire da una colezione di carte fissa ( ogni deck avrà le carte dello stesso set )
## Riproduzione
Si mischiano due mazzi secondo alcuni criteri
## Mutazione
Si muta una o più carte del mazzo
## Valutazione
Si fa una stima della bontà del mazzo facendo combatterlo con gli altri mazzi / contro se stesso _m_ volte


#  Il  Gioco
## Carte
Le carte sono composte da tre componenti principali
    - attacco
    - difesa
    - abilità

Attacco:
	può variare da 2 a 7
Difesa:
	Può variare da 3 a 8
Abilità:

Alcune carte potrebbero non avere abilità.
Quelle che la possiedono attivano la propria in alcuni momenti della partita

    Attaccante : +1 all'attacco
    Difensore : +1 alla difesa
    Esperto: +1 punto aggiuntivo se sopravvive alle battaglie
    
Le abilità possono ripresentarsi più volte nella stessa carta. ( esempio Attacco, Attacco fornirà + 2 all'attacco base della carta )

## Regole
Ogni giocatore ha un mazzo di 10 carte e un contatore di punti vittoria ogni turno si pescano 3 carte e si mettono in campo 
Si fanno combattere valutando rispettivamente attacco e punti vita 
Ogni carta che rimane in campo genera un punto vittoria all'avversario

Il primo che arriva a 20 punti vittoria vince
Svolgimento del combattimento ( Turno ): 
Ogni combattimento è diviso in round: 
In un round ogni carta combatte con quella che ha davanti se al termine del round entrambe le carte hanno ancora punti difesa si passa al round successivo

Quando le carte del mazzo finiscono, esso si rimescola e si continua la partita.


# TO DO
* Impostare la generazione dei deck in modo che escano liste ordinate

* Sistemare la mutazione con le rispettive probabilità:
    possibile soluzione:\ 
    lancio di una moneta\
    + testa cambiare una carta ( se ordinato di pari valore del valore desiderato)
    + croce cambiare la skill della carta

* Ottimizzare il simulatore delle battaglie
* Migliorare i commenti del codice
* Scrivere un piccolo report
### se ci rimane tempo
* aggiungere un piccolo test di parametrizzazione
* aggiungere un plot dell'evoluzione della popolazione
