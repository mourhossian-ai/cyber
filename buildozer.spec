[app]
android.accept_sdk_license = True
# (str) Title of your application
title = Zinia

# (str) Package name
package.name = zinia

# (str) Package domain (needed for android packaging)
package.domain = org.zinia

# (str) Source files where the *.py files exist
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy
# (str) Supported orientations
orientation = portrait

# (int) Indicate if the application should be full screen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET
version = 0.1
