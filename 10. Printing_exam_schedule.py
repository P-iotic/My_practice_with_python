"""
P.iotic

Q: 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)

This one felt a bit strain, there was not much to it, just treated it like a
list but I still dont get how it pulls it of without being told to do so.
"""
exam_st_date = (11, 12,2014)
print(str(exam_st_date[0])+"/"+str(exam_st_date[1])+"/"+str(exam_st_date[2]))
"""
Solution

exam_st_date = (11, 12,2014)
print("The examination will start from : %i /%i /%i"%exam_st_date)
"""
