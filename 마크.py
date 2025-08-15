리템
retem_
온라인

#ㄹㄹㅜㅜㄴㄴ 채널의 시작이에요. 
리템 — 2025-06-20(금) 오후 5:56
초반에 마법봉으로 마나 채우면서 몹 잡기
리템 — 2025-06-21(토) 오전 4:00
그런 지형이 peaks 라고 해서 한국어론 봉우리라고 번역되어 있는 바이옴인데
보통 이런 바이옴이 눈이 덮혀있는 형태가 많음

그래서 이런 바이옴의 가장 y값이 높은 곳에서 파고 내려가면 딥 다크 지형(스컬크 지형)은 무조건 있고
고대 도시가 있을 확률이 높음
리템 — 2025-06-21(토) 오후 6:30
1054 11 -1156 마석가루
리템 — 2025-06-22(일) 오전 1:27
https://docs.google.com/spreadsheets/d/1i_qiR_t7fQSRLDteCIxKcmHXtfowYshvuXPmovTEpwU/edit?gid=0#gid=0
리템 — 2025-06-26(목) 오후 7:42
눈 덮인 비탈, 
뾰족한 봉우리 (Jagged Peak)

얼어붙은 봉우리 (Frozen Peak)

돌 봉우리,
벚나무 숲 (heey Grove)

목초지 (Meadow)

산림 (Grove)
통 가능한지
리템 — 2025-06-27(금) 오전 2:39
/쓰래기통
있음
리템 — 2025-06-28(토) 오후 5:31
농작지 몇x몇린지 확인
리템 — 2025-06-29(일) 오후 11:27
옵시디언 차원석
돈 던전으로 함
리템 — 2025-06-30(월) 오후 10:19
https://cafe.naver.com/bjcrocodile/3631845?tc=shared_link
리템 — 2025-06-30(월) 오후 11:55
희귀에 탱커에 좋은룬 많음
리템 — 2025-07-04(금) 오후 7:11
희귀룬 감정 5000
리템 — 2025-07-05(토) 오후 8:49
몇몇npc 위치 변경
타룬에 정보상인있음
리템 — 2025-07-06(일) 오후 7:27
요번 회차 2시간(이벤트 제외)
후원연동 다음주에 무조건 추가 예정(악어님에게 말씀함) 네더 도구1%, 수선 0.5%, 05% 아래는 서버 전체 알람이 뜸
회귀무기(룬슬롯 4개), 갑옷(중요할듯?)갑옷 다 못구하면 한방날수도 풀셋맞추면 이김(예상)
아이스볼 ap 210% 필요마나 110
pvp계수생김 안젹혀 있으면 기본 0.5 
15초동안 전투 안하면 신속 2 제공 공격당하거나 하면 바로 풀림
마법룬(신의룬?) 이번 회차 가치X 나중에 가치 있음
길드 창고 다음 금액 백만원 한줄씩 늘어남
야생 들어가면 바로 앞에 에메랄드 있을만한 지역있음 가보기
용병 다음에는 할수 있도록 노력
리템 — 2025-07-07(월) 오후 8:18
아티펙트는 롤에서 따온게 있음
리템 — 2025-07-25(금) 오후 11:22
https://cfx3awqnknjftoavdph9cd.streamlit.app/#56edc69b
리템 — 2025-07-27(일) 오후 7:20
https://retemrune1.streamlit.app/
Streamlit
Streamlit
This app was built in Streamlit! Check it out and visit https://streamlit.io for more awesome community apps. 🎈
Streamlit
리템 — 2025-07-27(일) 오후 9:39
좌표 입력하면 어디 텔포가 가까운지
리템 — 2025-07-28(월) 오전 3:03
새로운 목록 만들어서 재료 클릭하면 어느 보스에서 나오는지
가상 지도 비슷하게 만들기
리템 — 2025-07-31(목) 오후 5:58
{"name": "", "location": [, , ], "region": "", "reward": "", "notes": ""},
리템 — 2025-08-03(일) 오후 7:37
import streamlit as st
import math
import plotly.express as px
import pandas as pd
import os
확장
message.txt
18KB
리템 — 2025-08-03(일) 오후 7:50
# ------------------ 거리 계산 ------------------
def get_nearest_teleport(location, teleports):
    def euclidean(a, b):
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))
    nearest = min(teleports, key=lambda t: euclidean(t["location"], location))
    return nearest, round(euclidean(nearest["location"], location))
확장
message.txt
11KB
리템 — 2025-08-04(월) 오전 2:25
전쟁 지도 만들기
리템 — 2025-08-05(화) 오전 11:57
1
리템 — 2025-08-08(금) 오후 10:47
방플가능
리템 — 오후 8:59
import streamlit as st
import math
import pandas as pd
import plotly.graph_objects as go



# ------------------ 데이터 정의 ------------------
data = {
    "dungeons": [
        {"name": "수호기사 클로스", "location": [1370, 46, -1030], "region": "", "reward": ""},
        {"name": "슬라임 킹", "location": [1214, 10, -600], "region": "", "reward": ""},
        {"name": "변이된 언데드", "location": [1702, 10, -870], "region": "오염된 땅", "reward": ""},
        {"name": "슬라임 기사", "location": [1632, 10, -690], "region": "끈적이는 땅", "reward": ""},
        {"name": "란", "location": [1154, 9, -1340], "region": "", "reward": "2000G"},
        {"name": "변이된 스켈레톤", "location": [1290, 22, -1380], "region": "", "reward": "2000G"},
        {"name": "말괄량이 마법사 데이비", "location": [1050, 10, -1155], "region": "", "reward": ""},
        {"name": "전사 브루스", "location": [1110, 75, -1214], "region": "낡은 검의 은신처", "reward": "3000G"},
        {"name": "펜리르", "location": [1180, 75, -1130], "region": "고독한 늑대의 요람", "reward": "5000G, 영험한 힘이 깃든 늑대 이빨, 미약한 힘이 담긴 영혼"},
        {"name": "슬라임 퀸", "location": [1355, 70, -1114], "region": "부패의 모체", "reward": "3000G, 슬라임 퀸의 핵"},
        {"name": "포레스트 골렘", "location": [1100, 78, -1100], "region": "대자연의 수호전", "reward": "3000G, 골렘의 핵"},
        {"name": "흑량", "location": [1630, 81, -690], "region": "잿빛 사냥꾼의 영역", "reward": "3000G,  검은 이리 가죽"},
        {"name": "고블린 라이더 & 와일드 보어 킹", "location": [1660, 69, -1200], "region": "야만의 군체", "reward": "3000G, 고블린라이더의 깃발"},
        {"name": "야만 전사 헬턴", "location": [1532, 16, -790], "region": "야만의 격전지", "reward": "3000G, 야만전사 도끼"},
        {"name": "침묵의 검무 키에린", "location": [114, 67, 611], "region": "저무는 칼날의 길", "reward": "5000G, 검의 인식처, 미약한 힘이 담긴 영혼"},
        {"name": "봉인된 문장 그린힐름", "location": [-472, 71, 502], "region": "봉인된 성소", "reward": "5000G, 페데도트의 문장, 미약한 힘이 담긴 영혼"},
        {"name": "사자혼종", "location": [-160, 69, 74], "region": "혼돈의 미궁", "reward": "5000G, 거친 사자갈기, 미약한 힘이 담긴 영혼"},
        {"name": "윌시의 파괴자 울라프", "location": [4, 70, 23], "region": "피엄닉 불모지", "reward": "5000G, 선봉장의 허리띠, 미약한 힘이 담긴 영혼"},
        {"name": "철혈의 심판자 타르콘", "location": [197, 73, 33], "region": "심판의 보루", "reward": "5500G, 망치자루, 미약한 힘이 담긴 영혼"},
        {"name": "악마 기사 베아르논", "location": [-654, 69, 217], "region": "파멸의 선봉대", "reward": "5500G, 번개조각, 미약한 힘이 담긴 영혼"},
        {"name": "심연의 기사 아르반델", "location": [-335, 72, -65], "region": "망각의 성채", "reward": "5500G, 심연을 비추는 등불, 미약한 힘이 담긴 영혼"},
        {"name": "타락한 성직자 시네리아(심연을 걷는자)", "location": [-117, 67, 978], "region": "그림자 예배당", "reward": "6000G, 부러진 낫, 미약한 힘이 담긴 영혼"},
        {"name": "꽃의 왈츠 플뢰리스", "location": [-340, 70, 950], "region": "가시 장미 정원", "reward": "6000G, 끝없는 개화, 미약한 힘이 담긴 영혼", "notes": "y좌표 임시"},
        {"name": "비열한 그림자 셀렌", "location": [556, 72, 113], "region": "침묵의 회랑", "reward": "6000G, 목공 도구, 미약한 힘이 담긴 영혼", "notes": ""},
        {"name": "폭풍의 창 오닉스", "location": [336, 70, 248], "region": "꿰뚫는 폭퐁의 눈", "reward": "5000G, 꺽여버린 창, 미약한 힘이 담긴 영혼", "notes": ""},
        {"name": "저주 설계자 모르모트", "location": [-226, 72, 369], "region": "공허의 전당", "reward": "5000G, 공허한 운석, 미약한 힘이 담긴 영혼", "notes": ""},
        {"name": "키메라워리어", "location": [-158, 73, 33], "region": "혼동의 미궁", "reward": "", "notes": "사자혼종에서 변경된 보스"},
        {"name": "", "location": [199 , 70, 73], "region": "파편의 보루 던전", "reward": "", "notes": ""},
        {"name": "새벽을 가르는 자 엘리나", "location": [903, 68, 381], "region": "여명의 경계 던전", "reward": "", "notes": ""},
    ],
    "npcs": [
        {"name": "정수 상인", "location": [-4077, 72, 78], "notes": ""},
        {"name": "아이벨, 파르티오", "location": [2550, 86, -1011], "notes": ""},
        {"name": "샤벨", "location": [2774, 106, -940], "notes": ""},
        {"name": "잡화 상점 글리아", "location": [2660, 72, -756], "notes": ""},
        {"name": "농작물 상인", "location": [2699, 84, -1013]},
        {"name": "잡화 상인", "location": [2754, 72, -1001]},
        {"name": "광물 상인", "location": [2741, 69, -1001]},
        {"name": "정보 상인", "location": [2755, 73, -1015]},
        {"name": "낚시 상인", "location": [2757, 71, -986]},
        {"name": "연금 npc", "location": [2932, 87, -957], "notes": "닐란"},
        {"name": "우편 npc", "location": [2667, 103, -1071], "notes": "메이"},
        {"name": "기부 npc", "location": [2816, 129, -1355], "notes": "세르카"},
        {"name": "제작 npc", "location": [2625, 122, -1319], "notes": "드반"},
        {"name": "강화 npc", "location": [2625, 122, -1319], "notes": "브렌"},
        {"name": "룬감정 npc", "location": [2861, 94, -1070], "notes": "파이렌"},
        {"name": "잡화 상인", "location": [1312, 14, -860], "notes": "타룬"}
    ],
    "teleports": [
        {"name": "루네아 기사단 앞 길목", "location": [2661, 122, -1330], "region_type": "마을"},
        {"name": "루네아 중앙 분수", "location": [2900, 84, -940], "region_type": "마을"},
        {"name": "루네아 상점가", "location": [2760, 72, -1062], "region_type": "마을"},
        {"name": "루네아 마법의 섬", "location": [2903, 84, -943], "region_type": "마을"},
        {"name": "루네아 대형분수", "location": [2660, 104, -1084], "region_type": "마을"},
        {"name": "키나르 마을 중앙", "location": [1290, 14, -874], "region_type": "던전"},
        {"name": "타룬 황국지대 남부", "location": [1446, 11, -623], "region_type": "던전"},
        {"name": "타룬 황국지대 북쪽", "location": [1178, 9, -1245], "region_type": "던전"},
        {"name": "글리야 마을 중앙", "location": [20, 90, 332], "region_type": "던전"},
        {"name": "글리야 마을 동쪽", "location": [428, 71, 395], "region_type": "던전"},
        {"name": "글리야 마을 남쪽", "location": [140, 70, 774], "region_type": "던전"},
        {"name": "글리야 마을 북동쪽", "location": [246, 68, 115], "region_type": "던전"},
        {"name": "글리야 마을 북서쪽", "location": [-235, 71, 29], "region_type": "던전"}
    ],
    "Dungeon Boys": [
        {"name": "임시 주성", "location": [111, 111, 111]},
    ],
    "Wasobeso": [
        {"name": "임시 주성", "location": [222, 222, 222]},
    ],
    "Tangled Dahye": [
        {"name": "임시 주성", "location": [333, 333, 333]},
    ]
}


# ------------------ 거리 계산 ------------------
def get_nearest_teleport(location, teleports):
    def euclidean(a, b):
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))
    nearest = min(teleports, key=lambda t: euclidean(t["location"], location))
    return nearest, round(euclidean(nearest["location"], location))

# ------------------ 검색 기능 ------------------
def search_data(keyword, data):
    keyword = keyword.strip().lower()
    results = {"던전": [], "NPC": [], "텔레포트": []}

    for npc in data["npcs"]:
        npc_region = npc.get("region", "")
        if keyword in npc["name"].lower() or keyword in npc.get("notes", "").lower() or keyword in npc_region.lower() or keyword == "":
... (281줄 남음)
접기
message.txt
22KB
﻿
import streamlit as st
import math
import pandas as pd
import plotly.graph_objects as go



# ------------------ 데이터 정의 ------------------
data = {
    "dungeons": [
        {"name": "수호기사 클로스", "location": [1370, 46, -1030], "region": "", "reward": ""},
        {"name": "슬라임 킹", "location": [1214, 10, -600], "region": "", "reward": ""},
        {"name": "변이된 언데드", "location": [1702, 10, -870], "region": "오염된 땅", "reward": ""},
        {"name": "슬라임 기사", "location": [1632, 10, -690], "region": "끈적이는 땅", "reward": ""},
        {"name": "란", "location": [1154, 9, -1340], "region": "", "reward": "2000G"},
        {"name": "변이된 스켈레톤", "location": [1290, 22, -1380], "region": "", "reward": "2000G"},
        {"name": "말괄량이 마법사 데이비", "location": [1050, 10, -1155], "region": "", "reward": ""},
        {"name": "전사 브루스", "location": [1110, 75, -1214], "region": "낡은 검의 은신처", "reward": "3000G"},
        {"name": "펜리르", "location": [1180, 75, -1130], "region": "고독한 늑대의 요람", "reward": "5000G, 영험한 힘이 깃든 늑대 이빨, 미약한 힘이 담긴 영혼"},
        {"name": "슬라임 퀸", "location": [1355, 70, -1114], "region": "부패의 모체", "reward": "3000G, 슬라임 퀸의 핵"},
        {"name": "포레스트 골렘", "location": [1100, 78, -1100], "region": "대자연의 수호전", "reward": "3000G, 골렘의 핵"},
        {"name": "흑량", "location": [1630, 81, -690], "region": "잿빛 사냥꾼의 영역", "reward": "3000G,  검은 이리 가죽"},
        {"name": "고블린 라이더 & 와일드 보어 킹", "location": [1660, 69, -1200], "region": "야만의 군체", "reward": "3000G, 고블린라이더의 깃발"},
        {"name": "야만 전사 헬턴", "location": [1532, 16, -790], "region": "야만의 격전지", "reward": "3000G, 야만전사 도끼"},
        {"name": "침묵의 검무 키에린", "location": [114, 67, 611], "region": "저무는 칼날의 길", "reward": "5000G, 검의 인식처, 미약한 힘이 담긴 영혼"},
        {"name": "봉인된 문장 그린힐름", "location": [-472, 71, 502], "region": "봉인된 성소", "reward": "5000G, 페데도트의 문장, 미약한 힘이 담긴 영혼"},
        {"name": "사자혼종", "location": [-160, 69, 74], "region": "혼돈의 미궁", "reward": "5000G, 거친 사자갈기, 미약한 힘이 담긴 영혼"},
        {"name": "윌시의 파괴자 울라프", "location": [4, 70, 23], "region": "피엄닉 불모지", "reward": "5000G, 선봉장의 허리띠, 미약한 힘이 담긴 영혼"},
        {"name": "철혈의 심판자 타르콘", "location": [197, 73, 33], "region": "심판의 보루", "reward": "5500G, 망치자루, 미약한 힘이 담긴 영혼"},
        {"name": "악마 기사 베아르논", "location": [-654, 69, 217], "region": "파멸의 선봉대", "reward": "5500G, 번개조각, 미약한 힘이 담긴 영혼"},
        {"name": "심연의 기사 아르반델", "location": [-335, 72, -65], "region": "망각의 성채", "reward": "5500G, 심연을 비추는 등불, 미약한 힘이 담긴 영혼"},
        {"name": "타락한 성직자 시네리아(심연을 걷는자)", "location": [-117, 67, 978], "region": "그림자 예배당", "reward": "6000G, 부러진 낫, 미약한 힘이 담긴 영혼"},
        {"name": "꽃의 왈츠 플뢰리스", "location": [-340, 70, 950], "region": "가시 장미 정원", "reward": "6000G, 끝없는 개화, 미약한 힘이 담긴 영혼", "notes": "y좌표 임시"},
        {"name": "비열한 그림자 셀렌", "location": [556, 72, 113], "region": "침묵의 회랑", "reward": "6000G, 목공 도구, 미약한 힘이 담긴 영혼", "notes": ""},
        {"name": "폭풍의 창 오닉스", "location": [336, 70, 248], "region": "꿰뚫는 폭퐁의 눈", "reward": "5000G, 꺽여버린 창, 미약한 힘이 담긴 영혼", "notes": ""},
        {"name": "저주 설계자 모르모트", "location": [-226, 72, 369], "region": "공허의 전당", "reward": "5000G, 공허한 운석, 미약한 힘이 담긴 영혼", "notes": ""},
        {"name": "키메라워리어", "location": [-158, 73, 33], "region": "혼동의 미궁", "reward": "", "notes": "사자혼종에서 변경된 보스"},
        {"name": "", "location": [199 , 70, 73], "region": "파편의 보루 던전", "reward": "", "notes": ""},
        {"name": "새벽을 가르는 자 엘리나", "location": [903, 68, 381], "region": "여명의 경계 던전", "reward": "", "notes": ""},
    ],
    "npcs": [
        {"name": "정수 상인", "location": [-4077, 72, 78], "notes": ""},
        {"name": "아이벨, 파르티오", "location": [2550, 86, -1011], "notes": ""},
        {"name": "샤벨", "location": [2774, 106, -940], "notes": ""},
        {"name": "잡화 상점 글리아", "location": [2660, 72, -756], "notes": ""},
        {"name": "농작물 상인", "location": [2699, 84, -1013]},
        {"name": "잡화 상인", "location": [2754, 72, -1001]},
        {"name": "광물 상인", "location": [2741, 69, -1001]},
        {"name": "정보 상인", "location": [2755, 73, -1015]},
        {"name": "낚시 상인", "location": [2757, 71, -986]},
        {"name": "연금 npc", "location": [2932, 87, -957], "notes": "닐란"},
        {"name": "우편 npc", "location": [2667, 103, -1071], "notes": "메이"},
        {"name": "기부 npc", "location": [2816, 129, -1355], "notes": "세르카"},
        {"name": "제작 npc", "location": [2625, 122, -1319], "notes": "드반"},
        {"name": "강화 npc", "location": [2625, 122, -1319], "notes": "브렌"},
        {"name": "룬감정 npc", "location": [2861, 94, -1070], "notes": "파이렌"},
        {"name": "잡화 상인", "location": [1312, 14, -860], "notes": "타룬"}
    ],
    "teleports": [
        {"name": "루네아 기사단 앞 길목", "location": [2661, 122, -1330], "region_type": "마을"},
        {"name": "루네아 중앙 분수", "location": [2900, 84, -940], "region_type": "마을"},
        {"name": "루네아 상점가", "location": [2760, 72, -1062], "region_type": "마을"},
        {"name": "루네아 마법의 섬", "location": [2903, 84, -943], "region_type": "마을"},
        {"name": "루네아 대형분수", "location": [2660, 104, -1084], "region_type": "마을"},
        {"name": "키나르 마을 중앙", "location": [1290, 14, -874], "region_type": "던전"},
        {"name": "타룬 황국지대 남부", "location": [1446, 11, -623], "region_type": "던전"},
        {"name": "타룬 황국지대 북쪽", "location": [1178, 9, -1245], "region_type": "던전"},
        {"name": "글리야 마을 중앙", "location": [20, 90, 332], "region_type": "던전"},
        {"name": "글리야 마을 동쪽", "location": [428, 71, 395], "region_type": "던전"},
        {"name": "글리야 마을 남쪽", "location": [140, 70, 774], "region_type": "던전"},
        {"name": "글리야 마을 북동쪽", "location": [246, 68, 115], "region_type": "던전"},
        {"name": "글리야 마을 북서쪽", "location": [-235, 71, 29], "region_type": "던전"}
    ],
    "Dungeon Boys": [
        {"name": "임시 주성", "location": [111, 111, 111]},
    ],
    "Wasobeso": [
        {"name": "임시 주성", "location": [222, 222, 222]},
    ],
    "Tangled Dahye": [
        {"name": "임시 주성", "location": [333, 333, 333]},
    ]
}


# ------------------ 거리 계산 ------------------
def get_nearest_teleport(location, teleports):
    def euclidean(a, b):
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))
    nearest = min(teleports, key=lambda t: euclidean(t["location"], location))
    return nearest, round(euclidean(nearest["location"], location))

# ------------------ 검색 기능 ------------------
def search_data(keyword, data):
    keyword = keyword.strip().lower()
    results = {"던전": [], "NPC": [], "텔레포트": []}

    for npc in data["npcs"]:
        npc_region = npc.get("region", "")
        if keyword in npc["name"].lower() or keyword in npc.get("notes", "").lower() or keyword in npc_region.lower() or keyword == "":
            nearest, dist = get_nearest_teleport(npc["location"], data["teleports"])
            results["NPC"].append({**npc, "type": "NPC", "nearest_tp": nearest, "dist": dist})

    for d in data["dungeons"]:
        if keyword in d["name"].lower() or keyword in d["region"].lower() or keyword in d["reward"].lower() or keyword == "":
            nearest, dist = get_nearest_teleport(d["location"], data["teleports"])
            results["던전"].append({**d, "type": "던전", "nearest_tp": nearest, "dist": dist})

    for tp in data["teleports"]:
        if keyword in tp["name"].lower() or keyword in tp.get("region_type", "").lower() or keyword == "":
            results["텔레포트"].append({**tp, "type": "텔레포트"})

    return results

# ------------------ 지도 기능 ------------------
def plot_virtual_map_interactive(data, mode="normal"):
    fig = go.Figure()

    if mode == "normal":
        show_dungeon = st.sidebar.checkbox("던전 표시", value=True)
        show_npc = st.sidebar.checkbox("NPC 표시", value=True)
        show_tp = st.sidebar.checkbox("텔레포트 표시", value=True)

        if show_dungeon:
            dungeon_names = [d["name"] for d in data["dungeons"]]
            selected_dungeons = []
            with st.sidebar.expander("던전 목록", expanded=False):
                toggle_dungeon_names = st.checkbox("던전 이름 전체 표시 ON/OFF", value=True, key="toggle_dungeon_names")
                for i, name in enumerate(dungeon_names):
                    checked = st.checkbox(f"{name}", key=f"dungeon_{i}_{name}", value=toggle_dungeon_names)
                    if checked:
                        selected_dungeons.append(name)

            df_dungeon = pd.DataFrame([
                {"이름": d["name"], "X": d["location"][0], "Y": d["location"][1], "Z": d["location"][2],
                 "지역": d["region"], "보상": d["reward"]}
                for d in data["dungeons"]
            ])
            fig.add_trace(go.Scatter(
                x=df_dungeon["X"], y=df_dungeon["Z"], mode="markers+text", name="던전",
                marker=dict(color="red", size=8),
                text=df_dungeon["이름"].where(df_dungeon["이름"].isin(selected_dungeons), ""),
                textposition="top center",
                customdata=df_dungeon[["X", "Y", "Z", "이름", "지역", "보상"]],
                hovertemplate="X=%{customdata[0]}<br>Y=%{customdata[1]}<br>Z=%{customdata[2]}<br>"
                              "이름=%{customdata[3]}<br>지역=%{customdata[4]}<br>보상=%{customdata[5]}"
            ))

        if show_npc:
            npc_names = [n["name"] for n in data["npcs"]]
            selected_npcs = []
            with st.sidebar.expander("NPC 목록", expanded=False):
                toggle_npc_names = st.checkbox("NPC 이름 전체 표시 ON/OFF", value=True, key="toggle_npc_names")
                for i, name in enumerate(npc_names):
                    checked = st.checkbox(f"{name}", key=f"npc_{i}_{name}", value=toggle_npc_names)
                    if checked:
                        selected_npcs.append(name)

            df_npc = pd.DataFrame([
                {"이름": n["name"], "X": n["location"][0], "Y": n["location"][1], "Z": n["location"][2],
                 "비고": n.get("notes", "")}
                for n in data["npcs"]
            ])
            fig.add_trace(go.Scatter(
                x=df_npc["X"], y=df_npc["Z"], mode="markers+text", name="NPC",
                marker=dict(color="yellow", size=8),
                text=df_npc["이름"].where(df_npc["이름"].isin(selected_npcs), ""),
                textposition="top center",
                customdata=df_npc[["X", "Y", "Z", "이름", "비고"]],
                hovertemplate="X=%{customdata[0]}<br>Y=%{customdata[1]}<br>Z=%{customdata[2]}<br>"
                              "이름=%{customdata[3]}<br>비고=%{customdata[4]}"
            ))

        if show_tp:
            df_tp = pd.DataFrame([
                {"이름": tp["name"], "X": tp["location"][0], "Y": tp["location"][1], "Z": tp["location"][2],
                 "지역구분": tp["region_type"]}
                for tp in data["teleports"]
            ])
            tp_names = df_tp["이름"].tolist()
            selected_tps = []
            with st.sidebar.expander("텔레포트 목록", expanded=False):
                toggle_tp_names = st.checkbox("텔레포트 이름 전체 표시 ON/OFF", value=True, key="toggle_tp_names")
                for i, name in enumerate(tp_names):
                    checked = st.checkbox(f"{name}", key=f"tp_{i}_{name}", value=toggle_tp_names)
                    if checked:
                        selected_tps.append(name)
            fig.add_trace(go.Scatter(
                x=df_tp["X"], y=df_tp["Z"], mode="markers+text", name="텔레포트",
                marker=dict(color="purple", size=8),
                text=df_tp["이름"].where(df_tp["이름"].isin(selected_tps), ""),
                textposition="top center",
                customdata=df_tp[["X", "Y", "Z", "이름", "지역구분"]],
                hovertemplate="X=%{customdata[0]}<br>Y=%{customdata[1]}<br>Z=%{customdata[2]}<br>"
                              "이름=%{customdata[3]}<br>지역구분=%{customdata[4]}"
            ))

    elif mode == "war":
        war_categories = [
            ("Dungeon Boys", "던전보이즈", "green"),
            ("Wasobeso", "와쏘베쏘", "blue"),
            ("Tangled Dahye", "탱글다혜", "brown")
        ]
    
        with st.sidebar.expander("전쟁 지도 표시 옵션", expanded=True):
            show_war_names_toggle = st.checkbox("이름 전체 표시 ON/OFF", value=True, key="toggle_war_names")

        for data_key, display_name, color in war_categories:
            if data_key in data:
                df = pd.DataFrame([
                    {"이름": item["name"], "X": item["location"][0], "Y": item["location"][1], "Z": item["location"][2]}
                    for item in data[data_key]
                ])
    
                # 체크박스 UI
                selected_names = []
                with st.sidebar.expander(f"{display_name} 목록", expanded=False):
                    for i, name in enumerate(df["이름"]):
                        checked = st.checkbox(f"{name}", key=f"war_{data_key}_{i}", value=show_war_names_toggle)
                        if checked:
                            selected_names.append(name)
    
                # 마커 표시
                fig.add_trace(go.Scatter(
                    x=df["X"], y=df["Z"], mode="markers+text", name=display_name,
                    marker=dict(color=color, size=8),
                    text=df["이름"].where(df["이름"].isin(selected_names), ""),
                    textposition="top center",
                    customdata=df[["X", "Y", "Z", "이름"]],
                    hovertemplate="X=%{customdata[0]}<br>Y=%{customdata[1]}<br>"
                                  "Z=%{customdata[2]}<br>이름=%{customdata[3]}"
                ))

  
        df_tp = pd.DataFrame([
            {"이름": tp["name"], "X": tp["location"][0], "Y": tp["location"][1], "Z": tp["location"][2],
             "지역구분": tp["region_type"]}
            for tp in data["teleports"]
        ])
        tp_names = df_tp["이름"].tolist()
        selected_tps = []
        with st.sidebar.expander("텔레포트 목록", expanded=False):
            toggle_tp_names = st.checkbox("텔레포트 이름 전체 표시 ON/OFF", value=True, key="toggle_war_tp_names")
            for i, name in enumerate(tp_names):
                checked = st.checkbox(f"{name}", key=f"war_tp_{i}", value=toggle_tp_names)
                if checked:
                    selected_tps.append(name)

        fig.add_trace(go.Scatter(
            x=df_tp["X"], y=df_tp["Z"], mode="markers+text", name="텔레포트",
            marker=dict(color="purple", size=8),
            text=df_tp["이름"].where(df_tp["이름"].isin(selected_tps), ""),
            textposition="top center",
            customdata=df_tp[["X", "Y", "Z", "이름", "지역구분"]],
            hovertemplate="X=%{customdata[0]}<br>Y=%{customdata[1]}<br>"
                          "Z=%{customdata[2]}<br>이름=%{customdata[3]}<br>지역구분=%{customdata[4]}"
        ))

    if not fig.data:
        st.warning("표시할 데이터가 없습니다.")
        return

    fig.update_layout(height=700, dragmode="pan")
    st.plotly_chart(fig, use_container_width=True, config={"scrollZoom": True})

# ------------------ Streamlit ------------------
st.set_page_config(layout="wide")
st.sidebar.title("메뉴")

tab_option = st.sidebar.radio("탭 선택", ["검색기능", "카테고리", "좌표 검색", "가상 지도", "전쟁지도"])

# ------------------ 검색 탭 ------------------
if tab_option == "검색기능":
    st.title("룬제로 검색기")

    if "keyword" not in st.session_state:
        st.session_state["keyword"] = ""
    if "search_triggered" not in st.session_state:
        st.session_state["search_triggered"] = False
    if "show_all" not in st.session_state:
        st.session_state["show_all"] = False

    def trigger_search():
        st.session_state["search_triggered"] = True
        st.session_state["show_all"] = False

    def show_all_items():
        st.session_state["keyword"] = ""
        st.session_state["search_triggered"] = False
        st.session_state["show_all"] = True

    col_input, col_button = st.columns([5, 1])
    with col_input:
        st.text_input("검색어", key="keyword", placeholder="검색어 입력 후 엔터", on_change=trigger_search)
    with col_button:
        st.markdown(" ")
        st.markdown(" ")
        st.button("검색", on_click=trigger_search)

    st.button("모든 항목 보기", on_click=show_all_items)

    if st.session_state.search_triggered or st.session_state.show_all:
        results = search_data(st.session_state["keyword"], data)
        total = sum(len(results[k]) for k in results)
        st.info(f"총 {total}개 결과")

        for category in ["던전", "NPC", "텔레포트"]:
            if results[category]:
                st.subheader(category)
                for item in results[category]:
                    st.markdown(f"### [{item['type']}] {item['name']}")
                    st.write(f"위치: {item['location']}")
                    if item["type"] == "던전":
                        st.write(f"지역: {item['region']}")
                        st.write(f"보상: {item['reward']}")
                        st.write(f"가장 가까운 텔레포트: {item['nearest_tp']['name']} ({item['nearest_tp']['region_type']}) - {item['dist']}m")
                    elif item["type"] == "NPC":
                        if item.get("notes"):
                            st.write(f"비고: {item['notes']}")
                        st.write(f"가장 가까운 텔레포트: {item['nearest_tp']['name']} ({item['nearest_tp']['region_type']}) - {item['dist']}m")
                    elif item["type"] == "텔레포트":
                        st.write(f"지역 구분: {item['region_type']}")
                    st.markdown("---")

        st.session_state["search_triggered"] = False

# ------------------ 카테고리 탭 ------------------
elif tab_option == "카테고리":
    st.title("카테고리 보기")
    category = st.radio("카테고리 선택", ["던전", "재료"])

    if category == "던전":
        for dungeon in data["dungeons"]:
            with st.expander(dungeon["name"]):
                st.write(f"위치: {dungeon['location']}")
                st.write(f"지역: {dungeon['region']}")
                st.write(f"보상: {dungeon['reward']}")

    elif category == "재료":
        reward_set = set()
        for dungeon in data["dungeons"]:
            for reward in dungeon["reward"].split(","):
                reward = reward.strip()
                if reward and not reward.endswith("G"):
                    reward_set.add(reward)
        for reward in sorted(reward_set):
            with st.expander(reward):
                related = [d for d in data["dungeons"] if reward in d["reward"]]
                for d in related:
                    st.write(f"- {d['name']} @ {d['region']}")

# ------------------ 좌표 기반 탭 ------------------
elif tab_option == "좌표 검색":
    st.title("좌표 기반 텔레포트 찾기")

    x = st.number_input("X 좌표", value=0)
    y = st.number_input("Y 좌표", value=0)
    z = st.number_input("Z 좌표", value=0)

    if st.button("가까운 텔레포트 찾기"):
        location = [x, y, z]
        nearest, dist = get_nearest_teleport(location, data["teleports"])
        st.success(f"가장 가까운 텔레포트는 **{nearest['name']}** ({nearest['region_type']}) - {dist}m")

# ------------------ 가상 지도 탭 ------------------
elif tab_option == "가상 지도":
    st.title("가상 지도")
    plot_virtual_map_interactive(data)

elif tab_option == "전쟁지도":
    st.title("전쟁지도")
    plot_virtual_map_interactive(data, mode="war")

