---
orphan: true
---

# פתרון: 3. קרח בכוס

<p><a href="../board.html?round=ice">→ חזרה ללוח התשובות</a></p>

**התשובה: כ-17.3 גרם קרח.** המים מוסרים כ-20,930 ג'אול כשהם מתקררים עד 0°C, ומספיקים להמיס כ-62.7 גרם מתוך 80.

## הנתונים

הפרמטרים מתא הנתונים בעמוד, שעליהם מבוססות כל השורות בהמשך:

<div dir="ltr" style="text-align: left">

```python
c = 4.186                               # specific heat of water (J/(g*C))
L = 334.0                               # heat of fusion of ice (J/g)
m_water = 250.0                         # mass of the water in each glass (g)
m_cube = 20.0                           # mass of one ice cube, at 0 C (g)
T_glasses = [20.0, 30.0, 40.0, 50.0]    # initial temperature of the water in four glasses (C)


# a new list with f applied to every value
def apply_to_all(f, values):
    return [f(x) for x in values]
```

</div>

## שלב אחר שלב

הסעיפים כאן זהים לסעיפי העמוד.

**1. קריאת קוד.** הניבוי: בכוס של 20°C המים מוסרים כ-21,000 ג'אול, וקוביה אחת צריכה כ-6,700, ולכן היא נמסה כולה בכל הכוסות. הערכים ב-`cooling` צריכים להיות חיוביים, כמה מעלות. בפועל:

<div dir="ltr" style="text-align: left">

```python
print(T_final)              # about [12.6, 21.9, 31.1, 40.4]
print(cooling)              # [0.0, 0.0, 0.0, 0.0]
T_final is T_glasses        # True
print(T_glasses)            # about [12.6, 21.9, 31.1, 40.4]: changed too
# running the cell again cools the same glasses again: about [5.8, 14.3, 22.9, 31.5]
```

</div>

<span dir="ltr">`T_final = T_glasses`</span> לא יוצרת רשימה חדשה, אלא שם נוסף לאותה רשימה. הלולאה משנה את הרשימה היחידה שיש, ולכן `cooling` משווה כל טמפרטורה לעצמה.

**2. התיקון.** בונים רשימה חדשה:

<div dir="ltr" style="text-align: left">

```python
T_final = []
for T in T_glasses:
    T_final.append((m_water * c * T - m_cube * L) / ((m_water + m_cube) * c))

cooling = [T_glasses[i] - T_final[i] for i in range(len(T_glasses))]
print(cooling)              # about [7.4, 8.1, 8.9, 9.6]
T_final is T_glasses        # False
T_glasses[0] == 20.0        # True
min(cooling) > 0            # True
```

</div>

פתרון שקול: <span dir="ltr">`T_final = T_glasses.copy()`</span> בשורה הראשונה, והלולאה כפי שהיא.

**3. האם כל הקרח נמס?**

<div dir="ltr" style="text-align: left">

```python
melts = apply_to_all(lambda T: m_water * c * T >= 4 * m_cube * L, T_glasses)
print(melts)                # [False, True, True, True]

m_i = 4 * m_cube
(m_water * c * 20.0 - m_i * L) / ((m_water + m_i) * c)    # about -4.19
```

</div>

בכוס של 20°C לא כל הקרח נמס. הנוסחה נותנת מים בטמפרטורה של כ-4°C מתחת לאפס, יחד עם קרח: אבל מים וקרח יכולים להיות יחד בשיווי משקל רק ב-0°C. הנוסחה הניחה שכל הקרח נמס, וההנחה לא מתקיימת.

**4. הפונקציות.** שתי הפונקציות בודקות את אותו תנאי:

<div dir="ltr" style="text-align: left">

```python
def final_temperature(T_w, m_ice, m_w=m_water):
    if m_w * c * T_w >= m_ice * L:
        return (m_w * c * T_w - m_ice * L) / ((m_w + m_ice) * c)
    else:
        return 0


def ice_left(T_w, m_ice, m_w=m_water):
    if m_w * c * T_w >= m_ice * L:
        return 0
    else:
        return m_ice - m_w * c * T_w / L


abs(final_temperature(30.0, 0) - 30.0) < 1e-12      # True
ice_left(30.0, 4 * m_cube) == 0                      # True
final_temperature(20.0, 4 * m_cube) == 0             # True

melted = 4 * m_cube - ice_left(20.0, 4 * m_cube)
abs(m_water * c * 20.0 - L * melted) < 1e-9          # True

left = round(ice_left(20.0, 4 * m_cube), 1)          # 17.3
```

</div>

## מה עומד מאחורי זה

השמה של רשימה למשתנה חדש (<span dir="ltr">`T_final = T_glasses`</span>) אינה מעתיקה אותה: שני השמות מפנים לאותה רשימה בזיכרון, ושינוי דרך אחד מהם נראה גם דרך השני. כאן הטעות הייתה שקטה: הטמפרטורות הסופיות חושבו נכון, ורק ההשוואה ל"לפני" נכשלה, כי ה"לפני" כבר לא היה קיים. הבדיקה הפיזיקלית בסעיף 3 היא אותו רעיון בצד הפיזיקה: נוסחה נכונה רק בתנאים שבהם היא נגזרה, ותוצאה בלתי אפשרית (מים מתחת לאפס עם קרח) מראה שהתנאי לא מתקיים.

## תשובות שגויות נפוצות

- **0:** הנחה שכל הקרח נמס, או תנאי הפוך בפונקציה.
- **<span dir="ltr">-4.19</span> (או <span dir="ltr">-4.2</span>):** הטמפרטורה לפי הנוסחה, בלי לבדוק את התנאי (סעיף 3).
- **62.7:** מסת הקרח **שנמס**, ולא זו שנשארה.
- **40.5:** חישוב עם <span dir="ltr">`T_glasses[0]`</span> אחרי שהוא שונה בסעיף 1 (כ-12.6°C) ולא שוחזר.

## למי שסיים

<div dir="ltr" style="text-align: left">

```python
n = 0
while ice_left(20.0, (n + 1) * m_cube) == 0:
    n = n + 1
print(n)                    # 3

print(len(backup))          # 2
print(backup[0][1])         # 5.0
```

</div>

שלוש קוביות (60 גרם) צריכות כ-20,040 ג'אול, פחות מ-20,930, וארבע כבר יותר.

<span dir="ltr">`glasses.copy()`</span> יוצרת רשימה חיצונית חדשה, ולכן `append` ל-`glasses` לא משפיע על `backup`. אבל האיברים של הרשימה, הרשימות הפנימיות `[מסה, טמפרטורה]`, לא הועתקו: שתי הרשימות החיצוניות מפנות לאותן רשימות פנימיות. לכן השינוי של <span dir="ltr">`glasses[0][1]`</span> נראה גם ב-<span dir="ltr">`backup[0][1]`</span>. עותק כזה נקרא **עותק רדוד** (shallow copy).

<p><a href="../board.html?round=ice">→ חזרה ללוח התשובות</a></p>
