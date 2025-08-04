def get_question_prompt(tech_stack):
    return f"""
You are a technical hiring assistant AI.

Based on the tech stack: {tech_stack}, generate **exactly 5** technical interview questions. 

Rules:
- Each question must end with a `?`
- Do not include titles, headings, or introductory lines
- Each question should be on a new line
- The questions should test core understanding of the listed tools
- Only return the questions — no explanation or context

Example format:
What is X?
How does Y work?
"""
