{
    "builds": [
      {
        "src": "euromilhoes/wsgi.py",
        "use": "@vercel/python"
      }
    ],
    "routes": [
      {
        "src": "/(.*)",
        "dest": "euromilhoes/wsgi.py"
      }
    ]
}
