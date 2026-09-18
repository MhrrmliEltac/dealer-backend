import os


def static_root() -> str:
    if root := os.getenv("STATIC_ROOT"):
        return root
    if os.getenv("VERCEL") == "1":
        return "/tmp/static"
    return "static"


def upload_dir(name: str) -> str:
    path = os.path.join(static_root(), "uploads", name)
    os.makedirs(path, exist_ok=True)
    return path


def static_url_to_path(url: str) -> str:
    prefix = "/static/"
    if url.startswith(prefix):
        return os.path.join(static_root(), url[len(prefix) :])
    return url.lstrip("/")


def ensure_static_layout() -> str:
    root = static_root()
    os.makedirs(root, exist_ok=True)
    for name in ("advantages", "auction", "services", "serviceInfo", "about"):
        upload_dir(name)
    return root
