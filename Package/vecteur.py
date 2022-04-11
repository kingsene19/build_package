"""
Ceci est un module contenant une classe Vecteur pour la manipulation de vecteurs.
"""


class Vecteur:
    """
    Classe Vecteur permet de créer et effectuer des opérations sur des vecteurs de dimension n
    """

    def __init__(self, *args):
        """
        Cette méthode est appelé lors de la création d'un objet de la classe vecteur.

        .. note::
            Les composantes du vecteur doivent être de type int ou float dans le cas contraire
            une exception ComposantesError sera levée.
            Elles peuvent être renseignées sous forme de tuple ou liste.
            On peut également les renseigner sous forme de suite de nombre.

        :param args: Les composantes du vecteurs
        :type args: tuple
        :return: Retourne un vecteur de composantes ceux renseignés dans args
        :rtype: Vecteur
        :raise ComposantesError: Si les composantes ne sont pas des int ou float

        :Exemple:

        >>> v1 = Vecteur((3, 5, 7, 8))
        """
        if isinstance(args[0], (tuple, list)):
            if all(map(lambda x: isinstance(x, (int, float)), args[0])):
                self.coords = tuple(*args)
            else:
                raise ComposantesError(
                    "Les composantes du vecteur doivent être des int ou float"
                )
        else:
            if all(map(lambda x: isinstance(x, (int, float)), args)):
                self.coords = args
            else:
                raise ComposantesError(
                    "Les composantes du vecteur doivent être des int ou float"
                )

    def __str__(self):
        """
        Cette méthode est appelé lorsqu'on essaie d'afficher un vecteur.
        Elle nous permet d'afficher le vecteur sous forme du tuple de ces composantes.
        Dans le cas où le vecteur est de dimension 1, on affiche l'unique composante.

        :return: Les coordonnées du vecteur
        :rtype: str

        :Exemple:

        >>> v = Vecteur((3, 5, 7, 8))
        >>> print(v)
        (3, 5, 7, 8)
        >>> v1 = Vecteur((10, 3))
        >>> print(v1)
        (10, 3)
        """
        if len(self.coords) == 1:
            return f"{self.coords[0]}"
        return f"{self.coords}"

    __repr__ = __str__

    def __len__(self):
        """
        Cette méthode permet de déterminer la taille d'un vecteur.

        :return: La taille du vecteur
        :rtype: int

        :Exemple:

        >>> v = Vecteur((3, 5, 7, 8))
        >>> len(v)
        4
        """
        return len(self.coords)

    def max(self):
        """
        Cette méthode permet de déterminer le maximum des composantes du vecteur.

        :return: Le maximum des composantes du vecteur
        :rtype: int/float

        :Example:

        >>> v = Vecteur((3, 5, 7, 8))
        >>> v.max()
        8
        """
        return max(self.coords)

    def min(self):
        """
        Cette méthode permet de déterminer le minimum des composantes du vecteur.

        :return: Le minimum des composantes du vecteur
        :rtype: int/float

        :Exemple:

        >>> v = Vecteur((3, 5, 7, 8))
        >>> v.min()
        3
        """
        return min(self.coords)

    def moyenne(self):
        """
        Cette méthode permet de calculer la moyenne des composantes du vecteur.

        :return: La moyenne des composantes du vecteur
        :rtype: float

        :Exemple:

        >>> v = Vecteur((3, 5, 7, 8))
        >>> v.moyenne()
        5.75
        """
        return sum(self.coords) / len(self.coords)

    def ecart_type(self):
        """
        Cette méthode permet de calculer l'écart type des composantes du vecteur.

        :return: L'écart type des composantes du vecteur
        :rtype: float

        :Exemple:

        >>> v = Vecteur((3, 5, 7, 8))
        >>> v.ecart_type
        1.920286436967152
        """
        somme = 0
        for i in self.coords:
            somme += pow(i - self.moyenne(), 2)
        variance = somme / len(self)
        return pow(variance, 0.5)

    def __pos__(self):
        """
        Cette méthode permet de renvoyer le vecteur

        :return: Le vecteur lui même
        :rtype: Vecteur

        :Exemple:

        >>> v = Vecteur((3, 5, 7, 8))
        >>> +v
        (3, 5, 7, 8)
        """
        return self

    def __neg__(self):
        """
        Cette méthode permet de rendre négatif un vecteur (-V).

        :return: Un vecteur dont les composantes sont les opposées de celles initiales
        :rtype: Vecteur

        :Exemple:

        >>> v = Vecteur((3, 5, 7, 8))
        >>> -v
        (-3, -5, -7, -8)
        """
        if len(self.coords) == 1:
            return Vecteur(list(map(lambda x: -x, self.coords))[0])
        return Vecteur(tuple(map(lambda x: -x, self.coords)))

    def __add__(self, other):
        """
        Cette méthode permet d'additionner deux vecteurs de même taille.

        :raise TailleError: Si les deux vecteurs ne sont pas de même taille
        :return: Un vecteur dont les composantes sont les sommes de ceux des deux vecteurs
        :rtype: Vecteur

        :Exemple:

        >>> v = Vecteur((3, -2, 1))
        >>> v1 = Vecteur((-1, 7, 9))
        >>> v + v1
        (2, 5, 10)
        """
        if len(self.coords) == len(other.coords):
            return Vecteur(tuple(map(lambda x, y: x + y, self.coords, other.coords)))
        raise TailleError("Les deux vecteurs doivent être de même longueur")

    __radd__ = __add__

    def __sub__(self, other):
        """
        Cette méthode permet de soustraire deux vecteurs de même taille.

        :raise TailleError: Si les deux vecteurs ne sont pas de même taille
        :return: Un vecteur dont les composantes sont les différences de ceux des deux vecteurs
        :rtype: Vecteur

        :Exemple:

        >>> v = Vecteur((3, -2, 1))
        >>> v1 = Vecteur((-1, 7, 9))
        >>> v - v1
        (4, -9, -8)
        """
        if len(self.coords) == len(other.coords):
            return Vecteur(tuple(map(lambda x, y: x - y, self.coords, other.coords)))
        raise TailleError("Les deux vecteurs doivent être de même longeur")

    __rsub__ = __sub__

    def __mul__(self, value):
        """
        Cette méthode de multiplier un vecteur par un scalaire.
        Elle lève une exception ValueError si on essaie de multiplier deux vecteurs.

        :raise ValueError: Si on essaie d'effectuer la multiplication de deux vecteurs
        :return: Un vecteur de composantes les produit des composantes initiales par le scalaire
        :rtype: Vecteur

        :Exemple:

        >>> v = Vecteur((3, -2, 1))
        >>> v * 4
        (12, -8, 4)
        """
        if not isinstance(value, (int, float)):
            raise ValueError(
                "Cette opération n'est pas supporté pour les vecteurs")
        return Vecteur(tuple(map(lambda x: value * x, self.coords)))

    __rmul__ = __mul__


class ComposantesError(Exception):
    """
    Cette classe permet de lever une exception lorsque les arguments passées
    lors de la création du vecteur ne sont pas de type int ou float
    """


class TailleError(Exception):
    """
    Cette classe permet de lever une exception lorsque les arguments passées
    lorsque deux vecteurs ne sont pas de même taille
    """
