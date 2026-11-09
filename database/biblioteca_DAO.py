from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = "SELECT id, nome, indirizzo FROM biblioteca "
            cursor.execute(query)
            for row in cursor:
                result.append(Biblioteca(row["id"],row["nome"],row["indirizzo"]))
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore di connessione al database")
            return[]# per non avere errore con valore None restituito