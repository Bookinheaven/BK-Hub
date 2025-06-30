import { useState, useEffect } from 'react';
import './NetworkStatus.css';

function NetworkStatus() {
  const [isOnline, setIsOnline] = useState(navigator.onLine);
  const [wasOffline, setWasOffline] = useState(false);

  useEffect(() => {
    const handleOnline = () => {
      setIsOnline(true);
    };

    const handleOffline = () => {
      setIsOnline(false);
      setWasOffline(true);
    };

    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);

    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);

  useEffect(() => {
    let timer;
    if (isOnline && wasOffline) {
      timer = setTimeout(() => {
        setWasOffline(false);
      }, 4000);
    }
    return () => clearTimeout(timer);
  }, [isOnline, wasOffline]);

  if (!isOnline) {
    return (
      <div
        id="network-status"
        className="network-status network-status-offline"
        aria-live="polite"
        role="status"
      >
        <span>You are offline. Please check your connection.</span>
      </div>
    );
  }

  if (isOnline && wasOffline) {
    return (
      <div
        id="network-status"
        className="network-status network-status-online"
        aria-live="polite"
        role="status"
      >
        <span>You are back online</span>
      </div>
    );
  }

  return null;
}

export default NetworkStatus;
