"""In the module, transform item'tyoe with extension

"""
extension_to_type_mapping_dict = {
    'txt': 'text/plain',
    'htm': 'text/html',
    'html': 'text/html',
    'php': 'text/html',
    'css': 'text/css',
    'js': 'application/javascript',
    'json': 'application/json',
    'xml': 'application/xml',
    'swf': 'application/x-shockwave-flash',
    'flv': 'video/x-flv',

    # images
    'png': 'image/png',
    'jpe': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'jpg': 'image/jpeg',
    'gif': 'image/gif',
    'bmp': 'image/bmp',
    'ico': 'image/vnd.microsoft.icon',
    'tiff': 'image/tiff',
    'tif': 'image/tiff',
    'svg': 'image/svg+xml',
    'svgz': 'image/svg+xml',

    # archives
    'zip': 'application/zip',
    'rar': 'application/x-rar-compressed',
    'exe': 'application/x-msdownload',
    'msi': 'application/x-msdownload',
    'cab': 'application/vnd.ms-cab-compressed',

    # audio/video
    'mp3': 'audio/mpeg',
    'ogg': 'audio/ogg',
    'qt': 'video/quicktime',
    'mp4': 'video/mp4',
    'mov': 'video/quicktime',
    'wav': 'audio/x-wav',
    'avi': 'application/octet-stream',

    # adobe
    'pdf': 'application/pdf',
    'psd': 'image/vnd.adobe.photoshop',
    'ai': 'application/postscript',
    'eps': 'application/postscript',
    'ps': 'application/postscript',

    # ms office
    'doc': 'application/msword',
    'rtf': 'application/rtf',
    'xls': 'application/vnd.ms-excel',
    'ppt': 'application/vnd.ms-powerpoint',

    # open office
    'odt': 'application/vnd.oasis.opendocument.text',
    'ods': 'application/vnd.oasis.opendocument.spreadsheet',
}

type_to_extension_mapping_dict = {v: k for k, v in extension_to_type_mapping_dict.items()}


def type_to_extension(type_name):
    """
    change type to extension
    :param type_name:type name
    :return:extension
    """
    if type_name in type_to_extension_mapping_dict.keys():
        return type_to_extension_mapping_dict[type_name]
    else:
        return ''


def extension_to_type(extension_name):
    """
    change extension to type
    :param extension_name:extension name
    :return:type
    """
    if extension_name in extension_to_type_mapping_dict.keys():
        return extension_to_type_mapping_dict[extension_name]
    else:
        return ''
