import re
from urllib import request
import requests

# set url format
url_format = "https://vas.samsungapps.com/stub/stubDownload.as?appId={}&deviceId={}" \
             "&mcc=425&mnc=01&csc=ILO&sdkVer={}&pd=0&systemId=1608665720954&callerId=com.sec.android.app.samsungapps" \
             "&abiType=64&extuk=0191d6627f38685f"

# get input from user
package_name = str(input("Enter the package name (samsung app only): "))
model = str(input("Enter the device model (SM-XXXXX format): "))
sdk_ver = str(input("Enter the android version (SDK format - 26, 28, 29 etc..): "))

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
            print(error_msg[0])
            return
        #
        print("No results!")
        return

    match = match[0]

    # print the available apk file
    print(f"\nThe version code is: {match['vs_code']}\nThe version name is: {match['vs_name']}\n")
    continue_msg = input("Enter [Y/n] to download: ")
    # download the apk file
    if continue_msg in ("Y", "y"):
        print("\nDownload started!")
        file = request.urlretrieve(match["uri"], f'{package_name}-{match["vs_code"]}.apk')
        yellow, end = '\033[93m', '\033[0m'
        print(f"APK saved: {yellow}{file[0]}{end}")
    elif continue_msg in ("N", "n"):
        print("OK!")
    else:
        print("error input")


if __name__ == '__main__':
    main()
