practics = {
    "left_angle_bracket": "<",
    "right_angle_bracket": ">",
    "tag_name": "",
    "close_tag_slash": "/",
    "children_elements": []
}
# <이세한>나야</이세한>을 만들어봐라
#<>를 조합한 이름을 만들어야야하고 그사이에 나야라는 문자열을 넣고
#</>를 조합한 이름을 넣는다.

name = []
name_1 = {"left_angle_bracket"},{"이세한"},{"right_angle_bracket"}
its_me_mario = "나야"
name_2 = {"left_angle_bracket"},{"이세한"},{"close_tag_slash"},{"right_angle_bracket"}

#다른 방식으로 한번 연결시켜보도록 하여 나만의 방식을 모색하고자 했고,각각의 변수를 만들어 변수안에 문자열을 넣어 기입후 출력을 시도. 결과는 그저 문자열만 나열하는 결과를 뽑아내어 내가 원하던 결과가 아니게 됨.다른 문법을 이용해보고 싶음.

print((name_1),(its_me_mario),(name_2))
print("<" + "이세한" + ">" )

# print("<" + "공욱재" + ">" + "나야" + "<" + "/ + "공욱재" + ">") 이답은 이렇게된다? 물론 예제를 보여주신것이지만 이렇게만 표현이 가능한가?라는 생각이 들어 나중에라도 다른 문법을 배우기만 하면 내가 한번 해봐야겠네 