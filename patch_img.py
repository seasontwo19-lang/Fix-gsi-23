with open("system.img", "rb") as f:
    content = f.read()

print(f"Loaded system.img, size: {len(content)} bytes")

# We can search and replace or inject properties if space allows, 
# or use standard android image unpacking tools.
