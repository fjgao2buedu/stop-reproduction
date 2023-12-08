import re

def extract_code(responses):
    """
    Extracts code snippets from a batch of text.
    This example assumes Python code enclosed in triple backticks for simplicity.
    """

    solutions = []
    print("[EXTRACTING CODE.....]")
    pattern = re.compile(r'```python(.*)```', re.DOTALL)  # Regex pattern to extract Python code blocks
    response = str(responses[0].message.content)
    matches = re.findall(pattern, response)

    solutions.append(matches[0])
    print("[EXTRACTED CODE]\n", solution)
    
    return solutions