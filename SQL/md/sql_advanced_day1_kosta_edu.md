# 고급 SQL 응용 실무 — 1일차 필기노트

---

## 1. 기본 개념 정리

### ROWID vs ROWNUM
- **ROWID**: 행의 물리적 저장 위치(디스크 주소). INSERT 시 자동 부여, 영구적.
- **ROWNUM**: 쿼리 결과가 반환(fetch)되는 순서에 따라 임시로 붙는 번호. 매 쿼리 실행마다 새로 부여.
- 둘은 서로 **연동되지 않으며** 완전히 독립적인 개념.

### PK (Primary Key)
- **NOT NULL + UNIQUE** 제약조건이 자동 적용.
- PK 생성 시 **Unique Index** 자동 생성 → 빠른 조회 가능.
- UNIQUE만 걸면 NULL 허용 → PK와 다름.

### NULL
- NULL은 **값이 아니라 "값이 없음"을 나타내는 속성**.
- 정렬 대상이 아님 (Oracle에서는 ASC 시 맨 뒤, DESC 시 맨 앞).
- 연산 결과도 NULL: `NULL + 100 = NULL`, `NULL * 0 = NULL`
- 비교 시 `= NULL` 불가 → `IS NULL` 사용.
- `COUNT(컬럼명)`은 NULL을 세지 않음.

### COUNT 함수 권장사항
- `COUNT(*)` 보다 **PK 또는 NOT NULL 컬럼** 명시 권장.
- 예: `COUNT(employee_id)`

---

## 2. UNION / UNION ALL

| | UNION | UNION ALL |
|---|---|---|
| 중복 제거 | ✅ 제거 (내부 정렬 발생) | ❌ 제거 안 함 |
| 순서 | 내부적으로 정렬 | 쿼리 작성 순서대로 반환 |
| 속도 | 느림 | 빠름 |

- 중복이 없다고 보장되면 **UNION ALL이 성능상 유리**.
- UNION 결과에 WHERE/HAVING 조건을 걸려면 **인라인뷰(서브쿼리)로 감싸야** 함.
- UNION 결과에 집계 조건 적용 예시:
```sql
SELECT COUNT(*)
FROM (
    SELECT * FROM employees
    UNION ALL
    SELECT * FROM employees
);
```

### ORDER BY 위치
- `ORDER BY`는 **바깥쪽(마지막)에만** 사용.
- 안쪽 서브쿼리의 ORDER BY는 UNION을 거치면 순서 보장 안 됨 → 불필요한 리소스 낭비.

---

## 3. 성능 관점 핵심 원칙

- 인덱스 생성, GROUP BY, ORDER BY는 **정렬 연산** 수반 → 디스크 I/O, 메모리, CPU 소모.
- 필터링 단계에서 ORDER BY 제거.
- **정렬은 최종 결과를 반환하는 마지막 단계에서만** 수행.
- 불필요한 연산 제거 = 성능 최적화.

### JPP (Join Predicate Pushdown)
- 바깥쪽 쿼리의 조건이 안쪽 서브쿼리/인라인뷰 안으로 밀려 들어가는 옵티마이저 변환.
- 안쪽에서 먼저 필터링 → 데이터량 감소 → 성능 향상.
- **JPP가 작동하지 않는 경우 (5가지)**: UNION/UNION ALL, ROWNUM, Window 함수, GROUP BY, DISTINCT

---

## 4. 서브쿼리

### 스칼라 서브쿼리 (SELECT 절)
- 반드시 **1행 1열** 결과만 반환해야 함.
- 1×N → `ORA-01427: single-row subquery returns more than one row`
- N×1 (열 2개) → `ORA-00913: too many values`
- 해결: 열이 2개면 `||` 연결연산자로 합치거나, WHERE로 1행 보장, MAX/MIN/AVG로 1행 압축.
- 데이터 흐름: **MQ → SQ** (메인쿼리 데이터가 스칼라의 조건으로 사용)

