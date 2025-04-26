CREATE TABLE Job (
    JobID INT PRIMARY KEY,
    JobRole VARCHAR(50) NOT NULL,
    JobLevel INT NOT NULL,
    Department VARCHAR(50) NOT NULL,
    Education INT NOT NULL,
    EducationField VARCHAR(50) NOT NULL,
    BusinessTravel VARCHAR(30) NOT NULL
);

CREATE TABLE EmployeeJob (
    EmployeeID INT REFERENCES Employees(EmployeeID) ON DELETE CASCADE,
    JobID INT REFERENCES Job(JobID) ON DELETE CASCADE,
    PRIMARY KEY (EmployeeID)
);

CREATE TABLE JobPay (
    JobID INT PRIMARY KEY REFERENCES Job(JobID),
    MonthlyRate INT NOT NULL,
    StockOptionLevel INT NOT NULL
);

CREATE TABLE Salary (
    SalaryID INT PRIMARY KEY,
    EmployeeID INT REFERENCES Employees(EmployeeID) ON DELETE SET NULL,
    JobID INT REFERENCES Job(JobID),
    MonthlyIncome INT NOT NULL,
    HourlyRate INT NOT NULL,
    PercentSalaryHike INT NOT NULL
);

INSERT INTO Job (JobID, JobRole, JobLevel, Department, Education, EducationField, BusinessTravel)
SELECT DISTINCT JobID, JobRole, JobLevel, Department, Education, EducationField, BusinessTravel
FROM JobDetails;

INSERT INTO EmployeeJob (EmployeeID, JobID)
SELECT EmployeeID, JobID
FROM JobDetails;

INSERT INTO JobPay (JobID, MonthlyRate, StockOptionLevel)
SELECT DISTINCT JobID, MonthlyRate, StockOptionLevel
FROM SalaryDetails;

INSERT INTO Salary (SalaryID, EmployeeID, JobID, MonthlyIncome, HourlyRate, PercentSalaryHike)
SELECT SalaryID, EmployeeID, JobID, MonthlyIncome, HourlyRate, PercentSalaryHike
FROM SalaryDetails;
