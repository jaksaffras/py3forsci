import sys

print("sys.version: {}\n".format(sys.version))

print("sys.version_info: {}\n".format(sys.version_info))

v = sys.version_info
print("v.major: {}".format(v.major))
print("v.minor: {}\n".format(v.minor))

if (v.major < 3) or (v.minor < 6):
    print("Sorry, this script requires 3.6 or later")
    exit(1)

print("sys.prefix: {}\n".format(sys.prefix))
print("sys.executable: {}\n".format(sys.executable))

print("sys.platform: {}\n".format(sys.platform))
# win32 = any Windows
# darwin = Mac
# linux = Linux

# sys.stdin sys.stdout sys.stderr

print("Houston, we have a problem", file=sys.stderr)





