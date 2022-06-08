import argparse
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument('--p', help='Enter directory', required=True)
parser.add_argument('--d', help='Enter Number of days', default=7)
args = parser.parse_args()


def run(*popenargs, **kwargs):
    input = kwargs.pop("input", None)
    check = kwargs.pop("handle", False)

    if input is not None:
        if 'stdin' in kwargs:
            raise ValueError('stdin and input arguments may not both be used.')
        kwargs['stdin'] = subprocess.PIPE

    process = subprocess.Popen(*popenargs, **kwargs)
    try:
        stdout, stderr = process.communicate(input)
    except:
        process.kill()
        process.wait()
        raise
    retcode = process.poll()
    if check and retcode:
        raise subprocess.CalledProcessError(
            retcode, process.args, output=stdout, stderr=stderr)
    return retcode, stdout, stderr


def delete_files(path, days):
    command = '''find "%s" -type f -mtime +%s -name '*.*' -execdir rm -- '{}' \;''' % (path, days)
    command_file_names = '''find "%s" -type f -mtime +%s -name '*.*' ''' % (path, days)

    # Below will print the files which will get deleted
    run([command_file_names], shell=True)
    # print(run_cmd)

    # Below will delete the files
    run_cmd = run([command], shell=True)
    return run_cmd[0]


if __name__ == '__main__':
    print('Done' if delete_files(args.p, args.d) == 0 else 'Some Issue')