### 진짜 서브쿼리 (WHERE 절)
- 서브쿼리 결과가 메인쿼리의 조건으로 사용.
- 데이터 흐름: **SQ → MQ** (스칼라 서브쿼리와 반대 방향)

### ⭐ 중요 — 서브쿼리 성능 원칙
> **서브쿼리는 메인쿼리보다 상대적으로 소량 집합을 사용하는 것이 성능상 유리하다.**

- MQ 실행 후 SQ 실행, **MQ 건수에 비례하여 SQ 실행**.
- MQ 107건 → SQ 107번 실행.
- SQ가 크면 반복 실행 시 부담 증가.
- 예: MQ=employees(107건), SQ=departments(27건) → 올바른 설계 ✅
- SQ가 효율적으로 동작하려면 **인덱스** 필요.
- 루프문과 반대 개념: 루프문은 안쪽이 커도 되지만, 스칼라 서브쿼리는 **SQ가 작아야** 함.

### 인라인뷰 vs 서브쿼리

| | 인라인뷰 | 서브쿼리 |
|---|---|---|
| 위치 | FROM 절 | WHERE / HAVING / SELECT 절 |
| 역할 | 가상의 테이블처럼 사용 | 조건값이나 필터로 사용 |
| 예시 | `FROM (SELECT ...)` | `WHERE salary > (SELECT AVG(...))` |

### HAVING vs 인라인뷰
- 성능 차이는 거의 없음.
- HAVING은 조건 변경 시 싱크 맞춰줘야 하는 번거로움 존재.
- 인라인뷰는 조건을 바깥에서 독립적으로 관리 → **유지보수 유리**.

### WHERE 1=1
- 항상 True → 전체 결과 반환.
- 다이나믹 쿼리에서 AND 조건을 계속 붙일 때 첫 줄 고정으로 사용.
- `1<>1`은 항상 False → 결과 0건.

### Alias 중요성
```sql
-- ❌ 모호한 표현 → 자기 자신과 비교 → 항상 True → 27건 반환
WHERE department_id = department_id

-- ✅ Alias로 명확히 구분
WHERE d.department_id = e.department_id
```

---

## 5. OUTER JOIN

### Oracle (+) 문법
```sql
WHERE D.DEPARTMENT_ID(+) = E.DEPARTMENT_ID
```
- `(+)` 붙은 쪽 = **후행 테이블** (나중에 실행)
- `(+)` 없는 쪽 = **선행(드라이빙) 테이블** (먼저 실행)
- **(+) 기호가 붙으면 안 붙은 쪽보다 무조건 나중에 실행** → 암기!

### 스칼라 서브쿼리 = OUTER JOIN 변환
- 스칼라 서브쿼리를 OUTER JOIN으로 변환 가능 (결과 동일).
- INNER JOIN으로 바꾸면 NULL 행 누락 → 결과 달라짐.
- 실행계획으로 조인 방식 확인:
  - `HASH JOIN` → INNER JOIN
  - `HASH JOIN (OUTER)` → LEFT OUTER JOIN
  - **OUTER 있으면 OUTER JOIN, 없으면 INNER JOIN**

### 힌트 (실행계획 강제 변경)
```sql
/*+ use_hash(d e) full(e) full(d) no_index(d dept_id_pk) */
```
| 힌트 | 의미 |
|---|---|
| `use_hash(d e)` | HASH JOIN 사용 |
| `full(e)` | employees 풀스캔 |
| `full(d)` | departments 풀스캔 |
| `no_index(d dept_id_pk)` | PK 인덱스 미사용 |

---

## 6. GROUP 함수

### ROLLUP / CUBE
```sql
GROUP BY ROLLUP(department_name)  -- 소계 + 총계 (계층적)
GROUP BY CUBE(department_name)    -- 모든 조합 소계 + 총계 (다차원)
```

| | ROLLUP | CUBE |
|---|---|---|
| 결과 건수 | 적음 | 많음 |
| 용도 | 일반 소계+총계 | 다차원 분석 |

