import argparse
import os
import time
from datetime import datetime

import fmt as f

from utility import *
from xf.client import Client
from xf.global_config import Config

Config.API_URL = 'https://forum.litebds.com/api'


def parse_args():
    parser = argparse.ArgumentParser(description='LiteLoaderBDS Forum CLI Tool')
    parser.add_argument('-t', '--token', help='Token to use for authentication', required=True)

    subparsers = parser.add_subparsers(metavar='commands')
    # Thread
    thread_parser = subparsers.add_parser('thread', help='Thread Commands')
    thread_parser.add_argument('-i', '--id', help='Thread ID')
    thread_parser.set_defaults(handler=handle_thread)

    # Resource
    resource_parser = subparsers.add_parser('resource', help='Resource Commands')
    resource_parser.add_argument('-i', '--id', help='Resource ID')
    resource_parser.set_defaults(handler=handle_resource)

    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()
    return args


def handle_thread(args):
    pass


def handle_resource(args):
    Config.API_TOKEN = args.token
    if args.id is None:
        pass
    else:
        resource = Client().get_resource(args.id)
        print(f(
'''{LIGHT_CYAN}[{resource.resource_id}] {ITALIC}{resource.title}{RESET}
{LIGHT_YELLOW}Author: {RESET}{resource.username}
{LIGHT_YELLOW}Version: {RESET}{resource.version}
{LIGHT_YELLOW}Category: {RESET}{resource.category.title}
{LIGHT_YELLOW}Downloads: {RESET}{resource.download_count}
{LIGHT_YELLOW}Views: {RESET}{resource.view_count}
{LIGHT_YELLOW}Created At: {RESET}{datetime.fromtimestamp(resource.resource_date):%Y-%m-%d %H:%M:%S}
{LIGHT_YELLOW}Updated At: {RESET}{datetime.fromtimestamp(resource.last_update):%Y-%m-%d %H:%M:%S}
'''))


if __name__ == '__main__':
    parse_args()
