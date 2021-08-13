import os
import re
from urllib import request
import requests
import argparse
from sys import argv

# set print colors
yellow, red, blue, green, end = '\033[93m', '\033[91m', '\033[94m', '\033[92m', '\033[0m'
# set url format
url_format = "https://vas.samsungapps.com/stub/stubDownload.as?appId={}&deviceId={}" \
             "&mcc=425&mnc=01&csc=ILO&sdkVer={}&pd=0&systemId=1608665720954&callerId=com.sec.android.app.samsungapps" \
             "&abiType=64&extuk=0191d6627f38685f"

# Get some input from the user
if len(argv) > 1:
    my_parser = argparse.ArgumentParser(prog='SamsungApkDownloader.py',
                                        description='List of arguments for SamsungAPkDownloader')

    my_parser.add_argument("-m", type=str, metavar="'device-model'", help="Samsung model in  'SM-XXXXX' format",
                           required=True)
    my_parser.add_argument("-v", type=int, metavar="'sdk-version'", help="Android sdk version (19-30)",
                           required=True)
    my_parser.add_argument("-p", type=str, metavar="'package-name'", help="Package Name 'com.package.name'",
                           required=True)

    args = my_parser.parse_args()
    package_name = args.p
    model = args.m
    sdk_ver = args.v
else:
    package_name = str(input(f"{green}Enter package name (Samsung apps only): {end}"))
    model = str(input(f"{green}Enter your device model ({yellow}SM-XXXXX{green} format): {end}"))
    sdk_ver = str(input(f"{green}Enter your android version (SDK format - {yellow}26 28 29{green} etc..): {end}"))

url = url_format.format(package_name, model.upper(), sdk_ver)
# get the text from xml respond
url = requests.get(url).text
# input the info from the xml into a dict
regex_info = re.compile(r"resultCode>(?P<status>\d+)</resultCode>"
                        r".*<resultMsg>(?P<msg>[^']*)</resultMsg>"
                        r".*<downloadURI><!\[CDATA\[(?P<uri>[^']*)\]\]></downloadURI>"
                        r".*<versionCode>(?P<vs_code>\d+)</versionCode>"
                        r".*<versionName>(?P<vs_name>[^']*)</versionName>", re.MULTILINE | re.DOTALL)


# deal with error cases
def main():
    match = [m.groupdict() for m in regex_info.finditer(url)]
    if not match:
        # Showing error message from samsung servers
        error_msg = re.compile(r"resultMsg>(.*)</resultMsg>").findall(url)
        if error_msg:
            print(f'{blue}Samsung Servers: {red}"{error_msg[0]}"{end}')
            return
        #
        print(f"{red}No results!{end}")
        return

    match = match[0]

    # Print the available apk file info
    print(f"{blue}\nThe available versionCode is: {yellow}{match['vs_code']}"
          f"\n{blue}The available versionName is: {yellow}{match['vs_name']}{end}\n")
    continue_msg = input(f"{blue}Do you want to download? {yellow}[Y/n]: ")
    # Download the apk file
    while continue_msg not in ["Y", "y", "", "N", "n"]:
        continue_msg = input(f"{blue}Error input. choose {yellow}[Y/n]: ")
    else:
        if continue_msg in ("Y", "y", ""):
            print(f"\n{blue}Download started!...{end}")
            file = request.urlretrieve(match["uri"], f'{package_name}-{match["vs_code"]}.apk')
            print(f"{blue}APK saved: {yellow}{os.getcwd()}/{file[0]}{end}")
        elif continue_msg in ("N", "n"):
            print(f"{blue}Okay, You can try me again any time :){end}")


if __name__ == '__main__':
    main()
