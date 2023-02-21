def load_bands():
    file_name = '/home/badgersky/Desktop/bands.txt'
    with open(file_name, 'r') as f:
        bands = f.read()
        return bands.split(',')


if __name__ == '__main__':
    pass
