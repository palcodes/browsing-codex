# Internet Codex

A simple tool to preserve your browsing history. Takes your OneTab exports and stores them in a searchable database.

## What it does

- Transforms your tab history chaos into organized knowledge.
- Intelligently parses necessary components for easy searching, tagging. 
- Builds a permanent, queryable archive that you can take anywhere with you. 
- Stores timestamps for visualizing your browsing journey over time.

## How to use

1. Export your tabs from OneTab as a text file.
2. Rename it to `links.txt`.
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
