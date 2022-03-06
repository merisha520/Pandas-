import pandas as pd
import numpy as np

#find the total number of rows and columns
df = pd.read_csv('Salaries.csv')
rows = len(df)
columns = (len(df.columns))
print('1. Rows = '+ str(rows)+ ',  Columns = '+ str(columns))

#find the maximum total pay
print('2. Maximum total pay =  '+ str(df['TotalPay'].max()))

#find the name of the employee who gets the max totalpay
max_salary_empname = (df[df['TotalPay']== df['TotalPay'].max()]['EmployeeName'].values[0])
print('3. {} gets the max total pay'.format(max_salary_empname))

#find the number of unique employee names
unique_names = len(pd.unique(df['EmployeeName']))
print('4. Number of unique employee names = ' + str(unique_names))

#find the numbe rof unique job titles
unique_jobs = len(pd.unique(df['JobTitle']))
print('5. Number of unique job titles = ' + str(unique_jobs))

#find the most common job title
most_common_job = df['JobTitle'].value_counts()
most_common_job_ = (most_common_job.index[0])
print('6. Most common job title is ' + most_common_job_)

#find the job tite of employee Joseph Driscoll
Joseph_title = df[df['EmployeeName']== 'Joseph Driscoll']['JobTitle'].values[0]
print('7. Job Title of Joseph Driscoll is '+ Joseph_title)

#find the employee who receives maximum totalpay benefits
max_totalpaybenefits_empname = (df[df['TotalPayBenefits']== df['TotalPayBenefits'].max()]['EmployeeName'].values[0])
print('8. {} receives maximum salary '.format(max_totalpaybenefits_empname))

#find employee who receives minimum totalpay benefits
min_totalpaybenefits_empname = (df[df['TotalPayBenefits']== df['TotalPayBenefits'].min()]['EmployeeName'].values[0])
print('9. {} receives minimum salary '.format(min_totalpaybenefits_empname))

#find mean basepay for the year 2011
year_2011 = round(df[df['Year']== 2011]['BasePay'].mean(), 2)
print('10. Mean base pay for 2011 is '+ str(year_2011))