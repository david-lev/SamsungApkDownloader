import os
import re
from urllib import request
import requests

# set print colors
yellow, red, blue, green, end = '\033[93m', '\033[91m', '\033[94m', '\033[92m', '\033[0m'
# set url format
url_format = "https://vas.samsungapps.com/stub/stubDownload.as?appId={}&deviceId={}" \
             "&mcc=425&mnc=01&csc=ILO&sdkVer={}&pd=0&systemId=1608665720954&callerId=com.sec.android.app.samsungapps" \
             "&abiType=64&extuk=0191d6627f38685f"

# get input from user
package_name = str(input(f"{green}Enter the package name (Samsung apps only): {end}"))
model = str(input(f"{green}Enter the device model ({yellow}SM-XXXXX{green} format): {end}"))
sdk_ver = str(input(f"{green}Enter the android version (SDK format - {yellow}26 28 29{green} etc..): {end}"))

url = url_format.format(package_name, model, sdk_ver)
# get the text from xml respond
url = requests.get(url).text
# input the info from the xml into dict
regex_info = re.compile(r"resultCode>(?P<status>\d+)</resultCode>"
                        r".*<resultMsg>(?P<msg>[^']*)</resultMsg>"
                        r".*<downloadURI><!\[CDATA\[(?P<uri>[^']*)\]\]></downloadURI>"
                        r".*<versionCode>(?P<vs_code>\d+)</versionCode>"
                        r".*<versionName>(?P<vs_name>[^']*)</versionName>", re.MULTILINE | re.DOTALL)


# dill with error cases
def main():
    match = [m.groupdict() for m in regex_info.finditer(url)]
    if not match:
        # print error message from samsung
        error_msg = re.compile(r"resultMsg>(.*)</resultMsg>").findall(url)
        if error_msg:
            print(f'{blue}Samsung Servers: {red}"{error_msg[0]}"{end}')
            return
        #
        print(f"{red}No results!{end}")
        return

    match = match[0]

    # print the available apk file
    print(f"{blue}\nThe available version Code is: {yellow}{match['vs_code']}"
          f"\n{blue}The available Version Name is: {yellow}{match['vs_name']}{end}\n")
    continue_msg = input(f"{blue}Do you want to download? {yellow}[Y/n]: ")
    # download the apk file
    if continue_msg in ("Y", "y"):
        print(f"\n{blue}Download started!...{end}")
        file = request.urlretrieve(match["uri"], f'{package_name}-{match["vs_code"]}.apk')
        print(f"{blue}APK saved: {yellow}{os.getcwd()}/{file[0]}{end}")
    elif continue_msg in ("N", "n"):
        print(f"{blue}Okay, You can try me again any time :){end}")
    else:
        print(f"{red}Error input | enter 'Y' or 'N'{end}")


if __name__ == '__main__':
    main()
