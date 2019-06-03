import sys.argv as argv

proper_args = ['a little', 'yes', 'no']


def spin_world():
    print(argv)  # Outputs [spin_world_v3.py 'a little']

    if argv[1] not in proper_args:
        print('Use with', *proper_args[:-1], 'or', proper_args[-1], 'Cool? ')
        return


if __name__ == '__main__':
    spin_world()
