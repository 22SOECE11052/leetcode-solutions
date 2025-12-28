import requests

username = "YOUR_LEETCODE_USERNAME"
url = f"https://leetcode-stats-api.herokuapp.com/{username}"
data = requests.get(url).json()

with open("README.md", "w") as f:
    f.write(f"""
# 🚀 LeetCode Progress

- Total Solved: {data['totalSolved']}
- Easy: {data['easySolved']}
- Medium: {data['mediumSolved']}
- Hard: {data['hardSolved']}
""")
