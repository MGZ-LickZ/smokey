import requests
import json
import time
import sys
import random
import threading
from datetime import datetime

class=class="str">"cmt"># Configuration
BASE_URL = class="str">"https:class="cmtclass="str">">//smokey.lichess.org"  # Assuming based on repo name, adjust if different
API_KEY = class="str">"YOUR_LICHESSES_API_KEY_HERE"  class=class="str">"cmt"># Replace with your Lichess API key
WEBHOOK_URL = class="str">"YOUR_DISCORD_WEBHOOK_URL_HERE"  class=class="str">"cmt"># Replace with your Discord webhook URL
GAME_DELAY_MIN = class="num">2  class=class="str">"cmt"># Seconds between games
GAME_DELAY_MAX = class="num">5  class=class="str">"cmt"># Seconds between games

def get_headers():
    return {
        class="str">"Authorization": fclass="str">"Bearer {API_KEY}",
        class="str">"Content-Type": class="str">"application/json"
    }

def get_current_game():
    class="str">""class="str">"Fetches the userclass="str">'s ongoing game if any."class="str">""
    try:
        response = requests.get(fclass="str">"{BASE_URL}/api/stream", headers=get_headers(), stream=True)
        if response.status_code == class="num">200:
            for line in response.iter_lines():
                if line:
                    data = json.loads(line)
                    if 'gameclass="str">' in data and 'idclass="str">' in data['gameclass="str">']:
                        return data['gameclass="str">']
    except Exception as e:
        print(fclass="str">"[ERROR] Failed to fetch current game: {e}")
    return None

def play_turn(game_id):
    class="str">""class="str">"Simulates playing a turn by making random moves."class="str">""
    try:
        class=class="str">"cmt"># Fetch game state
        game_url = fclass="str">"{BASE_URL}/api/bot/game/{game_id}"
        response = requests.get(game_url, headers=get_headers())
        if response.status_code != class="num">200:
            print(fclass="str">"[WARN] Could not fetch game state for {game_id}. Status: {response.status_code}")
            return False

        game_data = response.json()
        
        class=class="str">"cmt"># Check if it's our turn
        if game_data.get(class="str">'turnColor') != class="str">'white':  class=class="str">"cmt"># Adjust if your bot is black
            return True class=class="str">"cmt"># Not our turn, just continue

        class=class="str">"cmt"># Make a random move
        legal_moves = game_data.get(class="str">'moves', class="str">'').split()
        if not legal_moves:
            class=class="str">"cmt"># No moves left, game might be over
            return False

        move = random.choice(legal_moves)
        
        class=class="str">"cmt"># Send move
        move_url = fclass="str">"{BASE_URL}/api/bot/game/{game_id}/move/{move}"
        response = requests.post(move_url, headers=get_headers())
        
        if response.status_code == class="num">200:
            print(fclass="str">"[INFO] Played move: {move}")
            return True
        else:
            print(fclass="str">"[ERROR] Failed to play move {move}: {response.text}")
            return False
            
    except Exception as e:
        print(fclass="str">"[ERROR] Error during turn: {e}")
        return False

def notify_discord(message):
    class="str">""class="str">"Sends a message to a Discord webhook."class="str">""
    try:
        payload = {class="str">"content": message}
        requests.post(WEBHOOK_URL, json=payload)
    except Exception as e:
        print(fclass="str">"[WARN] Failed to send Discord notification: {e}")

def run_bot():
    class="str">""class="str">"Main loop for the bot."class="str">""
    print(class="str">"[INFO] Bot started. Waiting for games...")
    
    while True:
        try:
            game = get_current_game()
            
            if game:
                game_id = game[class="str">'id']
                print(fclass="str">"[INFO] Found game: {game_id}")
                
                class=class="str">"cmt"># Play until game ends
                while True:
                    if not play_turn(game_id):
                        break
                    
                    delay = random.uniform(GAME_DELAY_MIN, GAME_DELAY_MAX)
                    time.sleep(delay)
                
                class=class="str">"cmt"># Game finished
                notify_discord(fclass="str">"Game {game_id} finished.")
                print(fclass="str">"[INFO] Game {game_id} finished.")
                
            else:
                time.sleep(class="num">5) class=class="str">"cmt"># Wait if no active game
                
        except KeyboardInterrupt:
            print(class="str">"\n[INFO] Bot stopped by user.")
            break
        except Exception as e:
            print(fclass="str">"[ERROR] Unexpected error in main loop: {e}")
            time.sleep(class="num">10)

if __name__ == class="str">"__main__":
    class=class="str">"cmt"># Validate configuration
    if API_KEY == class="str">"YOUR_LICHESSES_API_KEY_HERE":
        print(class="str">"[FATAL] Please set your Lichess API key in the script.")
        sys.exit(class="num">1)
        
    if WEBHOOK_URL == class="str">"YOUR_DISCORD_WEBHOOK_URL_HERE":
        print(class="str">"[WARN] Discord webhook URL not set. Notifications will be skipped.")
    
    run_bot()
