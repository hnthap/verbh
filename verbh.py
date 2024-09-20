import argparse
import json
import os
    

def main():
    args = get_arguments()
    input_verb = get_input_verb(args)
    is_match = lambda s: input_verb in s
    verbs = get_verbs()
    result = []
    for verb in verbs:
        main_verb = verb['Verb']
        synonyms = verb['Synonyms']
        if is_match(main_verb) or any(map(is_match, synonyms)):
            result.append(verb)
    try:
        if len(result) == 0:
            print('No results')
        for result_no, verb in enumerate(result, 1):
            print('[{}/{}]'.format(result_no, len(result)))
            show_verb(verb)
            if args.one_by_one and result_no != len(result):
                input()
            else:
                print()
    except KeyboardInterrupt:
        pass


def get_arguments():
    parser = argparse.ArgumentParser(description='a verb helper')
    parser.add_argument('-v', '--verb', help='find the verb', type=str)
    parser.add_argument('-o', 
                        '--one-by-one', 
                        help='show the results one by one (default: False)', 
                        action='store_true')
    args = parser.parse_args()
    return args
    

def get_input_verb(args):
    verb = args.verb
    if verb is None:
        verb = input('Enter verb: ')
    verb = verb.strip().lower()
    return verb


def get_current_script_dir():
    script_dir = os.path.join(__file__, '..')
    script_dir = os.path.abspath(script_dir)
    return script_dir


def get_verbs():
    script_dir = get_current_script_dir()
    data_file = os.path.join(script_dir, 'data', 'verbs.json')
    with open(data_file, 'r') as f:
        data = json.load(f)
        return data['verbs']
    

def show_verb(verb):
    print('Verb       : {}'.format(verb['Verb']))
    if len(verb['Synonyms']) != 0:
        print('Synonyms   : {}'.format(', '.join(verb['Synonyms'])))
    print(verb['Action'])


if __name__ == '__main__':
    main()
