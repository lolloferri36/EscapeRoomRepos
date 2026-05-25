import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit

class FinestraEscapeRoom(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Escape Room")
        self.resize(400, 300)

        self._gestore = GestoreCatalogo(repo)

        self.labelEscapeRoom = QLabel("ESCAPE ROOM!")
        self.bottonAvvia = QPushButton("AVVIA APPLICAZIONE")

        layout = QVBoxLayout()
        layout.addWidget(self.labelEscapeRoom)
        layout.addWidget(self.bottonAvvia)

        self.setLayout(layout)

        self.bottonAvvia.clicked.connect(self.ApriFinestraHome)

    def ApriFinestraHome(self):
        self.finestraHome = FinestraHome(self._gestore)
        self.finestraHome.show()
        self.close()


class FinestraHome(QWidget):
    def __init__(self, gestore: GestoreCatalogo):
        super().__init__()
        self.setWindowTitle("Home Escape Room")
        self.resize(400, 300)

        self._gestore = gestore  

        self.labelHome = QLabel("BENVENUTO NEL SISTEMA ESCAPE ROOM!")
        self.labelMenù = QLabel("MENU' PRINCIPALE")
        self.bottonConsultaCatalogoStanze = QPushButton("1. Consulta catalogo stanze")
        self.bottonAccediCliente = QPushButton("2. Accedi come Cliente")
        self.bottonAccediAmministratore = QPushButton("3. Accedi come Amministratore")
        self.bottonRegistrati = QPushButton("4. Registrati")
        self.bottonEsci = QPushButton("0. Esci")

        layout = QVBoxLayout()
        layout.addWidget(self.labelHome)
        layout.addWidget(self.labelMenù)
        layout.addWidget(self.bottonConsultaCatalogoStanze)
        layout.addWidget(self.bottonAccediCliente)
        layout.addWidget(self.bottonAccediAmministratore)
        layout.addWidget(self.bottonRegistrati)
        layout.addWidget(self.bottonEsci)

        self.setLayout(layout)

        self.bottonAccediCliente.clicked.connect(self.ApriAreaCliente)
        self.bottonAccediAmministratore.clicked.connect(self.ApriAreaAmministratore)
        self.bottonEsci.clicked.connect(self.close)

    def ApriAreaCliente(self):
        self.finestraCliente = AreaCliente(self._gestore) 
        self.finestraCliente.show()
        self.close()
    
    def ApriAreaAmministratore(self):
        self.finestraAdmin = AreaAmministratore(self._gestore) 
        self.finestraAdmin.show()
        self.close()

class AreaCliente(QWidget):
    def __init__(self, gestore: GestoreCatalogo):
        super().__init__()
        self._gestore = gestore

        self.setWindowTitle("AREA RISERVATA AL CLIENTE, BENVENUTO!")
        self.resize(400, 300) 

        self.labelHome1 = QLabel("GENTILE CLIENTE, BENVENUTO NELL'AREA RISERVATA!")
        self.labelMenù2 = QLabel("SELEZIONA UN'OPZIONE")
        self.bottonConsultaCatalogoStanze = QPushButton("1. Consulta catalogo stanze")
        self.bottonVisualizzaLeMiePrenotazioni = QPushButton("2. Visualizza le mie prenotazioni")
        self.bottonPrenotaStanza = QPushButton("3. Prenota stanza")
        self.bottonDisdettaPrenotazione = QPushButton("4. Disdetta prenotazione")
        self.bottonModificaPrenotazione = QPushButton("5. Modifica prenotazione")
        self.bottonAvviaPartita = QPushButton("6. Avvia partita")
        self.bottonTerminaPartita = QPushButton("7. Termina partita")
        self.bottonChiediSuggerimento = QPushButton("8. Chiedi suggerimento")
        self.bottonAbbandonaPartita = QPushButton("9. Abbandona partita")
        self.bottonStoricoPartiteGiocate = QPushButton("10. Storico partite giocate")
        self.bottonLogout = QPushButton("0. Logout (Torna al menu principale)")

        layout = QVBoxLayout()
        layout.addWidget(self.labelHome1)
        layout.addWidget(self.labelMenù2)
        layout.addWidget(self.bottonConsultaCatalogoStanze)
        layout.addWidget(self.bottonVisualizzaLeMiePrenotazioni)
        layout.addWidget(self.bottonPrenotaStanza)
        layout.addWidget(self.bottonDisdettaPrenotazione)
        layout.addWidget(self.bottonModificaPrenotazione)
        layout.addWidget(self.bottonAvviaPartita)
        layout.addWidget(self.bottonTerminaPartita)
        layout.addWidget(self.bottonChiediSuggerimento)
        layout.addWidget(self.bottonAbbandonaPartita)
        layout.addWidget(self.bottonStoricoPartiteGiocate)
        layout.addWidget(self.bottonLogout)

        self.setLayout(layout)

        self.bottonLogout.clicked.connect(self.TornaHome)   

    def TornaHome(self):
        self.finestraHome = FinestraHome(self._gestore) 
        self.finestraHome.show()
        self.close()

class AreaAmministratore(QWidget):
    def __init__(self, gestore: GestoreCatalogo):
        super().__init__()
        self._gestore = gestore

        self.setWindowTitle("AREA RISERVATA ALL'AMMINISTRATORE, BENVENUTO!")
        self.resize(400, 300) 

        self.labelHome1 = QLabel("GENTILE AMMINISTRATORE, BENVENUTO NELL'AREA RISERVATA!")
        self.labelMenù2 = QLabel("SELEZIONA UN'OPZIONE")
        self.bottonVisualizzaClientiRegistrati = QPushButton("1. Visualizza clienti registrati")
        self.bottonVisualizzaTuttePrenotazioni = QPushButton("2. Visualizza tutte le prenotazioni")
        self.bottonAggiornaCatalogoStanze = QPushButton("3. Aggiorna catalogo stanze")
        self.bottonLogout = QPushButton("0. Logout (Torna al menu principale)")

        layout = QVBoxLayout()
        layout.addWidget(self.labelHome1)
        layout.addWidget(self.labelMenù2)
        layout.addWidget(self.bottonVisualizzaClientiRegistrati)
        layout.addWidget(self.bottonVisualizzaTuttePrenotazioni)
        layout.addWidget(self.bottonAggiornaCatalogoStanze)
        layout.addWidget(self.bottonLogout)

        self.setLayout(layout)

        self.bottonLogout.clicked.connect(self.TornaHome)   

    def TornaHome(self):
        self.finestraHome = FinestraHome(self._gestore) 
        self.finestraHome.show()
        self.close()

class FinestraRegistrazione(QWidget):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("Registrazione")
        self.resize(400, 300)

        self.labelBenvenuto = QLabel("GENTILE UTENTE, BENVENUTO NELLA REGISTRAZIONE!")
        self.labelSeleziona = QLabel("INSERISCI I TUOI DATI")

        rigaEmail = QHBoxLayout()
        rigaEmail.addWidget(QLabel("Email:"))
        self.campoEmail = QLineEdit()
        self.campoEmail.setPlaceholderText("es. mario.rossi@email.com")
        rigaEmail.addWidget(self.campoEmail)


        rigaPassword = QHBoxLayout()
        rigaPassword.addWidget(QLabel("Password:"))
        self.campoPassword = QLineEdit()
        self.campoPassword.setPlaceholderText("Inserisci password")
        self.campoPassword.setEchoMode(QLineEdit.EchoMode.Password)
        rigaPassword.addWidget(self.campoPassword)

        self.labelMessaggio = QLabel("")
        self.bottonRegistrati = QPushButton("Registrati")
        self.bottonAnnulla = QPushButton("0. Annulla (Torna al menu principale)")

        layout = QVBoxLayout()
        layout.addWidget(self.labelBenvenuto)
        layout.addWidget(self.labelSeleziona)
        layout.addLayout(rigaEmail)
        layout.addLayout(rigaPassword)
        layout.addWidget(self.labelMessaggio)
        layout.addWidget(self.bottonRegistrati)
        layout.addWidget(self.bottonAnnulla)

        self.setLayout(layout)

        self.bottonRegistrati.clicked.connect(self.Registrati)
        self.bottonAnnulla.clicked.connect(self.TornaHome)

    def Registrati(self):
        email = self.campoEmail.text().strip()
        password = self.campoPassword.text().strip()


        self.labelMessaggio.setText("✓ Registrazione avvenuta con successo!")
 

    def TornaHome(self):
        self.finestraHome = FinestraHome(None) 
        self.finestraHome.show()
        self.close()

class AccessoComeAmministratoreEseguitaConSuccesso(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Accesso come amministratore avvenuto con successo!")
        self.resize(300, 200)

        labelSuccesso = QLabel("✓ Congratulazioni! L'accesso come amministratore è avvenuto con successo!")
        layout = QVBoxLayout()
        layout.addWidget(labelSuccesso)
        self.setLayout(layout)

    app = QApplication(sys.argv)
    finestra = AccessoComeAmministratoreEseguitaConSuccesso()
    finestra.show()
    sys.exit(app.exec())