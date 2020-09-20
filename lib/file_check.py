import magic
import mimetypes

def file_check(file, ALLOWED_EXTENSIONS):
    return all([file_name_check(file.filename, ALLOWED_EXTENSIONS)])

def file_name_check(filename, ALLOWED_EXTENSIONS):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS