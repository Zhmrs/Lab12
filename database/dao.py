from datetime import time

from database.DB_connect import DBConnect
from model.rifugio import Rifugio
from model.connessione import Connessione

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    @staticmethod
    def readRifugi():  # nodi
        conn = DBConnect.get_connection()
        result = []
        if conn is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = conn.cursor(dictionary=True)
        query = " SELECT * FROM rifugio ORDER BY id"
        try:
            cursor.execute(query)
            for row in cursor:
                result.append(Rifugio(**row))
        except Exception as e:
            print(f"Errore durante la query readRifugio: {e}")
            result = None
        finally:
            cursor.close()
            conn.close()

        return result

    @staticmethod
    def readConnessioniAnno(anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT *
                    FROM connessione
                    WHERE anno <= %s;
                """
        try:
            cursor.execute(query, (anno,))
            for row in cursor:
                row['distanza']=float(row['distanza'])
                connessione=Connessione(row['id'],row['id_rifugio1'],row['id_rifugio2'], row['distanza'], row['difficolta'], row['durata'], row['anno'])  # lista di dizionari
                result.append(connessione)
        except Exception as e:
            print(f"Errore durante la query readConnessioniAnno: {e}")
            result = None
        finally:
            cursor.close()
            conn.close()

        return result
