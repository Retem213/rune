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
        {"name": "야만의 군체", "location": [-1600, 0, -1197], "region": "", "reward": "3,000 G, 부러진 대검"},
        {"name": "흑량", "location": [1630, 81, -690], "region": "잿빛 사냥꾼의 영역", "reward": "3,000 G,  검은 이리 가죽"},
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
        {"name": "저주 설계자 모르모트", "location": [-226, 72, 369], "region": "공허의 전당", "reward": "5,000 G, 공허한 운석, 미약한 힘이 담긴 영혼", "notes": ""},
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



# ------------------ 거리 계산 ------------------
def get_nearest_teleport(location, teleports):
    def euclidean(a, b):
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))
    nearest = min(teleports, key=lambda t: euclidean(t["location"], location))
    return nearest, round(euclidean(nearest["location"], location))


# ------------------ 보상 재료 리스트 추출 ------------------
def extract_unique_rewards(dungeons):
    all_rewards = []
    for d in dungeons:
        rewards = d.get("reward", "").split(",")
        for r in rewards:
            r = r.strip()
            if r and r not in all_rewards:
                all_rewards.append(r)
    return all_rewards


# ------------------ Streamlit 시작 ------------------
st.set_page_config(layout="wide")

# ------------------ 탭 분기 ------------------
st.sidebar.title("탐색 메뉴")
main_tab = st.sidebar.radio("탭 선택", ["카테고리", "좌표 검색"])


# ------------------ 카테고리 탭 ------------------
if main_tab == "카테고리":
    category = st.sidebar.radio("카테고리 선택", ["던전", "재료"])

    if category == "던전":
        dungeon_names = [d["name"] for d in data["dungeons"]]
        selected_name = st.sidebar.selectbox("던전을 선택하세요", dungeon_names)

        selected_dungeon = next((d for d in data["dungeons"] if d["name"] == selected_name), None)
        if selected_dungeon:
            st.header(f"[던전] {selected_dungeon['name']}")
            st.write(f"위치: {selected_dungeon['location']}")
            st.write(f"지역: {selected_dungeon.get('region', '')}")
            st.write(f"보상: {selected_dungeon.get('reward', '')}")
            if "notes" in selected_dungeon:
                st.write(f"비고: {selected_dungeon['notes']}")

            nearest_tp, dist = get_nearest_teleport(selected_dungeon["location"], data["teleports"])
            st.write(f"가장 가까운 텔레포트: **{nearest_tp['name']}** ({nearest_tp['region_type']}) - {dist}m")

    elif category == "재료":
        reward_items = extract_unique_rewards(data["dungeons"])
        selected_reward = st.sidebar.selectbox("재료를 선택하세요", reward_items)

        matched_dungeons = [d for d in data["dungeons"] if selected_reward in d.get("reward", "")]
        st.subheader(f"‘{selected_reward}’ 획득 가능한 던전")

        for d in matched_dungeons:
            st.markdown(f"### {d['name']}")
            st.write(f"위치: {d['location']}")
            st.write(f"지역: {d.get('region', '')}")
            st.write(f"보상: {d.get('reward', '')}")
            nearest_tp, dist = get_nearest_teleport(d["location"], data["teleports"])
            st.write(f"가장 가까운 텔레포트: **{nearest_tp['name']}** ({nearest_tp['region_type']}) - {dist}m")
            st.markdown("---")

# ------------------ 좌표 검색 탭 ------------------
elif main_tab == "좌표 검색":
    st.header("좌표 입력")
    x = st.number_input("X", step=1)
    y = st.number_input("Y", step=1)
    z = st.number_input("Z", step=1)

    if st.button("가장 가까운 텔레포트 찾기"):
        nearest_tp, dist = get_nearest_teleport([x, y, z], data["teleports"])
        st.success(f"가장 가까운 텔레포트는 **{nearest_tp['name']}** ({nearest_tp['region_type']}) - {dist}m")
        st.write(f"텔레포트 위치: {nearest_tp['location']}")


