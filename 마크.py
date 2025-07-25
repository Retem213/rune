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
        {"name": "타락한 성직자 시네리아(심연을 걷는자)", "location": [-117, 67, 978], "region": "그림자 예배당", "reward": "6,000 G, 부러진 낫, 미약한 힘이 담긴 영혼"}
    ],
    "npcs": [
        {"name": "정수 상인", "location": [-4077, 72, 78], "notes": "정수 15,000G 구매처"},
        {"name": "아이벨, 파르티오", "location": [2550, 86, -1011], "notes": "??? NPC"},
        {"name": "샤벨", "location": [2774, 106, -940], "notes": "??? NPC"},
        {"name": "잡화 상점 글리아", "location": [2660, 72, -756], "notes": "글리아 귀환석 판매"},
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
    distance = euclidean(nearest["location"], target_location)
    return nearest, round(distance)

# ------------------ 검색 기능 ------------------
def search_data(keyword):
    keyword = keyword.strip().lower()
    results = {
        "던전": [],
        "NPC": [],
        "텔레포트": []
    }

    for npc in data["npcs"]:
        name = npc["name"].lower()
        notes = npc.get("notes", "").lower()
        if keyword in name or keyword in notes or keyword == "":
            nearest_tp, dist = get_nearest_teleport(npc["location"])
            results["NPC"].append({
                "type": "NPC",
                "name": npc["name"],
                "location": npc["location"],
                "notes": npc.get("notes", ""),
                "nearest_tp": nearest_tp,
                "dist": dist
            })

    for d in data["dungeons"]:
        name = d["name"].lower()
        region = d["region"].lower()
        reward = d["reward"].lower()
        if keyword in name or keyword in region or keyword in reward or keyword == "":
            nearest_tp, dist = get_nearest_teleport(d["location"])
            results["던전"].append({
                "type": "던전",
                "name": d["name"],
                "location": d["location"],
                "region": d["region"],
                "reward": d["reward"],
                "nearest_tp": nearest_tp,
                "dist": dist
            })

    for tp in data["teleports"]:
        name = tp["name"].lower()
        region_type = tp["region_type"].lower()
        if keyword in name or keyword in region_type or keyword == "":
            results["텔레포트"].append({
                "type": "텔레포트",
                "name": tp["name"],
                "location": tp["location"],
                "region_type": tp["region_type"]
            })

    return results

# ------------------ UI ------------------
st.set_page_config(page_title="룬제로 검색기", layout="wide")
st.title("🔍 룬제로 검색기")

keyword = st.text_input("검색어를 입력하세요 (던전, 지역, 보상, NPC 등")

results = search_data(keyword)
total_count = sum(len(lst) for lst in results.values())

if keyword:
    st.info(f"🔎 총 {total_count}개의 결과가 검색되었습니다.")

    tabs = st.tabs(["🏰 던전", "🧙‍♂️ NPC", "🌀 텔레포트"])

    # 던전 탭
    with tabs[0]:
        if results["던전"]:
            for res in results["던전"]:
                with st.expander(f"[{res['type']}] {res['name']}"):
                    st.write(f"📍 위치: `{res['location']}`")
                    st.write(f"🌍 지역: `{res['region']}`")
                    st.write(f"🎁 보상: `{res['reward']}`")
                    st.write(f"🌀 가장 가까운 텔레포트: **{res['nearest_tp']['name']}** ({res['nearest_tp']['region_type']}) - {res['dist']}m")
        else:
            st.warning("결과가 없습니다.")

    # NPC 탭
    with tabs[1]:
        if results["NPC"]:
            for res in results["NPC"]:
                with st.expander(f"[{res['type']}] {res['name']}"):
                    st.write(f"📍 위치: `{res['location']}`")
                    if res.get("notes"):
                        st.write(f"📝 비고: `{res['notes']}`")
                    st.write(f"🌀 가장 가까운 텔레포트: **{res['nearest_tp']['name']}** ({res['nearest_tp']['region_type']}) - {res['dist']}m")
        else:
            st.warning("결과가 없습니다.")

    # 텔레포트 탭
    with tabs[2]:
        if results["텔레포트"]:
            for res in results["텔레포트"]:
                with st.expander(f"[{res['type']}] {res['name']}"):
                    st.write(f"📍 위치: `{res['location']}`")
                    st.write(f"🌍 지역 구분: `{res['region_type']}`")
        else:
            st.warning("결과가 없습니다.")
else:
    st.info("검색어를 입력하면 결과가 바로 나옵니다. ⌨️")

