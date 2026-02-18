
### Create `requirements.txt` in `backend/` folder

---

## 📤 Step 2: Push to GitHub

### Method 1: Using VS Code Git Integration

1. **Open VS Code** in your project folder (`gemini-chatbot/`)

2. **Initialize Git repository**
   - Click on the **Source Control** icon in the left sidebar (or press `Ctrl+Shift+G`)
   - Click **"Initialize Repository"**
   - Select your project folder

3. **Stage changes**
   - You'll see all your files listed under "Changes"
   - Click the **+** (plus) icon next to "Changes" to stage all files
   - Or hover over each file and click the + to stage individually

4. **Commit changes**
   - Type a commit message (e.g., "Initial commit: Environmental Chatbot")
   - Click the checkmark (✓) to commit

5. **Create GitHub repository**
   - Go to [GitHub.com](https://github.com) and sign in
   - Click the **+** icon in top right → **"New repository"**
   - Name: `gemini-chatbot` (or any name you prefer)
   - Description: "Environmental AI Chatbot powered by Gemini"
   - Choose Public or Private
   - **DO NOT** initialize with README (we already have one)
   - Click **"Create repository"**

6. **Add remote and push**
   - In VS Code, open terminal (`Ctrl+`` `)
   - Run these commands:
     ```bash
     git remote add origin https://github.com/YOUR_USERNAME/gemini-chatbot.git
     git branch -M main
     git push -u origin main
     ```
   - Replace `YOUR_USERNAME` with your GitHub username

7. **Authenticate**
   - A browser window might open for GitHub authentication
   - Sign in and authorize VS Code

### Method 2: Using Command Line

Open terminal in your project folder and run:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Environmental Chatbot"

# Add remote (replace with your username)
git remote add origin https://github.com/YOUR_USERNAME/gemini-chatbot.git

# Push to GitHub
git branch -M main
git push -u origin main
