# User Stories

#### Uutena käyttäjänä haluan

* pystyä luomaan uuden käyttäjätunnuksen

#### Tavallisena käyttäjänä haluan

* pystyä kirjautumaan sisään
* tarvittaessa muuttaa salasanani ja poistamaan tilini
* selata drinkkejä sovelluksessa
* hakea drinkkejä hakusanalla nimen tai osa-aineiden mukaan
* järjestää drinkit aakkosjärjestykseen, ainesosien mukaan tai juomalajin mukaan (ei toteutettu)
* ehdottaa uutta drinkkiä lisättäväksi
* lisätä drinkin omiin suosikkeihini

#### Pääkäyttäjänä haluan pystyä

* lisäämään järjestelmään drinkkejä
* hyväksymään muiden käyttäjien ehdottamia drinkkejä
* antamaan käyttäjälle admin oikeudet
* poistamaan drinkkejä ja ainesosia

### SQL-kyselyt

Drinkin haku hakusanalla 

```SQL
SELECT drink.id, drink.name FROM drink INNER JOIN ingredient_drink
ON ingredient_drink.drink_id = drink.id
INNER JOIN ingredient ON ingredient.id = ingredient_drink.ingredient_id 
WHERE (drink.name LIKE :word OR ingredient.name LIKE :word)
AND drink.accepted=1 GROUP BY drink.name LIMIT 5;
```

Käyttäjän suosikki drinkkien haku
```SQL
SELECT drink.name FROM drink
INNER JOIN user_drink ON user_drink.drink_id = drink.id
AND user_drink.account_id = :id GROUP BY drink.name;
```

Käyttäjän suosikki aineosat suosikki drinkkien perusteella
```SQL
SELECT COUNT(ingredient.id) AS favorites, ingredient.name FROM Ingredient
INNER JOIN ingredient_drink ON ingredient.id = ingredient_drink.ingredient_id
INNER JOIN drink ON ingredient_drink.drink_id = drink.id
INNER JOIN user_drink ON user_drink.drink_id = drink.id
INNER JOIN account on account.id = user_drink.account_id
WHERE account_id = :id GROUP BY ingredient.name
ORDER BY favorites DESC limit 3;
```
