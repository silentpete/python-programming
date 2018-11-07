images = ['domain/product-name:1.2.3-tag', 'domain/product-name:4.5.6-tag']

for image in images:
  print('Image: ' + image)
  image = image.replace(':','/')
  image_parts = image.strip('/').split("/")

  # Loop over parts of the image path and add a slash to each
  for idx, ipart in enumerate(image_parts):
    print('Image part: ' + str(idx) + ' => ' + ipart)
    image_parts[idx] = ipart + '/'
    print('Image part: ' + image_parts[idx])

  first_image_part = image_parts[0]
  print('First image part: ' + first_image_part)
  image_parts.pop(0)

  for idx, ipart in enumerate(image_parts):
    last_image_part = ''.join(image_parts[0:idx+1])
    print('image part: ' + last_image_part)
