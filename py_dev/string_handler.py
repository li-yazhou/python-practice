
import re

def handle_text():
   text = """
        this.initParams.tmMinCpu= temp.tmMinCpu;
        this.initParams.cpuMinRatio= temp.cpuMinRatio;
    """
   lines = re.split('\n', text)
   for line in lines:
       start_index =  line.find('=')
       line = line[0:start_index]
       line = line + " : '',"
       line = line.replace('this.initParams.', '')
       print(line)

handle_text()