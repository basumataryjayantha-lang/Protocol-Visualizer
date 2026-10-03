def generate_transport_events(activity):

    if activity == "browsing":

        return [
            {
                "step": 1,
                "type": "SYN",
                "direction": "Client → Server",
                "seq": 1000,
                "ack": 0,
                "window": 65535,
                "flags": "SYN",
                "length": 0,
                "state": "SYN-SENT"
            },
            {
                "step": 2,
                "type": "SYN-ACK",
                "direction": "Server → Client",
                "seq": 5000,
                "ack": 1001,
                "window": 65535,
                "flags": "SYN, ACK",
                "length": 0,
                "state": "SYN-RECEIVED"
            },
            {
                "step": 3,
                "type": "ACK",
                "direction": "Client → Server",
                "seq": 1001,
                "ack": 5001,
                "window": 65535,
                "flags": "ACK",
                "length": 0,
                "state": "ESTABLISHED"
            },
            {
                "step": 4,
                "type": "DATA",
                "direction": "Client → Server",
                "seq": 1001,
                "ack": 5001,
                "window": 64240,
                "flags": "PSH, ACK",
                "length": 120,
                "state": "ESTABLISHED"
            },
            {
                "step": 5,
                "type": "ACK",
                "direction": "Server → Client",
                "seq": 5001,
                "ack": 1121,
                "window": 64240,
                "flags": "ACK",
                "length": 0,
                "state": "ESTABLISHED"
            },
            {
                "step": 6,
                "type": "DATA",
                "direction": "Server → Client",
                "seq": 5001,
                "ack": 1121,
                "window": 64240,
                "flags": "PSH, ACK",
                "length": 500,
                "state": "ESTABLISHED"
            },
            {
                "step": 7,
                "type": "ACK",
                "direction": "Client → Server",
                "seq": 1121,
                "ack": 5501,
                "window": 64240,
                "flags": "ACK",
                "length": 0,
                "state": "ESTABLISHED"
            },
            {
                "step": 8,
                "type": "FIN-ACK",
                "direction": "Client → Server",
                "seq": 1121,
                "ack": 5501,
                "window": 64240,
                "flags": "FIN, ACK",
                "length": 0,
                "state": "FIN-WAIT-1"
            },
            {
                "step": 9,
                "type": "ACK",
                "direction": "Server → Client",
                "seq": 5501,
                "ack": 1122,
                "window": 64240,
                "flags": "ACK",
                "length": 0,
                "state": "FIN-WAIT-2"
            },
            {
                "step": 10,
                "type": "FIN-ACK",
                "direction": "Server → Client",
                "seq": 5501,
                "ack": 1122,
                "window": 64240,
                "flags": "FIN, ACK",
                "length": 0,
                "state": "LAST-ACK"
            },
            {
                "step": 11,
                "type": "ACK",
                "direction": "Client → Server",
                "seq": 1122,
                "ack": 5502,
                "window": 64240,
                "flags": "ACK",
                "length": 0,
                "state": "CLOSED"
            }
        ]


    elif activity == "mail":

        return [
            {
                "step": 1,
                "type": "SYN",
                "direction": "Client → Mail Server",
                "seq": 2000,
                "ack": 0,
                "window": 65535,
                "flags": "SYN",
                "length": 0,
                "state": "SYN-SENT"
            },
            {
                "step": 2,
                "type": "SYN-ACK",
                "direction": "Mail Server → Client",
                "seq": 7000,
                "ack": 2001,
                "window": 65535,
                "flags": "SYN, ACK",
                "length": 0,
                "state": "SYN-RECEIVED"
            },
            {
                "step": 3,
                "type": "ACK",
                "direction": "Client → Mail Server",
                "seq": 2001,
                "ack": 7001,
                "window": 65535,
                "flags": "ACK",
                "length": 0,
                "state": "ESTABLISHED"
            },
            {
                "step": 4,
                "type": "SMTP DATA",
                "direction": "Client → Mail Server",
                "seq": 2001,
                "ack": 7001,
                "window": 64000,
                "flags": "PSH, ACK",
                "length": 80,
                "state": "ESTABLISHED"
            },
            {
                "step": 5,
                "type": "ACK",
                "direction": "Mail Server → Client",
                "seq": 7001,
                "ack": 2081,
                "window": 64000,
                "flags": "ACK",
                "length": 0,
                "state": "ESTABLISHED"
            },
            {
                "step": 6,
                "type": "SMTP DATA",
                "direction": "Client → Mail Server",
                "seq": 2081,
                "ack": 7001,
                "window": 64000,
                "flags": "PSH, ACK",
                "length": 350,
                "state": "ESTABLISHED"
            },
            {
                "step": 7,
                "type": "ACK",
                "direction": "Mail Server → Client",
                "seq": 7001,
                "ack": 2431,
                "window": 64000,
                "flags": "ACK",
                "length": 0,
                "state": "ESTABLISHED"
            },
            {
                "step": 8,
                "type": "FIN-ACK",
                "direction": "Client → Mail Server",
                "seq": 2431,
                "ack": 7001,
                "window": 64000,
                "flags": "FIN, ACK",
                "length": 0,
                "state": "FIN-WAIT-1"
            },
            {
                "step": 9,
                "type": "ACK",
                "direction": "Mail Server → Client",
                "seq": 7001,
                "ack": 2432,
                "window": 64000,
                "flags": "ACK",
                "length": 0,
                "state": "FIN-WAIT-2"
            }
        ]


    elif activity == "streaming":

        return [
            {
                "step": 1,
                "type": "SYN",
                "direction": "Client → Streaming Server",
                "seq": 3000,
                "ack": 0,
                "window": 65535,
                "flags": "SYN",
                "length": 0,
                "state": "SYN-SENT"
            },
            {
                "step": 2,
                "type": "SYN-ACK",
                "direction": "Streaming Server → Client",
                "seq": 9000,
                "ack": 3001,
                "window": 65535,
                "flags": "SYN, ACK",
                "length": 0,
                "state": "SYN-RECEIVED"
            },
            {
                "step": 3,
                "type": "ACK",
                "direction": "Client → Streaming Server",
                "seq": 3001,
                "ack": 9001,
                "window": 65535,
                "flags": "ACK",
                "length": 0,
                "state": "ESTABLISHED"
            },
            {
                "step": 4,
                "type": "DATA",
                "direction": "Streaming Server → Client",
                "seq": 9001,
                "ack": 3001,
                "window": 60000,
                "flags": "PSH, ACK",
                "length": 1200,
                "state": "ESTABLISHED"
            },
            {
                "step": 5,
                "type": "ACK",
                "direction": "Client → Streaming Server",
                "seq": 3001,
                "ack": 10201,
                "window": 60000,
                "flags": "ACK",
                "length": 0,
                "state": "ESTABLISHED"
            },
            {
                "step": 6,
                "type": "DATA",
                "direction": "Streaming Server → Client",
                "seq": 10201,
                "ack": 3001,
                "window": 58000,
                "flags": "PSH, ACK",
                "length": 1200,
                "state": "ESTABLISHED"
            },
            {
                "step": 7,
                "type": "ACK",
                "direction": "Client → Streaming Server",
                "seq": 3001,
                "ack": 11401,
                "window": 58000,
                "flags": "ACK",
                "length": 0,
                "state": "ESTABLISHED"
            }
        ]

    return []
