'''
2.Electricity Bill Calculation

The consolidated power consumption for a commercial complex is sent in the following
format by EB department for a month. The complex has 5 shops each having a separate
meter box and the electricity tariff total for a month has to be calculated for each shop
separately based on the number of units consumed.
NOTE: The same shop may have more than one entry in a single line. Sometimes if a
shop does not
consume energy it will not be part of the list. On power shutdown days the entry will be
nothing just the date
Find the total power consumed if each shop is charged in the following slabs
First 999 units: 0.40/unit
1000-2000 units: 0.33/unit
2001-5000 units: 0.30/unit

5000+units: 0.20/unit
Input Format
&lt;MMM&gt;&lt;DD&gt;, &lt;YYYY&gt;: &lt;shop 1&gt;&lt;usage 1&gt;$&lt;shop 2&gt;&lt;usage 2&gt;$......&lt;shop
n&gt;&lt;usage n&gt;
Test case1:
Input    :
3
Jan 1, 2020: shop1 320$shop2 220$shop3 330$shop4 420$shop5 5
Jan 2, 2020: shop5 318$shop4 320$shop3 330$shop2 420$shop1 5
Jan 3, 2020:
Output :
shop1:130.00
shop2:256.00
shop3:264.00
shop4:296.00
shop5:129.20
Test case2:
Input    :
6
Jan 01, 2020: shop1 320$shop2 220$shop3 330$shop4 420$shop5 57
Jan 02, 2020: shop5 81$shop4 380$shop3 327$shop2 240$shop1 318
Jan 03, 2020: shop1 316$shop3 334$shop4 400$shop5 75$shop2 211
Jan 04, 2020:
Jan 05, 2020: shop1 323$shop2 210$shop3 300$shop4 418$shop5 43
Jan 06, 2020: shop1 324$shop3 315$shop4 411$shop5 48

Output :
shop1:528.33
shop2:352.40
shop3:529.98
shop4:608.70
shop5:121.60
Test case3:
Input :
8
Jan 1, 2020: shop1 320$shop2 220$shop3 330$shop4 420$shop5 5
Jan 2, 2020: shop5 318$shop4 320$shop3 330$shop2 420$shop1 5
Jan 3, 2020: shop1 316$shop1 820$shop3 330$shop4 420$shop5 5
Jan 4, 2020: shop1 314$shop2 110$shop3 68$shop4 420$shop5 5
Jan 5, 2020: shop1 323$shop2 220$shop3 330$shop4 420$shop5 5
Jan 6, 2020: shop1 324$shop3 330$shop4 420$shop5 5
Jan 7, 2020: shop1 320$shop2 220$shop3 330$shop4 420$shop5 51
Jan 8, 2020:

Output :
shop1:822.60
shop2:392.70
shop3:614.40
shop4:852.00
shop5:157.60
'''
def cacl_amnt(day):
    for i,j in day.items():
        if j<=999:
            amnt=j*0.40
            day[i]=[amnt,j]
        elif j>=1000 and j<=2000:
            amnt=j*0.33
            day[i]=[amnt,j]
        elif j>=2001 and j<=5000:
            amnt=j*0.33
            day[i]=[amnt,j]
    for i,j in day.items():
        print("{}:{:.2f}".format(i,j[0]))
n=int(input())
day={}
day_list=[]
try:
    for i in range(n):
            inpt="".join(input().split()[3:])
            inpt=inpt.split('$')
            day_list.append(inpt)
    for i in day_list:
        for j in i:
            shop="".join(j[:5])
            val=int("".join(j[5:]))
            if shop not in day.keys():
                day[shop]=val
            else:
                val1=day[shop]
                val1+=val
                day[shop]=val1
except:
    pass
print(day)
cacl_amnt(day)
