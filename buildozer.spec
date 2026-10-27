[app]

# (str) Title of your application
title = Zinia

# (str) Package name
package.name = zinia

# (str) Package domain (needed for android packaging)
package.domain = org.zinia

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (float) Application version
version = 0.1

# (list) Application requirements
# Added speech_recognition and setuptools for voice assistant support
requirements = python3,kivy,speech_recognition,setuptools

# (str) Supported orientations
orientation = portrait

# (bool) Use fullscreen mode or not
fullscreen = 0

# (list) Permissions
# Added RECORD_AUDIO permission for the microphone to listen to commands
android.permissions = INTERNET,RECORD_AUDIO

# (int) Target Android API, should be as high as possible.
# API 33 is highly recommended for building stability with current Buildozer
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 26c

# (bool) Use --private data directory
android.private_storage = True

# (bool) Accept SDK license without prompting
android.accept_sdk_license = True

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (str) The Android arch to build for
android.archs = armeabi-v7a, arm64-v8a


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
