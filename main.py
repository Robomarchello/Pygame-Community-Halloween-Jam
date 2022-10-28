from src.app import App
import asyncio

if __name__ == '__main__':
    asyncio.run(App((960, 540), 'One night at pygame\'s - F11 for fullscreen', 0).loop())