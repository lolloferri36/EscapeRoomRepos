# Gestionale Escape Room

Sistema informativo per la gestione di un complesso di escape room con 4 stanze.
Implementato in Python 3, architettura **MVC** ispirata al pattern **ECB** (Entity–Control–Boundary).

---

# Come avviare


cd gestion.escape
python main.py



**Requisiti:** Python 3.8+, nessuna dipendenza esterna.

---

# Credenziali predefinite
Ruolo: Amministratore
Email: "admin@escape.it"
Password: "Admin123!"


I clienti hanno la possibilità di registrarsi  attraverso il menu principale. 
Una volta registrati, le loro credenziali vengono salvate e saranno validate in fase di accesso.

---

## Struttura del progetto


gestionaleEscapeRoom/
├── main.py                         # Punto di ingresso; gestione sessione
├── MODELS/                         # Entity (dati + serializzazione)
│   ├── UTENTE.py                   # Base: email, password, statoAccesso
│   ├── CLIENTE.py                  # Utente registrato (UUID, prenotazioni)
│   ├── AMMINISTRATORE.py           # Utente pre-registrato, gestisce il sistema
│   ├── STANZA.py                   # 4 stanze, tariffa €50/90 min
│   ├── PRENOTAZIONE.py             # Associazione Cliente–Stanza, stato "confermata"/"disdetta"
│   └── PARTITA.py                  # Sessione di gioco con cronometro (solo in memoria)
├── REPOSITORY/                     
│   ├── AMMINISTRATORE_REPOSITORY.py
│   ├── CLIENTE_REPOSITORY.py
│   ├── PRENOTAZIONE_REPOSITORY.py
│   └── STANZA_REPOSITORY.py
├── SERVICES/                       
│   ├── GESTORE_ACCOUNT.py          # Registrazione e login
│   ├── GESTORE_CATALOGO.py         # Consulta e aggiornamento stanze
│   ├── GESTORE_CLIENTE.py          # Visualizzazione clienti (admin)
│   ├── GESTORE_PARTITA.py          # Andamento partita ed elenco partite
│   └── GESTORE_PRENOTAZIONE.py     # Prenota, disdetta, modifica, partita
├── TESTS/                          
│   ├── test_AMMINISTRATORE.py      # Test per l'entity Amministratore
│   ├── test_CLIENTE.py             # Test per l'entity Cliente
│   ├── test_PARTITA.py             # Test per l'entity Partita
│   ├── test_PRENOTAZIONE.py         # Test per l'entity Prenotazione
│   ├── test_STANZA.py              # Test per l'entity Stanza
│   ├── test_UTENTE.py              # Test per l'entity Utente base
│   └── test_GESTORE_CATALOGO.py    # Test per il gestore Catalogo
├── VIEWS/                          # Boundary (interfaccia terminale)      
│   ├── INTERFACCIA_ACCOUNT.py
│   ├── INTERFACCIA_CATALOGO.py
│   ├── INTERFACCIA_CLIENTE.py
│   ├── INTERFACCIA_PARTITA.py
│   └── INTERFACCIA_PRENOTAZIONE.py
└── DATA(JSON)/                     # File di persistenza
    ├── AMMINISTRATORE.json         # Singolo oggetto (admin pre-registrato)
    ├── CLIENTI.json                # Array di clienti registrati
    ├── PARTITE.json                # Array di partite terminate         
    ├─ PRENOTAZIONI.json            # Array di prenotazioni
    └── STANZE.json                 # Array di 4 stanze



### Architettura ECB (Entity --> Control --> Boundary).

Ogni layer comunica solo con il layer adiacente:

- Boundary (VIEWS) parla solo con Control (SERVICES)
- Control parla con Repository e Entity
- Le Boundary non accedono mai direttamente a Entity o Repository

### Persistenza JSON

Quando il programma viene avviato, il Repository legge il file JSON (carica()) e trasforma quel testo in oggetti Python utilizzabili dal codice tramite il metodo fromDict().

Quando fai una modifica, il programma fa il contrario: trasforma gli oggetti in testo tramite toDict() e il Repository sovrascrive il file JSON (salva()) per memorizzarli sul computer in modo permanente."

### main

main.py controlla l'accesso al programma tramite la variabile utente_corrente.

Se la variabile è vuota (None), il programma mostra il menu di login. Se l'utente fa l'accesso, il programma riconosce se si tratta di un cliente o di un amministratore e, grazie al controllo isinstance(), mostra a schermo solo il menu con le funzionalità dedicate a quel tipo di utente


### Vincolo 24 ore 

Disdetta e modifica controllano `prenotazione.getDatetime() - datetime.now() >= timedelta(hours=24)`. Se il vincolo non è rispettato, il service restituisce un messaggio di errore senza modificare i dati.



### Login sicuro


Email e password vengono verificate in `trovaPerEmailEPassword()`.

### Partita (RF06, RF07)

`Partita` vive solo in memoria durante la sessione (non persiste su file). `GestorePrenotazione` mantiene `_partita_corrente`. Il cronometro usa `datetime.now()` all'avvio e alla fine; l'esito è vittoria se `tempoTrascorso <= 90 min`.

### Admin pre-registrato

`AMMINISTRATORE.json` contiene un singolo oggetto JSON (non un array), rispecchiando che l'admin è unico e non si auto-registra.

### Mockup:

Per eseguire il codice dei mockup:
-dal terminale creare l'ambiente virtuale (.venv) con il comando "python -m venv .venv"
-dal terminale attivare l'ambiente virtuale (.venv) con il comando ".venv\Scripts\Activate"
-installare la libreria PyQt6 digitando "pip install PyQt6"
