import nmap
from st2actions.runners.pythonrunner import Action



class CheckLiveHosts(Action):  

  def run(self, network):
    host_list = []
    res = nmap.PortScanner()
    print "Starting Network Discovery...."
    lh = res.scan(network, arguments='-sP -n')
    print "Number of Live Hosts on network : ",lh['nmap']['scanstats']['uphosts']
    print "Live Hosts : "
    for ip in res.all_hosts():
      host_list.append(ip)
    return host_list
 


if __name__ == "__main__":
  check_up = check_live_hosts()
  check_up.run()



