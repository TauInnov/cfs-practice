---
orphan: true
---

# פתרון: 1. אייר פראנס 447, יוני 2009

<p><a href="../board.html?round=af447">→ חזרה ללוח התשובות</a></p>

**התשובה:** `FTFT`. ברגע 3 הכנף בעמידה עמוקה, אבל המהירות הנמדדת נמוכה מ-60 קשר, ולכן המערכת אינה משמיעה אזהרה.

## הנתונים

הפרמטרים מתא הנתונים בעמוד, שעליהם מבוססות כל השורות בהמשך:

```python
v_valid = 60          # below this measured speed the angle-of-attack data are invalid (kt)
aoa_limit = 10        # above this angle of attack the wing is stalled (deg), chosen for illustration

# four moments: measured speed (kt) and angle of attack (deg)
v1, aoa1 = 275, 2     # moment 1
v2, aoa2 = 100, 30    # moment 2
v3, aoa3 = 50, 40     # moment 3
v4, aoa4 = 65, 32     # moment 4
```

## שלב אחר שלב

הסעיפים כאן זהים לסעיפי העמוד. סעיפים 1 ו-2 בודקים את הרגעים, סעיף 3 כותב את הפונקציה, וסעיפים 4 ו-5 מרכיבים את התשובה.

**1. האם המדידה תקפה.** המדידה תקפה כשהמהירות אינה נמוכה מ-60 קשר:

```python
valid1 = v1 >= v_valid    # True
valid2 = v2 >= v_valid    # True
valid3 = v3 >= v_valid    # False
valid4 = v4 >= v_valid    # True
```

**2. האם הכנף בעמידה.** בשלושת הרגעים האחרונים הכנף בעמידה בפועל:

```python
stalled1 = aoa1 > aoa_limit    # False
stalled2 = aoa2 > aoa_limit    # True
stalled3 = aoa3 > aoa_limit    # True
stalled4 = aoa4 > aoa_limit    # True
```

**3. הפונקציה.** את תקפות המדידה בודקים ראשונה. אילו הזווית נבדקה קודם, הענף הראשון היה מחזיר `True` גם כשהמדידה לא תקפה:

```python
def stall_warning(speed, aoa):
    if speed < v_valid:        # invalid data: no warning, by design
        return False
    elif aoa > aoa_limit:
        return True
    else:
        return False
```

**4. ארבעת הרגעים.**

```python
w1 = stall_warning(v1, aoa1)    # False
w2 = stall_warning(v2, aoa2)    # True
w3 = stall_warning(v3, aoa3)    # False
w4 = stall_warning(v4, aoa4)    # True
```

**5. המחרוזת.** פונקציה קטנה לתו אחד, וחיבור של ארבעה תווים. זו התשובה שמגישים:

```python
def letter(w):
    if w:
        return "T"
    return "F"

pattern = letter(w1) + letter(w2) + letter(w3) + letter(w4)    # "FTFT"
```

## מה השתבש

לפי ממצאי החקירה של BEA, אזהרת העמידה מושבתת בתכנון כשערכי זווית ההתקפה נחשבים לא תקפים, וכך קרה כשהמהירות הנמדדת ירדה מתחת ל-60 קשר. כשהטייס הוריד מעט את האף, המהירות הנמדדת עלתה, המדידה חזרה להיות תקפה והאזהרה נשמעה שוב. הרמת האף השתיקה אותה. כך האזהרה נשמעה דווקא כשהטייס פעל בכיוון הנכון, והמטוס נשאר בעמידה עד הפגיעה במים.

## תשובות שגויות נפוצות

- **FTTT:** בדיקת זווית ההתקפה לפני תקפות המדידה (סעיף 3), או תשובה לפי הפיזיקה של הכנף ולא לפי המפרט.
- **FFTF:** תנאי התקפות הפוך, למשל `speed >= v_valid` במקום `speed < v_valid` בענף הראשון.

## למי שסיים

ברגע 3 הכנף בעמידה והאזהרה שקטה. אם בודקים קודם את זווית ההתקפה, הפונקציה מחזירה `True` ברגעים 2, 3 ו-4, והתשובה היא `FTTT`. כשתנאים חופפים, סדר הענפים בשרשרת `if / elif` קובע את התוצאה.

<p><a href="../board.html?round=af447">→ חזרה ללוח התשובות</a></p>
