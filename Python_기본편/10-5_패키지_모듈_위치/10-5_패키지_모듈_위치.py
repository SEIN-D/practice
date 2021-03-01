# import travel.thailand
# # import travel.thailand.ThailandPackage
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import *
from travel import *
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))
# 랜덤 모듈이 있는 파일에 내가 만든 패키지를 가져다 놓으면, 실행하는 파일이 패키지와 같은 경로에 있지 않아도 언제든 사용할 수 있다.
