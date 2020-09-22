import magic
import mimetypes

def file_check(filename, ALLOWED_EXTENSIONS):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS