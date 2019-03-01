# User Stories

#### Uutena käyttäjänä haluan

* pystyä luomaan uuden käyttäjätunnuksen
  - tarkistus ettei käyttäjänimeä ole jo varattu
    ```SQL
    SELECT * FROM account 
    WHERE account.username = ?;
    ```
  - uuden käyttäjän luominen
    ```SQL
    INSERT INTO account (name, username, password, role)
    VALUES (?, ?, ?, ?);
    ```

#### Tavallisena käyttäjänä haluan

* pystyä kirjautumaan sisään
  - tarkistus että käyttäjänimellä ja salasanalla löytyy käyttäjä
  ```SQL
  SELECT * FROM account 
  WHERE account.username = ? AND account.password = ?;
  ```
* tarvittaessa muuttaa salasanani ja poistamaan tilini
  - salasanan vaihto
  ```SQL
  UPDATE account SET password=? WHERE account.id = ?;
  ```
* selata drinkkejä sovelluksessa
  - kaikkien hyväksyttyjen drinkkien listaus
  ```SQL
  SELECT * FROM drink WHERE drink.accepted = 1;
  ```
* hakea drinkkejä hakusanalla nimen tai osa-aineiden mukaan
  - haetaan kaikki drinkit joiden nimestä tai ainesosan nimestä hakusana löytyy
  ```SQL
  SELECT drink.id, drink.name FROM drink INNER JOIN ingredient_drink
  ON ingredient_drink.drink_id = drink.id
  INNER JOIN ingredient ON ingredient.id = ingredient_drink.ingredient_id 
  WHERE (drink.name LIKE :word OR ingredient.name LIKE :word)
  AND drink.accepted=1 GROUP BY drink.name LIMIT 5;
  ```
* järjestää drinkit aakkosjärjestykseen, ainesosien mukaan tai juomalajin mukaan (ei toteutettu)
* ehdottaa uutta drinkkiä lisättäväksi
  - drinkki luodaan ja accepted arvo katsotaan sen mukaan onko lisääjä admin
  ```SQL
  INSERT INTO drink (name, drinktype_id, instructions, accepted) VALUES (?, ?, ?, ?)
  ```
  - drinkkiin lisätään ainesosat
  ```SQL
  INSERT INTO ingredient_drink (ingredient_id, drink_id, amount) VALUES (?, ?, ?)
  ```
* lisätä drinkin omiin suosikkeihini
  ```SQL
  INSERT INTO user_drink (user_id, drink_id) VALUES (?, ?)
  ```
* tarkastelemaan suosikki drinkkejäni
* tarkastelemaan suosikki ainesosiani

#### Pääkäyttäjänä haluan pystyä

* lisäämään järjestelmään drinkkejä
* hyväksymään muiden käyttäjien ehdottamia drinkkejä
* antamaan käyttäjälle admin oikeudet
* poistamaan drinkkejä ja ainesosia


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
