from flask_script import Command
import sys, argparse

"""
Job统一入口
python run.py runjob -m test (jobs/tasks/Test.py)
python run.py runjob -m movie (jobs/tasks/movie.py)
"""


class RunJob(Command):

    capture_all_args = True
    def run(self, *args, **kwargs):
        args = sys.argv[2:]
        parser = argparse.ArgumentParser(add_help=True)
        parser.add_argument("-m", "-name", dest="name", metavar="name", help="请指定Job", required=True)
        params = parser.parse_args(args)
        params_dict = params.__dict__
        print(params_dict)
        if "name" not in params_dict or not params_dict["name"]:
            return "请输入-m"
        return
