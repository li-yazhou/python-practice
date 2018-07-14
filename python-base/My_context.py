class Mycontext(object):
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print '__enter__'
        return self

    def do_self(self):
        print 'do_self'

    def __exit__(self,exc_type, exc_value, traceback):
        print '__exit__'
        print 'Error', exc_type, ' info:',exc_value

if __name__ == '__main__':
    with Mycontext('test context') as f:
        print f.name
        f.do_self()
