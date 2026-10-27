---
orphan: true
---

# פתרון: 1. אנני ג'אמפ קנון, הרווארד 1901

<p><a href="../board.html?round=stars">→ חזרה ללוח התשובות</a></p>

**התשובה:** `KAMG`. ארקטורוס מחלקה K, סיריוס A, בטלגז M והשמש G.

## הנתונים

הפרמטרים והפונקציה מתא הנתונים בעמוד, שעליהם מבוססות כל השורות בהמשך:

```python
b_wien = 2.898e-3     # Wien's displacement constant (m*K)

# wavelength at which each star's emission peaks (nm)
peak1 = 676     # Arcturus
peak2 = 292     # Sirius A
peak3 = 805     # Betelgeuse
peak4 = 502     # the Sun


# the function as it was given to you
def spectral_class(T):
    if T >= 30000:
        return "O"
    elif T >= 10000:
        return "B"
    elif T >= 6000:
        return "F"
    elif T >= 7500:
        return "A"
    elif T >= 5200:
        return "G"
    elif T >= 3700:
        return "K"
    else:
        return "M"
```

## שלב אחר שלב

הסעיפים כאן זהים לסעיפי העמוד. סעיף 1 מחשב טמפרטורה, סעיפים 2 ו-3 עוסקים בפונקציה שניתנה, וסעיפים 4 ו-5 מרכיבים את התשובה.

**1. חוק וין.** אורך הגל בננומטרים, ולכן כופלים ב-`1e-9` כדי לקבל מטרים:

```python
def wien_temperature(peak_nm):
    return b_wien / (peak_nm * 1e-9)

wien_temperature(peak4)    # about 5773 K
```

**2. בדיקת הפונקציה שניתנה.** עבור השמש היא נכונה, אבל עבור 8000 K היא מחזירה `"F"` במקום `"A"`. כל טמפרטורה של 7,500 ומעלה עונה כבר על התנאי `T >= 6000`, ולכן הענף של `"A"` לעולם אינו מתבצע:

```python
spectral_class(5772)    # "G", correct
spectral_class(8000)    # "F", should be "A"
```

**3. התיקון.** הענפים מסודרים מהסף הגבוה לנמוך, כך שהענף הראשון שמתקיים הוא הנכון:

```python
def spectral_class(T):
    if T >= 30000:
        return "O"
    elif T >= 10000:
        return "B"
    elif T >= 7500:
        return "A"
    elif T >= 6000:
        return "F"
    elif T >= 5200:
        return "G"
    elif T >= 3700:
        return "K"
    else:
        return "M"
```

**4. פונקציה שקוראת לפונקציות.**

```python
def classify(peak_nm):
    return spectral_class(wien_temperature(peak_nm))

s1 = classify(peak1)    # "K": about 4287 K
s2 = classify(peak2)    # "A": about 9925 K
s3 = classify(peak3)    # "M": about 3600 K
s4 = classify(peak4)    # "G": about 5773 K
```

**5. המחרוזת.** זו התשובה שמגישים:

```python
classes = s1 + s2 + s3 + s4    # "KAMG"
```

## מה השתבש

הפונקציה שניתנה נראית סבירה, וכל הספים בה נכונים. הטעות היא בסדר של שני ענפים בלבד: בשרשרת `elif` רק הענף הראשון שמתקיים מתבצע, וכל כוכב בטווח של A "נתפס" קודם בענף של F. הפונקציה עובדת נכון לכל מחלקה מלבד A, ולכן בדיקה על השמש, או על כל כוכב שאינו במחלקה A, עוברת בהצלחה.

## תשובות שגויות נפוצות

- **KFMG:** הפונקציה לא תוקנה (סעיף 3). סיריוס מקבל F.
- **MMMM:** אורך הגל לא הומר מננומטרים למטרים (סעיף 1). הטמפרטורות יוצאות זעירות, וכל הכוכבים נופלים לענף `else`.
- **KKMK:** הענפים סודרו מהסף הנמוך לגבוה (`T >= 3700` ראשון), וכל כוכב חם מ-3,700 K מקבל K.

## למי שסיים

בגרסה עם טווחים מלאים, כמו `7500 <= T and T < 10000`, כל טמפרטורה מקיימת תנאי אחד בלבד, ולכן סדר הענפים אינו משנה. הפונקציה המקורית מיינה לא נכון רק את סיריוס. השמש במחלקה G, שהענף שלה אינו מושפע מההחלפה, ולכן הבדיקה עליה עוברת: כדי לגלות את הטעות צריך לבדוק כוכב בטווח של A.

<p><a href="../board.html?round=stars">→ חזרה ללוח התשובות</a></p>
