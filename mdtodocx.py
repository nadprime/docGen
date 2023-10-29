# pip install pypandoc

import pypandoc

def convert_markdown_to_docx(markdown_file, docx_file):
    output = pypandoc.convert_file(markdown_file, 'docx', outputfile=docx_file)
    assert output == ""

# usage
convert_markdown_to_docx('input.md', 'output.docx')


