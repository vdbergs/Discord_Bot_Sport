# Discord Sports Bot

A Discord bot that scrapes sports fixtures (starting with rugby) and provides them via slash commands.

## Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/discord-sports-bot.git
   cd discord-sports-bot
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a** .env **file**:

   ```env
   DISCORD_TOKEN=your_discord_bot_token_here
   ```

4. **Run the bot**:

   ```bash
   python bot/main.py
   ```

## Usage

- /ping: Check if the bot is online.
- /rugby_fixtures: Get upcoming rugby fixtures.

## Adding New Sports

1. Create a new scraper in scraper/sports/&lt;sport&gt;.py.
2. Add a new cog in bot/cogs/&lt;sport&gt;.py with relevant slash commands.
3. Update the database schema if needed in storage/database.py.

## Testing

Run tests with:

```bash
python -m unittest discover tests
```

## Notes

- The bot uses SQLite for storage. The database is in storage/data/sports.db.
- Ensure .env is not committed to GitHub.