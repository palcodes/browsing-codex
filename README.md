# Internet Codex

A simple tool to preserve your browsing history. Takes your OneTab exports and stores them in a searchable database.

## What it does

- Transforms your tab chaos into organized knowledge.
- Intelligently parses necessary pieces for easy searching.
- Builds a permanent, queryable archive that you can carry everywhere.
- Captures timestamps for visualizing the internet journey over time.

## How to use

1. Export your tabs from OneTab as a text file.
2. Rename it to `links.txt` or whatever.
3. Run the script: `python archiver.py`.
4. Your links are now preserved in `web-archive.db`.

## File format expected

OneTab exports look like this:
```
https://example.com | Page Title
https://another-site.com | Another Page
```

## What you get

A database with your links organized by:
- URL and title
- Domain (easier to find stuff from specific sites)  
- Date added
- Tags (empty for now, ready for future features)

Your digital wanderings, catalogued and preserved.

## Future Features

Auto-monitoring, smart clustering by time/domain, and lightweight ML tagging - all running locally.

*Built with minimal dependencies - your archive stays simple and portable.*
