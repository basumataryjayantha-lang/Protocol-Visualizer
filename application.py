def generate_application_events(activity):

    if activity == "browsing":

        return [
            {
                "protocol": "DNS",
                "message": "DNS Query",
                "direction": "Client → DNS Server",
                "description": "Client asks for the IP address of example.com."
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
                "description": "Web server sends the requested page."
            }
        ]


    elif activity == "mail":

        return [
            {
                "protocol": "SMTP",
                "message": "SMTP Connection",
                "direction": "Client → Mail Server",
                "description": "Client establishes a connection with the mail server."
            },
            {
                "protocol": "SMTP",
                "message": "EHLO",
                "direction": "Client → Mail Server",
                "description": "Client identifies itself to the SMTP server."
            },
            {
                "protocol": "SMTP",
                "message": "MAIL FROM",
                "direction": "Client → Mail Server",
                "description": "Client specifies the sender address."
            },
            {
                "protocol": "SMTP",
                "message": "RCPT TO",
                "direction": "Client → Mail Server",
                "description": "Client specifies the receiver address."
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


    elif activity == "streaming":

        return [
            {
                "protocol": "HTTP",
                "message": "DNS Query",
                "direction": "Client → DNS Server",
                "description": "Client resolves the streaming server address."
            },
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
                "description": "Server returns available media segments."
            },
            {
                "protocol": "HTTP",
                "message": "Media Segment 1",
                "direction": "Streaming Server → Client",
                "description": "First media segment is transferred."
            },
            {
                "protocol": "HTTP",
                "message": "Media Segment 2",
                "direction": "Streaming Server → Client",
                "description": "Second media segment is transferred."
            },
            {
                "protocol": "HTTP",
                "message": "Media Segment 3",
                "direction": "Streaming Server → Client",
                "description": "Third media segment is transferred."
            }
        ]

    return []
