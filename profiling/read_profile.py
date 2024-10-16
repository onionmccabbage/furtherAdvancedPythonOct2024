import pstats
def main():
    '''open a cProfile report and show the results'''
    p = pstats.Stats('profiling/profile_output')
    p.print_stats()

if __name__ == '__main__':
    main()