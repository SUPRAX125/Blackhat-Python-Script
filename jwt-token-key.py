#!/usr/bin/env python3
import hmac
import hashlib
import base64, sys

file=open(sys.argv[3])
key = file.read()

#variable header dan payloadnya
header = sys.argv[1]
payload = sys.argv[2]

#encode header jadi base64
encodeHeaderBytes = base64.urlsafe_b64encode(header.encode("utf-8"))
print("Encode bytes header with base64: %s" %(encodeHeaderBytes))

encodeHeader = str(encodeHeaderBytes, "utf-8").rstrip("-")

#encode payload
encodePayloadBytes = base64.urlsafe_b64encode(payload.encode("utf-8"))
print("Encode bytes payload with base64: %s" %(encodePayloadBytes))

encodePayload = str(encodePayloadBytes, "utf-8").rstrip("-")

#nyatuin header sama payload, jadilah token
token = (encodeHeader+"."+encodePayload)

print("Encode Header: %s" % (encodeHeader))
print("Encode Payload: %s" % (encodePayload))
print("Token: %s" % (token))

#buat signature
sign = base64.urlsafe_b64encode(hmac.new(bytes(key, "UTF-8"), token.encode("utf-8"), hashlib.sha256).digest()).decode('UTF-8').rstrip('-')

print("Signature: %s" % (token+"."+sign))
