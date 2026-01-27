let cachedVoice: SpeechSynthesisVoice | null = null;

function getFemaleFriendlyVoice(): SpeechSynthesisVoice | null {
  const voices = window.speechSynthesis.getVoices();

  const preferred = [
    // Chrome / Google
    "Google UK English Female",
    "Google US English",

    // Microsoft Edge (very natural)
    "Microsoft Zira",
    "Microsoft Jenny",
    "Microsoft Aria",

    // macOS
    "Samantha",
    "Victoria",

    // Firefox / generic
    "English Female",
  ];

  for (const name of preferred) {
    const voice = voices.find(v =>
      v.name.toLowerCase().includes(name.toLowerCase())
    );
    if (voice) return voice;
  }

  return (
    voices.find(v =>
      v.lang.startsWith("en") &&
      /female|woman|zira|samantha|victoria/i.test(v.name)
    ) ||
    voices.find(v => v.lang.startsWith("en")) ||
    null
  );
}

export function speak(text: string, onEnd?: () => void) {
  const utterance = new SpeechSynthesisUtterance(text);

  if (!cachedVoice) {
    cachedVoice = getFemaleFriendlyVoice();
  }

  if (cachedVoice) {
    utterance.voice = cachedVoice;
  }

  utterance.rate = 0.95;    // calm & human
  utterance.pitch = 1.2;    // feminine, not robotic
  utterance.volume = 1.0;

  utterance.onend = () => {
    onEnd?.();
  };

  window.speechSynthesis.cancel();
  window.speechSynthesis.speak(utterance);
}
