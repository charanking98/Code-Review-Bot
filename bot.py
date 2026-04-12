import os
import requests
from groq import Groq

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
GROQ_API_KEY = os.environ["GROQ_API_KEY"]
REPO = os.environ["GITHUB_REPOSITORY"]  # auto-provided by GitHub Actions

REPO_OWNER = REPO.split("/")[0]
REPO_NAME = REPO.split("/")[1]

github_headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

client = Groq(api_key=GROQ_API_KEY)

def get_pull_requests():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls"
    response = requests.get(url, headers=github_headers)
    return response.json()

def get_pr_files(pr_number):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{pr_number}/files"
    response = requests.get(url, headers=github_headers)
    return response.json()

def analyze_code(code_patch):
    prompt = f"""
You are an expert software engineer performing a code review.
Analyze the following code changes and suggest improvements,
possible bugs, performance issues, and style improvements.

Code Changes:
{code_patch}

Provide clear, concise suggestions.
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def post_comment(pr_number, comment):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues/{pr_number}/comments"
    data = {"body": f"🤖 AI Code Review Suggestions:\n\n{comment}"}
    requests.post(url, headers=github_headers, json=data)
    print(f"✅ Comment posted on PR #{pr_number}")

prs = get_pull_requests()
print(f"Found {len(prs)} open PR(s)")

for pr in prs:
    pr_number = pr["number"]
    print(f"Reviewing PR #{pr_number}: {pr['title']}")
    files = get_pr_files(pr_number)
    for file in files:
        patch = file.get("patch", "")
        if patch:
            print(f"  Analyzing: {file['filename']}")
            review = analyze_code(patch)
            post_comment(pr_number, review)
