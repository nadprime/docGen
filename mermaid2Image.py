# pip install markdown-mermaid-to-images
# # For Ubuntu/Debian
# sudo apt-get install pandoc
# # For CentOS/RHEL
# sudo yum install pandoc
# # For macOS
# brew install pandoc


import os
import subprocess

def convert_mermaid_to_images(markdown_file, output_folder):
    try:
        # Run the markdown-mermaid-to-images command
        subprocess.run(["markdown_mermaid_to_images", "-m", markdown_file, "-o", output_folder], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")

# usage
convert_mermaid_to_images('input.md', 'output_folder')


