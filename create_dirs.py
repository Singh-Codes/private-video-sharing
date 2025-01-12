import os

def create_directories():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    app_dir = os.path.join(base_dir, 'app')
    
    directories = [
        os.path.join(app_dir, 'static'),
        os.path.join(app_dir, 'static', 'css'),
        os.path.join(app_dir, 'static', 'js'),
        os.path.join(app_dir, 'templates'),
        os.path.join(app_dir, 'templates', 'auth'),
        os.path.join(app_dir, 'templates', 'main'),
        os.path.join(app_dir, 'templates', 'files'),
        os.path.join(app_dir, 'uploads')
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f'Created directory: {directory}')

if __name__ == '__main__':
    create_directories()
