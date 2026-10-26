---
orphan: true
---

# פתרון: 3. ג'נסיס, ספטמבר 2004

<p><a href="../board.html?round=genesis">→ חזרה ללוח התשובות</a></p>

**התשובה:** `2`. בקריאה `a3` המתג שהותקן לא נפתח בהאטה, ובקריאה `a4` הוא נפתח בהאצה.

## הנתונים

הפרמטרים מתא הנתונים בעמוד, שעליהם מבוססות כל השורות בהמשך:

```python
a_threshold = 3.0     # the switch should fire at a deceleration of this size or more (g)

# readings along the capsule axis (g): positive = speeding up, negative = slowing down
a1 = 0.0
a2 = -1.5
a3 = -3.5
a4 = 3.5
```

## שלב אחר שלב

הסעיפים כאן זהים לסעיפי העמוד. סעיפים 1 ו-2 כותבים את שני המתגים, סעיף 3 משווה ביניהם, וסעיף 4 סופר.

**1. המתג שתוכנן.** האטה היא תאוצה שלילית, ולכן התנאי הוא על `-a`:

```python
def deploy_intended(a):
    return -a >= a_threshold    # the same as a <= -a_threshold
```

**2. המתג שהותקן הפוך.** אותה פונקציה, על הערך בסימן ההפוך:

```python
def deploy_as_built(a):
    return deploy_intended(-a)
```

**3. השוואה בכל קריאה.**

```python
d1 = deploy_intended(a1) != deploy_as_built(a1)    # False: both False
d2 = deploy_intended(a2) != deploy_as_built(a2)    # False: both False
d3 = deploy_intended(a3) != deploy_as_built(a3)    # True: True vs False
d4 = deploy_intended(a4) != deploy_as_built(a4)    # True: False vs True
```

**4. ספירה.** זו התשובה שמגישים:

```python
disagreements = int(d1) + int(d2) + int(d3) + int(d4)    # 2
```

## מה השתבש

לפי ועדת הבדיקה, שרטוטי התכן של Lockheed Martin משנת 2001 הראו את המתגים בכיוון הפוך, וכל ארבעת המתגים, שניים ראשיים ושניים לגיבוי, הותקנו כך. המתגים לא הגיבו להאטה בכניסה לאטמוספרה, המצנחים לא נפתחו, והכמוסה התנפצה בפגיעה בקרקע ביוטה.

## תשובות שגויות נפוצות

- **1:** נבדקה רק ההאטה בכניסה לאטמוספרה (`a3`). המתג ההפוך שונה גם בהאצה (`a4`).
- **0:** `deploy_as_built` הוגדרה בלי היפוך הסימן, כך ששתי הפונקציות זהות (סעיף 2).

## למי שסיים

עבור `a5 = -3.0` המתג שתוכנן מחזיר `True` (הסף כלול, `>=`), והמתג שהותקן מחזיר `False`. הקריאות `a1` ו-`a2` אינן מגיעות לסף באף כיוון, ושני המתגים מחזירים בהן `False`. בדיקה שכוללת רק קריאות כאלה עוברת גם כשהמתג הפוך: כדי לגלות את הטעות צריך קריאה מעבר לסף.

<p><a href="../board.html?round=genesis">→ חזרה ללוח התשובות</a></p>
