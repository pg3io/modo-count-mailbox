#!/usr/bin/env python
# coding: utf-8

"""
    File name: modo-count.py
    Author: Anthony Adrien Thibault PG3
    Date created: 21/11/2018
    Date last modified: 21/11/2018
    Python Version: 2.7<=3
"""


import requests
import sys
import json
import argparse


def get_account(email, headers, base_url):
    url = '{}/api/v1/accounts/exists/?email={}'.format(base_url, email)
    try:
        r = requests.get(url, headers=headers)
        email_exists = r.json()['exists']
    except ValueError:
        raise Exception("Impossible d'interroger l'api")

    if email_exists:
        url = '{}/api/v1/accounts/?search={}'.format(base_url, email)
        try:
            r = requests.get(url, headers=headers)
            account = r.json()[0]
        except ValueError:
            raise Exception('Impossible de récupérer les informations du compte {}'.format(email))
        return account

    else:
        print('Email inconnu : {}'.format(email))
        sys.exit(1)


def get_domains(adm_domains, headers, base_url):
    url = '{}/api/v1/domains/'.format(base_url)
    r = requests.get(url, headers=headers)
    try:
        domains = r.json()
        return [domain for domain in domains if domain['name'] in adm_domains]
    except ValueError:
        raise Exception("Impossible d'interroger l'api")

def print_term(mailbox_data):
    print("total mailbox : {0}\n".format(mailbox_data['total_mailbox']['count']))

    for item in mailbox_data['details']:
        print("{0}: {1}".format(item['name'], item['mailbox_count']))


def get_details_format(account, headers, base_url):
    mailbox = []
    mailbox_details = {}
    keys = ['name', 'mailbox_count']

    try:
        domains = get_domains(account['domains'], headers, base_url)
    except Exception as e:
        print(e)
        sys.exit(1)

    mailbox_count = sum(domain['mailbox_count'] for domain in domains)

    mailbox_details['total_mailbox'] = {"count": mailbox_count}
    for domain in domains:
        mailbox.append({key: domain[key] for key in keys})
    mailbox_details['details'] = mailbox

    return mailbox_details


def get_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--reseller", type=str, help="precise email of the reseller", metavar="EMAIL", required=True)
    parser.add_argument("-t", "--token", type=str, help="Token for access to data", required=True)
    parser.add_argument("-a", "--api", type=str, help="precise url modoboa", metavar="URL", required=True)
    parser.add_argument("-o", "--output", type=str, help="precise output : json/read", metavar="json/read", required=False, default=None)
    args = parser.parse_args()

    return args


def main():
    args = get_args_parser()
    headers = {'authorization': 'Token ' + args.token}
    base_url = args.api

    email = args.reseller
    try:
        account = get_account(email, headers, base_url)
    except Exception as e:
        if args.output == "read":
            print(e)
            sys.exit(1)
        else:
            print(json.dumps({'error': str(e)}, indent=4, separators=(',', ': ')))
            sys.exit(1)

    if account['role'] != 'Resellers':
        print("{} n'est pas un revendeur".format(email))
        sys.exit(1)

    mailbox_details = get_details_format(account, headers, base_url)

    if args.output == "json" or not args.output:
        mailbox_json = json.dumps(mailbox_details)
        print(mailbox_json)
    elif args.output == "read":
        print_term(mailbox_details)
    else:
        print("Output format can only be json/read")
        sys.exit(1)



if __name__ == '__main__':
    main()