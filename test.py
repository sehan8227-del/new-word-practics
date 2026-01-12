class Body:
    def __init__(self, content):
        self.content = content

a = Body("이세한")
print(a.content)
print(dir(a))

# 이세한이라는 콘텐츠를 꺼내오는것이다.