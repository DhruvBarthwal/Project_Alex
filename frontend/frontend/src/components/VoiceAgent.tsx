"use client";
import { useVoiceAgent } from "@/hooks/useVoiceAgent";
import { speak } from "@/lib/tts";

const VoiceAgent = () => {
  const { start, stop, reset, listening } = useVoiceAgent();

  return (
    <div className="flex flex-col items-center gap-4">
      {/* START */}
      <button
        onClick={() => {
          // unlock speech (browser requirement)
          const u = new SpeechSynthesisUtterance("");
          window.speechSynthesis.speak(u);

          speak("Hi, I am Alex. What would you like to do today?", () => {
            start();
          });
        }}
        className="px-6 py-3 rounded-full bg-black text-white"
      >
        Start Alex
      </button>

      {/* STOP */}
      {listening && (
        <button
          onClick={stop}
          className="px-6 py-3 rounded-full bg-gray-500 text-white"
        >
          Stop Listening
        </button>
      )}

      {/* RESET (always available) */}
      <button
        onClick={reset}
        className="px-6 py-3 rounded-full bg-red-600 text-white"
      >
        Reset Conversation
      </button>

      <p className="text-sm text-gray-500">
        {listening ? "Listening..." : "Idle"}
      </p>
    </div>
  );
};

export default VoiceAgent;
