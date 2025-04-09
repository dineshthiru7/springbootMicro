# Gen AI MR Reviewer (Python + Google Gen AI)

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set your Google Gen AI API key:

```bash
export GOOGLE_API_KEY=your_api_key_here
```

3. Run the Flask server:

```bash
python app.py
```

4. Trigger the `/webhook` endpoint with JSON body:

```json
{
  "description": "Added new LoginForm component",
  "diff": "diff --git a/src/components/LoginForm.jsx b/src/components/LoginForm.jsx\n+const login_form = () => {\n+ console.log('test'); }"
}
```