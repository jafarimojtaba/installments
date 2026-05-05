# Frontend

Next.js frontend for the Money Tracker application.

## Tech Stack

- Next.js (App Router)
- TypeScript
- Tailwind CSS
- React

## Setup

1. Install dependencies:
```bash
npm install
```

2. Configure environment variables:
```bash
cp .env.example .env.local
```

3. Run development server:
```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser.

## Project Structure

```
frontend/
├── src/
│   ├── app/              # Next.js app router
│   ├── components/       # Reusable UI components
│   ├── lib/             # Utility functions, API clients
│   ├── hooks/           # Custom React hooks
│   └── types/           # TypeScript types/interfaces
├── public/              # Static assets
└── package.json
```

## Environment Variables

- `NEXT_PUBLIC_API_URL` - Backend API URL (default: http://127.0.0.1:8000)
