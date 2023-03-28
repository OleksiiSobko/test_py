import os
git_command="git --help"
jenkins_upgrade_detected = os.popen(git_command).read()
print("jenkins_upgrade_detected: " + jenkins_upgrade_detected)
