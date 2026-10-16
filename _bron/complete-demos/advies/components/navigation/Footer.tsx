import Link from "next/link";
import { nav, paul } from "@/content/paul";

export function Footer({ base }: { base: string }) {
  return (
    <footer className="site-footer">
      <div className="container">
        <div className="site-footer__grid">
          <div>
            <h2>{paul.company}</h2>
            <p className="small" style={{ marginTop: "1rem", opacity: 0.85, maxWidth: "38ch" }}>
              {paul.name} · {paul.role.toLowerCase()} in {paul.place}. Aangesloten bij {paul.network}.
            </p>
          </div>
          <div>
            <h3>Contact</h3>
            <ul role="list">
              <li>
                <a href={paul.contact.phoneHref}>Telefoon: {paul.contact.phoneDisplay}</a>
              </li>
              <li>
                <a href={`mailto:${paul.contact.email}`}>E-mail: {paul.contact.email}</a>
              </li>
            </ul>
          </div>
          <div>
            <h3>Pagina’s</h3>
            <ul role="list">
              <li>
                <Link href={base}>Home</Link>
              </li>
              {nav.map((n) => (
                <li key={n.slug}>
                  <Link href={`${base}/${n.slug}`}>{n.label}</Link>
                </li>
              ))}
            </ul>
          </div>
        </div>
        <div className="site-footer__base">
          <span>
            © {new Date().getFullYear()} {paul.company}
          </span>
          <span>
            Conceptdemo, niet geïndexeerd. Dienstverleningsdocumenten en privacyverklaring volgen bij livegang.
          </span>
        </div>
      </div>
    </footer>
  );
}
