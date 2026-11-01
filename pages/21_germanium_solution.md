---
orphan: true
---

# פתרון: 2. הטבלה המחזורית, 1871

<p><a href="../board.html?round=germanium">→ חזרה ללוח התשובות</a></p>

**התשובה: משקל אטומי חזוי של כ-72.86**, הפרש של כ-0.3% מהמשקל שנמדד לגרמניום (72.63).

## הנתונים

הפרמטרים מתא הנתונים בעמוד, שעליהם מבוססות כל השורות בהמשך:

```python
names = [["Al", "Si", "P"],
         ["Ga", "?", "As"],
         ["In", "Sn", "Sb"]]

# atomic weights (modern values); None marks the gap in the table
weights = [[26.98, 28.09, 30.97],
           [69.72, None, 74.92],
           [114.82, 118.71, 121.76]]

w_germanium = 72.63     # the measured atomic weight of germanium
```

## שלב אחר שלב

הסעיפים כאן זהים לסעיפי העמוד. סעיפים 1 ו-2 מאתרים את המשבצת הריקה, סעיפים 3 ו-4 מחשבים את התחזית, וסעיף 5 משווה אותה לגרמניום.

**1. השורה.** `weights[i]` הוא שורה שלמה, כלומר רשימה, ולכן אפשר לבדוק בעזרת `in` אם יש בה `None`:

```python
None in weights[0]                         # False
None in weights[1]                         # True
None in weights[2]                         # False
row = 1
```

**2. העמודה.** `index` מחזיר את המיקום של `None` בתוך השורה:

```python
col = weights[row].index(None)             # 1
names[row][col]                            # "?"
```

**3. השכנים.** השכן מעל נמצא בשורה הקודמת ובאותה עמודה, השכן משמאל באותה שורה ובעמודה הקודמת, וכן הלאה:

```python
neighbors = []
neighbors.append(weights[row - 1][col])    # 28.09, Si (above)
neighbors.append(weights[row + 1][col])    # 118.71, Sn (below)
neighbors.append(weights[row][col - 1])    # 69.72, Ga (left)
neighbors.append(weights[row][col + 1])    # 74.92, As (right)
```

**4. התחזית.** זו התשובה שמגישים:

```python
prediction = sum(neighbors) / len(neighbors)    # 72.86
```

**5. ההשוואה לגרמניום.**

```python
(prediction - w_germanium) / w_germanium * 100  # about 0.32 percent
```

## מה עומד מאחורי זה

ברשימה מקוננת, האינדקס הראשון בוחר שורה והשני בוחר איבר בתוכה. "השכן מעל" הוא שינוי של האינדקס הראשון ב-1, ו"השכן משמאל" הוא שינוי של השני. מכיוון שהשכנים מחושבים מ-`row` ומ-`col`, אותן ארבע שורות יעבדו לכל משבצת פנימית בטבלה. התחזית של מנדלייב לאקה-סיליקון הייתה כ-72, והגרמניום אישר אותה. הטבלה לא רק סידרה את היסודות הידועים, היא חזתה את אלה שעוד לא היו ידועים.

## תשובות שגויות נפוצות

- **73.25:** ממוצע של כל שמונת השכנים, כולל האלכסונים.
- **72.32:** ממוצע של השכנים בשורה בלבד (Ga ו-As).
- **73.40:** ממוצע של השכנים בעמודה בלבד (Si ו-Sn).
- **TypeError:** ניסיון לסכם רשימה שיש בה `None`, למשל `sum(weights[row])`.

## למי שסיים

```python
sum(weights[row])        # TypeError: unsupported operand type(s) for +: 'float' and 'NoneType'
(weights[row][col - 1] + weights[row][col + 1]) / 2   # 72.32, row only
(weights[row - 1][col] + weights[row + 1][col]) / 2   # 73.40, column only
```

`sum` מחבר את האיברים אחד אחרי השני, ואי אפשר לחבר מספר ל-`None`. בתחזיות החלקיות, השורה קרובה יותר לגרמניום (הפרש של כ-0.31) מהעמודה (כ-0.77). המשקל משתנה בשורה בצעדים קטנים, ובעמודה בקפיצות גדולות, ולכן ממוצע של שכנים רחוקים מדויק פחות.

<p><a href="../board.html?round=germanium">→ חזרה ללוח התשובות</a></p>
