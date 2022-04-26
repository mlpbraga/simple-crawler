import argparse

parser = argparse.ArgumentParser(description='Crawller.')
parser.add_argument('--print', default=True,
                    action='store_true', help='Print crawller results.')
parser.add_argument('--save_csv', default=False,
                    action='store_true', help='Save crawller results to csv file.')
parser.add_argument('--save_json', default=False,
                    action='store_true', help='Save crawller results to json file.')
args = parser.parse_args()

if args.print:
    print('Print')
if args.save_csv:
    print('Save csv')
if args.save_json:
    print('Save json')