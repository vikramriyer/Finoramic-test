import pip, subprocess as sp, sys, json, os
from threading import Timer

def install(pkg):
    is_success, output = cmd_runner(pkg)
    if is_success:
        return 1
    else:
        print("ERROR: Installation of {} is NOT successful.".format(pkg))
        print("Error Message: [{}]".format(output))
        return 0

def cmd_runner(pkg):
    proc = sp.Popen([sys.executable, '-m', 'pip', 'install', pkg], stdout=sp.PIPE, stderr=sp.PIPE)
    timer = Timer(120, lambda P: P.kill(), [proc])
    try:
        timer.start()
        op, err = proc.communicate()
    except Error as error:
        print("The process of installing [{}] timed out. Please try again.".format(error))
    finally:
        timer.cancel()
    if proc.returncode == 0:
        return True, op
    else:
        return False, str(err)

def get_dependencies():
    file_path = "/data/Finoramic-test/dependencies-test.json"
    if os.path.exists(file_path):
        with open(file_path) as f:
            try:
                json_data = json.load(f)
                dependency_list = json_data["Dependencies"]
            except ValueError as error:
                print("JSON file invalid: [Error Msg: {}]".format(error))
                return
        return dependency_list
    else:
        print("File path is not valid.")

def main():
    dependency_list = get_dependencies()
    success_count = 0
    if dependency_list:
        for pkg in dependency_list:
            success_count += install(pkg)
    if success_count == len(dependency_list):
        print("Success.")

if __name__ == "__main__":
    main()
