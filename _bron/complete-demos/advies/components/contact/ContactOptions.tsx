import { paul } from "@/content/paul";
import { ChatIcon, MailIcon, PhoneIcon } from "./icons";

/** Directe contactroute naast het formulier. Duidelijk gelabeld. */
export function ContactOptions({ title = "Liever direct contact?" }: { title?: string }) {
  return (
    <aside className="contact-options" aria-labelledby="direct-contact-title">
      <h2 id="direct-contact-title" className="contact-options__title">
        {title}
      </h2>
      <ul role="list">
        <li>
          <a href={paul.contact.phoneHref}>
            <PhoneIcon />
            <span>
              <small>Telefoon</small>
              {paul.contact.phoneDisplay}
            </span>
          </a>
        </li>
        <li>
          <a href={`mailto:${paul.contact.email}`}>
            <MailIcon />
            <span>
              <small>E-mail</small>
              {paul.contact.email}
            </span>
          </a>
        </li>
        <li>
          <a href={paul.contact.whatsappHref} rel="noopener" target="_blank">
            <ChatIcon />
            <span>
              <small>WhatsApp</small>
              Stuur een bericht
            </span>
          </a>
        </li>
      </ul>
    </aside>
  );
}
