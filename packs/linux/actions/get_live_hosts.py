import nmap
from st2actions.runners.pythonrunner import Action



class CheckLiveHosts(Action):  

  def run(self, subnet):
    host_list = []
    res = nmap.PortScanner()
    lh = res.scan(network, arguments='-sP -n')
    for ip in res.all_hosts():
      host_list.append(ip)
    return host_list

