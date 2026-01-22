export function speak(text: string, onEnd?: () => void) {
  if (!("speechSynthesis" in window)) {
    console.warn("Speech synthesis not supported");
    return;
  }

  window.speechSynthesis.cancel(); // avoid queue bugs

  const utterance = new SpeechSynthesisUtterance(text);

  utterance.onstart = () => {
    console.log("🔊 Speaking:", text);
  };

  utterance.onerror = (e) => {
    console.error("🔴 Speech error", e);
  };

  if (onEnd) {
    utterance.onend = onEnd;
  }

  window.speechSynthesis.speak(utterance);
}
