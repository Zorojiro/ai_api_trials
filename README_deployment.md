# Text Generation API

A simple FastAPI application that generates text using the Groq API.

## Features

- Text generation using Groq's Llama model
- RESTful API with FastAPI
- Health check endpoints
- Ready for deployment on Render

## API Endpoints

- `GET /` - Root endpoint with status message
- `GET /health` - Health check endpoint
- `POST /generate-text` - Generate text from a prompt

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your actual Groq API key
# GROQ_API_KEY=your_actual_api_key_here
```

3. Run the application:
```bash
uvicorn app:app --reload
```

The application will be available at http://localhost:8000

## Deployment on Render

### Option 1: Using render.yaml (Recommended)

1. Push your code to a GitHub repository
2. Connect your GitHub repository to Render
3. Render will automatically detect the `render.yaml` file
4. Set the `GROQ_API_KEY` environment variable in the Render dashboard
5. Deploy!

### Option 2: Manual Setup

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Use the following settings:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r simple_requirements.txt`
   - **Start Command**: `uvicorn simple:app --host 0.0.0.0 --port $PORT`
4. Add environment variable `GROQ_API_KEY` with your API key
5. Deploy!

## Environment Variables

- `GROQ_API_KEY` - Your Groq API key (required for production)
- `PORT` - Port number (automatically set by Render)

## Usage

Once deployed, you can make requests to your API:

```bash
curl -X POST "https://your-app.onrender.com/generate-text" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Hello, how are you?"}'
```
