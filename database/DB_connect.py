import mysql.connector  # Importo il connettore
from mysql.connector import errorcode   # Dal connettore importo l'errorcode da sollevare
import pathlib  # pathlib gestisce i percorsi del file system ottimizzandoli per l'OOP


def get_connection() -> mysql.connector.connection:
    try:
        cnx = mysql.connector.connect(
            option_files=f"{pathlib.Path(__file__).parent.resolve()}/connector.cnf"
        )
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
            return None
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            return None
        else:
            print(err)
            return None

# Sequenza standard di comandi, ovviamente adattando i nomi, per ottenere una connessione
