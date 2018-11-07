def count_of_files(filename):
    sum_n = 0
    amount_n = 0

    with open(filename, 'r') as f:
        for line in f:
            try:
                sum_n += int(line)
                amount_n += 1
            except ValueError:
                # if it's not a number we should open the file
                count = count_of_files(line.strip())
                sum_n += count[0]
                amount_n += count[1]

    return sum_n, amount_n


if __name__ == '__main__':

    sum_n, len_n = count_of_files('onlynumbers.txt')
    print 'Testing only with digits. Result: ',  sum_n/len_n

    sum_n, len_n = count_of_files('case1.txt')
    print 'The average of numbers is:', sum_n/len_n
