from wsgiref import simple_server
from webdemo.api import app


def main():
    application = app.setup_app()
    httpd = simple_server.make_server('', 8080, application)
    httpd.serve_forever()
if __name__ == '__main__':
    main()