# EarnFlow Telegram Earning Platform Demo

EarnFlow is a polished, frontend-only Telegram earning platform demonstration built for StrongNationDev. It communicates the core product loop: earn, complete tasks, refer friends, and withdraw.

## Features

- Responsive Telegram-style app shell with Home, Tasks, Refer, Wallet, and Profile navigation
- Demo app-download tasks, surveys, and mini-games
- Survey flow with four questions and progress tracking
- Tap Challenge game with timer, retry, and reward animation
- Local reward balance, animated counters, task progress, and transaction history
- Referral center with fictional referrals, clipboard copy, and share fallback
- Wallet with simulated withdrawal validation and pending transaction receipt
- Notifications, profile information modals, toasts, loading states, and reduced-motion support
- Telegram Web App initialization with normal-browser fallback
- localStorage persistence and `?resetDemo=true` developer reset

## Tech Stack

HTML, CSS, JavaScript, Python, Telegram Bot API, and localStorage. There is no backend, database, payment service, or real offer provider.

## Local Frontend Testing

Open `index.html` directly in a browser, or serve this folder with any static file server. The app works without Telegram. Use `index.html?resetDemo=true` to clear the local demo state.

## Telegram Bot Setup

1. Create a bot with BotFather and copy its token.
2. Set `BOT_TOKEN` and `WEBAPP_URL` in the environment.
3. Install dependencies with `pip install -r requirements.txt`.
4. Run `python main.py`.

Required environment variables:

```text
BOT_TOKEN=your_bot_token
WEBAPP_URL=https://your-static-render-url.onrender.com
```

The bot supports `/start`, `/help`, `/balance`, `/tasks`, `/refer`, and `/withdraw`. The frontend URL is never hardcoded in Python.

## Deploy Frontend to Render

1. Push this project to GitHub.
2. Create a Render **Static Site** connected to the repository.
3. Leave the build command empty and set the publish directory to `.`.
4. Copy the HTTPS Render URL into `WEBAPP_URL` for the bot deployment.
5. Deploy the Python bot separately as a worker or another suitable Python service with `BOT_TOKEN` and `WEBAPP_URL` set.
6. Open the Telegram bot and press **Open EarnFlow**.

## Demo Limitations

All rewards, account details, tasks, referrals, and withdrawals are simulated. No real money is transferred, no real task or survey providers are connected, no database exists, and state is stored only in the current browser's localStorage.

## Future Production Architecture

A production implementation would need a secure backend, database, server-side Telegram authentication, an auditable reward ledger, real task and survey providers, payment and withdrawal integrations, fraud prevention, an admin panel, audit logs, security controls, and monitoring.

Built as a product demonstration by StrongNationDev.
