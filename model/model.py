from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
- Rappresenta la struttura dati

- Si occupa di gestire lo stato dell'applicazione

- Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)

'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

        self.lista_generi = []
        self.lista_biblioteche = []
        self.lista_libri=[]

        self.get_generi()
        self.get_biblioteche()


    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca: str, genere: str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        biblioteca= None if biblioteca == 'None' or biblioteca=="" else int(biblioteca)
        genere= None if genere == 'None' else genere
        self.lista_libri=self._libro_dao.get_libri(biblioteca, genere)
        return self.lista_libri

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        self.lista_generi = self._libro_dao.get_generi()
        return self.lista_generi

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        self.lista_biblioteche = self._biblioteca_dao.get_biblioteche()
        return self.lista_biblioteche