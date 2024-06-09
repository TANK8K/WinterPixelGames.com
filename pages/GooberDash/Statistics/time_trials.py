from math import floor, ceil, log10
import streamlit as st
import pandas as pd
import plotly.express as px
import time
import datetime

conn = st.connection("postgresql", type="sql")

country_region_list = [
    "🌐 Global",
    "🇦🇫 Afghanistan",
    "🇦🇱 Albania",
    "🇩🇿 Algeria",
    "🇼🇸 American Samoa",
    "🇦🇩 Andorra",
    "🇦🇴 Angola",
    "🇦🇮 Anguilla",
    "🇦🇬 Antigua and Barbuda",
    "🇦🇷 Argentina",
    "🇦🇲 Armenia",
    "🇦🇼 Aruba",
    "🇦🇺 Australia",
    "🇦🇹 Austria",
    "🇦🇿 Azerbaijan",
    "🇧🇸 Bahamas",
    "🇧🇭 Bahrain",
    "🇧🇩 Bangladesh",
    "🇧🇧 Barbados",
    "🇧🇾 Belarus",
    "🇧🇪 Belgium",
    "🇧🇿 Belize",
    "🇧🇯 Benin",
    "🇧🇲 Bermuda",
    "🇧🇹 Bhutan",
    "🇧🇴 Bolivia",
    "🇧🇦 Bosnia and Herzegovina",
    "🇧🇼 Botswana",
    "🇧🇻 Bouvet Island",
    "🇧🇷 Brazil",
    "🇮🇴 British Indian Ocean Territory",
    "🇧🇳 Brunei Darussalam",
    "🇧🇬 Bulgaria",
    "🇧🇫 Burkina Faso",
    "🇧🇮 Burundi",
    "🇰🇭 Cambodia",
    "🇨🇲 Cameroon",
    "🇨🇦 Canada",
    "🇨🇻 Cape Verde",
    "🇰🇾 Cayman Islands",
    "🇨🇫 Central African Republic",
    "🇹🇩 Chad",
    "🇨🇱 Chile",
    "🇨🇳 China",
    "🇨🇽 Christmas Island",
    "🇨🇨 Cocos (Keeling) Islands",
    "🇨🇴 Colombia",
    "🇰🇲 Comoros",
    "🇨🇬 Congo",
    "🇨🇩 Congo, the Democratic Republic of the",
    "🇨🇰 Cook Islands",
    "🇨🇷 Costa Rica",
    "🇭🇷 Croatia",
    "🇨🇺 Cuba",
    "🇨🇼 Curaçao",
    "🇨🇾 Cyprus",
    "🇨🇿 Czech Republic",
    "🇨🇮 Côte d'Ivoire",
    "🇩🇰 Denmark",
    "🇩🇯 Djibouti",
    "🇩🇲 Dominica",
    "🇩🇴 Dominican Republic",
    "🇪🇨 Ecuador",
    "🇪🇬 Egypt",
    "🇸🇻 El Salvador",
    "🇬🇶 Equatorial Guinea",
    "🇪🇷 Eritrea",
    "🇪🇪 Estonia",
    "🇪🇹 Ethiopia",
    "🇫🇰 Falkland Islands (Malvinas)",
    "🇫🇴 Faroe Islands",
    "🇫🇯 Fiji",
    "🇫🇮 Finland",
    "🇫🇷 France",
    "🇬🇫 French Guiana",
    "🇵🇫 French Polynesia",
    "🇹🇫 French Southern Territories",
    "🇬🇦 Gabon",
    "🇬🇲 Gambia",
    "🇬🇪 Georgia",
    "🇩🇪 Germany",
    "🇬🇭 Ghana",
    "🇬🇮 Gibraltar",
    "🇬🇷 Greece",
    "🇬🇱 Greenland",
    "🇬🇩 Grenada",
    "🇬🇵 Guadeloupe",
    "🇬🇺 Guam",
    "🇬🇹 Guatemala",
    "🇬🇬 Guernsey",
    "🇬🇳 Guinea",
    "🇬🇼 Guinea-Bissau",
    "🇬🇾 Guyana",
    "🇭🇹 Haiti",
    "🇭🇲 Heard Island and Mcdonald Islands",
    "🇭🇳 Honduras",
    "🇭🇰 Hong Kong",
    "🇭🇺 Hungary",
    "🇮🇸 Iceland",
    "🇮🇳 India",
    "🇮🇩 Indonesia",
    "🇮🇷 Iran",
    "🇮🇶 Iraq",
    "🇮🇪 Ireland",
    "🇮🇲 Isle of Man",
    "🇮🇱 Israel",
    "🇮🇹 Italy",
    "🇯🇲 Jamaica",
    "🇯🇵 Japan",
    "🇯🇪 Jersey",
    "🇯🇴 Jordan",
    "🇰🇿 Kazakhstan",
    "🇰🇪 Kenya",
    "🇰🇮 Kiribati",
    "🇽🇰 Kosovo",
    "🇰🇼 Kuwait",
    "🇰🇬 Kyrgyzstan",
    "🇱🇦 Lao People's Democratic Republic",
    "🇱🇻 Latvia",
    "🇱🇧 Lebanon",
    "🇱🇸 Lesotho",
    "🇱🇷 Liberia",
    "🇱🇾 Libya",
    "🇱🇮 Liechtenstein",
    "🇱🇹 Lithuania",
    "🇱🇺 Luxembourg",
    "🇲🇴 Macao",
    "🇲🇰 Macedonia",
    "🇲🇬 Madagascar",
    "🇲🇼 Malawi",
    "🇲🇾 Malaysia",
    "🇲🇻 Maldives",
    "🇲🇱 Mali",
    "🇲🇹 Malta",
    "🇲🇭 Marshall Islands",
    "🇲🇶 Martinique",
    "🇲🇷 Mauritania",
    "🇲🇺 Mauritius",
    "🇾🇹 Mayotte",
    "🇲🇽 Mexico",
    "🇫🇲 Micronesia",
    "🇲🇩 Moldova",
    "🇲🇨 Monaco",
    "🇲🇳 Mongolia",
    "🇲🇪 Montenegro",
    "🇲🇸 Montserrat",
    "🇲🇦 Morocco",
    "🇲🇿 Mozambique",
    "🇲🇲 Myanmar",
    "🇳🇦 Namibia",
    "🇳🇷 Nauru",
    "🇳🇵 Nepal",
    "🇳🇱 Netherlands",
    "🇳🇨 New Caledonia",
    "🇳🇿 New Zealand",
    "🇳🇮 Nicaragua",
    "🇳🇪 Niger",
    "🇳🇬 Nigeria",
    "🇳🇺 Niue",
    "🇳🇫 Norfolk Island",
    "🇰🇵 North Korea",
    "🇲🇵 Northern Mariana Islands",
    "🇳🇴 Norway",
    "🇴🇲 Oman",
    "🇵🇰 Pakistan",
    "🇵🇼 Palau",
    "🇵🇸 Palestine",
    "🇵🇦 Panama",
    "🇵🇬 Papua New Guinea",
    "🇵🇾 Paraguay",
    "🇵🇪 Peru",
    "🇵🇭 Philippines",
    "🇵🇳 Pitcairn",
    "🇵🇱 Poland",
    "🇵🇹 Portugal",
    "🇵🇷 Puerto Rico",
    "🇶🇦 Qatar",
    "🇷🇴 Romania",
    "🇷🇺 Russia",
    "🇷🇼 Rwanda",
    "🇷🇪 Réunion",
    "🇧🇱 Saint Barthélemy",
    "🇸🇭 Saint Helena, Ascension and Tristan Da Cunha",
    "🇰🇳 Saint Kitts and Nevis",
    "🇱🇨 marSaint Lucia",
    "🇲🇫 Saint Martin (French Part)",
    "🇵🇲 Saint Pierre and Miquelon",
    "🇻🇨 Saint Vincent and The Grenadines",
    "🇼🇸 Samoa",
    "🇸🇲 San Marino",
    "🇸🇹 Sao Tome and Principe",
    "🇸🇦 Saudi Arabia",
    "🇸🇳 Senegal",
    "🇷🇸 Serbia",
    "🇸🇨 Seychelles",
    "🇸🇱 Sierra Leone",
    "🇸🇬 Singapore",
    "🇸🇽 Sint Maarten (Dutch Part)",
    "🇸🇰 Slovakia",
    "🇸🇮 Slovenia",
    "🇸🇧 Solomon Islands",
    "🇸🇴 Somalia",
    "🇿🇦 South Africa",
    "🇬🇸 South Georgia",
    "🇰🇷 South Korea",
    "🇸🇸 South Sudan",
    "🇪🇸 Spain",
    "🇱🇰 Sri Lanka",
    "🇸🇩 Sudan",
    "🇸🇷 Suriname",
    "🇸🇯 Svalbard and Jan Mayen",
    "🇸🇿 Swaziland",
    "🇸🇪 Sweden",
    "🇨🇭 Switzerland",
    "🇸🇾 Syrian Arab Republic",
    "🇹🇼 Taiwan",
    "🇹🇯 Tajikistan",
    "🇹🇿 Tanzania",
    "🇹🇭 Thailand",
    "🇹🇱 Timor-Leste",
    "🇹🇬 Togo",
    "🇹🇰 Tokelau",
    "🇹🇴 Tonga",
    "🇹🇹 Trinidad and Tobago",
    "🇹🇳 Tunisia",
    "🇹🇷 Turkey",
    "🇹🇲 Turkmenistan",
    "🇹🇨 Turks and Caicos Islands",
    "🇹🇻 Tuvalu",
    "🇺🇬 Uganda",
    "🇺🇦 Ukraine",
    "🇦🇪 United Arab Emirates",
    "🇬🇧 United Kingdom",
    "🇺🇸 United States",
    "🇺🇲 United States Minor Outlying Islands",
    "🇺🇾 Uruguay",
    "🇺🇿 Uzbekistan",
    "🇻🇺 Vanuatu",
    "🇻🇦 Vatican City",
    "🇻🇪 Venezuela",
    "🇻🇳 Vietnam",
    "🇻🇬 Virgin Islands, British",
    "🇻🇮 Virgin Islands, U.S.",
    "🇼🇫 Wallis and Futuna",
    "🇪🇭 Western Sahara",
    "🇾🇪 Yemen",
    "🇿🇲 Zambia",
    "🇿🇼 Zimbabwe",
    "🇦🇽 Åland Islands",
]


