"""In the module, generate _signature parameter

execute signature.js with node.js to generate dynamic _signature parameter in
share_url to get json data

Main functions:
- generate_signature: generate _signature parameter
"""
import os


def generate_signature(value):
    """
    generate _signature parameter
    :param value:share_url id
    :return:signature string
    """
    cwd = os.path.dirname(__file__)
    p = os.popen('cd %s && node signture.js %s' % (cwd, value))
    return p.readlines()[0]


if __name__ == '__main__':
    result = generate_signature('75984155221')
    print(os.getcwd())
    print(result)
