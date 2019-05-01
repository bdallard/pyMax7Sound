from pythonosc import osc_message_builder
from pythonosc import udp_client
import numpy as np 

client=udp_client.UDPClient('127.0.0.1', 10042)

for i in range(10):
    np.random.randint(10042)
    rdm=np.random.dirichlet(np.ones(7),size=1)
    m=str([x for x in rdm.tolist()[0]])[1:-1].replace(",","")
    msg=osc_message_builder.OscMessageBuilder(address=m)
    msg.add_arg('unpacked ok')
    msg=msg.build()
    client.send(msg)

print(0)
