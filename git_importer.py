from github import Github
import re

with open("github_token.txt", 'r') as f:
    token = f.read()

g = Github(token)

commits = g.get_user().get_repo("gitcodenote_sandbox").get_commits() # commit은 최신순으로 정렬된다. 0번이 가장 최근의 커밋이다. 
test_text = commits[0].files[0].raw_data['patch']
test_text
symbol_regex = re.compile(r".*#.*<@\d+@>")
added_match_obj = symbol_regex.findall(test_text)
added_match_obj


# print(type(commits[0].files[0]))
# print(commits[0].files[0])
# print(commits[0].raw_data['files'])
# type(commits[0])

# print(commits[0].files[0].raw_url)
# print(commits[1].files[1].raw_url) 