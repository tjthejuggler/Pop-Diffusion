import numpy

areas = [3453,3464,2314,86,526,6784,2345,476867,23556,9]
scores = [23,5,76,3,678,65,573,263,88,99]
#get the index of the median area in areas
median_index = numpy.argsort(areas)[len(areas)//2]
print(areas[median_index])
print(sorted(areas))

#write "this string" to a file
f = open("test.txt", "w")
f.write("this string")
f.close()