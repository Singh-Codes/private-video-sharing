# Private Video Sharing Platform

A secure Flask-based platform for private file and video sharing with key-based access control.

## Features

- Secure file upload and storage
- Private key generation for each file
- Shareable links with key-based access
- Access tracking and logging
- Support for various file types including videos
- User authentication and authorization
- Responsive UI with Bootstrap

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Singh-Codes/private-video-sharing.git
cd private-video-sharing
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file with your configuration:
```
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///app.db
```

5. Initialize the database:
```bash
flask db upgrade
```

6. Run the application:
```bash
python run.py
```

## Usage

1. Register an account or login
2. Upload files through the upload page
3. Share files by:
   - Copying the generated private key
   - Sharing the file's unique link
4. Recipients can access files using the shared link and private key

## Security Features

- Secure file storage with unique filenames
- Private key authentication for file access
- CSRF protection
- User session management
- Access logging

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