- ⚠️ **HAVING절이 있으면 CUBE/ROLLUP 작동 안 함** → HAVING 제거 후 인라인뷰로 필터링.

### GROUPING 함수
- ROLLUP/CUBE가 만든 집계 행 식별:
  - `1` → ROLLUP/CUBE가 만든 소계/총계 행
  - `0` → 일반 데이터 행

### GROUPING + DECODE + NVL 패턴
```sql
DECODE(GROUPING(d.department_name),
    1, '총계',
    0, NVL(D.DEPARTMENT_NAME, '부서없음')
) AS 부서명
```

**문제 해결 흐름:**
1. 총계 필요 → CUBE/ROLLUP 사용
2. HAVING 제거 → 부서없음(진짜 NULL)과 총계(가짜 NULL) 섞임
3. GROUPING으로 식별 (1=총계, 0=일반)
4. DECODE로 가독성 확보
5. NVL로 부서없음 처리

---

## 7. 윈도우 함수 (Window Function)

### 핵심 개념
> **집계값과 원본 데이터를 같은 행에 함께 표현할 수 있다.**
- GROUP BY는 집계 시 원본 행 사라짐.
- 윈도우 함수는 **원본 행 유지 + 집계값 추가**.

### OVER() 구조
```sql
집계함수() OVER (
    PARTITION BY 컬럼  -- 그룹 쪼개기 (GROUP BY 역할)
    ORDER BY 컬럼      -- 순위/정렬 기준
)
```
- `OVER()` → 전체 행 대상 집계
- `OVER(PARTITION BY 부서)` → 부서별 집계

### GROUP BY vs PARTITION BY
| | GROUP BY | PARTITION BY |
|---|---|---|
| 결과 행 수 | 그룹 수만큼 축약 | 원본 행 수 유지 |
| DISTINCT 필요 | ❌ | ✅ (원본 데이터 없을 때) |

### DISTINCT 사용 기준
- 집계값만 있을 때 → **DISTINCT 필요** (같은 부서 직원 수만큼 중복)
- 개인 데이터(이름, 급여 등) 포함 시 → **DISTINCT 불필요** (각 행이 이미 고유)

### 전체 + 부서별 집계 동시 표현
```sql
SELECT DISTINCT
    COUNT(salary) OVER()                              AS 회사인원,
    SUM(salary)   OVER()                              AS 회사합계,
    D.department_name                                  AS 부서,
    COUNT(salary) OVER(PARTITION BY D.department_name) AS 부서인원,
    SUM(salary)   OVER(PARTITION BY D.department_name) AS 부서합계,
    first_name                                         AS 사원이름,
    salary                                             AS 사원급여
FROM employees E, departments D
WHERE E.department_id = D.department_id(+);
```

### GROUP BY vs 윈도우 함수 선택 기준
| 상황 | 선택 |
|---|---|
| 단순 집계만 필요 | **GROUP BY** |
| 원본 데이터 + 집계 동시 필요 | **윈도우 함수** |
| 전체 + 부서 집계 동시 필요 | **윈도우 함수** |

---

## 8. RANK / ROW_NUMBER

### RANK()
```sql
RANK() OVER(ORDER BY salary DESC) AS 순위
```
- OVER() 안에 ORDER BY 기준 필수.
- 기본 오름차순 → 낮은 값이 1등 → **DESC로 뒤집어야 높은 값이 1등**.
- 동률 발생 시 같은 순위 부여, 다음 순위 건너뜀 (1,1,3...).
- **동률 처리 방법 없음**.

### ROW_NUMBER() — 치트키
```sql
ROW_NUMBER() OVER(ORDER BY salary DESC, hire_date) AS 순번
```
- 동률 상관없이 무조건 고유 순번.
- 동률 시 추가 기준 컬럼(입사일 등)으로 해결.
- **RANK보다 성능상 빠름**.
- TOP N 추출, 페이징 처리에 자주 활용.

