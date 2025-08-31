from src.agenticAi.main import load_agenticAi_app

if __name__ == '__main__':
    try:
        load_agenticAi_app()

    except Exception as e:
        print(f'app.py --- An Error Occured:', {e})
