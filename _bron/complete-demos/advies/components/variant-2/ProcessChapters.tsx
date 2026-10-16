import Link from "next/link";
import { process } from "@/content/paul";
import { Reveal } from "@/components/motion/Reveal";
import { Arrow } from "@/components/contact/icons";

/** Scène V2-05: drie hoofdstukken; de woning krijgt per stap meer vorm. */
export function ProcessChapters({
  detailed = false,
  cta = true,
  title = "Zo werkt het",
}: {
  detailed?: boolean;
  cta?: boolean;
  title?: string;
}) {
  return (
    <section className="v2-proc section" aria-labelledby="v2-proc-title">
      <div className="container">
        <div className="v2-proc__head">
          <h2 id="v2-proc-title" className="h2">
            {title}
          </h2>
          {cta && (
            <Link href="/variant-3/werkwijze" className="text-link">
              Bekijk de werkwijze <Arrow />
            </Link>
          )}
        </div>
        <Reveal as="ol" className="v2-proc__list">
          {process.map((s) => (
            <li key={s.n} className="v2-proc__item" data-reveal>
              <div className="v2-proc__visual" aria-hidden="true">
                <span className="v2-proc__number">0{s.n}</span>
              </div>
              <p className="v2-proc__step">Stap {s.n}</p>
              <h3 className="h3">{s.title}</h3>
              <p>{s.text}</p>
              {detailed && <p className="v2-proc__detail">{s.detail}</p>}
            </li>
          ))}
        </Reveal>
      </div>
    </section>
  );
}
