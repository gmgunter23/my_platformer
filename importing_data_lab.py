import csv

with open('Norman2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    max_sum = 0.0
    min_sum = 0.0
    max_temp = 0.0
    min_temp = 100.00
    count = 0
    for row in reader:
        if float(row['TMAX']) != -996.00 and float(row['TMIN']) != 996.00:
            max_sum += float(row['TMAX'])
            min_sum += float(row['TMIN'])
            count += 1
            if float(row['TMAX']) > max_temp:
                max_temp = float(row['TMAX'])
            if float(row['TMAX']) < min_temp:
                min_temp = float(row['TMIN'])
        
    avg_max = max_sum / count
    avg_min = min_sum / count
    print(round(avg_max, 2))
    print(round(avg_min, 2))
    print(max_temp)
    print(min_temp)
