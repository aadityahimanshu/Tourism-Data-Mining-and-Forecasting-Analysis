import numpy as np
import pandas as pd

def generate_paths(year,n):
    main = 'data-students/TourismData-'
    a1 = '/DISTRIBUTION OF NATIONALITY-WISE FTAs IN INDIA ACCORDING TO AGE GROUP.xlsx'
    a2 = '/DISTRIBUTION OF NATIONALITY-WISE FTAs IN INDIA ACCORDING TO PURPOSE, ' # need to add year + .xlsx
    a3 = '/FTAs IN INDIA ACCORDING TO QUARTERS.xlsx'
    a4 = '/MODE WISE DISTRIBUTION OF INDIAN NATIONALS’ DEPARTURES FROM INDIA DURING ' # need to add year + .xlsx
    a5 = '/MONTH WISE NUMBER & PERCENTAGE SHARE OF INDIAN NATIONALS’ DEPARTURES FROM INDIA '
    a6 = '/MONTH-WISE FEE FROM TOURISM (CRORE) IN INDIA.xlsx'
    a7 = '/MONTH-WISE NUMBER & PERCENTAGE SHARE OF FTAs IN INDIA.xlsx'
    a8 = '/NATIONALITY-WISE GENDER-WISE DISTRIBUTION OF FTAs IN INDIA.xlsx'
    a9 = '/NATIONALITY-WISE QUARTER-WISE DISTRIBUTION OF FTAs IN INDIA DURING ' # need to add year + .xlsx
    a10 = '/PORT-WISE DEPARTURES OF INDIAN NATIONALS’ FROM INDIA.xlsx'
    a11 = '/QUARTER –WISE INDIAN NATIONALS’ DEPARTURES.xlsx'
    a12 = '/STATE UT-WISE DOMESTIC AND FOREIGN TOURIST VISITS.xlsx'
    
    p1 = np.empty(n,dtype=object)
    p2 = np.empty(n,dtype=object)
    p3 = np.empty(n,dtype=object)
    p4 = np.empty(n,dtype=object)
    p5 = np.empty(n,dtype=object)
    p6 = np.empty(n,dtype=object)
    p7 = np.empty(n,dtype=object)
    p8 = np.empty(n,dtype=object)
    p9 = np.empty(n,dtype=object)
    p10 = np.empty(n,dtype=object)
    p11 = np.empty(n,dtype=object)
    p12 = np.empty(n,dtype=object)
    
    num = year

    for i in range(n):
        if(num==2015):
          num = num + 1 
        val = str(num)
        p1[i] = main + val + a1
        p2[i] = main + val + a2 + val + '.xlsx'
        p3[i] = main + val + a3
        p4[i] = main + val + a4 + val + '.xlsx'
        p5[i] = main + val + a5 + val + '.xlsx'
        p6[i] = main + val + a6
        p7[i] = main + val + a7
        p8[i] = main + val + a8
        p9[i] = main + val + a9 + val + ' (in percentage).xlsx'
        p10[i] = main + val + a10
        p11[i] = main + val + a11
        p12[i] = main + val + a12

        num = num + 1

    paths = np.array([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12])
    
    paths[4,4] = 'data-students/TourismData-2018/MONTH WISE NUMBER & PERCENTAGE SHARE OF INDIAN NATIONALSG DEPARTURES FROM INDIA 2018.xlsx'
    paths[4,5] = 'data-students/TourismData-2019/MONTH WISE NUMBER & PERCENTAGE SHARE OF INDIAN NATIONALS DEPARTURES FROM INDIA 2019.xlsx'
    paths[4,6] = 'data-students/TourismData-2020/MONTH WISE NUMBER & PERCENTAGE SHARE OF INDIAN NATIONALS DEPARTURES FROM INDIA 2020.xlsx'
    paths[4,7] = 'data-students/TourismData-2021/MONTH WISE NUMBER & PERCENTAGE SHARE OF INDIAN NATIONAL DEPARTURES FROM INDIA.xlsx'
    paths[4,8] = 'data-students/TourismData-2022/MONTH WISE NUMBER & PERCENTAGE SHARE OF INDIAN NATIONALS’ DEPARTURES FROM INDIA 2022.xlsx'
    paths[6,0] = 'data-students/TourismData-2013/MONTH-WISE NUMBER & PERCENTAGE SHARE OF FTAs IN INDIA1.xlsx'
    paths[6,8] = 'data-students/TourismData-2013/MONTH-WISE NUMBER & PERCENTAGE SHARE OF FTAs IN INDIA1.xlsx'
    paths[4,0] = 'data-students/TourismData-2013/MONTH WISE NUMBER & PERCENTAGE SHARE OF INDIAN NATIONALS’ DEPARTURES FROM INDIA.xlsx'

    return paths
