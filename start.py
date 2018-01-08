import os.path
import subprocess

def confirm_installed(program):
    try:
        return subprocess.check_call(['which', program])
    except subprocess.CalledProcessError as e:
        if e.returncode == 1:
            print("Please make sure {} is installed".format(program))
            exit(1)
        raise e


if __name__ == '__main__':
		if confirm_installed('docker') == 0:
			if confirm_installed('docker-compose') == 0:
				if os.path.isfile('./docker-compose.yml'):
					subprocess.check_call(['docker-compose', 'up', '--build'])
				else:
					print('Make sure there\'s a docker-compose.yml file')