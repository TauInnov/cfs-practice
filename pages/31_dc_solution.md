---
orphan: true
---

# פתרון: 2. זרם ישר, ניו יורק 1882

<p><a href="../board.html?round=dc">→ חזרה ללוח התשובות</a></p>

**התשובה: 550 מטר.** במרחק 550 מטר המתח הוא כ-100.65 וולט, ובמרחק 600 מטר כבר כ-99.8 וולט.

## הנתונים

הפרמטרים מתא הנתונים בעמוד, שעליהם מבוססות כל השורות בהמשך:

```python
V_station = 110     # voltage at the station (V)
V_min = 100         # the lamps need at least this voltage (V)
I = 50              # current drawn by one street (A)
rho = 1.7e-8        # resistivity of copper (ohm*m)
area_mm2 = 100      # cross-section of each copper wire (mm^2)
step = 50           # the distances are checked every 50 m


# the function as it was given to you: the farthest distance (m), in steps of `step`, where the lamps get at least V_min
# (it calls voltage_at, which you will write in section 1)
def max_distance():
    d = 0
    while voltage_at(d) >= V_min:
        d = d + step
    return d
```

## שלב אחר שלב

הסעיפים כאן זהים לסעיפי העמוד.

**1. פונקציה במקום ארבע שורות.**

```python
print(V_200, V_400, V_600, V_800)       # about 106.6, 103.2, 104.9, 96.4

def voltage_at(d):
    R = rho * 2 * d / (area_mm2 * 1e-6)
    return V_station - I * R

voltage_at(200), voltage_at(400), voltage_at(600), voltage_at(800)   # about 106.6, 103.2, 99.8, 96.4
```

בשורה של 600 מטר חסר הגורם 2 (החוט בחזרה), ולכן היא נותנת 104.9 וולט, יותר מאשר ב-400 מטר, ומעל `V_min` במקום מתחתיו. בפונקציה הנוסחה כתובה פעם אחת, ואין שורה שאפשר לשכוח לעדכן.

**2. המתח בכמה מרחקים.**

```python
voltages = [voltage_at(d) for d in range(0, 1001, 100)]
print(voltages)    # about [110.0, 108.3, 106.6, 104.9, 103.2, 101.5, 99.8, 98.1, 96.4, 94.7, 93.0]
```

המתח יורד ב-1.7 וולט בכל 100 מטר, ועובר מתחת ל-100 וולט בין 500 ל-600 מטר.

**3. הלולאה הולכת צעד אחד יותר מדי.**

```python
d_max = max_distance()
print(d_max)                            # 600
voltage_at(d_max) >= V_min              # False: about 99.8 V
```

הלולאה ממשיכה כל עוד המתח מספיק, ולכן היא נעצרת רק ב-`d` הראשון שבו המתח **אינו** מספיק. הפונקציה מחזירה את המרחק שכבר נכשל.

**4. תיקון ותשובה.** הצעד האחרון שעבר הוא אחד לפני המקום שבו הלולאה נעצרה. זו התשובה שמגישים:

```python
def max_distance():
    d = 0
    while voltage_at(d + step) >= V_min:
        d = d + step
    return d

d_max = max_distance()                  # 550
voltage_at(d_max) >= V_min              # True
voltage_at(d_max + step) < V_min        # True
```

פתרון שקול: להשאיר את הלולאה כפי שהיא ולהחזיר `d - step`.

## מה השתבש

בלולאת `while` שמחפשת את "האחרון שעובר", הלולאה נעצרת רק אחרי שהיא מגיעה לראשון שנכשל. זו טעות "צעד אחד יותר" נפוצה, והיא מתגלה כשבודקים את הערך שהפונקציה מחזירה, ולא רק מסתכלים עליו. בקוד שחוזר על עצמו הייתה טעות שנייה: שורה אחת שבה חסר גורם, שנותנת תוצאה סבירה למראה אבל שגויה.

## תשובות שגויות נפוצות

- **600:** הפונקציה שקיבלתם בלי תיקון (סעיף 3).
- **1150:** חוט אחד בלבד, בלי הגורם 2, כמו בשורה של `V_600`.
- **588:** פתרון מדויק של המשוואה, בלי קפיצות של 50 מטר.
- **500:** המרחק האחרון שעובר ברשימה של סעיף 2, שבה הקפיצות הן של 100 מטר.

## למי שסיים

```python
I = I * V_station / 2200                # same power: 2.5 A
V_station = 2200
V_min = 2000
max_distance()                          # 235250 m, about 235 km
235250 / 550                            # about 428 times farther
```

הזרם קטן פי 20, ולכן הפסד המתח בחוט קטן פי 20; וההפסד המותר גדל פי 20 (200 וולט במקום 10). יחד המרחק גדל פי כ-400. זו הסיבה שרשתות החשמל עברו לזרם חילופין, שבו קל להעלות ולהוריד את המתח.

<p><a href="../board.html?round=dc">→ חזרה ללוח התשובות</a></p>
