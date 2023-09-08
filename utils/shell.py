from subprocess import Popen, PIPE, STDOUT

def run_shell(command):
  process = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, text=True)
  process.wait()
  output = process.stdout.read()
  return_code = process.returncode
  
  return (return_code, output)
