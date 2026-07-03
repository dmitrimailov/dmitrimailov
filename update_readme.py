import datetime

def generate_readme():
    # Получаем текущее время
    current_time = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    
    # Текст вашей будущей визитки
    content = f"""### Привет! 👋

Этот профиль обновляется автоматически с помощью скрипта на Python и GitHub Actions.



🕒 **Последний запуск скрипта:** {current_time} UTC
"""
    
    # Записываем текст в файл README.md (он перезапишет всё старое содержимое)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    generate_readme()
