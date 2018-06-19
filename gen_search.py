def search(keyword, filename):
    print('generator started')
    f = open(filename, 'r')
    # Looping through the file line by line
    for line in f:
        print('inside for loop----------')
        if keyword in line:
            # If keyword found, return it
            print('inside for loop---------- before yield')
            yield line
            print('inside for loop---------- after yield')
    f.close()
