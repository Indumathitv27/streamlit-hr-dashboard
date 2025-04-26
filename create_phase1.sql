-- Create database
CREATE DATABASE HR_Employee_Attrition;
\c HR_Employee_Attrition;

-- Drop existing tables (optional for re-runs)
DROP TABLE IF EXISTS hr_emp_staging CASCADE;
DROP TABLE IF EXISTS EmployeeEngagement CASCADE;
DROP TABLE IF EXISTS Training CASCADE;
DROP TABLE IF EXISTS Tenure CASCADE;
DROP TABLE IF EXISTS Performance CASCADE;
DROP TABLE IF EXISTS SalaryDetails CASCADE;
DROP TABLE IF EXISTS JobDetails CASCADE;
DROP TABLE IF EXISTS Employees CASCADE;

CREATE TABLE IF NOT EXISTS public.hr_emp_staging
(
    age integer NOT NULL,
    attrition character varying(5) COLLATE pg_catalog."default" NOT NULL,
    businesstravel character varying(30) COLLATE pg_catalog."default" NOT NULL,
    dailyrate integer NOT NULL,
    department character varying(50) COLLATE pg_catalog."default" NOT NULL,
    distancefromhome integer NOT NULL,
    education integer NOT NULL,
    educationfield character varying(50) COLLATE pg_catalog."default" NOT NULL,
    employeecount integer NOT NULL,
    employeenumber integer NOT NULL,
    environmentsatisfaction integer NOT NULL,
    gender character varying(10) COLLATE pg_catalog."default" NOT NULL,
    hourlyrate integer NOT NULL,
    jobinvolvement integer NOT NULL,
    joblevel integer NOT NULL,
    jobrole character varying(50) COLLATE pg_catalog."default" NOT NULL,
    jobsatisfaction integer NOT NULL,
    maritalstatus character varying(20) COLLATE pg_catalog."default" NOT NULL,
    monthlyincome integer NOT NULL,
    monthlyrate integer NOT NULL,
    numcompaniesworked integer NOT NULL,
    over18 character varying(5) COLLATE pg_catalog."default" NOT NULL,
    overtime character varying(10) COLLATE pg_catalog."default" NOT NULL,
    percentsalaryhike integer NOT NULL,
    performancerating integer NOT NULL,
    relationshipsatisfaction integer NOT NULL,
    standardhours integer NOT NULL DEFAULT 40,
    stockoptionlevel integer NOT NULL DEFAULT 0,
    totalworkingyears integer NOT NULL,
    trainingtimeslastyear integer NOT NULL,
    worklifebalance integer NOT NULL,
    yearsatcompany integer NOT NULL,
    yearsincurrentrole integer NOT NULL,
    yearssincelastpromotion integer NOT NULL,
    yearswithcurrmanager integer NOT NULL
)


-- Create Employees table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    Age INT NOT NULL,
    Gender VARCHAR(10) NOT NULL,
    MaritalStatus VARCHAR(20),
    DistanceFromHome INT,
    Attrition VARCHAR(5)
);

-- Create JobDetails table
CREATE TABLE JobDetails (
    JobID INT PRIMARY KEY,
    EmployeeID INT REFERENCES Employees(EmployeeID) ON DELETE CASCADE,
    JobRole VARCHAR(50),
    JobLevel INT,
    Department VARCHAR(50),
    Education INT,
    EducationField VARCHAR(50),
    BusinessTravel VARCHAR(50)
);

-- Create SalaryDetails table
CREATE TABLE SalaryDetails (
    SalaryID INT PRIMARY KEY,
    EmployeeID INT REFERENCES Employees(EmployeeID) ON DELETE SET NULL,
    JobID INT REFERENCES JobDetails(JobID) ON DELETE CASCADE,
    PercentSalaryHike INT,
    MonthlyIncome INT NOT NULL,
    MonthlyRate INT,
    HourlyRate INT,
    StockOptionLevel INT
);

-- Create Performance table
CREATE TABLE Performance (
    PerformanceID INT PRIMARY KEY,
    EmployeeID INT REFERENCES Employees(EmployeeID) ON DELETE CASCADE,
    PerformanceRating INT,
    JobSatisfaction INT,
    EnvironmentSatisfaction INT,
    RelationshipSatisfaction INT,
    WorkLifeBalance INT,
    JobInvolvement INT
);

-- Create Tenure table
CREATE TABLE Tenure (
    TenureID INT PRIMARY KEY,
    EmployeeID INT REFERENCES Employees(EmployeeID) ON DELETE CASCADE,
    TotalWorkingYears INT,
    YearsAtCompany INT,
    YearsInCurrentRole INT,
    YearsSinceLastPromotion INT,
    YearsWithCurrManager INT
);

-- Create Training table
CREATE TABLE Training (
    TrainingID INT PRIMARY KEY,
    EmployeeID INT REFERENCES Employees(EmployeeID) ON DELETE CASCADE,
    TrainingTimesLastYear INT NOT NULL,
    StandardHours INT NOT NULL
);

-- Create EmployeeEngagement table
CREATE TABLE EmployeeEngagement (
    EngagementID INT PRIMARY KEY,
    EmployeeID INT REFERENCES Employees(EmployeeID) ON DELETE CASCADE,
    JobSatisfaction INT,
    WorkLifeBalance INT,
    JobInvolvement INT,
    PerformanceRating INT,
    RelationshipSatisfaction INT,
    EnvironmentSatisfaction INT
);
