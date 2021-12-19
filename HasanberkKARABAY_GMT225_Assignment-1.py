# this is the database for the dates of the leap second applications
leap_second_data = [
    [1972,6,30,86400],[1972,12,31,86400],[1973,12,31,86400],[1974,12,31,86400],[1975,12,31,86400],[1976,12,31,86400],[1977,12,31,86400],[1978,12,31,86400],[1979,12,31,86400],
    [1981,6,30,86400],[1982,6,30,86400],[1983,6,30,86400],[1985,6,30,86400],[1987,12,31,86400],[1989,12,31,86400],[1990,12,31,86400],[1992,6,30,86400],[1993,6,30,86400],
    [1994,6,30,86400],[1995,12,31,86400],[1997,6,30,86400],[1998,12,31,86400],[2005,12,31,86400],[2008,12,31,86400],[2012,6,30,86400],[2015,6,30,86400],[2016,12,31,86400]]


# this function converts the date into the seconds
# it takes the first leap second as a reference point
def date_to_seconds_converter(date):
 
    year = (date[0]-1972)*12*30*86400
    month = date[1]*30*86400
    day = date[2]*86400
    seconds = date[3]

    total_seconds = year+month+day+seconds- 18230400
    return total_seconds


# this function convert those seconds to a list
# we are going to use this list to determine the leap seconds
def leap_sec_list(leap_second_data):
    leap_second_list = []
    for tarih in leap_second_data:
        leap_second_list.append(date_to_seconds_converter(tarih))
    
    return leap_second_list 



# this function calculates the number of the leap seconds for a given date
def num_of_leap_secs(input,leap_second_list):
    date_to_check = date_to_seconds_converter(input)
    leap_sec_count = 0 
    for date in leap_second_list:
        # we check if the seconds for a given date is greater than the leap second dates. if so we add a leap second.
        if date_to_check >= date:
            leap_sec_count = leap_sec_count + 1
    return leap_sec_count




# this function makes the formatting adjustments
# it adds the difference as a second and convert those seconds as [year , month , day, seconds]
def final_format_check(date,addon):
    year = date[0]
    month = date[1]
    day = date[2]
    seconds = date[3]

    # this part checeks whether or not we are staying in the borders for month day and second variables and transfers them between eachother
    if seconds + addon > 86400:
        seconds = addon
        day += 1

        if day > 31:
            day = 1
            month += 1

            if month > 12:
                month = 1
                year +=1
    # if we dont pass our second limit, we dont need to make any adjustments
    else:
      seconds = seconds + addon

    return [year , month , day ,seconds]



# this is the main function
def converttime(utc):
    
    leap_sec_listed_data = leap_sec_list(leap_second_data)
    number_of_leap_secs = num_of_leap_secs(utc,leap_sec_listed_data)
    # we transform our initial utc date to seconds to use it with functions
    time_utc = date_to_seconds_converter(utc)

    
    tai_time = tai_converter(time_utc,number_of_leap_secs,utc)
    gpst_time = gpst_converter(time_utc,number_of_leap_secs,utc)
    tt_time = tt_converter(utc, date_to_seconds_converter(tai_time))


    print(f'tai- {tai_time}')
    print(f'gpst- {gpst_time}')
    print(f'tt- {tt_time}')        



# this function converts the utc time to tai time
def tai_converter(time_utc,leap_amount,date):
    tai_time = time_utc + 10 + leap_amount
    final_format = final_format_check(date,(tai_time-time_utc))
    
    return final_format



# this function converts the utc time to gpst time
def gpst_converter(time_utc,leap_amount,date):
    
    gpst_time = time_utc + leap_amount - 9
    final_format = final_format_check(date,(gpst_time-time_utc))
    

    return final_format


# this function converts the tai time to tt time
def tt_converter(date, tai_time):
    tt_time = tai_time + 32.184
    final_format = final_format_check(date,(tt_time-tai_time))
    

    return final_format                




## EVALUATION ##

converttime( [2020, 12, 31, 86400])
