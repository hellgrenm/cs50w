# CS50 Web Programming 
## Project 1: Wiki https://cs50.harvard.edu/web/projects/1/

## Overview

The goal of this project is to design a Wikipedia-like online encyclopedia.
Each encyclopedia entry is stored using Markdown, but rendered as HTML for users.

## Specifications

### Index Page

- Display a list of all encyclopedia entries.
- Each entry should be a clickable link that navigates to that entry’s page.

### Entry Page

- Visiting `/wiki/TITLE` should display the encyclopedia entry titled `TITLE`.
- The page should:
  - Retrieve the entry’s Markdown content.
  - Convert the Markdown to HTML before displaying it.
- If the entry does not exist, display an appropriate error message.

### Search

- Allow users to search for an entry using a search box in the sidebar.
- Search behavior:
  - Exact match: If the query exactly matches an entry title, redirect directly to that entry page.
  - Partial match: If the query matches part of one or more entry titles, display a list of matching entries.
- Each result should link to its respective entry page.

### Create New Page

- Provide a link in the sidebar that allows users to create a new encyclopedia entry.
- The page must include:
  - A text input for the title.
  - A textarea for Markdown content.
  - A submit button.
- When the form is submitted:
  - If an entry with the same title already exists, display an error message.
  - Otherwise, save the new entry and redirect the user to its page.

### Edit Page

- Each entry page must include a link to edit the entry.
- The edit page should:
  - Display a textarea pre-filled with the entry’s existing Markdown content.
  - Allow the user to modify and save the content.
- After saving, redirect the user back to the updated entry page.

### Random Page

- Provide a link in the sidebar that takes the user to a randomly selected entry.

### Markdown to HTML Conversion

- All entry content must be converted from Markdown to HTML before being displayed.
- You may use the `markdown2` Python library for this conversion.
- HTML output must be rendered safely in templates.

### Notes

- Django escapes HTML by default.
- To render converted HTML correctly, mark it as safe in your template.
