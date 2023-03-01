from pyspark import SparkContext 

sc = SparkContext("local", "Wordcount app") 


lines = sc.textFile(r"C:\Users\miles\Desktop\Codes\Linux\futurense_hadoop-pyspark\labs\dataset\wordcount\wordcount-input.txt")

lines.collect()
counts = lines.flatMap(lambda x: x.split(' '))
co=counts.reduceByKey(lambda a, b: a + b)
output = counts.collect()
for (word, count) in output:
	print("%s: %i" % (word, count))
