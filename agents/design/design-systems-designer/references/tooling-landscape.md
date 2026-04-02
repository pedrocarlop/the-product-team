# Design Systems Tooling Landscape

Verified against official public documentation on April 2, 2026.

Use this file when the assignment mentions a tool outside the default repo + Figma path, or when a stronger evidence path is available through a specialist platform.

## Interoperability Anchor

- [Design Tokens Community Group (DTCG)](https://www.designtokens.org/): vendor-neutral token specification. The official site says the first stable version `2025.10` is available and positions the format as the interoperability layer across tools and theming workflows.
- [Style Dictionary](https://styledictionary.com/): token transformation pipeline for code delivery. Official docs describe it as a build system that transforms tokens for platforms such as CSS, JS, iOS, and Android, and say version 4 is forward-compatible with DTCG.

Use DTCG as the preferred interoperability target when defining token architecture or cross-tool export rules. Use Style Dictionary when the assignment needs code delivery, platform transforms, alias resolution, or multi-platform output.

## Design Authoring And Token Management

- [Tokens Studio](https://docs.tokens.studio/): Figma-based token authoring and management. Official docs describe reusable tokens across spacing, radius, semantic color, and typography, plus import paths from Figma variables/styles and documented Style Dictionary transforms.
- [Penpot Design Tokens](https://help.penpot.app/user-guide/design-tokens/): Penpot documents native design-token support, DTCG alignment, themes, token sets, and direct use across design surfaces.

Use these when token truth lives in design authoring rather than in code. Prefer Tokens Studio when the team is already centered on Figma token workflows. Prefer Penpot when the system is open-source friendly, self-hosted, or the design evidence already lives in Penpot.

## Documentation And Governance Platforms

- [zeroheight](https://help.zeroheight.com/hc/en-us/articles/35887043779995-Tracking-component-status): documentation platform with component sets, synced status tables, Figma and Storybook links, and status automation via its API.
- [Supernova](https://learn.supernova.io/latest/getting-started/welcome-to-supernova-Jocg9JuY): design-system platform for synchronized documentation, token/component management, code automation, and an official MCP surface for design-system data.

Use these when the assignment needs a stronger evidence path for governance, adoption, status tracking, or documentation truth than raw Figma files alone can provide.

## Code Truth, QA, And Handoff

- [Storybook](https://storybook.js.org/): component workshop and documentation surface for isolated states, component docs, and system-visible implementation truth.
- [Chromatic](https://www.chromatic.com/storybook): Storybook-native visual testing across browsers, viewports, and themes, useful for system QA and regression evidence.
- [Specify](https://docs.specifyapp.com/): token and asset distribution platform with HTTP API, SDK, and SDTF transport format for programmable token delivery.

Use Storybook when the assignment needs real code-state evidence, component inventories, or docs attached to implementation. Use Chromatic when visual regression and story coverage are the best QA evidence. Use Specify when token distribution, transformation, or automation is externalized outside the product repo.

## Historical Or Migration-Only Note

- [Backlight](https://backlight.dev/): the official site states on its homepage that `Backlight.dev is shutting down June 1st 2025`.

Do not position Backlight as a current recommended destination tool. Only mention it for legacy migration context when an assignment references an existing Backlight estate.

## Routing Heuristics

- If token naming, aliasing, theme matrices, or cross-platform export is the hard part, bias toward DTCG + Style Dictionary and then trace the design source from Tokens Studio, Penpot, Supernova, or Specify.
- If the hard part is component parity between design and code, bias toward Figma or Penpot plus Storybook and Chromatic.
- If the hard part is documentation status, adoption, and lifecycle governance, bias toward zeroheight or Supernova before inventing repo-only governance.
- If only repository files and docs are available, use the repo as the source of truth and treat external tooling categories as enrichment guidance, not proof that the project uses them.

