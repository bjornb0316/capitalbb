import type { SummaryGroup } from "@/lib/demo-submission";
import { paul } from "@/content/paul";

/** "Zo ontvangt de adviseur de hulpvraag": overzichtelijke preview voor de verkoopdemo. */
export function InboxPreview({
  title,
  subject,
  groups,
  footnote = "Demoweergave. Er is niets verzonden of opgeslagen.",
  intro,
}: {
  title: string;
  subject: string;
  groups: SummaryGroup[];
  footnote?: string;
  intro?: string;
}) {
  return (
    <section aria-labelledby="inbox-title">
      <h2 id="inbox-title" className="inbox-label">
        {title}
      </h2>
      <div className="inbox">
        <div className="inbox__bar" aria-hidden="true">
          <i />
          <i />
          <i />
          <span style={{ marginLeft: "0.5rem" }}>Inbox · {paul.contact.email}</span>
        </div>
        <div className="inbox__head">
          <p className="inbox__meta">Van: websiteformulier · Aan: {paul.name}</p>
          <p className="inbox__subject">{subject}</p>
          {intro && (
            <p className="inbox__meta" style={{ marginTop: "0.5rem" }}>
              {intro}
            </p>
          )}
        </div>
        <div className="inbox__body">
          {groups.map((g) => (
            <div key={g.id} className="inbox__group">
              <h4>{g.title}</h4>
              <dl>
                {g.rows.map((r) => (
                  <div key={r.label} className="inbox__row">
                    <dt>{r.label}</dt>
                    <dd>{r.value || "—"}</dd>
                  </div>
                ))}
              </dl>
            </div>
          ))}
        </div>
        <p className="inbox__foot">{footnote}</p>
      </div>
    </section>
  );
}
