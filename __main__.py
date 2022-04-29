import argparse
from crawller import crawller
from constans import url_mapper

parser = argparse.ArgumentParser(description='Crawller.')
parser.add_argument('target', type=str, help='target URL to retrieve information')
parser.add_argument('--print', default=True,
                    action='store_true', help='print crawller results')
parser.add_argument('--save_csv', default=False,
                    action='store_true', help='save crawller results to csv file')
parser.add_argument('--save_json', default=False,
                    action='store_true', help='save crawller results to json file')
args = parser.parse_args()

results = crawller(args.target)
if args.print:
    print(results)
if args.save_csv:
    results.to_csv(f'{url_mapper[args.target]}.csv', index=False)
if args.save_json:
    results.to_json(f'{url_mapper[args.target]}.json')

