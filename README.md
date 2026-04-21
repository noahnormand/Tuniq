# Tunïq 🎵

> Your wardrobe, dressed by your music.

Tunïq is a mobile app that generates outfits from your music mood. Take a photo of your clothes, play a track, and Tunïq picks an outfit from your wardrobe that matches the vibe.

A lo-fi beat → cozy oversized fit. A dark trap banger → all-black streetwear. A funky colorful track → bold colorblock look.

---

## How it works

1. **Scan your wardrobe** — take photos of your clothes one by one. The AI recognizes each item (type, color, style) and builds your digital wardrobe.
2. **Play a track** — share a Spotify link or search a song directly in the app.
3. **Get your outfit** — Tunïq analyzes the track's mood (energy, vibe, danceability) and generates an outfit from your own wardrobe.
4. **Shop the gaps** — missing a piece to complete the look? Tunïq suggests items to buy that match your style.

---

## Tech stack

| Layer | Tech |
|---|---|
| Mobile app | React Native + Expo |
| Backend API | Python + FastAPI |
| AI / clothing recognition | Hugging Face Inference API |
| Music analysis | Spotify API |
| Database | PostgreSQL |
| Infrastructure | Docker + GitHub Actions |

---

## Project structure

```
tuniq/
├── backend/        # FastAPI — AI, Spotify integration, outfit generation
├── frontend/       # React Native — mobile app
└── docker-compose.yml
```

---

## Getting started

```bash
# Clone the repo
git clone https://github.com/noahnormand/Tuniq.git
cd Tuniq

# Backend
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd frontend
npx expo start
```

---

## Author

Fueled by **N2O** 💨
