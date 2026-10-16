"use client";

import { createContext, useContext, useEffect, useState, type ReactNode } from "react";

// Alleen een weergavevoorkeur voor de presentatie, geen persoonsgegevens.
const KEY = "demo-notes";
const Ctx = createContext<{ notes: boolean; setNotes: (v: boolean) => void }>({ notes: false, setNotes: () => {} });

export function DemoProvider({ children }: { children: ReactNode }) {
  const [notes, setNotesState] = useState(false);
  useEffect(() => {
    try {
      setNotesState(sessionStorage.getItem(KEY) === "1");
    } catch {}
  }, []);
  const setNotes = (v: boolean) => {
    setNotesState(v);
    try {
      sessionStorage.setItem(KEY, v ? "1" : "0");
    } catch {}
  };
  useEffect(() => {
    document.documentElement.toggleAttribute("data-demo-notes", notes);
  }, [notes]);
  return <Ctx.Provider value={{ notes, setNotes }}>{children}</Ctx.Provider>;
}

export const useDemo = () => useContext(Ctx);

/** Redactioneel label: alleen zichtbaar als de demonotities aanstaan. */
export function EditorialNote({ children }: { children: ReactNode }) {
  const { notes } = useDemo();
  if (!notes) return null;
  return (
    <p className="editorial-note" role="note">
      <span>Redactie</span> {children}
    </p>
  );
}
