line_count=$(wc -l < "$1")
echo "Number of lines are: $line_count"
hadoop dfs -ls /
# to make the dir
# hadoop fs -mkdir /user/training/weather 

# to put the data into weather
# hadoop fs -put ~/futurence_hadoop-pyspark/labs/dataset /user/training/weather

# to display the content in weather 
# hadoop fs -cat /user/training/weather

