---
orphan: true
---

# פתרון: 2. נחתת מאדים, דצמבר 1999

<p><a href="../board.html?round=polar">→ חזרה ללוח התשובות</a></p>

**התשובה:** כ-`21.6` מטר לשנייה, פי תשעה בערך ממהירות הנחיתה המתוכננת.

## הנתונים

הפרמטרים והפונקציה מתא הנתונים בעמוד, שעליהם מבוססות כל השורות בהמשך:

```python
g_mars = 3.71        # gravitational acceleration at the surface of Mars (m/s^2)
v_at_40 = 13.0      # downward speed of the lander at 40 m above the surface (m/s)
v_nominal = 2.4     # planned touchdown speed with the engines firing (m/s)
h_logic = 40        # the touchdown sensors are read at this altitude and below (m)


# the function as it was given to you
def engine_cut(altitude, touchdown_signal):
    if altitude <= h_logic and touchdown_signal:
        print(True)
    else:
        print(False)
```

## שלב אחר שלב

הסעיפים כאן זהים לסעיפי העמוד. סעיפים 1 ו-2 עוסקים בפונקציה שניתנה, סעיף 3 בשלושה רגעים בירידה, וסעיפים 4 ו-5 במהירות.

**1. הפונקציה שניתנה.** היא מדפיסה את ההחלטה, אבל אינה מחזירה דבר, ולכן `r` מקבל `None`:

```python
r = engine_cut(1500, True)    # prints False
print(r)                      # None
```

**2. החזרה במקום הדפסה.** הביטוי הבוליאני עצמו הוא ההחלטה:

```python
def engine_cut(altitude, touchdown_signal):
    return altitude <= h_logic and touchdown_signal

r = engine_cut(1500, True)    # False
```

**3. שלושה רגעים.** רק ברגע (ב) שני התנאים מתקיימים:

```python
engine_cut(1500, True)    # False: the sensors are not read yet
engine_cut(40, True)      # True: the recorded signal is read as touchdown
engine_cut(40, False)     # False
```

**4. מהירות בנפילה חופשית.** $v^2 = v_0^2 + 2gh$:

```python
def impact_speed(v0, h, g):
    return (v0**2 + 2 * g * h) ** 0.5
```

**5. מהירות הנחיתה.** הפונקציה קוראת לשתי הפונקציות הקודמות. זו התשובה שמגישים:

```python
def landing_speed(touchdown_signal):
    if engine_cut(h_logic, touchdown_signal):
        return impact_speed(v_at_40, h_logic, g_mars)
    else:
        return v_nominal

speed = landing_speed(True)    # 21.58... (m/s)
landing_speed(False)           # 2.4
```

## מה השתבש

לפי דוח ועדת הבדיקה, הסיבה הסבירה היא אות רגעי מזויף בחיישני המגע, שנוצר בזמן פריסת רגלי הנחיתה, הרבה מעל פני השטח. כשהתוכנה התחילה לקרוא את החיישנים בגובה 40 מטר, היא פירשה את האות הזה כנגיעה בקרקע וכיבתה את מנועי הירידה. לפי הדוח, הנחתת פגעה בקרקע במהירות של כ-22 מטר לשנייה, במקום 2.4.

## תשובות שגויות נפוצות

- **2.4:** הפונקציה `engine_cut` לא תוקנה (סעיף 2). היא מחזירה `None`, ש-`if` מתייחס אליו כ-`False`, ולכן `landing_speed` מחזירה את מהירות הנחיתה המתוכננת.
- **17.2:** נפילה ממנוחה, בלי המהירות ההתחלתית `v_at_40` (סעיף 4).
- **13.0:** המהירות בגובה 40 מטר, בלי הנפילה (סעיף 5).
- **466:** $v^2$ במקום $v$, בלי השורש (סעיף 4).

## למי שסיים

בכיבוי בגובה 20 מטר המהירות היא כ-17.8 מטר לשנייה, ב-40 מטר כ-21.6, וב-80 מטר כ-27.6. הגובה מכפיל את עצמו, אבל המהירות גדלה הרבה פחות, כי היא תלויה בשורש של $v_0^2 + 2gh$.

<p><a href="../board.html?round=polar">→ חזרה ללוח התשובות</a></p>
