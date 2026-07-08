# YouTube Clone

A full-stack **YouTube Clone** built using **Python, Django, HTML, CSS, JavaScript, and ImageKit.io**. The application allows users to upload, watch, and interact with videos through a clean and responsive interface.

## Features

- User authentication (Sign Up, Login, Logout)
- Upload videos with thumbnails
- Video streaming
- Like and dislike videos
- Delete videos (Owner only)
- Channel pages
- Dark mode
- View count tracking
- Responsive user interface
- Optimized media storage and delivery using **ImageKit.io**

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Cloud Storage & CDN:** ImageKit.io

## Sample Video


## Installation

### 1. Clone the repository

```bash
git clone https://github.com/1rishu0/YouTube-Clone.git
cd YouTube-Clone
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

```env
IMAGEKIT_PUBLIC_KEY=your_public_key
IMAGEKIT_PRIVATE_KEY=your_private_key
DEBUG=True
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

## Project Structure

```text
YouTube-Clone/
│── videos/
│── users/
│── static/
│── templates/
│── media/
│── manage.py
│── requirements.txt
│── README.md
```

## Future Improvements

- User subscriptions
- Playlists
- Watch history
- Video recommendations
- Notifications

## Author

**Rishabh Sharma**

- GitHub: https://github.com/1rishu0

## License

This project is intended for **learning and educational purposes**.
