# every tiem we use a function, 
# Python gathers the positional arguments into a tuple
# and the keyword arguments into a dictionary

def A(*args):
    '''reveal all the positional arguments'''
    return args # this is a tuple
def B(**kwargs):
    '''reveal the keyword arguments'''
    return kwargs # dict

if __name__ == '__main__':
    ''''''
    result_a = A(3,2,6,True,(), {}, 'all done')
    print(result_a, type(result_a))
    # we can iterate over an indexed collection (tuple, string, list)
    for item in result_a:
        print(item)

    result_b = B(x=3,y=2,n=6,flag=True,e=(), j={}, s='all done')
    print(result_b, type(result_b))

    # we can get the members of a dict like this
    for (k,v) in result_b.items():
        print(k, v)
