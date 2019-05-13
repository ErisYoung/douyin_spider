"""In the module, transform item'tyoe with extension

"""
from douyin_spider.config import extension_to_type_mapping_dict

# get type2extension_mapping_dict from origin dict
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
