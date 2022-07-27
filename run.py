from application import app, manager
from www import *
from flask_script import Server, Command
import sys, traceback
from jobs.launcher import RunJob

manager.add_command("runserver", Server(host='0.0.0.0',
                                        use_debugger=True, use_reloader=True))
manager.add_command("runjob", RunJob)


@Command
def create_db():
    app.logger.info("Command create_db")


manager.add_command("create_db", create_db)


def main():
    manager.run()


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        traceback.print_exc()
