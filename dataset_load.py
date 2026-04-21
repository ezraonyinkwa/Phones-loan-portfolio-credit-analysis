#------------------Load Sales Details dataset------------------------
sales_details = pd.read_csv(r'C:\Users\MGAUSER\Downloads\Mophones Portfolio Analysis\Sales Details.csv')
print("sales details data imported successfully with : {} rows and {} columns".format(sales_details.shape[0], sales_details.shape[1]))

#-----------------Load Customer Dataset DOB------------------------
customer_dob = pd.read_csv(r'C:\Users\MGAUSER\Downloads\Mophones Portfolio Analysis\Customer Data - DOB.csv')
print("customer DOB data imported successfully with : {} rows and {} columns".format(customer_dob.shape[0], customer_dob.shape[1]))

#----------------------Load Customer Dataset Income Level-----------------
customer_income = pd.read_csv(r'C:\Users\MGAUSER\Downloads\Mophones Portfolio Analysis\Customer Data - Income Level.csv')
print("customer income data imported successfully with : {} rows and {} columns".format(customer_income.shape[0], customer_income.shape[1]))

#----------------------Load Customer Dataset Gender------------------------
customer_gender = pd.read_csv(r'C:\Users\MGAUSER\Downloads\Mophones Portfolio Analysis\Customer Data-Gender.csv')
print("customer gender data imported successfully with : {} rows and {} columns".format(customer_gender.shape[0], customer_gender.shape[1]))

#----------------------------NPS Dataset--------------------------------
nps = pd.read_csv(r'C:\Users\MGAUSER\Downloads\Mophones Portfolio Analysis\Nps Data.csv', encoding='latin1')
print("NPS data imported successfully with : {} rows and {} columns".format(nps.shape[0], nps.shape[1])) 

#---------------------Load Credit Dataset----------------------------------
files = [
    'Credit Data - 01-01-2025.csv',
    'Credit Data - 30-03-2025.csv',
    'Credit Data - 30-06-2025.csv',
    'Credit Data - 30-09-2025.csv',
    'Credit Data - 30-012-2025.csv'
]

path = r'C:\Users\MGAUSER\Downloads\Mophones Portfolio Analysis\\'

files = [f for f in os.listdir(path) if f.startswith('Credit Data')]

dfs = []

for file in files:
    df = pd.read_csv(path + file)
    df['snapshot_date'] = file
    dfs.append(df)

credit = pd.concat(dfs, ignore_index=True)
print("credit data imported successfully with : {} rows and {} columns".format(credit.shape[0], credit.shape[1]))

credit.shape
credit['snapshot_date'].value_counts()