### DESC 위치에 따른 차이
| 위치 | 역할 |
|---|---|
| `RANK() OVER(ORDER BY salary DESC)` | **순위값 자체** 결정 |
| 메인쿼리 `ORDER BY 사원급여 DESC` | **화면 출력 순서**만 결정 |

### 동률 처리 기준
- 동률 허용 → `RANK()`
- 동률 불허 → `ROW_NUMBER()` + 추가 기준 컬럼

### RANK로 최대/최소값 추출
```sql
-- 부서별 최고 급여 직원
SELECT * FROM (
    SELECT D.department_name AS 부서, salary,
           RANK() OVER(PARTITION BY D.department_name ORDER BY salary DESC) AS 부서순위
    FROM employees E, departments D
    WHERE E.department_id = D.department_id(+)
)
WHERE 부서순위 = 1;
```
- `ORDER BY DESC` → 최댓값 1등
- `ORDER BY ASC` → 최솟값 1등

### RANK vs MAX/MIN
| | MAX/MIN | RANK |
|---|---|---|
| 직원 정보 포함 | ❌ 추가 조인 필요 | ✅ 한 번에 가능 |
| 성능 | 상대적으로 느릴 수 있음 | 한 번 스캔으로 처리 |

---

## 9. CONNECT BY (계층형 쿼리)

### 언제 쓰나?
- **Self Reference 구조** 데이터 (같은 테이블에서 자기 자신 참조).
- 실무에서 **조직도** 만들 때 가장 많이 사용.

### 기본 구조 (메모장에 저장해두고 쓸 것)
```sql
SELECT LEVEL,
       LPAD(' ', (LEVEL-1)*4) || 컬럼명     AS 계층표시,
       SYS_CONNECT_BY_PATH(컬럼명, '/')      AS 경로
FROM 테이블
START WITH FK컬럼 IS NULL                   -- 최상위 조건
CONNECT BY PRIOR PK컬럼 = FK컬럼            -- 부모 → 자식
ORDER SIBLINGS BY 정렬기준컬럼;
```

### PRIOR 방향 규칙
```
CONNECT BY PRIOR 자식(FK) = 부모(PK)  -- 상위 → 하위 (하향식)
CONNECT BY 자식(FK) = PRIOR 부모(PK)  -- 하위 → 상위 (상향식)
```
- **PRIOR가 붙은 쪽이 부모(상위)**
- START WITH: 시작 노드 조건 → **데이터를 따로 파악해야 함**

### LEVEL
- 자동 생성 가상 컬럼. 계층 깊이에 따라 증가.
- depth가 깊어질수록 LEVEL 값 증가.

### LPAD
- `LPAD(employee_id, LEVEL*5, '-')`: LEVEL에 비례해서 왼쪽을 `-`로 채움.
- `*5`는 임의 간격값 (변경 가능).

### ORDER SIBLINGS BY
- 일반 ORDER BY → 계층 구조 무너짐 ⚠️
- **ORDER SIBLINGS BY** → 같은 부모의 형제끼리만 정렬, 계층 구조 유지.

### SYS_CONNECT_BY_PATH
- 루트부터 현재 노드까지 경로를 문자열로 표현.
- 디렉토리 구조 구현에 주로 사용.
```sql
SYS_CONNECT_BY_PATH(employee_id, '/') -- /100/101/103
```

---

## 핵심 원칙 모음

1. **불필요한 연산(ORDER BY, GROUP BY, 인덱스)은 제거** → 성능 최적화
2. **서브쿼리는 소량 집합** → MQ 건수에 비례해서 SQ 실행되므로
3. **(+) 붙은 쪽이 나중에 실행** → 드라이빙 순서 제어
4. **HAVING 있으면 CUBE/ROLLUP 작동 안 함** → 인라인뷰로 대체
5. **윈도우 함수 = 집계값 + 원본 데이터 동시 표현**
6. **동률 허용 → RANK, 불허 → ROW_NUMBER**
7. **CONNECT BY 정렬은 ORDER SIBLINGS BY 사용**
8. **SQL 짤 때 코드부터 짜지 말고, 무엇이 필요한지 먼저 생각**
