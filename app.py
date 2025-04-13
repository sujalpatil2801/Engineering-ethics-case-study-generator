from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Configuration (REMOVE AFTER TESTING)
API_KEY = "AIzaSyDSvUs6NmXxJH3DGmH4R23mUvSCGq5n6kA"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash")  # Note: Corrected typo from "geminini" to "gemini"

@app.route('/', methods=['GET', 'POST'])
def index():
    case_study = ""
    if request.method == 'POST':
        # Get form inputs
        discipline = request.form.get('discipline', 'general engineering').strip()
        complexity = request.form.get('complexity', 'intermediate')
        ethical_principle = request.form.get('principle', 'conflict of interest')
        
        # Generate prompt
        prompt = f"""Generate a detailed engineering ethics case study with these specifications:
        - Engineering discipline: {discipline}
        - Complexity level: {complexity}
        - Primary ethical principle involved: {ethical_principle}
        
        Structure the case study as follows:
        1. Scenario Background (3-4 paragraphs)
        2. Key Stakeholders (bulleted list)
        3. Ethical Dilemma (clear statement of the conflict)
        4. Discussion Questions (3-5 questions)
        5. Potential Consequences (for different decisions)
        
        Make the situation realistic and professionally challenging."""
        
        try:
            response = model.generate_content(prompt)
            case_study = response.text
        except Exception as e:
            case_study = f"Error generating case study: {str(e)}"
    
    return render_template('index.html', case_study=case_study)

if __name__ == '__main__':
    app.run(debug=True)