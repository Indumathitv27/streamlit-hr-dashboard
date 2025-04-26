INSERT INTO Employees (EmployeeID, Age, Gender, MaritalStatus, DistanceFromHome, Attrition)
SELECT DISTINCT
    EmployeeNumber,
    Age,
    Gender,
    MaritalStatus,
    DistanceFromHome,
    Attrition
FROM hr_emp_staging;

INSERT INTO JobDetails (JobID, EmployeeID, JobRole, JobLevel, Department, Education, EducationField, BusinessTravel)
SELECT DISTINCT
    EmployeeNumber,  -- Assuming JobID = EmployeeID if no separate JobID in raw data
    EmployeeNumber,
    JobRole,
    JobLevel,
    Department,
    Education,
    EducationField,
    BusinessTravel
FROM hr_emp_staging;

INSERT INTO SalaryDetails (SalaryID, EmployeeID, JobID, PercentSalaryHike, MonthlyIncome, MonthlyRate, HourlyRate, StockOptionLevel)
SELECT DISTINCT
    EmployeeNumber,  -- SalaryID = EmployeeID as identifier
    EmployeeNumber,
    EmployeeNumber,  -- JobID assumed to match EmployeeNumber
    PercentSalaryHike,
    MonthlyIncome,
    MonthlyRate,
    HourlyRate,
    StockOptionLevel
FROM hr_emp_staging;

INSERT INTO Performance (PerformanceID, EmployeeID, PerformanceRating, JobSatisfaction, EnvironmentSatisfaction, RelationshipSatisfaction, WorkLifeBalance, JobInvolvement)
SELECT DISTINCT
    EmployeeNumber,
    EmployeeNumber,
    PerformanceRating,
    JobSatisfaction,
    EnvironmentSatisfaction,
    RelationshipSatisfaction,
    WorkLifeBalance,
    JobInvolvement
FROM hr_emp_staging;

INSERT INTO Tenure (TenureID, EmployeeID, TotalWorkingYears, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager)
SELECT DISTINCT
    EmployeeNumber,
    EmployeeNumber,
    TotalWorkingYears,
    YearsAtCompany,
    YearsInCurrentRole,
    YearsSinceLastPromotion,
    YearsWithCurrManager
FROM hr_emp_staging;

INSERT INTO Training (TrainingID, EmployeeID, TrainingTimesLastYear, StandardHours)
SELECT DISTINCT
    EmployeeNumber,
    EmployeeNumber,
    TrainingTimesLastYear,
    StandardHours
FROM hr_emp_staging;

INSERT INTO EmployeeEngagement (EngagementID, EmployeeID, JobSatisfaction, WorkLifeBalance, JobInvolvement, PerformanceRating, RelationshipSatisfaction, EnvironmentSatisfaction)
SELECT DISTINCT
    EmployeeNumber,
    EmployeeNumber,
    JobSatisfaction,
    WorkLifeBalance,
    JobInvolvement,
    PerformanceRating,
    RelationshipSatisfaction,
    EnvironmentSatisfaction
FROM hr_emp_staging;
