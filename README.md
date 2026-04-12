# 🤖 AI Code Review Bot for GitHub

An automated code review bot that uses **Llama 3.3 70B** (via Groq API) to review 
Pull Requests and post AI-generated feedback directly on GitHub — fully automated 
with GitHub Actions.

## 🚀 How It Works

1. A Pull Request is opened on the repository
2. GitHub Actions automatically triggers the bot
3. The bot fetches the code diff from the PR
4. Sends it to Llama 3.3 70B via Groq API for analysis
5. Posts the AI review as a comment on the PR

## 🛠️ Tech Stack

- **Python** — core bot logic
- **Groq API** — fast LLM inference (Llama 3.3 70B)
- **GitHub REST API** — fetching PRs and posting comments
- **GitHub Actions** — fully automated trigger on every PR

## ⚙️ Setup

### 1. Clone the repo
git clone https://github.com/charanking98/Code-Review-Bot.git

### 2. Add your Groq API key as a GitHub Secret
Go to: Settings → Secrets and variables → Actions → New repository secret
- Name: GROQ_API_KEY
- Value: your Groq API key

### 3. That's it!
Every time a Pull Request is opened, the bot will automatically review the code 
and post suggestions as a comment.

## 📸 Example Output

The bot analyzes code changes and provides suggestions on:
- 🐛 Potential bugs
- ⚡ Performance improvements  
- 🎨 Code style and readability
- 📝 Documentation improvements

## 🔧 Configuration

The workflow is defined in `.github/workflows/code_review.yml` and triggers on:
- Pull request opened
- Pull request updated (new commits pushed)

## 👤 Author

**Charan Sai Maddineni**  
Purdue University Northwest — Engineering Technology  
[GitHub](https://github.com/charanking98)
