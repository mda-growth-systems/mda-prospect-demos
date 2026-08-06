# MDA Growth Systems — Batch 15 Revalidation Report

Batch ID: `2026-08-06-batch-15`  
Repository: `mda-growth-systems/mda-prospect-demos`  
Repair branch: `outreach/2026-08-06-batch-15`  
Status: **INCOMPLETE — SENDING LOCKED**

The upgraded master prompt was run as a resume/revalidation of the existing Batch 15 rather than generating duplicate prospects and drafts.

## Gate status

| Gate | Result | Summary |
|---|---|---|
| -1 Batch control | Passed | Existing Batch 15 identified; repair branch and control records established. |
| 0 MDA readiness | Failed | 2/10; `.info` sender, identity mismatch and unverified authentication/reputation. |
| 1 History/suppression | Passed with limitations | Gmail, GitHub and outreach log checked; suppression file created. |
| 2 Research/compliance | Failed | 20 candidates documented, but only 6/10 selected recipients currently pass the subscriber-type gate. |
| 3 Unique demos | Failed | Ten demos exist, but the shared generator architecture does not meet the stricter material-uniqueness rule. |
| 4 GitHub/deployment | Passed for existing deployment | Ten public URLs recorded as live; repair records are on a separate branch. |
| 5 QA | Failed | Existing static/link QA is insufficient for the upgraded four-viewport and accessibility evidence standard. |
| 6 Messages | Partial | Ten first-contact drafts and ten standalone follow-up drafts exist; follow-ups are not genuine threads. |
| 7 Approval/sending | Locked | No Batch 15 email sent. Sending is prohibited until readiness and compliance pass. |

## Prospects

| # | Business | Domain | Subscriber class | Compliance result | Score | Demo | Gmail |
|---:|---|---|---|---|---:|---|---|
| 1 | ICE Drainage Ltd | icedrainage.co.uk | Corporate subscriber | Eligible for preparation only; sending remains locked by MDA readiness | 93 | Live | Drafts exist; not sent |
| 2 | AngliaSolar | angliasolar.co.uk | Individual subscriber | Ineligible for unsolicited email without documented consent or another PECR exception | 91 | Live | Drafts exist; not sent |
| 3 | Industrial Doors North West | idnw.co.uk | Unknown | Ineligible until corporate subscriber status is resolved | 90 | Live | Drafts exist; not sent |
| 4 | Naylor Technical Services Ltd | ntsltd.uk | Corporate subscriber | Eligible for preparation only; sending remains locked by MDA readiness | 86 | Live | Drafts exist; not sent |
| 5 | CDF Management Group Ltd | cdfmgroup.co.uk | Corporate subscriber | Eligible for preparation only; sending remains locked by MDA readiness | 89 | Live | Drafts exist; not sent |
| 6 | Engetech Ltd | engetech.co.uk | Corporate subscriber | Eligible for preparation only; recheck exact legal entity before sending | 92 | Live | Drafts exist; not sent |
| 7 | UK Cabling | ukcabling.com | Unknown | Ineligible until corporate subscriber status and legal entity are resolved | 91 | Live | Drafts exist; not sent |
| 8 | Total Air Solutions Ltd | totalairsolutions.co.uk | Corporate subscriber | Eligible for preparation only; sending remains locked by MDA readiness | 90 | Live | Drafts exist; not sent |
| 9 | RWR Commercial | rwrcommercial.co.uk | Corporate subscriber | Eligible for preparation only; sending remains locked by MDA readiness | 88 | Live | Drafts exist; not sent |
| 10 | UK Pump Maintenance | ukpumpmaintenance.com | Unknown | Ineligible until corporate subscriber status is resolved | 84 | Live | Drafts exist; not sent |

## Work completed in this revalidation

- Resumed Batch 15 without creating duplicate prospects, folders, deployments or drafts.
- Confirmed the connected GitHub repository and established the required batch repair branch.
- Rechecked Gmail for pre-batch contact history: no selected address had a matching message before 6 August 2026.
- Confirmed ten first-contact drafts and ten standalone `Re:` follow-up drafts; none was sent for Batch 15.
- Confirmed the repository's public-link verification record for all ten demo URLs.
- Created `candidate-research.csv`, `suppression-list.csv`, `batch-manifest.csv`, `mda-readiness-report.md`, this report and a strict QA revalidation.
- Separated verified facts from commercial assessments and identified unsupported MDA website claims.

## Exact blockers

1. Configure and verify the approved `.com` sender, exact display name and matching Reply-To.
2. Verify SPF, DKIM, DMARC and the actual reputation dashboard.
3. Unify the public MDA business identity and replace the personal Gmail contact.
4. Resolve or replace AngliaSolar, Industrial Doors North West, UK Cabling and UK Pump Maintenance before any outreach.
5. Rebuild the ten demos to satisfy material uniqueness and run the complete four-viewport/browser QA matrix.
6. Do not treat the existing standalone follow-up drafts as threaded replies.

## Email status

**No email was sent or scheduled by this run.**
