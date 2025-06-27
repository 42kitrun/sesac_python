#pip install pillow
from tracemalloc import BaseFilter
from PIL import Image

# 이미지 열기
image = Image.open('cat2.jpeg')

# 이미지 크기를 줄이고 싶음
resized_image = image.resize((400,300))
resized_image.save('small_cats.jpg')

# 이미지 블러
blurred_image = image.filter(BaseFilter.BLUR)
blurred_image.save('blur_cat.jpeg')

# 이미지 블러
# blurred_image = image.filter(BaseFilter)
# blurred_image.save('l.jpeg')