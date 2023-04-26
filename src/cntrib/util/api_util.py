import json

import requests

from cntrib.util.token_util import get_gh_token


def get_contribs(username: str) -> dict:
    # query grabs contributions for the last 365 days
    # TODO: pass from: and to: args to contributionsCollection to get more or certain years
    query = """
            query($username: String!) {
                user(login: $username) {
                    name
                    contributionsCollection {
                    contributionCalendar {
                        colors
                        totalContributions
                        weeks {
                        contributionDays {
                            color
                            contributionCount
                            date
                            weekday
                        }
                        firstDay
                        }
                    }
                }
            }
        }
    """
    variables = {"username": username}
    headers = {"Authorization": f"token {get_gh_token()}"}

    request = requests.post(
        "https://api.github.com/graphql",
        json={"query": query, "variables": variables},
        headers=headers,
    )

    if request.status_code == 200:
        # with open("data.json", "w") as f:
        #     json.dump(request.json(), f, ensure_ascii=False, indent=4)
        return json.loads(request.json())
    return None
