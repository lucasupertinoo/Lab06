from database.DB_connect import get_connection
from model.strumento import Strumento
# Nel model.py importo le classi create nella cartella model che mi servono e anche il connector al database

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

# Definisco come sopra il deposito degli strumenti rappresentando la struttura dei dati

    def get_strumenti(self) -> list[Strumento] | None:  # Annotazione di tipo: significa "restituisce una lista di strumenti oppure None"
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        cnx = get_connection()  # Chiamo get connection per connettermi
        if cnx is None:  # connessione fallita
            return None

        cursor = None
        try:
            cursor = cnx.cursor(dictionary=True)    # Mi apro un cursore dizionario
            cursor.execute("SELECT * FROM strumento")   # Esegue la query e cursor si carica di tutti i dati che ne deriva

            strumenti = []  # Mi creo la lista degli strumenti
            for row in cursor:
                strumenti.append(Strumento(row["codice"], row["tipo"], row["marca"], row["anno_acquisto"], row["valore"], bool(row["disponibile"])))
                # Appendo alla lista degli strumenti un oggetto strumento con tutte le righe prese dal database come variabili
            return strumenti
        except Exception as e:
            print(f"Errore durante la lettura degli strumenti: {e}")
            return None
        finally:
            if cursor is not None:
                cursor.close()  # Chiudere sempre il cursore
            cnx.close()

# Come sopra, mi definisco la funzione che parla con il db prendendone i dati e mettendoli in una struttura dati

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # Meglio sempre creare una connessione e un cursore per ogni funzione che interroga il DB
        cnx = get_connection()
        if cnx is None:
            return None

        cursor = None
        try:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM strumento WHERE tipo = %s", (tipo,))  # Segnaposto %s che verrà sostituita da "tipo,"
            # La virgola dopo tipo è fondamentale dato che ci permettere di assegnare un valore a tipo che è quello prelevato dal DB

            strumenti = []
            for row in cursor:
                strumenti.append(Strumento(row["codice"], row["tipo"], row["marca"], row["anno_acquisto"], row["valore"], bool(row["disponibile"])))
            return strumenti
        except Exception as e:
            print(f"Errore durante la ricerca per tipo: {e}")
            return None
        finally:
            if cursor is not None:
                cursor.close()
            cnx.close()

# Creo l'altra funzione che mi serve in base alle richieste: se devo ne servono altre le aggiungo sotto
