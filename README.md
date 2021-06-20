![Alt Text](https://i.imgur.com/Y4oAkA7.gif)
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
```
python3 SamsungApkDownloader.py
```
- Enter the package name of the app that you want to download
- Enter your device model (SM-XXXXX)
- Enter your [android sdk version](https://source.android.com/setup/start/build-numbers#platform-code-names-versions-api-levels-and-ndk-releases) (android 8 - 26, android 9 - 28 etc..)
- The APK file will be saved in the script path in the folowing format ``com.package.name-123.apk``

> created by [David Lev](https://linktr.ee/davidlev) & [Yehuda By](https://t.me/m100achuzbots)
---
