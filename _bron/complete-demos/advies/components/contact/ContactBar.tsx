"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { paul, primaryCta } from "@/content/paul";
import { PhoneIcon } from "./icons";

/** Compacte sticky contactactie op mobiel. Verborgen tijdens de intake. */
export function ContactBar({ base }: { base: string }) {
  const pathname = usePathname();
  const hidden = pathname.startsWith(`${base}/kennismaken`);
  return (
    <div className="contact-bar" data-hidden={hidden} aria-hidden={hidden || undefined}>
      <Link href={`${base}/kennismaken`} className="btn btn--light" tabIndex={hidden ? -1 : undefined}>
        {primaryCta}
      </Link>
      <a
        href={paul.contact.phoneHref}
        className="btn btn--outline-light contact-bar__call"
        aria-label={`Bel de adviseur op ${paul.contact.phoneDisplay}`}
        tabIndex={hidden ? -1 : undefined}
      >
        <PhoneIcon />
      </a>
    </div>
  );
}
