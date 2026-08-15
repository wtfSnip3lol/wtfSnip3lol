# Setup Guide

## GitHub Profile README

1. **Create a new repository** with your GitHub username (e.g., if your username is `kanati`, create a repo called `kanati`)
2. **Make it public**
3. **Copy the content** from `README.md` into your new repo's README
4. **Customize** all the `[PLACEHOLDERS]`:

### Placeholders to Replace:
- `[YOUR_NAME]` - Your actual name
- `[YOUR_USERNAME]` - Your GitHub username (3 places in stats)
- `[YOUR_DISCORD_INVITE]` - Your Discord server invite link
- `[YOUR_DISCORD_ID]` - Your Discord user ID (get this from Discord profile)

### Skill Icons:
- Edit the icons in "My Experiences" section
- Go to [skillicons.dev](https://skillicons.dev) to see all available tech icons
- Change the `i=cs,py,js,html,css,cpp` part to your skills
- Examples: `js,ts,react,python,java,cpp,csharp,docker,git`

### Discord Widget:
- The Discord widget shows your online status
- Replace `[YOUR_DISCORD_ID]` with your actual Discord user ID
- You can change the theme by replacing `theme-3` (options: theme-1 through theme-5)

### Statistics Cards:
- GitHub profile summary cards automatically pull your data
- Just update `[YOUR_USERNAME]` with your GitHub username
- Cards update daily automatically

**GitHub will automatically display this README on your profile when you visit your profile page!**

---

## Discord Status Bot

### Setup:

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create a Discord Application:**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Click "New Application"
   - Go to "Bot" → "Add Bot"
   - Copy the token

3. **Create `.env` file:**
   ```bash
   cp .env.example .env
   ```
   - Paste your bot token in `.env`

4. **Customize the status:**
   - Edit `discord_status.py`
   - Change `STATUS_MESSAGE` to what you want
   - Change `STATUS_TYPE` (playing, streaming, listening, watching)

5. **Run the bot:**
   ```bash
   python discord_status.py
   ```

### Status Types:
- `discord.ActivityType.playing` → "Playing [message]"
- `discord.ActivityType.streaming` → "Streaming [message]"
- `discord.ActivityType.listening` → "Listening to [message]"
- `discord.ActivityType.watching` → "Watching [message]"

### Examples:
```python
STATUS_MESSAGE = "🎮 Code"  # watching
STATUS_MESSAGE = "💻 Building"  # playing
STATUS_MESSAGE = "🎵 Your Favorite Song"  # listening
```

---

**Useful Links:**
- [Discord Developer Portal](https://discord.com/developers/applications)
- [Skill Icons](https://skillicons.dev)
- [Discord.py Documentation](https://discordpy.readthedocs.io/)

