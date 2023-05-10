import argparse


def args_parser():
    parser = argparse.ArgumentParser(description='Polling args')
    parser.add_argument('--token',
                        type=str,
                        help='Telegram Bot Token')
    parser.add_argument('--deltime',
                        type=int,
                        default=10,
                        help='Password messages lifetime')
    args = parser.parse_args()
    return args