# print(generate_paths(2013,9))

paths = generate_paths(2013,9)
q1_paths = paths[6,:]

absolute = np.zeros((12,8), dtype=float)
percentage = np.zeros((12,8), dtype=float)
totalyearly = np.zeros(9, dtype=float)
yearlychange = np.zeros(8, dtype=float)
############################################################################################
def convert_to_float(element):
    if isinstance(element, str) and ',' in element:
        return float(element.replace(',', ''))
    else:
        return float(element)
############################################################################################
for i in range(8):
  tab1 = pd.read_excel(q1_paths[i])
  tab2 = pd.read_excel(q1_paths[i+1])
  val1 = tab1.values
  val2 = tab2.values
  total = 0

  for j in range(12):
    v1 = convert_to_float(val1[j+1,1])
    v2 = convert_to_float(val2[j+1,1])
    absolute[j,i] = v2-v1
    percentage[j,i] = ((v2-v1)/v1)*100
############################################################################################
for i in range(9):
  tab = pd.read_excel(q1_paths[i])
  val1=tab.values
  total = 0
  for j in range(12):
    v1 = convert_to_float(val1[j+1,1])
    total = total + v1
  totalyearly[i] = total

for i in range(8):
  yearlychange[i] = totalyearly[i+1] - totalyearly[i]
############################################################################################
monthly = np.zeros((11,10), dtype=float)
for i in range(9):
  tab1 = pd.read_excel(q1_paths[i])
  val1 = tab1.values
  for j in range(11):
    v1 = convert_to_float(val1[j+1,1])
    v2 = convert_to_float(val1[j+2,1])
    monthly[j,i] = v2-v1
for i in range(11):
  for j in range(10):
    monthly[i,9] = monthly[i,9] + monthly[i,j]
############################################################################################
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthdiff = ['Jan-Feb', 'Feb-Mar', 'Mar-Apr', 'Apr-May', 'May-Jun', 'Jun-Jul', 'Jul-Aug', 'Aug-Sep', 'Sep-Oct', 'Oct-Nov', 'Nov-Dec']
year1 = ['2013', '2014', '2016', '2017', '2018', '2019', '2020', '2021', '2022', 'Total']
years = ["2013-14", "2014-16", "2016-17", "2017-18", "2018-19", "2019-20", "2020-21", "2021-22"]
yeartxt = ['Year']
year = ['2013', '2014', '2016', '2017', '2018', '2019', '2020', '2021', '2022']

absolutedf = pd.DataFrame(absolute, index=months, columns=years)
percentagedf = pd.DataFrame(percentage, index=months, columns=years)
totalyearlydf = pd.DataFrame(totalyearly, index=year, columns=yeartxt)
yearlychangedf = pd.DataFrame(yearlychange, index=years, columns=yeartxt)
monthlydf = pd.DataFrame(monthly, index=monthdiff, columns=year1)

print("Monthwise Yearly Change, Absolute")
print(absolutedf)
print("Monthwise Yearly Change, Percentage")
print(percentagedf)
print('Total Incoming Tourists, Yearly')
print(totalyearlydf)
print('Yearly Change in Incoming Tourist')
print(yearlychangedf)
print('Monthly Change in Incoming Tourists, Yearly')
print(monthlydf)

a = np.argmax(yearlychange)
b = np.argmin(yearlychange)

print('Maximum Positive Change Yearwise is observed in year', years[a])
print('Maximum Negative Change Yearwise is observed in year', years[b])

max = np.zeros(9)
min = np.zeros(9)
for i in range(9):
  arr = monthly[:,i]
  arr1 = arr.astype(int)
  # print(arr1)
  max[i] = np.argmax(arr1)
  min[i] = np.argmin(arr1)
maxind = max.astype(int)
minind = min.astype(int)
for i in range(9):
  print("Max Change is seen in months of", monthdiff[maxind[i]], 'for the year', year[i])
for i in range(9):
  print("Min Change is seen in months of", monthdiff[minind[i]], 'for the year', year[i])