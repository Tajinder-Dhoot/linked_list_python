def writeDataToFile(data_list, file_name):
    with open(file_name, 'w') as f:
        for line in data_list:
            line = str(line)
            f.write(line)
            f.write('\n')