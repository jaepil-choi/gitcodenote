from github import Github
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

symbol_regex = re.compile(r".*#.*@\d+@")

# TODO: 만약 git commit의 기능을 적극 활용할 것이 아니라면 url로 충분히 가능하다. Python library가 아닌 Django에서 바로 Github API를 쓰는 것이 나을 수도 있다는 것이다. 
# TODO: 하지만 scalability를 위해선 일단 pygithub를 쓰도록 한다. 

with open("github_token.txt", 'r') as f:
    token = f.read()

g = Github(token)

# TODO: Which branch도 정할 수 있어야 함. 일단은 default로 사용. 
commits = g.get_user().get_repo("gitcodenote_sandbox").get_commits() # commit은 최신순으로 정렬된다. 0번이 가장 최근의 커밋이다. 하지만 이 object는 list가 아니다.

def get_files(sha):
    commit = g.get_user().get_repo("gitcodenote_sandbox").get_commit(sha)
    return commit.files

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

    # TODO: commit, file, note_num 으로 specify 가능하게. 
def get_linked_note(commit_id, file_name, note_num):
    commit_files = get_files(commit_id)
    note_file = [x for x in commit_files if x.filename == file_name][0]
    return get_note_nums(note_file)[note_num]