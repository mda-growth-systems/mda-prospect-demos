# MDA Growth Systems credibility audit — Batch 08

Date: 2026-08-05

## Completed checks

- Connected Gmail messages currently display the sender as **Michael <michael@mdagrowthsystems.info>**, not the requested **Michael | MDA Growth Systems** display name.
- The sending domain is `mdagrowthsystems.info`, while the main website used in outreach is `mdagrowthsystems.com`.
- The public website exposes a personal Gmail contact address, creating a third identity in the trust chain.
- Public website language varies between MDA, Modern Digital Agency, MDA Growth Portal and MDA Growth Systems.
- Public claims observed include ROI, lead-volume, partner-rating, guarantee and senior-engineer statements. No supporting evidence was available in the connected sources used for this batch, so these claims were not repeated in outreach.
- The connected tools do not expose Gmail display-name configuration, Google Postmaster Tools, DNS management or a branded demo-domain control panel.
- DNS command-line resolution was unavailable in the execution environment, so SPF, DKIM and DMARC were **not verified** and are not claimed as configured.

## Recommended manual fixes

1. Change the Gmail display name to `Michael | MDA Growth Systems`.
2. Configure and use a genuine mailbox on `@mdagrowthsystems.com` when available.
3. Replace the personal Gmail address on the website with the matching-domain mailbox.
4. Standardise the brand name to `MDA Growth Systems` throughout the website and outreach.
5. Verify SPF, DKIM and DMARC for the actual sending domain before increasing volume.
6. Review all ROI, lead-volume, partner-rating, guarantee and staffing claims; publish evidence or replace them with truthful process-based statements.
7. Add genuine named case studies, dated screenshots and permissioned testimonials.
8. Configure a branded public demo route such as `demos.mdagrowthsystems.com`; this batch uses verified GitHub Pages links because no branded deployment integration was available.
