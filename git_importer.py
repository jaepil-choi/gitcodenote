from github import Github

g = Github("cd4437a7a66ddd1420ae589b3a0d03c62fefb9f8")

g.get_user().get_repo("gitcodenote_sandbox").get_commits()[0].files[1].raw_url