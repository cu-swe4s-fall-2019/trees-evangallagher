import argparse
import sys
import binary_tree
import avl_tree
import time
import hash_tables as ht


def main():

    parser = argparse.ArgumentParser(description='Store key'
                                     'data structures',
                                     prog='insert_key_value_pairs')

    parser.add_argument('--datastructure', type=str, help='Name of '
                        "datastructure to use. Choose from 'hash', "
                        "'binary_tree', or 'avl_tree'", required=True)

    parser.add_argument('--dataset', type=str, help='Name of txt file'
                        ', value pairs', required=True)

    parser.add_argument('--number_keys', type=int, help='Number of keys from'
                        'dataset to read in', required=True)

    args = parser.parse_args()

    datastructure = args.datastructure
    filename = args.dataset
    N = args.number_keys

    if datastructure == 'hash':
        print('initializing')
        hashtable = ht.ChainedHash(10000000, ht.hash_functions.h_rolling)
        insert_t0 = time.time()
        counter = 0
        for line in open(filename, 'r'):
            data = line.rstrip().split('\t')
            hashtable.add(data[0], data[1])
            counter += 1
            if counter == N:
                break
        insert_t1 = time.time()
        search_t0 = time.time()
        counter = 0
        for line in open(filename, 'r'):
            data = line.rstrip().split('\t')
            hashtable.search(data[0])
            counter += 1
            if counter == N:
                break
        search_t1 = time.time()
        print('time to insert: ' + str(insert_t1 - insert_t0))
        print('time to search: ' + str(search_t1 - search_t0))

    elif datastructure == 'binary_tree':
        print('initialize binary tree')
        insert_t0 = time.time()
        datatree = binary_tree.create_tree(filename, N)
        insert_t1 = time.time()
        search_t0 = time.time()
        counter = 0
        for line in open(filename, 'r'):
            data = line.rstrip().split('\t')
            binary_tree.search(datatree, data[0])
            counter += 1
            if counter == N:
                break
        search_t1 = time.time()
        print('time to insert: ' + str(insert_t1 - insert_t0))
        print('time to search: ' + str(search_t1 - search_t0))

    elif datastructure == 'avl_tree':
        print('initialize AVL tree')
        insert_t0 = time.time()
        datatree = avl_tree.create_AVLtree(filename, N)
        insert_t1 = time.time()
        search_t0 = time.time()
        counter = 0
        for line in open(filename, 'r'):
            data = line.rstrip().split('\t')
            avl_tree.search(datatree, data[0])
            counter += 1
            if counter == N:
                break
        search_t1 = time.time()
        print('time to insert: ' + str(insert_t1 - insert_t0))
        print('time to search: ' + str(search_t1 - search_t0))

    else:
        print('does not recognize ')


if __name__ == '__main__':
    main()
