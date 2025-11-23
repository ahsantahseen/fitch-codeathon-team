# Fitch Group Sustainability Analytics Dashboard

## Project Structure

```
fitch-codeathon-team/
├── backend/          # FastAPI backend server
│   └── main.py       # API endpoints
├── frontend/         # React + TypeScript frontend
│   └── src/          # Source code
├── data/             # CSV data files
│   └── train.csv     # Main dataset
└── README.md         # This file
```

## Prerequisites

- **Python 3.8+** (for backend)
- **Node.js 18+** and **npm** (for frontend)

## Backend Setup

The backend is built with FastAPI and serves company data from CSV files.

### 1. Navigate to the backend directory

```bash
cd backend
```

### 2. Create a virtual environment (recommended)

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn pandas
```

Or install from the root requirements.txt:

```bash
# From project root
pip install -r requirements.txt
```

### 4. Run the backend server

```bash
# Make sure you're in the backend directory
uvicorn main:app --reload --port 8000
```

The backend will start on `http://localhost:8000`

You can verify it's working by visiting `http://localhost:8000/` in your browser, which should return:
```json
{"message": "FastAPI backend is running!"}
```

## Frontend Setup

The frontend is built with React, TypeScript, Vite, and Tailwind CSS.

### 1. Navigate to the frontend directory

```bash
cd frontend
```

### 2. Install dependencies

```bash
npm install
```

### 3. Run the development server

```bash
npm run dev
```

The frontend will start on `http://localhost:3000` and should automatically open in your browser.

## Running the Full Application

1. **Start the backend** (in one terminal):
   ```bash
   cd backend
   # Activate virtual environment if needed
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   
   uvicorn main:app --reload --port 8000
   ```

2. **Start the frontend** (in another terminal):
   ```bash
   cd frontend
   npm run dev
   ```

3. **Access the application**:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000

## API Endpoints

The backend provides the following endpoints:

- `GET /` - Health check endpoint
- `GET /entity_ids` - Get list of all entity IDs
- `GET /company/{entity_id}` - Get company data for a specific entity ID
- `GET /comparisons/{entity_id}?n=5` - Get comparison records (default: 5)

## Features

- **Entity ID Selection**: Toggle between different entity IDs using the dropdown in the header
- **Client Score Card**: Displays overall sustainability score, percentile ranking, and breakdown by Environmental, Social, and Governance scores
- **Industry Comparison Table**: Shows how the selected entity compares to other companies in the dataset
- **Real-time Updates**: Changing the entity ID automatically fetches new data and updates all components

## Technologies Used

### Backend
- FastAPI - Modern Python web framework
- Pandas - Data manipulation
- Uvicorn - ASGI server

### Frontend
- React 18 - UI library
- TypeScript - Type safety
- Tailwind CSS - Styling

## Troubleshooting

### Backend Issues

- **Port already in use**: If port 8000 is busy, specify a different port:
  ```bash
  uvicorn main:app --reload --port 8001
  ```
  Then update the frontend API URL in `frontend/src/context/DashboardContext.tsx`

- **CSV file not found**: Make sure `data/train.csv` exists relative to the backend directory (`../data/train.csv`)

### Frontend Issues

- **Port already in use**: Vite will automatically use the next available port if 3000 is busy
- **CORS errors**: Ensure the backend is running and the CORS middleware is configured (already set up in `main.py`)
- **API connection issues**: Verify the backend is running on `http://localhost:8000`

## Building for Production

### Frontend

```bash
cd frontend
npm run build
```

This creates an optimized production build in the `frontend/build` directory.

### Backend

The backend can be deployed using any ASGI server. For production, consider:
- Using a reverse proxy (nginx, Apache)
- Running multiple worker processes
- Setting up proper logging and monitoring

