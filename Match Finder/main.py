import requests
from bs4 import BeautifulSoup


# Create url and PAGE and Print it
WEBSITE = "https://www.yallakora.com/match-center/?date="

DATE = input("Enter date (MM/DD/YYYY) : ")
PAGE = requests.get(WEBSITE + DATE)


def main(page):
    html = page.content
    soup = BeautifulSoup(html, "lxml")
    matches_details = []
    keys = ["Championship", "Team A", "Team B", "Time", "Score"]

    # If there aren't any match today STOP
    if soup.find("div", {"class": "noStatsDiv"}):
        print("There aren't any match today!")
        pass

    championships = soup.find_all("div", {"class": "matchCard"})
    for championship in championships:

        championship_name = championship.find("h2").text.strip()

        matches = championship.find_all("div", {"class": "teamsData"})
        for match in matches:

            team1 = match.find("div", {"class": "teamA"}).p.text.strip()
            team2 = match.find("div", {"class": "teamB"}).p.text.strip()
            info = match.find("div", {"class": "MResult"})
            scores = info.find_all("span", {"class": "score"})
            time = info.find("span", {"class": "time"}).text.strip()
            f_scores = f"{scores[0].text.strip()} - {scores[1].text.strip()}"

            # print(f""" {team1} - {team2}
            #            {f_scores}
            #            Time: {time}
            # """)

            matches_details.append({
                "Championship": championship_name,
                "Team A": team1,
                "Team B": team2,
                "Time": time,
                "Score": f_scores
            })

    print(matches_details)


main(PAGE)
