# Graphite GitHub Editor Shortcut

A Chrome extension that adds the `.` keyboard shortcut to Graphite PR pages, allowing you to quickly open the PR in the GitHub web editor.

## Features

- Press `.` (period) on any Graphite PR page to instantly open it in GitHub's web editor
- Automatically extracts organization, repository, and PR number from the Graphite URL
- Smart detection: won't trigger when typing in input fields or text areas

## Installation

1. Clone or download this repository
2. Open Chrome and navigate to `chrome://extensions/`
3. Enable "Developer mode" in the top right corner
4. Click "Load unpacked"
5. Select the directory containing this extension
6. Navigate to a Graphite PR page (e.g., `https://app.graphite.dev/github/pr/org/repo/123/title`)
7. Press `.` to open the PR in the GitHub web editor!

## URL Mapping

The extension automatically converts:
- From: `https://app.graphite.dev/github/pr/{org}/{repo}/{pr_number}/{title}`
- To: `https://github.dev/{org}/{repo}/pull/{pr_number}`

## Example

On page: `https://app.graphite.dev/github/pr/circuitly/circuitly/2835/document-add-updateDocumentHash-endpoint`

Press `.` to navigate to: `https://github.dev/circuitly/circuitly/pull/2835`

## Notes

- The extension requires placeholder icon files (icon16.png, icon48.png, icon128.png) to be added for Chrome Web Store publishing
- For development purposes, you can remove the icons section from manifest.json if needed
