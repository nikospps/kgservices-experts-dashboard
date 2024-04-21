import subprocess

#result = subprocess.call(['java', '-jar', '/home/nikospps/Desktop/Jena_reasoner.jar'])

def execreas():
    process = subprocess.Popen(['java', '-jar', '/usr/local/etc/res/Jars/rule5.jar'], stdout=subprocess.PIPE)
    stdout = process.communicate()[0]
    result = stdout.decode("utf-8")
    finalres = [substring for substring in result.split('\n') if substring!='']
    return finalres

def readreas(exap=execreas()):
    for i in exap:
        print(i)

# readreas()
if __name__ == '__main__':
    readreas()
