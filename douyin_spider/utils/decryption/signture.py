import os

def generate_signature(value):
    p = os.popen('node signture.js %s' % value)
    return p.readlines()[0]


if __name__ == '__main__':
    result=generate_signature('75984155221')
    print(result)


