---
orphan: true
---

# פתרון: 3. מגדל פיזה

<p><a href="../board.html?round=pisa">→ חזרה ללוח התשובות</a></p>

**התשובה: 5.6 מטר.** כשכדור הברזל פוגע בקרקע, אחרי כ-3.40 שניות, כדור העץ עדיין נמצא בגובה של כ-5.6 מטר.

## הנתונים

הפרמטרים מתא הנתונים בעמוד, שעליהם מבוססות כל השורות בהמשך:

```python
g = 9.81          # gravitational acceleration (m/s^2)
h = 56            # height of the tower (m)
dt = 0.001        # time step (s)

# four balls of the same size (10 cm), and their drag coefficient c (1/m): the drag acceleration is c * v**2
materials = ["iron", "marble", "wood", "cork"]
c_values = [0.00054, 0.00157, 0.00705, 0.01762]
c_iron = c_values[0]
c_wood = c_values[2]


# the function as it was given to you: the time (s) for a ball with drag coefficient c to fall from height h
def fall_time(c):
    y = h
    v = 0
    t = 0
    while y < 0:
        a = g - c * v**2
        v = v + a * dt
        y = y - v * dt
        t = t + dt
    return t
```

## שלב אחר שלב

הסעיפים כאן זהים לסעיפי העמוד.

**1. הלולאה לא רצה אף פעם.** לפני הסיבוב הראשון `y` שווה ל-56, ולכן התנאי `y < 0` הוא `False`, הלולאה לא רצה, והפונקציה מחזירה 0. הלולאה צריכה לרוץ כל עוד הכדור **מעל** הקרקע:

```python
(2 * h / g) ** 0.5                      # about 3.379
fall_time(0)                            # 0

def fall_time(c):
    y = h
    v = 0
    t = 0
    while y > 0:
        a = g - c * v**2
        v = v + a * dt
        y = y - v * dt
        t = t + dt
    return t

fall_time(0)                            # about 3.379
```

**2. כל הכדורים בשורה אחת.**

```python
times = [fall_time(c) for c in c_values]
print(materials, times)                 # about [3.396, 3.429, 3.605, 3.952]
T_iron = times[0]                       # about 3.396
```

כדור הברזל נופל הכי מהר, וכדור השעם הכי לאט.

**3. פונקציה במקום שתי לולאות.**

```python
print(y_iron, y_wood)                   # both about -0.02: the balls land together?

def height_after(c, T):
    y = h
    v = 0
    t = 0
    while t < T:
        a = g - c * v**2
        v = v + a * dt
        y = y - v * dt
        t = t + dt
    return y

height_after(c_iron, T_iron)            # about -0.02 (one step below the ground)
height_after(c_wood, T_iron)            # about 5.64
```

בלולאה של כדור העץ בקוד שקיבלתם נשאר `c_iron` מהלולאה של כדור הברזל, כנראה מהעתקה. לכן שני הכדורים "נוחתים יחד", והקוד שגוי. בפונקציה הלולאה כתובה פעם אחת, והכדור נבחר רק דרך הפרמטר `c`.

**4. התשובה.** זו התשובה שמגישים:

```python
height = round(height_after(c_wood, T_iron), 1)    # 5.6
```

## מה השתבש

בפונקציה שקיבלתם התנאי של לולאת ה-`while` היה הפוך, ולכן היא לא רצה אף פעם. טעות כזאת לא עוצרת את התוכנית ולא מדפיסה שגיאה: היא פשוט מחזירה 0. היא מתגלה רק כשבודקים את הפונקציה על מקרה שהתשובה שלו ידועה, כאן נפילה בלי אוויר. בקוד שחוזר על עצמו הייתה טעות שנייה: לולאה שהועתקה ולא עודכנה כולה, ונתנה תוצאה שנראתה סבירה.

## תשובות שגויות נפוצות

- **56.0:** הגובה ההתחלתי, כשהפונקציה `fall_time` לא תוקנה ו-`T_iron` הוא 0 (סעיף 1).
- **0.0:** התוצאה של `y_wood` מהקוד שקיבלתם, עם `c_iron` במקום `c_wood` (סעיף 3).
- **11.9:** הגובה של כדור השעם, `c_values[3]`, במקום כדור העץ.

## למי שסיים

```python
for i in range(len(materials)):
    print(materials[i], height_after(c_values[i], T_iron))
# iron about -0.02, marble about 1.0, wood about 5.6, cork about 11.9

times[3] - times[0]                     # about 0.56 s
```

כדור השיש נמצא כמטר אחד מעל הקרקע כשכדור הברזל נוחת, הפרש של כ-3 מאיות שנייה בזמן הנפילה (סעיף 2), שקשה מאוד לראות בעין. רק כשאחד הכדורים קל מאוד, כמו עץ או שעם, ההבדל גדול מספיק כדי לראות אותו בבירור.

<p><a href="../board.html?round=pisa">→ חזרה ללוח התשובות</a></p>
