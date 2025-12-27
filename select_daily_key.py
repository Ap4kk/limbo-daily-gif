#!/usr/bin/env python3
import os
import random
from datetime import datetime

def select_daily_key():
    """Выбирает ключ на основе даты, гарантируя уникальность каждый день"""
    
    # Получаем текущую дату
    today = datetime.now()
    date_seed = int(today.strftime('%Y%m%d'))
    
    # Получаем список всех ключей
    keys_dir = 'all_keys'
    all_keys = sorted([f for f in os.listdir(keys_dir) if f.endswith('.gif')])
    total_keys = len(all_keys)
    
    if total_keys == 0:
        print("Error: No keys found!")
        return None
    
    # Используем дату как seed для предсказуемости
    random.seed(date_seed)
    
    # Читаем последний использованный ключ
    last_key_file = 'last_key.txt'
    last_key = None
    if os.path.exists(last_key_file):
        with open(last_key_file, 'r') as f:
            last_key = f.read().strip()
    
    # Выбираем новый ключ, отличный от предыдущего
    available_keys = [k for k in all_keys if k != last_key]
    
    # Если все ключи использованы, можем использовать любой
    if not available_keys:
        available_keys = all_keys
    
    # Выбираем ключ детерминированно на основе даты
    key_index = date_seed % len(available_keys)
    selected_key = available_keys[key_index]
    
    # Сохраняем выбранный ключ
    with open(last_key_file, 'w') as f:
        f.write(selected_key)
    
    # Копируем выбранный ключ
    source = os.path.join(keys_dir, selected_key)
    target = 'current.gif'
    
    with open(source, 'rb') as src:
        with open(target, 'wb') as dst:
            dst.write(src.read())
    
    print(f"Selected key for {today.strftime('%Y-%m-%d')}: {selected_key}")
    print(f"Previous key: {last_key if last_key else 'None'}")
    
    return selected_key

if __name__ == '__main__':
    select_daily_key()
