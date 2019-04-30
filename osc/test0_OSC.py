from pythonosc import osc_message_builder
from pythonosc import udp_client
import numpy as np 

client=udp_client.UDPClient('127.0.0.1', 10042)

for i in range(10):
    rdm=np.random.dirichlet(np.ones(7),size=1)
    n=[x for x in rdm.tolist()[0]]
    m=str(n)[1:-1]
    msg=osc_message_builder.OscMessageBuilder(address=m)
    msg.add_arg('message ok')
    msg=msg.build()
    client.send(msg)

print(0)
