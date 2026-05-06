import ollama

def analyze_resume(resume_text, role):
    """
    Analyzes resume using Ollama LLaMA 3 and returns structured feedback.
    
    Args:
        resume_text: Resume content as string
        role: Target job role/position
    
    Returns:
        String with formatted analysis (HTML-ready)
    """
    
    # Improved prompt with clear structure and constraints
    prompt = f"""
You are an expert career coach.

User wants to become: {role}

Analyze the resume and return output in clean HTML format.

Use this structure EXACTLY:

<h3>Missing Skills</h3>
<ul>
<li>Skill 1</li>
<li>Skill 2</li>
</ul>

<h3>Skills to Remove</h3>
<ul>
<li>Skill</li>
</ul>

<h3>Recommended Projects</h3>
<ul>
<li>Project</li>
</ul>

<h3>Learning Roadmap</h3>
<ol>
<li>Step 1</li>
<li>Step 2</li>
</ol>

Do not add anything else. Only return HTML.

Resume:
{resume_text}
"""

    try:
        # Call Ollama with timeout and token limits
        response = ollama.chat(
            model='llama3',
            messages=[
                {
                    'role': 'system', 
                    'content': 'You are a professional career coach. Provide clear, structured, and actionable advice. Keep responses concise and well-formatted.'
                },
                {
                    'role': 'user', 
                    'content': prompt
                }
            ],
            options={
                'temperature': 0.7,  # Balanced creativity
                'num_predict': 500,  # Limit response length (~400 words)
            }
        )
        
        return response['message']['content']
    
    except Exception as e:
        # Handle Ollama errors gracefully
        return f"""
**ERROR: Unable to analyze resume**

{str(e)}

**Possible solutions:**
- Make sure Ollama is running: `ollama serve`
- Verify LLaMA 3 is installed: `ollama pull llama3`
- Check if Ollama service is accessible on localhost:11434
"""