# Drinkkiarkisto

Drinkkiarkisto on selainpohjaista käyttöliittymää käyttävä drinkinhakusovellus. 
Drinkkejä ovat cocktailit ja muut juomasekoitukset. 
Drinkkejä voi hakea juoman nimeen liittyvällä hakusanalla tai osa-aineen mukaan. 

Järjestelmään kirjaudutaan sisään.

Tavallinen käyttäjä voi hakea drinkkejä kannasta ja ehdottaa uusien lisäämistä kantaan. Tavallinen käyttäjä voi myös lisätä drinkkejä suosikkeihinsa jotka näytetään käyttäjälle. Käyttäjälle näytetään myös hänen lempi osa-aineensa laskettuna siitä montako kertaa aineosa on käyttäjän suosikki drinkeissä.
Järjestelmän ylläpitäjä voi lisätä järjestelmään drinkkejä joko kokonaan itse tai ehdotettuja hyväksymällä.  
Ylläpitäjä voi myös antaa muille käyttäjille admin oikeudet tai poistaa muun käyttäjän tilin.

Toimintoja:

  * Kirjautuminen
  * Drinkin haku
  * Drinkkien selailu
  * Drinkkien lisäys lomakkeella
  * Drinkin lisäys suosikkeihin
  * Uuden drinkin ehdottaminen / ehdotuksen hyväksyminen
  * Uuden osa-aineen ehdottaminen / ehdotuksen hyväksyminen
  * Käyttäjätunnuksen luominen
  * Salasanan muutos ja tilin poisto
  
### Heroku

https://tsoha-drinkkisovellus.herokuapp.com/

Admin
```
käyttäjätunnus: admin, salasana: salainen1
```
Regular
```
käyttäjätunnus: eika, salasana: salainen1
```

### Dokumentaatio

[Tietokantakaavio ja CREATE TABLE -lauseet](https://github.com/karoliinaemilia/drinkkiarkisto/blob/master/documentation/tietokantakaavio.md)

[User Stories ja SQL-kyselyt](https://github.com/karoliinaemilia/drinkkiarkisto/blob/master/documentation/userstories.md)

[Asennus- ja käyttöohjeet](https://github.com/karoliinaemilia/drinkkiarkisto/blob/master/documentation/asennus_kayttoohje.md)
