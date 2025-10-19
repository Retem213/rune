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
        {"name": "천둥의 포효 드렌자르 던전", "location": [-238, 68, -125], "region": "폭풍 첨탑 성채", "reward": "6000G, 벽조목, 미약한 힘이 담긴 영혼", "notes": ""},
        {"name": "공허한 어둠 아벨", "location": [-32, 75, -188], "region": "암연의 응시", "reward": "7000G, 공허의 촉수, 미약한 힘이 담긴 영혼", "notes": ""},
        {"name": "새벽을 가르는 자 엘리나", "location": [903, 68, 381], "region": "여명의 경계 던전", "reward": "8000G, 응측된 힘이 담긴 영혼", "notes": ""},
        {"name": "부패한 사령 벨모라", "location": [-1365, 24, 1060], "region": "불길한 무덤", "reward": "8000G, 불길한 가죽책", "notes": ""},
        {"name": "황천의 심판자 아누비스", "location": [-1822, 68, 1560], "region": "사자의 서", "reward": "8000G, 심판의 추", "notes": ""},
        {"name": "사막의 무법자 타리크", "location": [-1599, 88, 1314], "region": "모래바람의 투기장", "reward": "푸른 머리띠", "notes": ""},
        {"name": "사막의 암살자 살라딘", "location": [-1327, 72, 1592], "region": "고요한 황무지", "reward": "8000G, 부러진 차그람", "notes": ""},
        {"name": "사막의 무희 살리나", "location": [-1260, 74, 1170], "region": "황폐한 땅", "reward": "7000G", "notes": ""},
        {"name": "피에 물든 파멸자 카르노스", "location": [-1481, 82, 665], "region": "혈혼의 맹세", "reward": "불길한 보석, 응축된 힘이 담긴 영혼", "notes": ""},
        {"name": "폭풍을 두른 자 매그니르", "location": [-1662, 77, 259], "region": "뇌운의 신전", "reward": "뇌운, 응축된 힘이 담긴 영혼, 매그니르 보상 상자", "notes": ""},
        {"name": "수확자 드렐리스", "location": [-2168, 82, 394], "region": "영혼의 들판", "reward": "낫 자루, 드렐리스 보상 상자, 응축된 힘이 담긴 영혼", "notes": ""},
        {"name": "용의 전사 드라코니스", "location": [-2290, 70, 611], "region": "용의 안식처", "reward": "드라코니스 보상 상자, 전설룬, 드래곤의 뿔", "notes": ""},
        {"name": "", "location": [1987, 102, -2249], "region": "마지막 섬광", "reward": "", "notes": ""},
    ],
    "npcs": [
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
        {"name": "글리야 마을 북서쪽", "location": [-235, 71, 29], "region_type": "던전"},
        {"name": "프론티아 마을 중앙", "location": [-1313, 77, 1854], "region_type": "마을"},
        {"name": "프론티아 마을 동쪽", "location": [-1048, 70, 1182], "region_type": "던전"},
        {"name": "프론티아 서쪽", "location": [-1976, 68, 1544], "region_type": "던전"},
        {"name": "프론티아 남쪽", "location": [-1976, 69, 1717], "region_type": "던전"},
        {"name": "프론티아 마을 북쪽", "location": [-2080, 73, 464], "region_type": "던전"},
        {"name": "???. 잊혀진 섬", "location": [2053, 137, -2438], "region_type": "던전"},
    ],
    "Dungeon Boys": [
        {"name": "주성", "location": [948, 80, -605]},
        {"name": "부성", "location": [-607, 77, 93]},
        {"name": "부성 파괴", "location": [1305, 24, -973]},
        {"name": "부성 파괴", "location": [-1976, 68, -158]},
    ],
    "Wasobeso": [
        {"name": "부성 파괴", "location": [365, 67, -510]},
        {"name": "부성 파괴", "location": [219, 80, -331]},
        {"name": "부성 파괴", "location": [-2493, 67, 271]},
        
    ],
    "Tangled Dahye": [ 
        {"name": "부성 파괴", "location": [-2232, 67, 44]},
        {"name": "부성 파괴", "location": [1026, 70, 53]},
        {"name": "누군가의 성", "location": [440, 67, -1640]},
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

        # ------------------ 던전 ------------------
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
                {
                    "이름": d["name"], "X": d["location"][0], "Y": d["location"][1], "Z": d["location"][2],
                    "지역": d["region"], "보상": d["reward"],
                    **dict(zip(["nearest_tp", "nearest_tp_type", "dist"],
                               (lambda n, dist: (n["name"], n["region_type"], dist))
                               (*get_nearest_teleport(d["location"], data["teleports"]))))
                }
                for d in data["dungeons"]
            ])
            fig.add_trace(go.Scatter(
                x=df_dungeon["X"], y=df_dungeon["Z"], mode="markers+text", name="던전",
                marker=dict(color="red", size=8),
                text=df_dungeon["이름"].where(df_dungeon["이름"].isin(selected_dungeons), ""),
                textposition="top center",
                customdata=df_dungeon[["X","Y","Z","이름","지역","보상","nearest_tp","nearest_tp_type","dist"]],
                hovertemplate="이름=%{customdata[3]}<br>"
                              "좌표=(%{customdata[0]}, %{customdata[1]}, %{customdata[2]})<br>"
                              "지역=%{customdata[4]}<br>보상=%{customdata[5]}<br>"
                              "가까운 텔레포트:%{customdata[6]} (%{customdata[7]})<br>"
                              "거리:%{customdata[8]}m"
            ))

        # ------------------ NPC ------------------
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
                {
                    "이름": n["name"], "X": n["location"][0], "Y": n["location"][1], "Z": n["location"][2],
                    "비고": n.get("notes", ""),
                    **dict(zip(["nearest_tp", "nearest_tp_type", "dist"],
                               (lambda t, dist: (t["name"], t["region_type"], dist))
                               (*get_nearest_teleport(n["location"], data["teleports"]))))
                }
                for n in data["npcs"]
            ])
            fig.add_trace(go.Scatter(
                x=df_npc["X"], y=df_npc["Z"], mode="markers+text", name="NPC",
                marker=dict(color="yellow", size=8),
                text=df_npc["이름"].where(df_npc["이름"].isin(selected_npcs), ""),
                textposition="top center",
                customdata=df_npc[["X","Y","Z","이름","비고","nearest_tp","nearest_tp_type","dist"]],
                hovertemplate="이름=%{customdata[3]}<br>"
                              "좌표=(%{customdata[0]}, %{customdata[1]}, %{customdata[2]})<br>"
                              "비고=%{customdata[4]}<br>"
                              "가까운 텔레포트:%{customdata[5]} (%{customdata[6]})<br>"
                              "거리:%{customdata[7]}m"
            ))

        # ------------------ 텔레포트 ------------------
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
                customdata=df_tp[["X","Y","Z","이름","지역구분"]],
                hovertemplate="이름=%{customdata[3]}<br>"
                              "좌표=(%{customdata[0]}, %{customdata[1]}, %{customdata[2]})<br>"
                              "지역구분=%{customdata[4]}"
            ))

    elif mode == "war":
        war_categories = [
            ("Dungeon Boys", "던전보이즈", "green"),
            ("Wasobeso", "와쏘베쏘", "blue"),
            ("Tangled Dahye", "탱글다혜", "brown")
        ]

        for data_key, display_name, color in war_categories:
            if data_key in data:
                df_rows = []
                for item in data[data_key]:
                    nearest, dist = get_nearest_teleport(item["location"], data["teleports"])
                    df_rows.append({
                        "이름": item["name"], "X": item["location"][0], "Y": item["location"][1], "Z": item["location"][2],
                        "nearest_tp": nearest["name"], "nearest_tp_type": nearest["region_type"], "dist": dist
                    })
                df = pd.DataFrame(df_rows)

                group_names = df["이름"].tolist()
                selected_names = []
                with st.sidebar.expander(f"{display_name} 목록", expanded=False):
                    toggle_names = st.checkbox(f"{display_name} 전체 ON/OFF", value=True, key=f"toggle_{data_key}")
                    for i, name in enumerate(group_names):
                        checked = st.checkbox(f"{name}", key=f"{data_key}_{i}", value=toggle_names)
                        if checked:
                            selected_names.append(name)

                fig.add_trace(go.Scatter(
                    x=df["X"], y=df["Z"], mode="markers+text", name=display_name,
                    marker=dict(color=color, size=8),
                    text=df.apply(lambda r: f"{r['이름']} (↔{r['nearest_tp']})" if r["이름"] in selected_names else "", axis=1),
                    textposition="top center",
                    customdata=df[["X","Y","Z","이름","nearest_tp","nearest_tp_type","dist"]],
                    hovertemplate="이름=%{customdata[3]}<br>"
                                  "좌표=(%{customdata[0]}, %{customdata[1]}, %{customdata[2]})<br>"
                                  "가까운 텔레포트:%{customdata[4]} (%{customdata[5]})<br>"
                                  "거리:%{customdata[6]}m"
                ))
        df_tp = pd.DataFrame([
            {"이름": tp["name"], "X": tp["location"][0], "Y": tp["location"][1], "Z": tp["location"][2],
             "지역구분": tp["region_type"]}
            for tp in data["teleports"]
        ])
        tp_names = df_tp["이름"].tolist()
        selected_tps = []
        with st.sidebar.expander("텔레포트 목록", expanded=False):
            toggle_tp_names = st.checkbox("텔레포트 전체 ON/OFF", value=True, key="toggle_war_tp_names")
            for i, name in enumerate(tp_names):
                checked = st.checkbox(f"{name}", key=f"war_tp_{i}", value=toggle_tp_names)
                if checked:
                    selected_tps.append(name)

        fig.add_trace(go.Scatter(
            x=df_tp["X"], y=df_tp["Z"], mode="markers+text", name="텔레포트",
            marker=dict(color="purple", size=8),
            text=df_tp["이름"].where(df_tp["이름"].isin(selected_tps), ""),
            textposition="top center",
            customdata=df_tp[["X","Y","Z","이름","지역구분"]],
            hovertemplate="이름=%{customdata[3]}<br>"
                          "좌표=(%{customdata[0]}, %{customdata[1]}, %{customdata[2]})<br>"
                          "지역구분=%{customdata[4]}"
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
































