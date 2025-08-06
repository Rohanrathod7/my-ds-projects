from custom_stats import mean, median, mode, variance, std_dev, timer

data = [12, 15, 12, 15, 17, 18, 15, 15, 14]

with timer("Statistics Analysis"):
    mean(data)
    median(data)
    mode(data)
    variance(data)
    std_dev(data)
