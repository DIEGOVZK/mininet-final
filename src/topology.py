from mininet.topo import Topo

class MinhaTopologia(Topo):
    def __init__(self):
        super().__init__()

        # Adiciona hosts e switches
        hosts = [self.addHost(f'h{i+1}') for i in range(9)]
        switches = [self.addSwitch(f's{i+1}') for i in range(4)]

        # Adiciona links
        links = [
            (hosts[0], switches[0]), (hosts[1], switches[0]),
            (hosts[2], switches[1]), (hosts[3], switches[1]),
            (hosts[4], switches[2]), (hosts[5], switches[2]),
            (hosts[6], switches[3]), (hosts[7], switches[3]), (hosts[8], switches[3]),
            (switches[0], switches[1]), (switches[1], switches[2]), (switches[2], switches[3])
        ]

        for link in links:
            self.addLink(*link)

topos = {'minhatopologia': MinhaTopologia}