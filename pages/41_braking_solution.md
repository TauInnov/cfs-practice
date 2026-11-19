---
orphan: true
---

# פתרון: 2. מרחק בלימה

<p><a href="../board.html?round=braking">→ חזרה ללוח התשובות</a></p>

**התשובה: כ-51.2 קמ"ש.** בכביש יבש המהירות המקסימלית היא כ-63.2 קמ"ש: הגשם מוריד אותה בכ-12 קמ"ש.

## הנתונים

הפרמטרים והפונקציות מתא הנתונים בעמוד, שעליהם מבוססות כל השורות בהמשך:

<div dir="ltr" style="text-align: left">

```python
g = 9.81                        # gravitational acceleration (m/s^2)
t_react = 1.0                   # reaction time of the driver (s)
mu_dry = 0.7                    # friction coefficient between tires and road, dry road
mu_wet = 0.4                    # friction coefficient between tires and road, wet road
speeds_kmh = [30, 50, 70, 90]   # speeds to check (km/h)
D = 40.0                        # distance to the obstacle when the driver sees it (m)

mu = mu_dry                     # the road is dry


# the function as it was given to you: the stopping distance (m) for an initial speed v0 (m/s)
def stopping_distance(v0, mu=mu):
    return v0 * t_react + v0 ** 2 / (2 * mu * g)


# a new list with f applied to every value
def apply_to_all(f, values):
    return [f(x) for x in values]
```

</div>

## שלב אחר שלב

הסעיפים כאן זהים לסעיפי העמוד.

**1. קריאת קוד.** `d_dry` ו-`d_wet` הם מרחקי העצירה במהירות 50 קמ"ש בכביש יבש וברטוב. בכביש רטוב החיכוך חלש יותר, ולכן `d_wet` צריך להיות גדול יותר. בפועל:

<div dir="ltr" style="text-align: left">

```python
mu = mu_wet
d_dry = stopping_distance(50 / 3.6, mu_dry)    # 27.93...
d_wet = stopping_distance(50 / 3.6)            # 27.93...: the same, as if the road were dry
print(mu)                                      # 0.4
```

</div>

ערך ברירת המחדל <span dir="ltr">`mu=mu`</span> מחושב **פעם אחת**, כשהשורה `def` רצה. באותו רגע `mu` היה 0.7, וזה הערך שנשמר. השינוי של `mu` אחר כך לא משפיע עליו.

**2. התיקון.**

<div dir="ltr" style="text-align: left">

```python
def stopping_distance(v0, mu):
    return v0 * t_react + v0 ** 2 / (2 * mu * g)

# running the cell of section 1 again: TypeError: stopping_distance() missing 1 required positional argument: 'mu'

d_wet = stopping_distance(50 / 3.6, mu_wet)     # 38.47...
d_wet > d_dry                                   # True
v0 = 50 / 3.6
abs((d_wet - v0 * t_react) / (d_dry - v0 * t_react) - mu_dry / mu_wet) < 1e-12    # True
```

</div>

הודעת שגיאה עוצרת את הריצה ומראה איפה הבעיה. מספר שגוי שנראה סביר ממשיך הלאה בלי שאיש ישים לב.

**3. מרחקי העצירה.**

<div dir="ltr" style="text-align: left">

```python
wet_distances = apply_to_all(lambda v: stopping_distance(v / 3.6, mu_wet), speeds_kmh)
print(wet_distances)        # about [17.2, 38.5, 67.6, 104.6]
```

</div>

המרחק עובר את 40 מטר בין 50 ל-70 קמ"ש.

**4. המהירות המקסימלית.**

<div dir="ltr" style="text-align: left">

```python
def max_speed(D, mu, t_r=t_react):
    a = 1 / (2 * mu * g)
    b = t_r
    c = -D
    return (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

v = max_speed(D, mu_wet)                                        # about 14.22 m/s
abs(stopping_distance(v, mu_wet) - D) < 1e-9                    # True
abs(max_speed(D, mu_wet, t_r=0) - (2 * mu_wet * g * D) ** 0.5) < 1e-9    # True
v_max_kmh = round(v * 3.6, 1)                                   # 51.2
50 < v_max_kmh < 70                                             # True
```

</div>

הפתרון החיובי הוא זה עם הסימן <span dir="ltr">`+`</span> לפני השורש: מכיוון ש-<span dir="ltr">&#8288;$c < 0$</span>, השורש גדול מ-<span dir="ltr">&#8288;$b$</span>, ולכן <span dir="ltr">&#8288;$-b + \sqrt{b^2 - 4ac} > 0$</span>.

## מה עומד מאחורי זה

ערך ברירת מחדל מחושב פעם אחת, כשהפונקציה מוגדרת. ערך ברירת מחדל שנלקח ממשתנה גלובלי "מקפיא" את הערך שהיה לו באותו רגע, ולכן שינוי מאוחר של המשתנה לא משפיע על הפונקציה. כשאין ערך סביר אחד שמתאים לרוב הקריאות, כמו מקדם החיכוך, עדיף פרמטר בלי ברירת מחדל. זמן התגובה, לעומת זאת, הוא ברירת מחדל סבירה, ואפשר לשנות אותו בקריאה כשצריך.

## תשובות שגויות נפוצות

- **63.2:** מקדם החיכוך של כביש יבש, למשל בגלל ערך ברירת המחדל מסעיף 1.
- **14.2:** המהירות במטר לשנייה, בלי ההמרה לקמ"ש.
- **63.8:** בלי זמן התגובה.
- **ערך שלילי (בערך <span dir="ltr">-79.5</span>):** הפתרון השלילי של המשוואה.

## למי שסיים

<div dir="ltr" style="text-align: left">

```python
round(max_speed(D, mu_wet, t_r=2.0) * 3.6, 1)    # 41.5

mu = mu_dry
start_raining()
print(mu)                                        # 0.7
```

</div>

עם זמן תגובה של 2 שניות המהירות המקסימלית יורדת בעוד כ-10 קמ"ש. בפונקציה `start_raining` ההשמה <span dir="ltr">`mu = mu_wet`</span> יוצרת משתנה **מקומי** בשם `mu`, שקיים רק בתוך הפונקציה. המשתנה הגלובלי `mu` לא משתנה, ולכן מודפס 0.7.

<p><a href="../board.html?round=braking">→ חזרה ללוח התשובות</a></p>
