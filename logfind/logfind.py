import os
# import sys
import argparse

def get_file_paths(config_file):
    paths = []
    for path in open(config_file):
        path = path.rstrip('\n')
        paths.append(path)
    return paths

def search(search_terms, file_path, o=False):

    f = open(os.path.expanduser(file_path))
    contents = f.read()

    if o:
        result = False
        for search in search_terms:
            if search in contents:
                result = True
                break
    else:
        result = True
        for search in search_terms:
            if not search in contents:
                result = False
                break
    f.close()
    return result

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', action='store_true')
    parser.add_argument('search_terms', type=str, nargs='+')
    args = parser.parse_args()

    config_file = os.path.expanduser('~/.logfind')
    log_files = get_file_paths(config_file)

    results = []
    for file_path in log_files:
        if search(args.search_terms, file_path, args.o):
            results.append(file_path)
    print results

if __name__ == '__main__':
    main()

# def search_all(search_terms, log_file):
#     file = open(log_file)
#     contents = file.read()
#     result = True
#     for search in search_terms:
#         # print log_file, search, search in contents
#         if not search in contents:
#             result = False
#             break
#     file.close()
#     return result

# def search_any(search_terms, log_file):
#     file = open(log_file)
#     contents = file.read()
#     result = False
#     for search in search_terms:
#         if search in contents:
#             result = True
#             break
#     file.close()
#     return result

# def logfind(search_terms, search_type):
#     config_file = os.path.expanduser('~/.logfind')
#     results = []
#     for path in open(config_file):
#         path = path.rstrip('\n')
#         path = os.path.expanduser(path)
#         if search_type == 'and':
#             if search_all(search_terms, path):
#                 results.append(path)
#         else:
#             if search_any(search_terms, path):
#                 results.append(path)
#     return results

# if __name__ == '__main__':
#     if sys.argv[1] == '-o':
#         search_terms = sys.argv[2:]
#         search_type = 'or'
#     else:
#         search_terms = sys.argv[1:]
#         search_type = 'and'

#     results = logfind(search_terms, search_type)
#     if len(results) > 0:
#         for result in results:
#             print(result)
#     else:
#         print("No results")

