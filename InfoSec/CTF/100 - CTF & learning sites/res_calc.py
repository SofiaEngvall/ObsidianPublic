# Calculating the height needed for a 4:3 aspect ratio with a width of 1024 pixels
width = 1024
aspect_ratio_width = 3
aspect_ratio_height = 4

# Calculate height
height = int((width / aspect_ratio_width) * aspect_ratio_height)
print(height)
