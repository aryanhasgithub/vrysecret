<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Drop-In on Rester</title>
</head>
<body>
    <h2>Connect to Rester</h2>
    <button onclick="startCall()">Drop-In</button>
    <script>
        const SIGNALING_SERVER = "wss://your-twingate-ip-or-hostname:8765";
        let pc = new RTCPeerConnection();
        
        async function startCall() {
            let stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            stream.getTracks().forEach(track => pc.addTrack(track, stream));
            
            let ws = new WebSocket(SIGNALING_SERVER);
            ws.onopen = async () => {
                let offer = await pc.createOffer();
                await pc.setLocalDescription(offer);
                ws.send(JSON.stringify({ sdp: pc.localDescription.sdp, type: 'offer' }));
            };
            
            ws.onmessage = async (event) => {
                let data = JSON.parse(event.data);
                let answer = new RTCSessionDescription(data);
                await pc.setRemoteDescription(answer);
                console.log("Connected to Rester!");
            };
        }
    </script>
</body>
</html>
