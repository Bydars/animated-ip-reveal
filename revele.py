import curses
import time
import random
import socket
import psutil
import math

def get_ip_info():
    ip_info = {}
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                ip_info[interface] = {
                    "ip": addr.address,
                    "netmask": addr.netmask,
                    "broadcast": addr.broadcast
                }
    return ip_info

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    green_color = curses.color_pair(1)

    text = "You've been trolled!"
    numbers = list(range(10))
    ip_info = get_ip_info()
    ip_address = ip_info.get('Wi-Fi', {}).get('ip', 'IP not found')
    netmask = ip_info.get('Wi-Fi', {}).get('netmask', 'N/A')
    broadcast = ip_info.get('Wi-Fi', {}).get('broadcast', 'N/A')

    for i in range(50):
        w.clear()
        
        for _ in range(50):
            y = random.randint(0, sh - 2)
            x = random.randint(0, sw - 2)
            w.addch(y, x, str(random.choice(numbers)), green_color)
        
        w.refresh()
        time.sleep(0.1)
    
    x_pos = (sw - len(text)) // 2
    y_pos = sh // 2
    w.clear()
    w.addstr(y_pos, x_pos, text, green_color)
    w.refresh()
    
    time.sleep(3)

    ip_text = f"Your IP: {ip_address}"
    netmask_text = f"Netmask: {netmask}"
    broadcast_text = f"Broadcast: {broadcast}"
    x_ip_pos = (sw - len(ip_text)) // 2
    x_netmask_pos = (sw - len(netmask_text)) // 2
    x_broadcast_pos = (sw - len(broadcast_text)) // 2
    w.addstr(y_pos + 2, x_ip_pos, ip_text, green_color)
    w.addstr(y_pos + 3, x_netmask_pos, netmask_text, green_color)
    w.addstr(y_pos + 4, x_broadcast_pos, broadcast_text, green_color)
    w.refresh()
    
    time.sleep(2)

    for i in range(5):
        w.clear()
        for j in range(1, sw, 2):
            if y_pos - i >= 0 and y_pos - i < sh:
                w.addch(y_pos - i, j, '|', green_color)
            if y_pos + i < sh and y_pos + i >= 0:
                w.addch(y_pos + i, j, '|', green_color)
        w.refresh()
        time.sleep(0.1)
    
    time.sleep(2)

    for _ in range(20):
        for symbol in "/-\\|":
            w.clear()
            x = random.randint(0, sw - 2)
            y = random.randint(0, sh - 2)
            w.addch(y, x, symbol, green_color)
            w.refresh()
            time.sleep(0.1)

    for _ in range(3):
        for offset in range(0, sh, 2):
            w.clear()
            for x in range(0, sw):
                y = (offset + x) % sh
                if y < sh and y >= 0:
                    w.addch(y, x, '*', green_color)
            w.refresh()
            time.sleep(0.1)
    
    time.sleep(2)

    for _ in range(30):
        w.clear()
        for _ in range(100):
            y = random.randint(0, sh - 2)
            x = random.randint(0, sw - 2)
            char = chr(random.randint(33, 126))
            w.addch(y, x, char, green_color)
        w.refresh()
        time.sleep(0.1)

    cx, cy = sw // 2, sh // 2
    max_radius = min(sh, sw) // 2
    for radius in range(max_radius):
        w.clear()
        for angle in range(0, 360, 10):
            x = int(cx + radius * math.cos(math.radians(angle)))
            y = int(cy + radius * math.sin(math.radians(angle)))
            if 0 <= x < sw and 0 <= y < sh:
                w.addch(y, x, '*', green_color)
        w.refresh()
        time.sleep(0.1)

    time.sleep(2)

    final_message = "hacked by dars"
    x_final_pos = (sw - len(final_message)) // 2
    w.clear()
    w.addstr(y_pos, x_final_pos, final_message, green_color)
    w.refresh()
    
    time.sleep(3)

curses.wrapper(main)
