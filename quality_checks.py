#Quality checks for column names
credit.columns
#Quality check for customer income dataset columns
customer_income.columns
#Quality check for customer gender dataset columns        
customer_gender.columns
#Quality check for customer_dob dataset columns
customer_dob.columns
#Check unique values in the gender
customer_gender['gender'].unique()
#Quality check after standardization
customer_gender['gender'].unique()
customer_gender['citizenship'].unique()
