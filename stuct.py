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

print((name_1),(its_me_mario),(name_2))

# print("<" + "공욱재" + ">" + "나야" + "<" + "/ + "공욱재" + ">") 이답은 이렇게된다?