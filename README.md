![Alt Text](https://i.imgur.com/JSazRzr.gif)
---
# Samsung APK Downloader

### How it's work?
Manually updating Samsung apps can be tricky and even impossible especially from Android 9 and up.
This script goes directly to Samsung servers (a kind of Galaxy Store) with your device details and downloads clean APK file without any signatures so you can install it manually on the device that matches the details you provided when running the script

### How to use?
- clone this repository:
```
git clone https://github.com/david-lev/SamsungApkDownloader.git
```
- go to script directory:
```
cd SamsungApkDownloader
```
- run the script:
```shell
python3 SamsungApkDownloader.py -m SM-XXXX -v 29 -p com.sec.android.app.myfiles
```
```
The available versionCode is: 1150403081
The available versionName is: 11.5.04.81

Do you want to download? [Y/n]: Y

Download started!...
APK saved: /home/david/Downloads/com.sec.android.app.myfiles-1150403081.apk
```
* You can also run the script without arguments and input the details manually:
 - ``python3 SamsungApkDownloader.py``
- Enter the package name of the app that you want to download
- Enter your device model (SM-XXXXX)
- Enter your [android sdk version](https://source.android.com/setup/start/build-numbers#platform-code-names-versions-api-levels-and-ndk-releases) (android 8 - 26, android 9 - 28 etc..)
- The APK file will be saved in the script path in the folowing format ``com.package.name-123.apk``

> created by [David Lev](https://linktr.ee/davidlev) & [Yehuda By](https://t.me/m100achuzbots)
---
