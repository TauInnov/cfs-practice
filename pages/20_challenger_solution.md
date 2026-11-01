---
orphan: true
---

# פתרון: 1. צ'לנג'ר, ינואר 1986

<p><a href="../board.html?round=challenger">→ חזרה ללוח התשובות</a></p>

**התשובה: שיעור הנזק בטיסות הקרות היה גדול פי 6.33 משיעור הנזק בשאר הטיסות.** בכל ארבע הטיסות הקרות נמצא נזק, לעומת 3 מתוך 19 בשאר הטיסות.

## הנתונים

הפרמטרים מתא הנתונים בעמוד, שעליהם מבוססות כל השורות בהמשך:

```python
launch_temp = 36      # air temperature at the Challenger launch, 28 January 1986 (F)
cold_limit = 65       # in this exercise, a launch below this temperature is "cold" (F)

# launch temperatures (F) of the 23 earlier flights whose boosters were inspected
temps_damage = [70, 57, 63, 70, 53, 75, 58]                                      # O-ring damage found
temps_clean = [66, 69, 68, 67, 72, 73, 70, 78, 67, 67, 75, 70, 81, 76, 79, 76]   # no damage found
```

## שלב אחר שלב

הסעיפים כאן זהים לסעיפי העמוד. סעיף 1 הוא מה שנבחן לפני השיגור, וסעיפים 2 עד 5 מסתכלים על כל הטיסות.

**1. רק הטיסות עם נזק.** נזק נמצא גם בשיגור הקר ביותר וגם בשיגור חם יחסית:

```python
min(temps_damage)                          # 53
max(temps_damage)                          # 75
```

מכאן נראה שנזק קורה בכל טמפרטורה, ושהקור אינו גורם מיוחד.

**2. כל הטיסות, ממוינות.** חיבור שתי הרשימות ומיון:

```python
all_temps = sorted(temps_damage + temps_clean)
len(all_temps)                             # 23
```

**3. הטיסות הקרות ושאר הטיסות.** ברשימה הממוינת, הטמפרטורה הראשונה שאינה קרה היא 66, וכל מה שלפניה קר:

```python
n_cold = all_temps.index(66)               # 4
cold = all_temps[:n_cold]                  # [53, 57, 58, 63]
warm = all_temps[n_cold:]                  # 19 flights
```

**4. נזק בטיסות הקרות.** בדיקה לכל טיסה קרה אם היא ברשימת הטיסות עם נזק:

```python
checks = [cold[0] in temps_damage, cold[1] in temps_damage,
          cold[2] in temps_damage, cold[3] in temps_damage]   # [True, True, True, True]
damage_cold = sum(checks)                  # 4
```

**5. שיעורי הנזק והיחס.** שאר הטיסות עם נזק הן אלה שאינן קרות. זו התשובה שמגישים:

```python
damage_warm = len(temps_damage) - damage_cold   # 3
rate_cold = damage_cold / len(cold)             # 1.0
rate_warm = damage_warm / len(warm)             # about 0.158
ratio = rate_cold / rate_warm                   # about 6.33
```

## מה השתבש

הרשימה `temps_damage` לבדה מראה נזק בין 53°F ל-75°F, ולכן נראה שאין קשר לטמפרטורה. המידע החשוב נמצא ברשימה שלא נבחנה: 16 הטיסות בלי נזק כולן שוגרו ב-66°F ומעלה. רק כשמחברים את שתי הרשימות רואים שבכל טיסה קרה היה נזק. הקוד בכל אחד מהשלבים תקין; השגיאה היא בבחירה אילו נתונים להכניס לחישוב.

## תשובות שגויות נפוצות

- **0.158:** יחס הפוך, או שיעור הנזק בטיסות החמות בלבד (סעיף 5).
- **0.304:** שיעור הנזק בכל 23 הטיסות יחד (7 מתוך 23), בלי להפריד לקבוצות.
- **1.0:** שיעור הנזק בטיסות הקרות בלבד (סעיף 5).
- **2.71:** שימוש ב-`len(temps_damage)` במקום `damage_warm`, כלומר ספירה של הטיסות הקרות פעמיים.

## למי שסיים

```python
min(all_temps) - launch_temp               # 17 degrees colder
all_temps.insert(0, launch_temp)           # goes in at index 0, before every earlier flight
```

שיגור צ'לנג'ר היה קר ב-17°F מהשיגור הקר ביותר שקדם לו, והוא נכנס בתחילת הרשימה הממוינת. לא היה אף שיגור קודם בטמפרטורה כזאת, ולכן הנתונים לא יכלו להראות שהשיגור בטוח; כל מה שהם הראו הוא שבכל ארבעת השיגורים הקרים שכן היו, נמצא נזק.

<p><a href="../board.html?round=challenger">→ חזרה ללוח התשובות</a></p>
