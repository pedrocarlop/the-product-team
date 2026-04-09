import os
import glob
import re

# The directory to search
base_dir = '/Users/pedrocarrascolopezbrea/Projects/The product team/agents/'

# The replacement text
replacement_text = """- **Embed and Store Visual Artifacts**: When capturing or creating visual artifacts (e.g., using Chrome DevTools `take_screenshot`, `generate_image`, or `browser_subagent`), you MUST ensure they are saved directly in the project's local directory: `knowledge/assets/`.
  - For `take_screenshot`, you MUST supply the `filePath` parameter using an absolute path pointing to the project's assets directory.
  - If a tool auto-saves to `.gemini`, `.antigravity`, or `/tmp/`, you MUST use the `run_command` tool to copy (`cp`) those images/videos into the project's `knowledge/assets/` folder.
  - Reference them in the markdown deliverable using a RELATIVE path: `![Caption](assets/screenshot.png)`. NEVER link to `.gemini` or `.antigravity` paths."""

count = 0
for filepath in glob.glob(os.path.join(base_dir, '**/*.md'), recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We use a regex to find the line starting with "- **Embed and Store Visual Artifacts**:" and terminating at the end of the line
    pattern = r"- \*\*Embed and Store Visual Artifacts\*\*:.*?(?=\n)"
    if re.search(pattern, content):
        new_content = re.sub(pattern, replacement_text, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated {filepath}")

print(f"Total files updated: {count}")
