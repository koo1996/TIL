# 사전 설정

## 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

## Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

## table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
CREATE TABLE healthcare (
id PRIMARY KEY,        
sido INTEGER NOT NULL, 
gender INTEGER NOT NULL,
age INTEGER NOT NULL,  
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,   
va_left REAL NOT NULL, 
va_right REAL NOT NULL,

blood_pressure INTEGER 
NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);
```

# 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
COUNT(*)
--------
1000000
```

### 2. 나이 그룹이 10(age)미만인 사람의 수를 출력하시오.

```sql
```
SELECT COUNT(*) FROM healthcare WHERE age < 10;

--------
156277
```
```

### 3. 성별이 1인 사람의 수를 출력하시오.

```sql
```
SELECT COUNT(*) FROM healthcare WHERE gender = 1;

--------
510689
```
```

### 4. 흡연 수치(smoking)가 3이면서 음주(is_drinking)가 1인 사람의 수를 출력하시오.

```sql
```
SELECT COUNT(*) FROM healthcare WHERE smoking = 3 and is_drinking = 1;

--------
150361
```
```

### 5. 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람의 수를 출력하시오.

```sql
```
SELECT COUNT(*) FROM healthcare WHERE va_left = 2.0 or va_right = 2.0;

--------
8443
```
```

### 6. 시도(sido)를 모두 중복 없이 출력하시오.

```sql
```
SELECT DISTINCT sido FROM healthcare;

----
36
27
11
31
41
44
48
30
42
43
46
28
26
47
45
29
49
```
```

### 자유롭게 조합해서 원하는 데이터를 출력해보세요.

1번) 나이가 20초과 30미만인 사람중에 흡연수치가 3인 사람의 수를 출력하시오.
SELECT count(*) FROM healthcare WHERE 20 < age < 30 AND smoking = 3;

--------
183711

2번) 나이가 20미만이면서 음주가 1인 사람의 수를 출력하시오.
SELECT count(*) FROM healthcare WHERE age < 20 AND is_drinking = 1;

--------
584685

3번) 나이가 10이상이면서 양쪽 시력이 1.0이상이면서 성별이 2인 사람의 수를 출력하시오.
SELECT count(*) FROM healthcare WHERE age >= 10 AND va_left >= 1.0 AND va_right >= 1.0 AND gender = 2;

--------
104859
> 예) 허리 둘레가 x이상이면서 몸무게가 y이하인 사람