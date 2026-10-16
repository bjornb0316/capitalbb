/** A real touch primes Safari's inline video decoder; the scroll timeline owns playback. */
export function unlockScrollVideo(video: HTMLVideoElement | null, seek: () => void) {
  if (!video) return () => {};
  let disposed = false;
  const unlock = () => {
    video.play()?.then(() => {
      video.pause();
      if (!disposed) seek();
    }).catch(() => { /* Poster remains visible if the browser refuses playback. */ });
  };
  document.addEventListener('touchstart', unlock, { once: true, passive: true });
  return () => {
    disposed = true;
    document.removeEventListener('touchstart', unlock);
  };
}
