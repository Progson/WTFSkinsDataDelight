# WTF-skins-data-analyzing using selenium

website: wtfskins.com

The overall project's idea is to conduct a data analysis of bets on the WTF Skins website, compile the data, and draw interesting insights.

The script "webscrapingBets.py" extracts information about bets from the WTF Skins website using Selenium. It creates a folder (if it doesn't already exist) named "bets" and saves the entire web pages into HTML files. It takes two arguments indicating the type of data we want (-partial or -full) and from which game we want to extract bet data (-crash or -roulette).

The script "extractingPartialCrashInfo.py" extracts only the relevant data from the downloaded pages. Currently, it does not accept any arguments and is specific to the game "crash" and partial data extraction.
