from pythonosc import osc_message_builder
from pythonosc import udp_client
rdm = np.random.dirichlet(np.ones(7),size=1)
client = udp_client.UDPClient('127.0.0.1', 10042)
msg = osc_message_builder.OscMessageBuilder(address = list(rdm.tolist()))
msg.add_arg('something special')
msg = msg.build()
client.send(msg)


