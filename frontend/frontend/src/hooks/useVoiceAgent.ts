import { useRef, useState } from "react";
import { createDeepgramSocket } from "@/lib/deepgram";
import { sendToBackend } from "@/lib/api";
import { speak } from "@/lib/tts";

export function useVoiceAgent() {
  const mediaRecorder = useRef<MediaRecorder | null>(null);
  const socketRef = useRef<WebSocket | null>(null);

  const [listening, setListening] = useState(false);
  const [lastEmailId, setLastEmailId] = useState<string | null>(null);

  async function start() {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

    socketRef.current = createDeepgramSocket(async (finalText) => {
      console.log("🧑 User:", finalText);

      setListening(false);

      const data = await sendToBackend(finalText, lastEmailId);

      if (typeof data.email_id === "string") {
        setLastEmailId(data.email_id);
      }

      if (data.deleted === true) {
        setLastEmailId(null);
      }

      console.log("🤖 Alex:", data.response);

      speak(data.response);
    });

    socketRef.current.onopen = () => {
      console.log("🎙️ Starting MediaRecorder");

      mediaRecorder.current = new MediaRecorder(stream, {
        mimeType: "audio/webm;codecs=opus",
      });

      mediaRecorder.current.ondataavailable = (e) => {
        if (socketRef.current?.readyState === WebSocket.OPEN) {
          socketRef.current.send(e.data);
        }
      };

      mediaRecorder.current.start(250);
      setListening(true);
    };
  }

  function stop() {
    console.log("🛑 Stopping voice agent");

    mediaRecorder.current?.stop();
    mediaRecorder.current = null;

    socketRef.current?.close();
    socketRef.current = null;

    setListening(false);
  }

  async function reset() {
    stop();

    // clear frontend memory
    setLastEmailId(null);

    // tell backend to reset state
    await sendToBackend("reset", null);

    // restart cleanly
    setTimeout(() => {
      start();
    }, 300);
  }

  return { start, stop, reset, listening };
}
