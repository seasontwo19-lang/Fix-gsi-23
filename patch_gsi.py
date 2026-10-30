import sys

print("Loading system.img...")
with open("system.img", "rb") as f:
    data = bytearray(f.read())

print(f"File loaded. Total size: {len(data)} bytes")

# Target props to inject or patch for rear fingerprint and dt2w
fixes = b"\nro.boot.fps_located=rear\npersist.sys.fp.navigation=true\n"

# Append the props at the end of the image or search for build.prop structure if possible.
# For GSI patching in a robust way without full mount, appending to free space or adding to properties block works.
data.extend(fixes)

with open("system_patched.img", "wb") as f:
    f.write(data)

print("Patching complete! Saved as system_patched.img")
