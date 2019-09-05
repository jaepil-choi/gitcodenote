from github import Github
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

symbol_regex = re.compile(r".*#.*@\d+@")

with open("github_token.txt", 'r') as f:
    token = f.read()

g = Github(token)

commits = g.get_user().get_repo("gitcodenote_sandbox").get_commits() 

def get_files(commit_num): # commit은 최신순으로 정렬된다. 0번이 가장 최근의 커밋이다. 
    if commit_num >= len(list(commits)):
        print("ERROR: commit_num out of range of commits list")
        return
    return list(commits)[commit_num].files 

def get_note_nums(file): # TODO: 고작 파일의 raw 하나 가져오는데 request와 bs를 쓰는 것은 비효율적인 것 같다. 
    html = urlopen(file.raw_url)
    parsed = bs(html.read(), 'html.parser').string
    codelines = symbol_regex.findall(parsed)
    symbol = re.compile(r"@\d+@")
    note_nums = {}
    for line in codelines:
        num = symbol.search(line).group()
        num = int(num.strip('@'))
        note_nums[num] = line
    return note_nums