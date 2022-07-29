def split_and_join(line):
    split_string = line.split(" ")
    join_string = "-".join(split_string)
    return join_string
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)