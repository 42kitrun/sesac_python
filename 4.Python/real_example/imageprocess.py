#pip install pillow
from PIL import Image, ImageFilter
import os


print(os.getcwd())

# 이미지 열기
image = Image.open('./4.python/real_example/cat2.jpeg')

# 이미지 크기를 줄이고 싶음
resized_image = image.resize((80,60))
resized_image.save("./4.python/real_example/small_cats.jpeg")

# 이미지 블러
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save("./4.python/real_example/blur_cats.jpeg")

# 이미지 블러
blurred_image = image.filter(ImageFilter.CONTOUR)
blurred_image.save('./4.python/real_example/contour_cats.jpeg')