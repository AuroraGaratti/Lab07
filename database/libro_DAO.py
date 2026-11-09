from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""


class LibroDAO:
    def __init__(self):
        pass

    def get_generi(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")
            query = "SELECT DISTINCT genere FROM libro"
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query)
            result = []
            for row in cursor:
                if row["genere"] is not None:
                    result.append(row["genere"])
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore di connessione al database")
            return []

    def get_libri(self, id_biblioteca, genere):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")
            query = """
                SELECT id, titolo, autore, genere, anno_pubblicazione, id_biblioteca 
                FROM libro 
                WHERE (id_biblioteca = COALESCE(%s, id_biblioteca)) 
                  AND (genere = COALESCE(%s, genere))
            """

            cursor = cnx.cursor(dictionary=True)
            valori = (id_biblioteca, genere)
            cursor.execute(query, valori)

            result = []
            for row in cursor:
                result.append(Libro(
                    row["id"],
                    row["titolo"],
                    row["autore"],
                    row["genere"],
                    row["anno_pubblicazione"],
                    row["id_biblioteca"]
                ))
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore di connessione al database")
            return [] #per non avere errore con valore None restituito