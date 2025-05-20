# Discord Bot README

# Discord Bot

This is a simple Discord bot built using Python. It responds to a ping command with a pong message, demonstrating basic bot functionality.

## Project Structure

```
discord-bot
├── bot.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Setup Instructions

1. **Set Up Your Environment**:
   - Ensure you have Python installed (preferably Python 3.8 or higher).
   - Create a new directory for your project and navigate into it.

2. **Create the Project Structure**:
   - Create the files as per the provided structure.

3. **Install Dependencies**:
   - Create a virtual environment (optional but recommended):
     ```
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```
       source venv/bin/activate
       ```
   - Install the required packages:
     ```
     pip install -r requirements.txt
     ```

4. **Create the `.env` File**:
   - In the `.env` file, add your Discord bot token:
     ```
     DISCORD_TOKEN=your_token_here
     ```

5. **Update the `.gitignore` File**:
   - Add the following line to ensure the `.env` file is ignored:
     ```
     .env
     ```

6. **Write the Bot Logic**:
   - In `bot.py`, add the following code:
     ```python
     import os
     import discord
     from discord.ext import commands
     from dotenv import load_dotenv

     load_dotenv()
     TOKEN = os.getenv('DISCORD_TOKEN')

     bot = commands.Bot(command_prefix='!')

     @bot.command()
     async def ping(ctx):
         await ctx.send('pong')

     bot.run(TOKEN)
     ```

7. **Run the Bot**:
   - Execute the bot by running:
     ```
     python bot.py
     ```

8. **Test the Bot**:
   - Invite the bot to your Discord server using the OAuth2 URL generated in the Discord Developer Portal.
   - In a text channel, type `!ping` and the bot should respond with `pong`.

## Troubleshooting
- Ensure that your bot has the necessary permissions in the Discord server.
- Check the console for any error messages if the bot fails to start.
- Verify that the token in the `.env` file is correct and that the file is in the same directory as `bot.py`.