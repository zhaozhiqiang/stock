import os, stat


def creat_soft_link():
    os.symlink(os.getcwd() + '/stock', '/usr/local/bin/stock')
    os.chmod('stock', stat.S_IRWXU)

if '__main__' == __name__:
    creat_soft_link()