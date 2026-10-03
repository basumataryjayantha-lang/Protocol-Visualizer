
import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/simulate", methods=["POST"])
def simulate():
    data = request.get_json(silent=True) or {}
    activity = data.get("activity", "browsing")

    print("Activity:", activity)

    # Application Layer Events
    if activity == "browsing":
        application = [
            {
                "protocol": "DNS",
                "message": "DNS Query",
                "direction": "Client → DNS Server",
                "description": "Client requests the IP address of example.com."
            },
            {
                "protocol": "DNS",
                "message": "DNS Response",
                "direction": "DNS Server → Client",
                "description": "DNS server returns the IP address."
            },
            {
                "protocol": "HTTP",
                "message": "HTTP GET",
                "direction": "Client → Web Server",
                "description": "Client requests the web page."
            },
            {
                "protocol": "HTTP",
                "message": "HTTP 200 OK",
                "direction": "Web Server → Client",
                "description": "Web server sends the web page."
            }
        ]

        # TCP Events
        transport = [
            {
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
        application = [
            {
                "protocol": "SMTP",
                "message": "EHLO",
                "direction": "Client → Mail Server",
                "description": "Client introduces itself to the SMTP server."
            },
            {
                "protocol": "SMTP",
                "message": "MAIL FROM",
                "direction": "Client → Mail Server",
                "description": "Client specifies the sender."
            },
            {
                "protocol": "SMTP",
                "message": "RCPT TO",
                "direction": "Client → Mail Server",
                "description": "Client specifies the receiver."
            },
            {
                "protocol": "SMTP",
                "message": "DATA",
                "direction": "Client → Mail Server",
                "description": "Client sends the email contents."
            },
            {
                "protocol": "SMTP",
                "message": "250 OK",
                "direction": "Mail Server → Client",
                "description": "Mail server accepts the message."
            }
        ]

        transport = [
            {
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
                "type": "DATA",
                "direction": "Client → Mail Server",
                "seq": 2001,
                "ack": 7001,
                "window": 64000,
                "flags": "PSH, ACK",
                "length": 350,
                "state": "ESTABLISHED"
            },
            {
                "type": "ACK",
                "direction": "Mail Server → Client",
                "seq": 7001,
                "ack": 2351,
                "window": 64000,
                "flags": "ACK",
                "length": 0,
                "state": "ESTABLISHED"
            },
            {
                "type": "FIN-ACK",
                "direction": "Client → Mail Server",
                "seq": 2351,
                "ack": 7001,
                "window": 64000,
                "flags": "FIN, ACK",
                "length": 0,
                "state": "FIN-WAIT-1"
            },
            {
                "type": "ACK",
                "direction": "Mail Server → Client",
                "seq": 7001,
                "ack": 2352,
                "window": 64000,
                "flags": "ACK",
                "length": 0,
                "state": "FIN-WAIT-2"
            }
        ]

    else:
        application = [
            {
                "protocol": "HTTP",
                "message": "Manifest Request",
                "direction": "Client → Streaming Server",
                "description": "Client requests the streaming manifest."
            },
            {
                "protocol": "HTTP",
                "message": "Manifest Response",
                "direction": "Streaming Server → Client",
                "description": "Server returns the media manifest."
            },
            {
                "protocol": "HTTP",
                "message": "Media Segment",
                "direction": "Streaming Server → Client",
                "description": "Server sends a media segment."
            }
        ]

        transport = [
            {
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
                "type": "DATA",
                "direction": "Streaming Server → Client",
                "seq": 10201,
                "ack": 3001,
                "window": 58000,
                "flags": "PSH, ACK",
                "length": 1200,
                "state": "ESTABLISHED"
            }
        ]

    return jsonify({
        "activity": activity,
        "application": application,
        "transport": transport
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )

