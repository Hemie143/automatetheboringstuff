import datetime


oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))                        # '2019/10/21 16:29:00'
print(oct21st.strftime('%I:%M %p'))                                 # '04:29 PM'
print(oct21st.strftime("%B of '%y"))                                # "October of '19"

print(datetime.datetime.strptime('October 21, 2019', '%B %d, %Y'))                  # datetime.datetime(2019, 10, 21, 0, 0)
print(datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))       # datetime.datetime(2019, 10, 21, 16, 29)
print(datetime.datetime.strptime("October of '19", "%B of '%y"))                    # datetime.datetime(2019, 10, 1, 0, 0)
print(datetime.datetime.strptime("November of '63", "%B of '%y"))                   # datetime.datetime(2063, 11, 1, 0, 0)
