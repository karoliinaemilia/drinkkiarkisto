## Asennusohjeet

```
git clone git@github.com:karoliinaemilia/drinkkiarkisto.git
cd drinkkiarkisto
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 run.py
```

Sovellus käynnistyy osoitteeseen localhost:5000

Sovelluksessa eii voi lisätä juomalajeja joten ne täytyy lisätä terminaalin kautta.

```
cd application
sqlite3 drink.db
INSERT INTO drinktype (name) VALUES ('Shotti');
```
Tee INSERT INTO lause kaikille haluamillasi juomalajin nimillä.

## Käyttöohjeet

#### Kirjautuminen ja rekisteröityminen
Sivun oikeasta yläkulmasta voit kirjautua sisään tai valita uuden tunnuksen luomisen.
Rekistöröityessä sinulta kysytään nimi, käyttäjänimi ja salasana.


#### Etusivu ja drinkkien haku
Kirjauduttuasi sisään sinut ohjataan etusivulle jossa voit hakea drinkkejä vapaasana haulla. Tuloksista näytetään vain viisi
ensimmäistä joten hakusanan kannattaa olla tarkka, hakutuloksissä näkyy drinkit joiden nimi tai ainesosan nimi vastaa hakusanaa.

Etusivulla on myös napit joiden avulla voit navigoida kaikkien drinkkien listaukseen, osa-aineiden listaukseen tai omaan profiiliisi.
Linkit näille sivuille löytyvät myös yläpalkistastä.

Jos hakusanallasi löytyy tuloksia ne näkyvät haku kentän alla ja drinkin nimeä painamalla pääset tarkastelemaan sitö tarkemmin.

#### Drinkkien selailu

Drinkkilistaus sivulla on listattuna kaikki sovelluksen drinkit, drinkin nimeä painamalla pääset drinkin omalle sivulle.
Jos drinkkejä on sovelluksessa yli viisi näkyy listan alla painike next jota painamalla löydät loputkin drinkit.
Drinkin vieressä on nappi Lisää suosikkeihin, jota painamalla voit lisätä drinkin omiin suosikkeihisi.

#### Ainesosien listaus ja lisääminen

Yläpalkin linkistä ainesosat pääset ainesosien listaukseen. Tällä sivulla voit myös ehdottaa uuden ainesosan lisäämistä.
Kirjoita ainesosan nimi kenttään ja paina lisää ainesosa. Järjestelmän ylläpitäjä voi sen jälkeen nähdä ehdotuksesi ja hyväksyä sen.

#### Drinkin lisäys

Painamalla yläpalkin nappi ehdota uutta drinkkiä pääset ehdottamaan uuden drinkin lisäystä sovellukseen. Ennen kuin aloitat drinkin
lisäämisen tarkista ainesosat sivulta että sovelluksessa on kaikki ainesosat joita drinkkiisi tarvitaan. Jos jokin ainesosa puuttuu
voit ehdottaa sitä aineosien sivulla. Täytä ensin drinkin nimi, valitse juomalaji ja kirjoita ohjeet jonka jälkeen voit painaa
lisää drinkki nappia jolloin sinut ohjataan ainesosien lisäämiseen. Valitse listalta ainesosa ja kirjoita ruutuun sitä tarvittava määrä
(esimerkiksi 1 kpl, 2 dl, tai 5 pulloa). Kun olet lisännyt kaikki aineet voit painaa hyväksy nappia jolloine järjestelmän ylläpitäjä
voi arvioida ehdotuksesi.

#### Oma profiili

Oma profiili sivulla näet suosikeiksi lisäämäsi drinkit ja lempi ainesosasi jos sinulla on suosikki drinkkejä. Tällä sivulla
voit myös vaihtaa salasanasi.

### Ylläpitäjä

#### Drinkin ja ainesosan lisäys

Kun käyttäjä jolla on ylläpitäjän oikeudet lisää drinkin tai ainesosan se lisätään sovellukseen automaattisesti eikä sitä tarvitse 
hyväksyä. 

#### Muut käyttäjät

Ylläpitäjä voi nähdä kaikki sovelluksen käyttäjät käyttäjä listaus -sivulla ja antaa haluamalleen käyttäjälle käyttöoikeudet tai
poistaa jonkin käyttäjän profiilin.

#### Ehdotuksien hyväksyminen

Ylläpitäjä voi navigoida ehdotuksien listaukseen yläpalkin Tarkastele ehdotettuja drinkkejä ja ainesosia -linkin kautta. Tällä sivulla
ylläpitäjä näkee kaikki ehdotetut drinkit ja ainesosat ja voi joko hyväksyä tai poistaa ne. Jos ehdotuksia ei ole näkyy sivulla tieto siitä.

### Drinkkien ja ainesosien poisto

Ylläpitäjä voi poistaa ainesosan tai drinkin niiden listauksessa näkyvistä poisto napeista.
