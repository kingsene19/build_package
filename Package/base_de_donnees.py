"""
Ceci est un module qui a une classe Database pour la création et la manipulation de bases de données
"""


import sqlite3


class Database:
    """
    Classe Database établit la connexion avec la base de données et permet sa manipulation
    """

    def __init__(self):
        """
        Cette méthode est appelé lors de la création d'une instance de la classe Database.
        Elle permet de créer la base de données.

        :return: Un objet de classe Database
        :rtype: Database

        :Exemple:

        >>> db = Database()
        Connexion effectué avec succès
        """
        try:
            self.conn = sqlite3.connect("dicgit_database.db")
            self.cursor = self.conn.cursor()
            print("Connexion effectué avec succès")
        except sqlite3.Error as err:
            print("Sql error: %s" % (" ".join(err.args)))

    def create_table_db(self):
        """
        Cette méthode permet de créer une table ``dicgit``

        .. note::
            Les champs de la table sont nom, prenom, id_ept, telephone et niveau.

        :return: None
        :rtype: NoneType

        :Exemple:

        >>> db = Database()
        Connexion effectué avec succès
        >>> db.create_table_db()
        La table a été créée!
        La connexion a été fermée
        """
        try:
            self.conn = sqlite3.connect("dicgit_database.db")
            self.cursor = self.conn.cursor()
            query = (
                "CREATE TABLE dicgit "
                "(nom text, "
                "prenom text, "
                "id_ept integer PRIMARY KEY, "
                "niveau text, "
                "telephone text)"
            )
            self.cursor.execute(query)
            self.conn.commit()
            print("La table a été créée!")
            self.cursor.close()
        except sqlite3.Error as error:
            print("La création de la table a échoué", error)
        finally:
            if self.conn:
                self.conn.close()
                print("La connexion a été fermée")

    def save_student_db(self, *, nom, prenom, niveau, telephone):
        """
        Cette méthode  permet d'enregister un élève au niveau de la table ``dicgit``.

        :param nom: Le nom de l'élève
        :type nom: str
        :param prenom: Le prénom de l'élève
        :type prenom: str
        :param niveau: La classe de l'élève
        :type niveau: str
        :param telephone: Le numéro de téléphone de l'élève
        :type telephone: str
        :return: None
        :rtype: NoneType

        .. note::
           Nom, prenom, niveau et telephone doivent être appelés comme des arguments nommés.
           L'id_ept n'est pas à renseigner car il est automatiquement incrémenté.


        :Exemple:

        >>> db = Database()
        Connexion effectué avec succès
        >>> db.create_table_db()
        La table a été créée!
        La connexion a été fermée
        >>> db.save_student_db(nom="Sene",prenom="Mohamed",niveau="DIC1-GIT",telephone="77777777")
        Les données ont été insérées avec succès
        La connexion a été fermée
        """
        try:
            self.conn = sqlite3.connect("dicgit_database.db")
            self.cursor = self.conn.cursor()
            requete = "INSERT INTO dicgit (nom, prenom, niveau, telephone) VALUES (?, ?, ?, ?);"
            tuple_donnee = (nom, prenom, niveau, telephone)
            self.cursor.execute(requete, tuple_donnee)
            self.conn.commit()
            print("Les données ont été insérées avec succès")
            self.cursor.close()
        except sqlite3.Error as error:
            print("L'insertion a échoué", error)
        finally:
            if self.conn:
                self.conn.close()
                print("La connexion a été fermée")

    def delete_student_db(self, id_ept):
        """
        Cette méthode permet d'efface de la table ``dicgit`` l'élève dont l'idenfiant est saisi.

        :param id_ept: L'identifiant de l'élève
        :type id_ept: int
        :return: None
        :rtype: NoneType

        :Exemple:

        >>> db = Database()
        Connexion effectué avec succès
        >>> db.create_table_db()
        La table a été créée!
        La connexion a été fermée
        >>> db.save_student_db(nom="Sene",prenom="Mohamed",niveau="DIC1-GIT",telephone="77777777")
        Les données ont été insérées avec succès
        La connexion a été fermée
        >>> db.delete_student_db(1)
        Suppression effectué avec succès
        La connexion a été fermée
        """
        try:
            self.conn = sqlite3.connect("dicgit_database.db")
            self.cursor = self.conn.cursor()
            self.cursor.execute("DELETE FROM dicgit WHERE id_ept = ?", (id_ept,))
            self.conn.commit()
            print("Suppression effectué avec succès")
            self.cursor.close()
        except sqlite3.Error as error:
            print("La suppression a échoué", error)
        finally:
            if self.conn:
                self.conn.close()
                print("La connexion a été fermée")

    def modify_student_db(self, id_ept, *, nom="", prenom="", niveau="", telephone=""):
        """
        Cette méthode permet de modifier les champs donnés pour l'élève d'identifiant est saisi.

        :param id_ept: L'identifiant de l'élève à modifier
        :type id_ept: int
        :param nom: La nouvelle valeur que l'on veut donner au champ nom
        :type nom: str
        :param prenom: La nouvelle valeur que l'on veut donner au champ prenom
        :type prenom: str
        :param niveau: La nouvelle valeur que l'on veut donner au champ niveau
        :type niveau: str
        :param telephone: La nouvelle valeur que l'on veut donner au champ telephone
        :type telephone: str
        :return: None
        :rtype: NoneType

        .. warning::
            Nom, prenom, niveau et telephone doivent être appelés comme des arguments nommés.

        :Exemple:

        >>> db = Database()
        Connexion effectué avec succès
        >>> db.save_student_db(nom="Sene",prenom="Mohamed",niveau="DIC1-GIT",telephone="77777777")
        Les données ont été insérées avec succès
        La connexion a été fermée
        >>> db.modify_student_db(1, prenom = "Mohamed Massamba")
        L'enregistrement a été modifié avec succès
        La connexion a été fermée
        >>> db.get_student_db(1, ("prenom", "nom"))
        La connexion a été fermée
        {'prenom': 'Mohamed Massamba', 'nom': 'Sene'}
        """
        try:
            self.conn = sqlite3.connect("dicgit_database.db")
            self.cursor = self.conn.cursor()
            if nom:
                self.cursor.execute(
                    "UPDATE dicgit SET nom = ? WHERE id_ept = ?",
                    (
                        nom,
                        id_ept,
                    ),
                )
            if prenom:
                self.cursor.execute(
                    "UPDATE dicgit SET prenom = ? WHERE id_ept = ?",
                    (
                        prenom,
                        id_ept,
                    ),
                )
            if niveau:
                self.cursor.execute(
                    "UPDATE dicgit SET niveau = ? WHERE id_ept = ?",
                    (
                        niveau,
                        id_ept,
                    ),
                )
            if telephone:
                self.cursor.execute(
                    "UPDATE dicgit SET telephone = ? WHERE id_ept = ?",
                    (
                        telephone,
                        id_ept,
                    ),
                )
            self.conn.commit()
            print("L'enregistrement a été modifié avec succès")
            self.cursor.close()
        except sqlite3.Error as error:
            print("La modification a échoué", error)
        finally:
            if self.conn:
                self.conn.close()
                print("La connexion a été fermée")

    def get_student_db(self, id_ept, *args):
        """
        Permet de récupérer les informations souhaitées d'un élève sous forme de dictionnaire.

        :param id_ept: L'identifiant de l'élève à modifier
        :type id_ept: int
        :param args: Les différents champs souhaités
        :type args: tuple
        :return: Un dictionnaire contenant les informations souhaités
        :rtype: dict

        .. Note::
            Les champs souhaités doivent être renseignés sous forme de chaine de caractère

        :Exemple:

        >>> db = Database()
        Connexion effectué avec succès
        >>> db.save_student_db(nom="Sene",prenom="Mohamed",niveau="DIC1-GIT",telephone="77777777")
        Les données ont été insérées avec succès
        La connexion a été fermée
        >>> db.get_student_db(1, ("nom", "prenom", "niveau"))
        La connexion a été fermée
        {'nom':'Sene','prenom':'Mohamed','niveau':'DIC1-GIT'}
        """
        try:
            dico = {}
            self.conn = sqlite3.connect("dicgit_database.db")
            self.cursor = self.conn.cursor()
            for i in args:
                self.cursor.execute(f"SELECT  {i} FROM dicgit WHERE id_ept = {id_ept}")
                dico[i] = tuple(self.cursor.fetchone())[0]
            self.conn.commit()
            self.cursor.close()
            return dico
        except sqlite3.Error as error:
            print("La lecture des données a échoué", error)
        finally:
            if self.conn:
                self.conn.close()
                print("La connexion a été fermée")

    def get_all_db(self):
        """
        Cette méthode permet de récupérer les informations de tous les élèves de la table ``dicgit``

        :return: Un dictionnaire contenant tous les enregistrements de la base
        :rtype: dict

        :Exemple:

        >>> db = Database()
        Connexion effectué avec succès
        >>> db.save_student_db(nom="Sene",prenom="Mohamed",niveau="DIC1-GIT",telephone="77777777")
        Les données ont été insérées avec succès
        La connexion a été fermée
        >>> db.save_student_db(nom="Ndiaye",prenom="Fatou",niveau="DIC1-GIT",telephone="77777777")
        Les données ont été insérées avec succès
        La connexion a été fermée
        >>> db.get_all_db()
        Le nombre total de ligne est  2
        La connexion a été fermée
        {1:{'id_ept':1,'nom':'Sene','prenom':'Mohamed','niveau':'DIC1-GIT','telephone':'77777777'},
        2:{'id_ept':2,'nom':'Ndiaye','prenom':'Fatou','niveau':'DIC1-GIT','telephone':'77777777'}}
        """
        try:
            dico = {}
            self.conn = sqlite3.connect("dicgit_database.db")
            self.cursor = self.conn.cursor()
            requete = "SELECT * from dicgit"
            self.cursor.execute(requete)
            records = self.cursor.fetchall()
            print("Le nombre total de ligne est ", len(records))
            for row in records:
                dico[row[2]] = {
                    "id_ept": row[2],
                    "nom": row[0],
                    "prenom": row[1],
                    "niveau": row[3],
                    "telephone": row[4],
                }
            self.cursor.close()
            return dico
        except sqlite3.Error as error:
            print("La lecture des données a échoué", error)
        finally:
            if self.conn:
                self.conn.close()
                print("La connexion a été fermée")
