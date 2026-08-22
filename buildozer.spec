[app]

# (string) Title of your application
title = Education App

# (string) Package name
package.name = educationapp

# (string) Package domain (needed for android packaging)
package.domain = org.education

# (string) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (string) Application version
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (int) Android API to target
android.api = 31

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 31
