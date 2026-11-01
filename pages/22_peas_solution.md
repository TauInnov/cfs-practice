---
orphan: true
---

# פתרון: 3. האפונים של מנדל, 1865

<p><a href="../board.html?round=peas">→ חזרה ללוח התשובות</a></p>

**התשובה: יחס של כ-2.98**, כלומר 14,949 צמחים בצורה השלטת לעומת 5,010 בצורה הנסגרת.

## הנתונים

הפרמטרים מתא הנתונים בעמוד, שעליהם מבוססות כל השורות בהמשך:

```python
# the seven traits, and the counts in the second generation of each experiment
traits = ["seed shape", "seed color", "seed coat color", "pod shape",
          "pod color", "flower position", "stem length"]
dominant = [5474, 6022, 705, 882, 428, 651, 787]     # plants showing the dominant form
recessive = [1850, 2001, 224, 299, 152, 207, 277]    # plants showing the recessive form
```

## שלב אחר שלב

הסעיפים כאן זהים לסעיפי העמוד. סעיף 1 בודק את הנתונים, סעיפים 2 ו-3 מסתכלים על ניסויים בודדים, וסעיף 4 על כל הניסויים יחד.

**1. מספר הניסויים.** ברשימות מקבילות, האורכים חייבים להיות שווים:

```python
len(traits)                                              # 7
len(traits) == len(dominant) and len(dominant) == len(recessive)   # True
```

**2. הניסוי הגדול ביותר.** `max` מחזיר את הערך, ו-`index` את המיקום שלו. באותו מיקום נמצאים שם התכונה והספירה הנסגרת של אותו ניסוי:

```python
i = dominant.index(max(dominant))         # 1
traits[i]                                 # "seed color"
dominant[i] / recessive[i]                # about 3.01
```

**3. הניסוי הקטן ביותר.**

```python
j = recessive.index(min(recessive))       # 4
traits[j]                                 # "pod color"
dominant[j] / recessive[j]                # about 2.82
```

בניסוי הגדול היחס קרוב יותר ל-3. בניסוי קטן, הבדל של כמה צמחים משנה את היחס הרבה יותר.

**4. כל הניסויים יחד.** זו התשובה שמגישים:

```python
total_dom = sum(dominant)                 # 14949
total_rec = sum(recessive)                # 5010
ratio = total_dom / total_rec             # about 2.98
```

## מה עומד מאחורי זה

הרשימות המקבילות שומרות את הקשר בין הנתונים דרך האינדקס: `traits[i]`, `dominant[i]` ו-`recessive[i]` מתארים את אותו ניסוי. לכן `index` של ערך ברשימה אחת מאפשר לשלוף את המידע המתאים מהאחרות. כשמחברים את כל הניסויים, הסטיות של הניסויים הקטנים כמעט נעלמות, והיחס מתקרב ל-3.

## תשובות שגויות נפוצות

- **0.335:** יחס הפוך, נסגרת חלקי שלטת.
- **0.749:** החלק של הצמחים בצורה השלטת מכלל הצמחים, 14,949 מתוך 19,959.
- **3.01 או 2.82:** היחס בניסוי בודד (סעיפים 2 ו-3), ולא בכל הניסויים יחד.
- **3:** הערך התיאורטי, ולא הערך שחושב מהנתונים.

## למי שסיים

```python
total = total_dom + total_rec             # 19959
total / 4                                 # 4989.75 expected recessive plants
total_rec - total / 4                     # about 20 more than expected
```

הצפי הוא כ-4,990 צמחים בצורה הנסגרת, ונספרו 5,010, הפרש של כ-0.4%. פישר טען שבמקריות "רגילה" הסטיות היו צפויות להיות גדולות יותר, ובדק זאת בניתוח סטטיסטי של כל הניסויים של מנדל. הוויכוח על הטענה נמשך עד היום. הכלי המקובל לבדיקה כזאת הוא מבחן חי בריבוע.

<p><a href="../board.html?round=peas">→ חזרה ללוח התשובות</a></p>
