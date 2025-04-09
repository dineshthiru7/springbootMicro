from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Load your API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Load guidelines
with open("review-guidelines.md", "r") as f:
    guidelines = f.read()

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    pr_description = data.get("description", "")
    diff = data.get("diff", "")

    prompt = f"""
You're a senior React code reviewer. Use the following guidelines to review the code:

{guidelines}

Now, review this Merge Request for guideline compliance:

## PR Description:
{pr_description}

## Code Diff:
{diff}

Provide detailed feedback per section, flag violations, and offer improvements.
"""

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    review_comment = response.text

    return jsonify({"review": review_comment})

if __name__ == "__main__":
    app.run(port=5000, debug=True)