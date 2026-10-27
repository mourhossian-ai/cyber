[app]
title = Zinia
package.name = zinia
package.domain = org.zinia
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# (list) Application requirements
# আপনার ভয়েস অ্যাসিস্ট্যান্ট অ্যাপে অন্য কোনো লাইব্রেরি (যেমন speech_recognition) 
# ব্যবহার করলে কমা দিয়ে নিচে যোগ করে নেবেন
requirements = python3,kivy

orientation = portrait
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data directory (True) or a public user directory (False)
android.private_storage = True

# (bool) Accept SDK license without prompting
android.accept_sdk_license = True

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (str) The Android arch to build for
android.archs = armeabi-v7a, arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
