# MDA Growth Systems credibility audit — Batch 08

Date: 2026-08-05

## Completed checks

- Connected Gmail drafts display the sender as **Michael <michael@mdagrowthsystems.info>**, not the requested **Michael | MDA Growth Systems** display name.
- The sending domain is `mdagrowthsystems.info`, while the intended branded website is `mdagrowthsystems.com`.
- The public MDA website previously exposed a personal Gmail contact address, creating a third identity in the trust chain.
- Public website language observed during research varied between MDA, Modern Digital Agency, MDA Growth Portal and MDA Growth Systems.
- Public claims observed included ROI, lead-volume, partner-rating, guarantee and senior-engineer statements. No supporting evidence was available in the connected sources used for this batch, so these claims were not repeated in outreach.
- GitHub Actions attempted to resolve `https://mdagrowthsystems.com` on 2026-08-05 and failed at DNS resolution. The branded `.com` link was therefore removed from all 20 Batch 08 drafts.
- A truthful MDA public profile was published and publicly verified at:
  https://mda-growth-systems.github.io/mda-prospect-demos/mda-growth-systems/
- All 20 drafts use the verified profile above until the branded domain is repaired.
- The connected tools do not expose Gmail display-name configuration, Google Postmaster Tools, DNS management or a branded demo-domain control panel.
- SPF, DKIM and DMARC were **not verified** and are not claimed as configured.

## Completed fixes in this execution

1. Published a consistent MDA Growth Systems public profile without unsupported performance claims.
2. Replaced the non-resolving `.com` URL in all 20 Batch 08 messages with the verified working profile.
3. Verified all ten prospect demo URLs, all ten thank-you pages and the MDA profile through GitHub Pages.
4. Preserved the sender as Michael and did not invent a matching-domain mailbox.

## Recommended manual fixes

1. Repair DNS for `mdagrowthsystems.com`, then test HTTPS, forms and all accessible pages.
2. Change the Gmail display name to `Michael | MDA Growth Systems`.
3. Configure and use a genuine mailbox on `@mdagrowthsystems.com` when available.
4. Replace personal or mismatched public email addresses with the matching-domain mailbox.
5. Standardise the brand name to `MDA Growth Systems` throughout the website and outreach.
6. Verify SPF, DKIM and DMARC for the actual sending domain before increasing volume.
7. Review all ROI, lead-volume, partner-rating, guarantee and staffing claims; publish evidence or replace them with truthful process-based statements.
8. Add genuine named case studies, dated screenshots and permissioned testimonials.
9. Configure a branded public demo route such as `demos.mdagrowthsystems.com`; this batch uses verified GitHub Pages links because no branded deployment integration was available.
