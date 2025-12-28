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

def convert_to_float(element):
    if isinstance(element, str) and ',' in element:
        return float(element.replace(',', ''))
    else:
        return float(element)

totalval = np.zeros((12,9))
for i in range(9):
  tab = pd.read_excel(paths[4,i])
  val = tab.values
  for j in range(12):
    totalval[j,i] = convert_to_float(val[j,1])

# print(totalval)
##############################################################################
totalmonthdiff = np.zeros((11,9))
for j in range(9):
  for i in range(11):
    totalmonthdiff[i,j] = totalval[i+1,j]-totalval[i,j]
# print(totalmonthdiff)
##############################################################################
yeardata = np.zeros(9)
for i in range(9):
  yeardata[i] = np.sum(totalval[:,i])
# print(yeardata)

finyear = np.zeros(8)
for i in range(8):
  finyear[i] = yeardata[i+1] - yeardata[i]
# print(finyear)


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthdiff = ['Jan-Feb', 'Feb-Mar', 'Mar-Apr', 'Apr-May', 'May-Jun', 'Jun-Jul', 'Jul-Aug', 'Aug-Sep', 'Sep-Oct', 'Oct-Nov', 'Nov-Dec']
year1 = ['2013', '2014', '2016', '2017', '2018', '2019', '2020', '2021', '2022', 'Total']
years = ["2013-14", "2014-16", "2016-17", "2017-18", "2018-19", "2019-20", "2020-21", "2021-22"]
yeartxt = ['Year']
year = ['2013', '2014', '2016', '2017', '2018', '2019', '2020', '2021', '2022']

a = np.argmax(finyear)
b = np.argmin(finyear)
print("Max Positive Change is seen in", years[a])
print("Max Negative Change is seen in", years[b])

max = np.zeros(9)
min = np.zeros(9)
for i in range(9):
  arr = totalmonthdiff[:,i]
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