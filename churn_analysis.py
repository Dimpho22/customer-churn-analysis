import pandas as pd
df = pd.read_csv("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")
print(df.head())
#import pandas as pd — Loads the pandas library into Python. pd is the nickname/alias we use for pandas.
#df = pd.read_csv("...") — Uses pandas to read a CSV file and stores the dataset in a DataFrame called df.
#print(df.head()) — Displays the first 5 rows of the DataFrame so I can get a quick look at the data.


df = pd.read_csv("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv", sep=";")
print(df.shape)
#sep=";" tells pandas that the semicolon is the character separating the different columns in my CSV file
#df.shape returns the number of rows and columns in a DataFrame in the format (rows, columns

# View the column names
print(df.columns)

# Check data types and missing values
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Check for duplicate rows
print(df.duplicated().sum())

# 7. Summary statistics for numerical columns
print(df.describe())

# 8. Check the distribution of churn
print(df["Churn"].value_counts())


################Data cleaning ###################################################################
print(df["TotalCharges"].head(10))
print(df["TotalCharges"].tail(10))
# this is shwing the fist and last 10 values of the total charges coloumn 

print(pd.to_numeric(df["TotalCharges"], errors="coerce").isnull().sum())
# this converts text to numbers while checking fo invalid numbers and counting how many problematic numbers are there

print(df.loc[pd.to_numeric(df["TotalCharges"], errors="coerce").isnull(), ["customerID", "tenure", "TotalCharges"]])
#inspecting the rows with invalid values, it come out blank on total charges column 

print(df.loc[pd.to_numeric(df["TotalCharges"], errors="coerce").isnull(), "TotalCharges"].tolist())
#this shows the problematic values as a list 

df["TotalCharges"]=pd.to_numeric(df["TotalCharges"], errors="coerce")
#converts to number  and missing values to NaN
print(df["TotalCharges"].isnull().sum())
# how many missing values 

print(df.loc[pd.to_numeric(df["TotalCharges"], errors="coerce").isnull(), ["customerID", "tenure", "MonthlyCharges", "TotalCharges"]])

df["TotalCharges"]= df["TotalCharges"].fillna(0)
#after inverstigation decide to treat the Nan as zero because they are real customers who havent accumilated any total charges 
print(df["TotalCharges"].isnull().sum())


################spelling variation#################################
print(df["gender"].value_counts())

print(df["Partner"].value_counts())

print(df["Dependents"].value_counts())

print(df["PhoneService"].value_counts())

print(df["MultipleLines"].value_counts())

print(df["InternetService"].value_counts())

print(df["OnlineSecurity"].value_counts())

print(df["OnlineBackup"].value_counts())

print(df["DeviceProtection"].value_counts())

print(df["TechSupport"].value_counts())

print(df["StreamingTV"].value_counts())

print(df["StreamingMovies"].value_counts())

print(df["Contract"].value_counts())

print(df["PaperlessBilling"].value_counts())

print(df["PaymentMethod"].value_counts())

print(df["Churn"].value_counts())
#checking any unexpected spelling variation

############numeric columns############################
print(df["tenure"].min())
print(df["tenure"].max())

print(df["MonthlyCharges"].min())
print(df["MonthlyCharges"].max())

print(df["TotalCharges"].min())
print(df["TotalCharges"].max())

print(df["SeniorCitizen"].value_counts())

###########last data check#####
print(df.info())
print(df.isnull().sum().sum())
print(df.duplicated().sum())

########################################Exploratory Data Analysis##################################

print(df["Churn"].value_counts(normalize=True)*100)
#what percentange of customers are leaving

print(pd.crosstab(df["Contract"], df["Churn"]))
#How contract type relate to churn

print(pd.crosstab(df["Contract"], df["Churn"], normalize="index")* 100)
#calculating %churn rate by contract

df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[-1,12,24,48,72],
    labels=["0-12 months", "13-24 months", "25-48 months", "49-72 months"]
)
print(df["TenureGroup"].value_counts().sort_index())
#creating groups of tenure 

print(pd.crosstab(df["TenureGroup"], df["Churn"], normalize="index")* 100)
#calculating churn rate for each group

df["MonthlyChargeGroup"] = pd.cut(
    df["MonthlyCharges"],
    bins=[0,30,60,90,120],
    labels=["Low", "Medium", "High", "Very High"]
)
#grouping according to monthly charges

print(pd.crosstab(df["MonthlyChargeGroup"], df["Churn"], normalize="index")* 100)
# calcute churn rate to each monthyly charge group

print(pd.crosstab(df["PaymentMethod"], df["Churn"], normalize="index")* 100)
#calculating churn rate for paymentmethod 

print(pd.crosstab(df["TechSupport"], df["Churn"], normalize="index")* 100)
#calculating churn rate to techsupport

print(pd.crosstab(df["InternetService"], df["Churn"], normalize="index")* 100)
#calculating churn rate to internetservice

print(pd.crosstab(df["OnlineSecurity"], df["Churn"], normalize="index")* 100)
#calculating churn rate to OnlineSecurity

print(pd.crosstab(df["SeniorCitizen"], df["Churn"], normalize="index")* 100)
#calculating churn rate to SeniorCitizen

print(pd.crosstab(df["Partner"], df["Churn"], normalize="index")* 100)
#calculating churn rate to partner/spouse

print(pd.crosstab(df["Dependents"], df["Churn"], normalize="index")* 100)
#calculating churn rate to dependents

print(df.groupby("Churn")["TotalCharges"].mean())
#calculating churn rate to totalcharges