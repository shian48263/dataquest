## 4. SQLite ##

SELECT Rank,Major FROM recent_grads;

## 5. Specifying column order ##

SELECT Major,Rank FROM recent_grads;

## 6. Practice: Select ##

SELECT Rank, Major_code, Major, Major_category, Total FROM recent_grads;

## 7. Where ##

SELECT Major, ShareWomen FROM recent_grads WHERE ShareWomen > 0.5;

## 8. Practice: Where ##

SELECT Major, Employed FROM recent_grads WHERE Employed > 10000;

## 9. Limit ##

SELECT Major FROM recent_grads WHERE Employed > 10000 LIMIT 10;