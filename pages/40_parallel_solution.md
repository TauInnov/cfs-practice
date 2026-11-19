---
orphan: true
---

# פתרון: 1. נגדים במקביל

<p><a href="../board.html?round=parallel">→ חזרה ללוח התשובות</a></p>

**התשובה: 2.374 וואט.** ההתנגדות השקולה היא כ-56.6 אוהם, הזרם מהסוללה כ-0.205 אמפר, ומתח ההדקים כ-11.59 וולט. עם סוללה אידיאלית ההספק היה 2.545 וואט.

## הנתונים

הפרמטרים והפונקציות מתא הנתונים בעמוד, שעליהם מבוססות כל השורות בהמשך:

<div dir="ltr" style="text-align: left">

```python
V = 12.0                            # battery voltage (V)
resistors = [100, 220, 470, 1000]   # the resistances, all connected in parallel to the battery (ohm)
r_internal = 2.0                    # internal resistance of the battery, used in section 4 (ohm)


# the function as it was given to you: the equivalent resistance of resistors in parallel
def parallel(rs):
    for i in range(len(rs)):
        rs[i] = 1 / rs[i]
    return 1 / sum(rs)


# the equivalent resistance of resistors in series
def series(rs):
    return sum(rs)


# a new list with f applied to every value
def apply_to_all(f, values):
    return [f(x) for x in values]
```

</div>

## שלב אחר שלב

הסעיפים כאן זהים לסעיפי העמוד.

**1. קריאת קוד.** `R_p` היא ההתנגדות השקולה במקביל, וצריכה להיות קטנה מ-100 אוהם. `R_s` היא ההתנגדות השקולה בטור, סכום הנגדים: 1790 אוהם. בפועל:

<div dir="ltr" style="text-align: left">

```python
R_p = parallel(resistors)
R_s = series(resistors)
print(R_p)              # 56.58...: as expected
print(R_s)              # 0.0176...: not 1790
print(resistors)        # [0.01, 0.0045..., 0.0021..., 0.001]
```

</div>

השורה <span dir="ltr">`rs[i] = 1 / rs[i]`</span> מחליפה כל התנגדות בהופכי שלה. `rs` אינו עותק של `resistors`, אלא שם נוסף לאותה רשימה, ולכן הפונקציה שינתה את `resistors`. `parallel` עצמה החזירה ערך נכון, כי היא סכמה את ההופכיים כפי שהנוסחה דורשת. אבל `series` קיבלה אחר כך את הרשימה המשונה, וסכמה את ההופכיים במקום את ההתנגדויות.

**2. התיקון.** מחשבים את הסכום במשתנה נפרד, ואת `rs` רק קוראים:

<div dir="ltr" style="text-align: left">

```python
def parallel(rs):
    total = 0
    for R in rs:
        total = total + 1 / R
    return 1 / total

R_s == 1790             # True
R_p < min(resistors)    # True
```

</div>

**3. הזרמים.**

<div dir="ltr" style="text-align: left">

```python
currents = apply_to_all(lambda R: V / R, resistors)    # about [0.12, 0.0545, 0.0255, 0.012]
abs(sum(currents) - V / R_p) < 1e-12                    # True
```

</div>

**4. סוללה אמיתית.** כל פונקציה מתרגמת שלב אחד, וקוראת לפונקציה של השלב הקודם. את `emf` ו-`r` מעבירים הלאה, אחרת הפונקציה הפנימית תשתמש בערכי ברירת המחדל שלה:

<div dir="ltr" style="text-align: left">

```python
def battery_current(rs, emf=12.0, r=0.0):
    return emf / (r + parallel(rs))

def terminal_voltage(rs, emf=12.0, r=0.0):
    return emf - battery_current(rs, emf, r) * r

terminal_voltage(resistors) == 12                  # True
terminal_voltage(resistors, r=r_internal) < 12      # True: about 11.59

def total_power(rs, emf=12.0, r=0.0):
    Vt = terminal_voltage(rs, emf, r)
    return sum(apply_to_all(lambda R: Vt ** 2 / R, rs))

abs(total_power(resistors) - V ** 2 / R_p) < 1e-12  # True: about 2.545

P_total = round(total_power(resistors, r=r_internal), 3)    # 2.374

I = battery_current(resistors, r=r_internal)
abs(12.0 * I - (total_power(resistors, r=r_internal) + I ** 2 * r_internal)) < 1e-12    # True
```

</div>

הסוללה מספקת כ-2.458 וואט: כ-2.374 הופכים לחום בנגדים, וכ-0.084 בתוך הסוללה.

## מה עומד מאחורי זה

רשימה היא אובייקט שאפשר לשנות (mutable). כשמעבירים רשימה לפונקציה, הפרמטר הוא שם נוסף לאותה רשימה, ולא עותק שלה. בסעיף 1 הפונקציה `parallel` החזירה ערך נכון, ולכן הטעות לא נראתה בה עצמה, אלא רק בשורה הבאה שהשתמשה ב-`resistors`. בדיקה של התוצאה מול ערך שאפשר לדעת מראש (1790) חושפת את הבעיה מיד. בסעיף 4, הבדיקות של המקרה האידיאלי ושל שימור האנרגיה הן אותו רעיון.

## תשובות שגויות נפוצות

- **2.545:** סוללה אידיאלית, בלי ההתנגדות הפנימית: `r` לא הועבר, ו-`total_power` השתמשה בערך ברירת המחדל 0.
- **2.458:** ההספק שהסוללה מספקת, <span dir="ltr">&#8288;$\varepsilon \cdot I$</span>, כולל ההפסד בתוכה, או חישוב ההספקים עם <span dir="ltr">&#8288;$\varepsilon$</span> במקום עם <span dir="ltr">&#8288;$V_t$</span>.
- **2.368:** חישוב הזרם בלי <span dir="ltr">&#8288;$r$</span> במכנה, <span dir="ltr">&#8288;$\varepsilon / R_p$</span>.
- **0.080:** חישוב עם ההתנגדות בטור במקום במקביל.
- **ערך עצום, אלפי וואט ויותר:** חישוב אחרי ש-`resistors` שונתה בסעיף 1 ולא שוחזרה.

## למי שסיים

<div dir="ltr" style="text-align: left">

```python
P9 = total_power(resistors, emf=9.0, r=r_internal)    # about 1.335
I9 = battery_current(resistors, emf=9.0, r=r_internal)
I9 ** 2 * r_internal / (9.0 * I9) * 100              # about 3.4 percent

print(add_resistor_a(resistors, 330), resistors)    # about 48.3, resistors unchanged
print(add_resistor_b(resistors, 330), resistors)    # about 48.3, resistors now has five resistors
```

</div>

האחוז שהופך לחום בתוך הסוללה הוא <span dir="ltr">&#8288;$r/(r + R_p)$</span>, בערך 3.4%, ואינו תלוי במתח.

<span dir="ltr">`rs + [R]`</span> יוצר רשימה **חדשה** ומצמיד אליה את השם המקומי `rs`, ולכן `resistors` לא משתנה. <span dir="ltr">`rs.append(R)`</span> משנה את הרשימה עצמה, ולכן גם את `resistors`.

<p><a href="../board.html?round=parallel">→ חזרה ללוח התשובות</a></p>
