## Tietokantakaavio

![](https://github.com/karoliinaemilia/drinkkiarkisto/blob/master/documentation/kuvat/tietokantakaavio_uusi.png)

# CREATE TABLE -lauseet
```
CREATE TABLE account (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        username VARCHAR(144) NOT NULL, 
        password VARCHAR(144) NOT NULL, 
        role VARCHAR(144) NOT NULL, 
        PRIMARY KEY (id)
)

CREATE TABLE ingredient (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        accepted BOOLEAN NOT NULL, 
        PRIMARY KEY (id), 
        CHECK (accepted IN (0, 1))
)

CREATE TABLE drinktype (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        PRIMARY KEY (id)
)

CREATE TABLE drink (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        drinktype_id INTEGER NOT NULL, 
        instructions VARCHAR(500) NOT NULL, 
        accepted BOOLEAN NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(drinktype_id) REFERENCES drinktype (id), 
        CHECK (accepted IN (0, 1))
)

CREATE TABLE ingredient_drink (
        ingredient_id INTEGER, 
        drink_id INTEGER, 
        amount VARCHAR(144), 
        FOREIGN KEY(ingredient_id) REFERENCES ingredient (id), 
        FOREIGN KEY(drink_id) REFERENCES drink (id)
)

CREATE TABLE user_drink (
        account_id INTEGER, 
        drink_id INTEGER, 
        FOREIGN KEY(account_id) REFERENCES account (id), 
        FOREIGN KEY(drink_id) REFERENCES drink (id)
)
```

### Alkuperäinen suunnitelma tietokannasta

![](https://github.com/karoliinaemilia/drinkkiarkisto/blob/master/documentation/kuvat/tietokantakaavio.png)
