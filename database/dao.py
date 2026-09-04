from database.DB_connect import DBConnect

class DAO:

    @staticmethod
    def get_cromosomi():

        cromosomi = []

        try:
            conn = DBConnect.get_connection()
            cursor = conn.cursor(dictionary=True)
            query = """ SELECT DISTINCT cromosoma
                        FROM gene
                        WHERE cromosoma != 0
                    """
            cursor.execute(query)
            for row in cursor:
                cromosomi.append(row)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

        return cromosomi

    @staticmethod
    def get_connessioni():

        connessioni = []

        try:
            conn = DBConnect.get_connection()
            cursor = conn.cursor(dictionary=True)
            query = """
                       SELECT g1.cromosoma AS c1, g2.cromosoma AS c2, i.correlazione
                       FROM interazione i, gene g1, gene g2
                       WHERE i.id_gene1 = g1.id AND i.id_gene2 = g2.id 
                       AND g1.cromosoma != 0
                       AND g2.cromosoma != 0
                       AND g1.cromosoma != g2.cromosoma
                    """
            cursor.execute(query)
            for row in cursor:
                connessioni.append(row)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

        return connessioni



print(DAO.get_cromosomi())