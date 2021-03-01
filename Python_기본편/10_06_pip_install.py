# 터미널에 ‘pip install (name)’ 입력 후 설치
# 'pypi.org' 에서 설치 가능
# pip list
# pip show (name)
# pip --upgrade (name)
# pip uninstall (name)

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