@st.cache_resource(show_spinner=True, ttl=43200)
def split_frame(input_df, rows):
    df = [input_df.loc[i : i + rows - 1, :] for i in range(0, len(input_df), rows)]
    return df


@st.cache_resource(show_spinner=True, ttl=43200)
def query_df_first_records():
    df_first_records = conn.query(
        """
        SELECT level_id, level_name, user_id, username, time, upload_time, rank_out_of
        FROM goober_dash_time_trials_records
        WHERE rank=1
        ORDER BY upload_time DESC;
    """
    )
    return df_first_records


def load_page():
    try:
        with open("../storage/last_update.txt", "r") as f:
            last_update = float(f.readline())

        with open("../storage/level_counts.txt", "r") as f:
            level_counts = int(f.readline())

        st.image(
            "static/goober_dash_logo_text.png",
            width=280,
        )
        st.html(
            '<span style="font-size: 25px; font-weight: bold;"><i class="fa-solid fa-flag-checkered" style="display: inline; margin: 0 5px 8px 0; width: 25px"></i>Time Trials<br><img style="display: inline; margin: 0 5px 8px 0; width: 25px" src="./app/static/medal_1st.png">World Records Statistics<span>'
        )
        st.caption(
            f"Last Update: {datetime.datetime.fromtimestamp(last_update).strftime('%Y-%m-%d %H:%M:%S')} UTC (Updated Every 12 Hours)"
        )
        tab1, tab2, tab3 = st.tabs(
            [
                "🏆 Performance Points Leaderboard",
                "🥇 World Records",
                "🥧 WRs Distribution",
            ]
        )

        with tab1:
            df_leaderboard = conn.query(
                "SELECT * FROM goober_dash_time_trials_leaderboard"
            )
            df_leaderboard.rename(
                columns={
                    "user_id": "User ID",
                    "username": "Player",
                    "total_points": "Performance Points",
                    "count": "Completed Levels",
                    "rank": "Global Rank",
                    "top_percentile": "Global Top %",
                    "rank_local": "Local Rank",
                    "top_percentile_local": "Local Top %",
                    "first": "🥇",
                    "second": "🥈",
                    "third": "🥉",
                },
                inplace=True,
            )
            display_global_rank_value = True
            display_local_rank_value = False
            display_user_id_value = False
            new_column_order = [
                "Global Rank",
                "Local Rank",
                "Player",
                "User ID",
                "Performance Points",
                "Global Top %",
                "Local Top %",
                "🥇",
                "🥈",
                "🥉",
                "Completed Levels",
            ]
            df_leaderboard = df_leaderboard[new_column_order]

            top_menu = st.columns(5)
            with top_menu[0]:
                sort_field = st.selectbox(
                    "Sort By",
                    options=[
                        "Global Rank",
                        "Local Rank",
                        "Completed Levels",
                        "Player",
                        "User ID",
                        "🥇",
                        "🥈",
                        "🥉",
                    ],
                )
            with top_menu[1]:
                sort_direction = st.radio("Order", options=["▲", "▼"], horizontal=True)
            with top_menu[2]:
                filter_country = st.selectbox(
                    "Country/Region",
                    options=country_region_list,
                )
                if filter_country != "🌐 Global":
                    display_local_rank_value = True
                    display_global_rank_value = False
                else:
                    display_local_rank_value = False
                    display_global_rank_value = True
            with top_menu[3]:
                filter_user = st.text_input(
                    "Search Player", placeholder="Username or User ID"
                )
            with top_menu[4]:
                display_global_rank = st.checkbox(
                    "Display Global Rank", value=display_global_rank_value
                )
                display_local_rank = st.checkbox(
                    "Display Local Rank", value=display_local_rank_value
                )
                display_user_id = st.checkbox(
                    "Display User ID", value=display_user_id_value
                )

            def search_dataframe(filter_country, filter_user):
                if filter_user != "":
                    player_match = df_leaderboard[
                        df_leaderboard["Player"].str.contains(
                            filter_user, case=False, na=False
                        )
                    ]
                    user_id_match = df_leaderboard[
                        df_leaderboard["User ID"].str.contains(
                            filter_user, case=False, na=False
                        )
                    ]
                    result = (
                        pd.concat([player_match, user_id_match])
                        .drop_duplicates()
                        .reset_index(drop=True)
                    )
                if filter_country != "🌐 Global":
                    if filter_user == "":
                        result = df_leaderboard
                    result = result[
                        result["Player"].str.contains(
                            filter_country[:2], case=False, na=False
                        )
                    ]
                return result

            if filter_country != "🌐 Global" or filter_user:
                df_leaderboard = search_dataframe(filter_country, filter_user)

            if df_leaderboard.empty:
                st.error("No Records Found", icon="❌")

            df_leaderboard = df_leaderboard.sort_values(
                by=sort_field,
                ascending=sort_direction == "▲",
                ignore_index=True,
            )
            pagination = st.container()

            bottom_menu = st.columns((5, 1, 1))
            with bottom_menu[2]:
                batch_size = st.selectbox("Page Size", options=[25, 50, 100])
            with bottom_menu[1]:
                total_pages = (
                    int(len(df_leaderboard) / batch_size) + 1
                    if int(len(df_leaderboard) / batch_size) > 0
                    else 1
                )
                current_page = st.number_input(
                    "Page", min_value=1, max_value=total_pages, step=1
                )

            pages = split_frame(df_leaderboard, batch_size)
            data = pages[current_page - 1]
            min_global_rank = data["Global Rank"].min()
            max_global_rank = data["Global Rank"].max()
            min_local_rank = data["Local Rank"].min()
            max_local_rank = data["Local Rank"].max()
            with bottom_menu[0]:
                bottom_info = (
                    f"Page **{current_page}** of **{total_pages}**{'&nbsp;'*5}"
                )
                if filter_country == "🌐 Global":
                    bottom_info += f"{filter_country} Rank **{min_global_rank}** to **{max_global_rank}** "
                else:
                    bottom_info += f"{filter_country} Rank **{min_local_rank}** to **{max_local_rank}** "
                bottom_info += f"(Total number of Players: **{len(df_leaderboard)}**)"
                st.markdown(bottom_info)

            column_order_config = [
                "Global Rank",
                "Local Rank",
                "Player",
                "User ID",
                "Performance Points",
                "Global Top %",
                "Local Top %",
                "🥇",
                "🥈",
                "🥉",
                "Completed Levels",
            ]
            if not display_global_rank:
                try:
                    column_order_config.remove("Global Rank")
                    column_order_config.remove("Global Top %")
                except Exception:
                    pass
            if not display_local_rank:
                try:
                    column_order_config.remove("Local Rank")
                    column_order_config.remove("Local Top %")
                except Exception:
                    pass
            if not display_user_id:
                try:
                    column_order_config.remove("User ID")
                except Exception:
                    pass
            pagination.dataframe(
                data=data,
                use_container_width=True,
                column_order=tuple(column_order_config),
                column_config={
                    "Global Rank": st.column_config.NumberColumn(format="# %d"),
                    "Local Rank": st.column_config.NumberColumn(format="# %d"),
                    "Completed Levels": st.column_config.ProgressColumn(
                        help="Total Number of Levels with Records",
                        format=f"%f/{level_counts}",
                        min_value=0,
                        max_value=level_counts,
                    ),
                    "User ID": st.column_config.ListColumn(),
                    "Performance Points": st.column_config.NumberColumn(
                        help="Total Performance Points (pp) in all levels combined",
                        format="%d pp",
                    ),
                    "Global Top %": st.column_config.NumberColumn(format="%f %%"),
                    "Local Top %": st.column_config.NumberColumn(format="%f %%"),
                },
                hide_index=True,
            )

            with st.expander("**❔ How Performance Points (pp) are calculated**"):
                st.latex(
                    r"""
                    \textrm{Performance \ Points} = 
                    \left\{
                    \begin{array}{lr}
                    \lfloor \frac{10000}{\textrm{Rank}} \rfloor & \textrm{if \ } 1 \leq \textrm{Rank} \leq 10\\
                    \lfloor \frac{1000}{2^{\left \lceil log_{10}\textrm{Rank} \right \rceil - 1}} \times (\frac{10^{\left \lceil log_{10}\textrm{Rank} \right \rceil - 1}}{\textrm{Rank}}+0.9) \rfloor & \textrm{if \ Rank} \gt 10
                    \end{array}
                    \right.
                    """
                )

                st.markdown("Top 100 Rank to Performance Points conversion")

                def pp_formula(i):
                    if i <= 10:
                        return floor(10000 / i)
                    else:
                        return floor(
                            1000
                            / (2 ** (ceil(log10(i) - 1)))
                            * (10 ** (ceil(log10(i)) - 1) / i + 0.9)
                        )

                split = st.columns((2, 1, 8))
                with split[0]:
                    df = pd.DataFrame(
                        {
                            "Rank": [i for i in range(1, 101)],
                            "Performance Points": [
                                pp_formula(i) for i in range(1, 101)
                            ],
                            "Performance Points pp": [
                                f"{pp_formula(i)} pp" for i in range(1, 101)
                            ],
                        }
                    )
                    st.dataframe(
                        df.drop(columns=["Performance Points"]).rename(
                            columns={"Performance Points pp": "Performance Points"}
                        ),
                        hide_index=True,
                        use_container_width=True,
                    )

                with split[2]:
                    fig = px.line(df, x="Rank", y="Performance Points")
                    st.plotly_chart(fig, use_container_width=True)

        with tab2:
            df_first_records = query_df_first_records()
            df_first_records.rename(
                columns={
                    "level_name": "Level",
                    "level_id": "Level ID",
                    "username": "Player",
                    "user_id": "User ID",
                    "time": "Time",
                    "upload_time": "Upload Time",
                    "rank_out_of": "Level Records Count",
                },
                inplace=True,
            )
            df_first_records["Player"] = df_first_records["Player"].str.replace(
                "-", "", regex=False
            )

            df_first_records["Upload Time"] = df_first_records["Upload Time"].astype(
                str
            )
            if not df_first_records["Upload Time"].str.endswith(" UTC").all():
                df_first_records["Upload Time"] = (
                    df_first_records["Upload Time"] + " UTC"
                )
            df_first_records["Watch Replay"] = (
                "https://gooberdash.winterpixel.io/?play="
                + df_first_records["Level ID"]
                + "&replay="
                + df_first_records["User ID"]
            )
            df_first_records["Race Ghost"] = (
                "https://gooberdash.winterpixel.io/?play="
                + df_first_records["Level ID"]
                + "&ghost="
                + df_first_records["User ID"]
            )

            display_level_id_value = False
            display_user_id_value = False
            display_records_count_value = False

            checkboxes = st.columns(3)
            with checkboxes[0]:
                display_level_id = st.checkbox(
                    "Display Level ID",
                    value=display_level_id_value,
                    key="first_display_leve_id",
                )
            with checkboxes[1]:
                display_user_id = st.checkbox(
                    "Display User ID",
                    value=display_user_id_value,
                    key="first_display_user_id",
                )
            with checkboxes[2]:
                display_records_count = st.checkbox(
                    "Display Records Count",
                    value=display_records_count_value,
                    key="first_display_records_count",
                )

            column_order_config = [
                "Level",
                "Level ID",
                "Player",
                "User ID",
                "Time",
                "Upload Time",
                "Level Records Count",
                "Watch Replay",
                "Race Ghost",
            ]
            if not display_level_id:
                try:
                    column_order_config.remove("Level ID")
                except Exception:
                    pass
            if not display_user_id:
                try:
                    column_order_config.remove("User ID")
                except Exception:
                    pass
            if not display_records_count:
                try:
                    column_order_config.remove("Level Records Count")
                except Exception:
                    pass
            st.dataframe(
                data=df_first_records,
                use_container_width=True,
                column_order=tuple(column_order_config),
                column_config={
                    "User ID": st.column_config.ListColumn(),
                    "Level ID": st.column_config.ListColumn(),
                    "Time": st.column_config.NumberColumn(format="%f s"),
                    "Watch Replay": st.column_config.LinkColumn(display_text="▶️"),
                    "Race Ghost": st.column_config.LinkColumn(display_text="👻"),
                },
                hide_index=True,
            )

        with tab3:
            df_first_records_2 = (
                df_first_records.groupby(["Player"]).size().reset_index(name="Counts")
            )
            fig = px.pie(
                df_first_records_2,
                values=df_first_records_2["Counts"],
                names=df_first_records_2["Player"],
                labels=df_first_records_2["Player"],
                hole=0.4,
            )
            fig.update_traces(textposition="inside", textinfo="percent+label")
            fig.update_layout(
                annotations=[
                    {
                        "text": f"{level_counts} Levels<br>{len(df_first_records_2.index)} WR Holders<br>{df_first_records_2['Counts'].sum()} WRs",
                        "showarrow": False,
                    }
                ]
            )
            st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        print(e)
        time.sleep(3)
