---
orphan: true
---

# פתרון: 1. נפטון, 1846

<p><a href="../board.html?round=neptune">→ חזרה ללוח התשובות</a></p>

**התשובה: הכלל טעה במרחק של נפטון ב-29.0%.** בשבעת הגופים הראשונים הטעות קטנה מ-5%, ובנפטון הכלל חוזה 38.8 יחידות אסטרונומיות במקום 30.07.

## הנתונים

הפרמטרים מתא הנתונים בעמוד, שעליהם מבוססות כל השורות בהמשך:

```python
# the bodies beyond Mercury, going out from the Sun, and their measured mean distance from the Sun (AU)
names = ["Venus", "Earth", "Mars", "Ceres", "Jupiter", "Saturn", "Uranus", "Neptune"]
actual = [0.723, 1.000, 1.524, 2.767, 5.203, 9.537, 19.19, 30.07]

tolerance = 10     # in this exercise, a prediction that misses by more than this has failed (percent)


# the function as it was given to you: the predictions a = 0.4 + 0.3 * 2**n for the first `count` bodies
def bode_predictions(count):
    for n in range(1, count):
        predicted = []
        predicted.append(0.4 + 0.3 * 2**n)
    return predicted
```

## שלב אחר שלב

הסעיפים כאן זהים לסעיפי העמוד.

**1. הרשימה מתאפסת בכל סיבוב.** השורה `predicted = []` נמצאת בתוך הלולאה, ולכן בכל סיבוב נוצרת רשימה ריקה חדשה, ונשאר רק הערך של הסיבוב האחרון. יוצרים את הרשימה פעם אחת, לפני הלולאה:

```python
predicted = bode_predictions(len(names))
print(predicted, len(predicted))        # [38.8] 1: one value instead of eight

def bode_predictions(count):
    predicted = []
    for n in range(1, count):
        predicted.append(0.4 + 0.3 * 2**n)
    return predicted

predicted = bode_predictions(len(names))
print(predicted)                        # seven values
```

**2. הלולאה מתחילה במקום הלא נכון.** `range(1, count)` מתחיל ב-1, ולכן התחזית הראשונה היא של כדור הארץ, כל תחזית זזה מקום אחד, והתחזית של נוגה חסרה:

```python
len(predicted) == len(names)            # False: 7 against 8
predicted[0]                            # 1.0, the prediction for Earth, not for Venus

def bode_predictions(count):
    predicted = []
    for n in range(count):
        predicted.append(0.4 + 0.3 * 2**n)
    return predicted

predicted = bode_predictions(len(names))
len(predicted) == len(names)            # True
predicted[0]                            # 0.7
```

**3. אותה רשימה בשורה אחת.**

```python
predicted2 = [0.4 + 0.3 * 2**n for n in range(len(names))]
predicted2 == predicted                 # True
```

**4. פונקציה במקום שמונה שורות.** את החישוב שחוזר על עצמו כותבים פעם אחת, בפונקציה, ולולאה קוראת לה לכל גוף:

```python
def rel_error(pred, real):
    return abs(pred - real) / real * 100

errors = []
for i in range(len(names)):
    errors.append(rel_error(predicted[i], actual[i]))
print(errors)                           # about [3.18, 0.0, 4.99, 1.19, 0.06, 4.85, 2.14, 29.03]

err_saturn                              # about 45.5, but errors[5] is about 4.85
```

בשורה של שבתאי בקוד שקיבלתם נשאר `predicted[4]` מהשורה של צדק, כנראה מהעתקה. בשבע השורות האחרות האינדקס נכון, ולכן קשה לראות את הטעות. בפונקציה ובלולאה האינדקס נכתב פעם אחת, ואין שורה שאפשר לשכוח לעדכן.

**5. הגוף הראשון שבו הכלל נכשל.** הלולאה נעצרת בגוף הראשון שהטעות בו גדולה מ-10%. זו התשובה שמגישים:

```python
for i in range(len(names)):
    if errors[i] > tolerance:
        print(names[i], errors[i])      # Neptune, about 29.03
        break

miss = round(errors[i], 1)              # 29.0
```

## מה השתבש

בפונקציה שקיבלתם היו שתי טעויות לולאה נפוצות: יצירת הרשימה בתוך הלולאה במקום לפניה, וטווח שמתחיל במקום הלא נכון. הראשונה גלויה מיד, כי נשאר ערך אחד; השנייה מתגלה רק כשבודקים את האורך או את הערך הראשון. בקוד שחוזר על עצמו הייתה טעות שלישית, שנוצרת כמעט רק בקוד כזה: שורה שהועתקה ולא עודכנה כולה.

בפיזיקה, כלל טיציוס-בודה אינו חוק טבע אלא התאמה לנתונים שהיו ידועים ב-1772, ולכן אין סיבה שיחזה נכון גם גוף נוסף. הוא התאים לאורנוס ולצרס, ונכשל בנפטון.

## תשובות שגויות נפוצות

- **38.3:** הטעות של נוגה, כשהטווח בסעיף 2 לא תוקן: נוגה מושווה לתחזית של כדור הארץ, וכבר הגוף הראשון "נכשל".
- **45.5:** הערך של `err_saturn` מהקוד שקיבלתם, עם האינדקס השגוי (סעיף 4).
- **22.5:** חלוקה בתחזית במקום במדידה.
- **8.73:** ההפרש ביחידות אסטרונומיות, בלי לחלק ובלי להכפיל ב-100.

## למי שסיים

```python
pluto = 39.48
n = 0
while 0.4 + 0.3 * 2**n < pluto:
    n = n + 1
print(n, 0.4 + 0.3 * 2**n)              # 8 77.2
print(0.4 + 0.3 * 2**(n - 1))           # 38.8, about 1.7% from Pluto
```

הלולאה נעצרת ב-<span dir="ltr">&#8288;$n = 8$</span>, שהתחזית שלו (77.2) רחוקה מאוד מפלוטו. התחזית של <span dir="ltr">&#8288;$n = 7$</span>, המקום שהכלל שמר לנפטון, קרובה לפלוטו בפחות מ-2%. ההתאמה הזאת מקרית: פלוטו אינו כוכב לכת, אלא אחד מגופים רבים שנמצאים מעבר לנפטון.

<p><a href="../board.html?round=neptune">→ חזרה ללוח התשובות</a></p>
