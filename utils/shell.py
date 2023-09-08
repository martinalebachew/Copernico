from subprocess import Popen, PIPE, STDOUT

def run_shell(command):
  process = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, text=True)
  return_code = process.wait()
  output = process.stdout.read()
  return (return_code, output)


def run_script(path):
  return run_shell(path)
