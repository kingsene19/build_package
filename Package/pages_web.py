"""
Ceci est un module contenant des fonctions pour le ``web scraping`` avec Python

.. note::
    Il faut avoir une connexion internet pour pouvoir utiliser ce module

"""

import re
import requests
from bs4 import BeautifulSoup


def get_page(url):
    """
    Cette fonction permet d' afficher le code HTML d'une page web.

    :param url: L'url de la page web que l'on cherche à accéder
    :type url: str
    :return: Le code html de la page
    :rtype: str

    :Exemple:

    >>> code = get_page("https://ept.sn/contactez-nous/")
    >>> print(code[:150])
    <!DOCTYPE html>
    <html lang="fr-FR">
    <head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1" name="viewport"/>
    <link
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup.prettify()


def get_emails(url):
    """
    Cette fonction permet de récupérer toutes les adresses emails contenues dans une page web.

    :param url: L'url de la page web que l'on cherche à accéder
    :type url: str
    :return: Une liste des emails contenues dans la page web
    :rtype: list

    :Exemple:

    >>> print(get_emails("https://ept.sn/contactez-nous/"))
    ['select2@4.1.0-beta.1', 'ept@ept.sn', 'dir.etudes@ept.sn', 'ept@ept.sn']
    """
    emails = []
    page = requests.get(url)
    email_reg = r"[\w\.-]+@[\w\.-]+"
    for re_match in re.findall(email_reg, page.text):
        emails.append(re_match)
    return emails


def get_urls(url):
    """
    Cette fonction permet de récupérer toutes les URls contenues dans une page web.

    :param url: L'url de la page web que l'on cherche à accéder
    :type url: str
    :return: Une liste des URLs contenues dans la page web
    :rtype: list

    :Exemple:

    >>> page_urls = get_urls("https://ept.sn/contactez-nous/")
    >>> print(page_urls[:5])
    ['https://web.facebook.com/EPT-lofficiel-401641523533850?_rdc=1&_rdr',
    'https://twitter.com/ept_officiel?lang=fr',
    'https://www.youtube.com/channel/UCH9KR3HcWPsJSxViD2LUujg/videos',
    'https://ept.sn/', 'https://ept.sn/mot-du-directeur']
    """
    urls = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    for i in soup.find_all('a'):
        href = i.attrs['href']
        if href.startswith("/"):
            page = url + href
            if page not in urls:
                urls.append(page)
        if href.startswith("https://") or href.startswith("http://"):
            if href not in urls:
                urls.append(href)
    return urls


def get_tables(url):
    """
    Cette fonction permet de récupérer le code HTML des tables contenues dans une page web.

    :param url: L'url de la page web que l'on cherche à accéder
    :type url: str
    :return: Une liste des codes HTML des tables dans la page web
    :rtype: list

    :Exemple:

    >>> page_tables = get_tables("https://ept.sn/contactez-nous/")
    >>> print(page_tables[0][:150])
    <table class="standing-table__table callfn" data-fn="table-sorter-lite" data-lite="true">
    <caption class="standing-table__caption">
    Premier League
    """
    codes = []
    page = requests.get(url)
    tables = BeautifulSoup(page.content, "html.parser").find_all("table")
    for i in tables:
        codes.append(str(i))
    return codes
