// Listen for the '.' key press on Graphite PR pages
document.addEventListener('keydown', function(event) {

  // Check if the '.' key was pressed
  if (event.key === '.' || event.key === 'Period') {

    // Don't trigger if user is typing in an input field or textarea
    const activeElement = document.activeElement;
    const isInputField = activeElement.tagName === 'INPUT' ||
                        activeElement.tagName === 'TEXTAREA' ||
                        activeElement.isContentEditable;

    if (isInputField) {
      return;
    }

    // Extract org, repo, and PR number from the current URL
    // URL format: https://app.graphite.dev/github/pr/{org}/{repo}/{pr_number}/{title}
    const urlMatch = window.location.pathname.match(/^\/github\/pr\/([^\/]+)\/([^\/]+)\/(\d+)/);

    if (urlMatch) {
      const [, org, repo, prNumber] = urlMatch;

      // Construct the GitHub web editor URL
      const githubEditorUrl = `https://github.dev/${org}/${repo}/pull/${prNumber}`;

      // Navigate to the GitHub web editor
      window.location.href = githubEditorUrl;

      // Prevent default behavior
      event.preventDefault();
    }
  }
});
