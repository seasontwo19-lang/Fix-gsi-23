import os

print("Processing system.img for fixes...")

# build.prop path inside extracted or binary search
# Let's append properties directly if possible or patch the image
# Since mounting direct erofs failed, let's use a robust tool or script to inject props if extracted, 
# or let's install erofs tools properly:
