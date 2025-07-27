import streamlit as st
import math

# ------------------ 데이터 정의 ------------------
data = {
    "dungeons": [
        {"name": "수호기사 클로스", "location": [1370, 46, -1030], "region": "", "reward": ""},
        {"name": "슬라임 킹", "location": [1214, 10, -600], "region": "", "reward": ""},
        {"name": "변이된 언데드", "location": [1702, 10, -870], "region": "오염된 땅", "reward": ""},
        {"name": "슬라임 기사", "location": [1632, 10, -690], "region": "끈적이는 땅", "reward": ""},
        {"name": "란", "location": [1154, 9, -1340], "region": "", "reward": "2,000 G"},
        {"name": "변이된 스켈레톤", "location": [1290, 22, -1380], "region": "", "reward": "2,000 G"},
        {"name": "말괄량이 마법사 데이비", "location": [1050, 10, -1155], "region": "", "reward": ""},
        {"name": "전사 브루스", "location": [1110, 75, -1214], "region": "낡은 검의 은신처", "reward": "3,000 G"},
        {"name": "펜리르", "location": [1180, 75, -1130], "region": "고독한 늑대의 요람", "reward": "5,000 G, 영험한 힘이 깃든 늑대 이빨, 미약한 힘이 담긴 영혼"},
        {"name": "슬라임 퀸", "location": [1355, 70, -1114], "region": "부패의 모체", "reward": "3,000 G, 슬라임 퀸의 핵"},
        {"name": "포레스트 골렘", "location": [1100, 78, -1100], "region": "대자연의 수호전", "reward": "3,000 G, 골렘의 핵"},
        {"name": "야만의 군체", "location": [-1600, 0, -1197], "region": "", "reward": ""},
        {"name": "흑량", "location": [1630, 81, -690], "region": "잿빛 사냥꾼의 영역", "reward": "3,000 G,  검은 이리 갑주"},
        {"name": "고블린 라이더 & 와일드 보어 킹", "location": [1660, 69, -1200], "region": "야만의 군체", "reward": "3,000 G, 고블린라이더의 깃발"},
        {"name": "야만 전사 헬턴", "location": [1532, 16, -790], "region": "야만의 격전지", "reward": "3,000 G, 야만전사 도끼"},
        {"name": "침묵의 검무 키에린", "location": [114, 67, 611], "region": "저무는 칼날의 길", "reward": "5,000 G, 검의 인식처, 미약한 힘이 담긴 영혼"},
        {"name": "봉인된 문장 그린힐름", "location": [-472, 71, 502], "region": "봉인된 성소", "reward": "5,000 G, 페데도트의 문장, 미약한 힘이 담긴 영혼"},
        {"name": "사자혼종", "location": [-160, 69, 74], "region": "혼돈의 미궁", "reward": "5,000 G, 거친 사자갈기, 미약한 힘이 담긴 영혼"},
        {"name": "윌시의 파괴자 울라프", "location": [4, 70, 23], "region": "피엄닉 불모지", "reward": "5,000 G, 선봉장의 허리띠, 미약한 힘이 담긴 영혼"},
        {"name": "철혈의 심판자 타르콘", "location": [197, 73, 33], "region": "심판의 보루", "reward": "5,500 G, 망치자루, 미약한 힘이 담긴 영혼"},
        {"name": "악마 기사 베아르논", "location": [-654, 69, 217], "region": "파멸의 선봉대", "reward": "5,500 G, 번개조각, 미약한 힘이 담긴 영혼"},
        {"name": "심연의 기사 아르반델", "location": [-335, 72, -65], "region": "망각의 성채", "reward": "5,500 G, 심연을 비추는 등불, 미약한 힘이 담긴 영혼"},
        {"name": "타락한 성직자 시네리아(심연을 걷는자)", "location": [-117, 67, 978], "region": "그림자 예배당", "reward": "6,000 G, 부러진 낫, 미약한 힘이 담긴 영혼"},
        {"name": "꽃의 왈츠 플뢰리스", "location": [-340, 70, 950], "region": "가시 장미 정원", "reward": "6,000 G, 끝없는 개화, 미약한 힘이 담긴 영혼", "notes": "y좌표 임시"},
        {"name": "비열한 그림자 셀렌", "location": [556, 72, 113], "region": "침묵의 회랑", "reward": "6,000 G, 목공 도구, 미약한 힘이 담긴 영혼", "notes": ""},
        {"name": "폭풍의 창 오닉스", "location": [336, 70, 248], "region": "꿰뚫는 폭퐁의 눈", "reward": "5,000 G, 꺽여버린 창, 미약한 힘이 담긴 영혼", "notes": ""},
        {"name": "저주 설계자 모르모트", "location": [-226, 72, 369], "region": "공허의 전당", "reward": "5,000 G, 공허한 운석", "notes": ""},
        {"name": "키메라워리어", "location": [-158, 70, 73], "region": "혼동의 미궁", "reward": "", "notes": "사자혼종에서 변경된 보스"},
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
    ]
}


# ------------------ 거리 계산 함수 ------------------
def get_nearest_teleport(target_location):
    def euclidean(loc1, loc2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(loc1, loc2)))
    nearest = min(data["teleports"], key=lambda t: euclidean(t["location"], target_location))
    return nearest, round(euclidean(nearest["location"], target_location))

# ------------------ 검색 함수 ------------------
def search_data(keyword):
    keyword = keyword.strip().lower()
    results = {"던전": [], "NPC": [], "텔레포트": []}

    for npc in data["npcs"]:
        if keyword in npc["name"].lower() or keyword in npc.get("notes", "").lower() or keyword == "":
            nearest, dist = get_nearest_teleport(npc["location"])
            results["NPC"].append({
                "type": "NPC",
                "name": npc["name"],
                "location": npc["location"],
                "notes": npc.get("notes", ""),
                "nearest_tp": nearest,
                "dist": dist
            })

    for d in data["dungeons"]:
        if keyword in d["name"].lower() or keyword in d["region"].lower() or keyword in d["reward"].lower() or keyword == "":
            nearest, dist = get_nearest_teleport(d["location"])
            results["던전"].append({
                "type": "던전",
                "name": d["name"],
                "location": d["location"],
                "region": d["region"],
                "reward": d["reward"],
                "nearest_tp": nearest,
                "dist": dist
            })

    for tp in data["teleports"]:
        if keyword in tp["name"].lower() or keyword in tp["region_type"].lower() or keyword == "":
            results["텔레포트"].append({
                "type": "텔레포트",
                "name": tp["name"],
                "location": tp["location"],
                "region_type": tp["region_type"]
            })

    return results

# ------------------ 상태 초기화 ------------------
if "keyword" not in st.session_state:
    st.session_state["keyword"] = ""
if "search_triggered" not in st.session_state:
    st.session_state["search_triggered"] = False

# ------------------ 검색 트리거 함수 ------------------
def trigger_search():
    st.session_state["search_triggered"] = True
    
# ------------------ Streamlit UI ------------------
import streamlit as st

st.set_page_config(layout="wide")

if "keyword" not in st.session_state:
    st.session_state["keyword"] = ""
if "search_triggered" not in st.session_state:
    st.session_state["search_triggered"] = False

def trigger_search():
    st.session_state["search_triggered"] = True


left, center, right = st.columns([1, 2, 1])

with center:

    st.markdown("<h1 style='text-align: center;'>룬제로 검색기</h1>", unsafe_allow_html=True)

    st.markdown("**검색어를 입력하세요 (엔터 또는 검색 버튼)**")
    
    input_col, button_col = st.columns([5, 1]) 
    with input_col:
        st.text_input(
            label="검색어", 
            key="keyword", 
            label_visibility="collapsed", 
            on_change=trigger_search
        )
    with button_col:
        st.button("검색", on_click=trigger_search)

    st.button("모든 항목 보기", key="show_all", on_click=lambda: setattr(st.session_state, "keyword", ""))


if st.session_state.search_triggered or st.session_state.keyword == "":
    keyword = st.session_state.keyword
    results = search_data(keyword)
    total_count = sum(len(lst) for lst in results.values())

    with center:
        st.info(f"총 {total_count}개 결과가 검색되었습니다.")

        for category in ["던전", "NPC", "텔레포트"]:
            if results[category]:
                st.markdown(f"## {category}")
                for res in results[category]:
                    st.markdown(f"### [{res['type']}] {res['name']}")
                    st.code(f"{res['name']} @ {res['location']}")
                    st.write(f"위치: {res['location']}")

                    if res["type"] == "NPC":
                        if res.get("notes"):
                            st.write(f"비고: {res['notes']}")
                        st.write(
                            f"가장 가까운 텔레포트: **{res['nearest_tp']['name']}** "
                            f"({res['nearest_tp']['region_type']}) - {res['dist']}m"
                        )

                    elif res["type"] == "던전":
                        st.write(f"지역: {res['region']}")
                        st.write(f"보상: {res['reward']}")
                        st.write(
                            f"가장 가까운 텔레포트: **{res['nearest_tp']['name']}** "
                            f"({res['nearest_tp']['region_type']}) - {res['dist']}m"
                        )

                    elif res["type"] == "텔레포트":
                        st.write(f"지역 구분: {res['region_type']}")

                    st.markdown("---")

    st.session_state.search_triggered = False

