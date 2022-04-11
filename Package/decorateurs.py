"""
Ceci est un module contenant un décorateur transform qui permet de modifier le comportement
d'une fonction.
"""


import re


def transform(**kwargs):
    """
    Ceci est un décorateur.

    :param kwargs: Un argument nommé pour spécifier le comportement voulu
    :type kwargs: dict
    :return: Elle renvoie le résultat de la fonction avec la modification apportée
    :rtype: str
    :Exemple:

    >>> @transform(upper = True)
    ... def func(s, s1):
    ...     return s + s1
    ...
    >>> func("Ceci est ", "un exemple")
    'CECI EST UN EXEMPLE'
    >>> @transform(lower = True)
    ... def func(s):
    ...     return s
    ...
    >>> func("Ceci est un exemple")
    'ceci est un exemple'
    >>> @transform(piglatin = True)
    ... def func(s1, s2, s3 = "exemple"):
    ...     return s1 + s2 + s3
    ...
    >>> func("This is ", "an ", s3 = "example")
    'Isthay isway anway exampleway'
    """

    def function(fonction):
        def wrapper(*args, **kw):
            if kwargs.get("upper"):
                return fonction(*args, **kw).upper()
            if kwargs.get("lower"):
                return fonction(*args, **kw).lower()
            if kwargs.get("piglatin"):
                return english2piglatin(fonction(*args, **kw))

        return wrapper

    return function


def english_word2piglatin(word):
    """
    Cette fonction permet de traduire un mot en Pig Latin.

    :param word: Le mot que l'on souhaite traduire
    :type word: str
    :return: La traduction en Pig Latin du mot
    :rtype: str
    """
    reg = "^[aeiouAEIOU][a-zA-Z0-9_]*"
    match_reg = re.compile(reg)
    if not re.match(match_reg, word[0]):
        try:
            mot_ret1 = (
                re.findall("[aeiouAEIOU]", word)[0].upper()
                + word.split(re.findall("[aeiouAEIOU]", word)[0])[1]
                + word.split(re.findall("[aeiouAEIOU]", word)[0])[0].lower()
                + "ay"
            )
            mot_ret2 = (
                re.findall("[aeiouAEIOU]", word)[0]
                + word.split(re.findall("[aeiouAEIOU]", word)[0])[1]
                + word.split(re.findall("[aeiouAEIOU]", word)[0])[0]
                + "ay"
            )
        except IndexError:
            return word + "ay"
        else:
            if word[0].isupper():
                return mot_ret1
            return mot_ret2
    else:
        return word + "way"


def english2piglatin(sentence):
    """
    Cette fonction permet de traduire une phrase en Pig Latin.

    :param sentence: La phrase ou le groupe de mot que l'on souhaite traduire
    :type sentence: str
    :return: La traduction en piglatin de la phrase ou du groupe de mot
    :rtype: str
    """
    return " ".join([english_word2piglatin(word) for word in sentence.split()])
