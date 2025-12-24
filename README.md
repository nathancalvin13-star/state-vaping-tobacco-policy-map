# State Vaping & Flavored Tobacco Policy Database

**Comprehensive Interactive Map of State Regulations (2024-2025)**

A professional-grade, interactive database of vaping and flavored tobacco policies across all 50 U.S. states and the District of Columbia. Designed for state attorneys general offices, public health officials, and tobacco control researchers.

---

## Overview

This database provides authoritative, up-to-date information on state-level tobacco control policies including:

- **Flavored E-Cigarette Restrictions** (comprehensive bans, partial restrictions, exemptions)
- **Menthol Cigarette Bans** (state-level prohibitions)
- **E-Cigarette Excise Taxes** (rates, structures, implementation details)
- **Indoor Vaping Restrictions** (smoke-free laws covering e-cigarettes)
- **Age Restrictions** (Tobacco 21 laws)
- **Licensing Requirements** (retailer licensing, fee structures)
- **Local Restrictions** (notable city/county-level policies)
- **Recent Policy Changes** (2024-2025 updates)

---

## Key Statistics

| Metric | Count |
|--------|-------|
| **States with Comprehensive Flavor Bans** | 7 |
| **States with Partial Restrictions** | 8 |
| **States Banning Menthol Cigarettes** | 2 (CA, MA) |
| **States with E-Cigarette Excise Taxes** | 34 |
| **States with Indoor Vaping Bans** | 20 |

---

## Features

### Interactive Database
- **Filterable by Policy Type**: View comprehensive bans, partial restrictions, menthol bans, tax status
- **Searchable**: Instant search across all states
- **Sortable Table**: Sort by any column
- **Detailed State Profiles**: Click any state for complete policy details

### Comprehensive Data
- All 50 states + District of Columbia
- Multiple policy dimensions per state
- Effective dates for major policies
- Recent policy changes (2024-2025)
- Direct citations to authoritative sources

### Professional Design
- Clean, accessible interface
- Mobile-responsive
- Print-friendly
- No external dependencies (works offline)
- Suitable for presentations and reports

---

## Data Sources

This database compiles data from the following authoritative sources:

1. **[Truth Initiative](https://truthinitiative.org/research-resources)** - Flavored Tobacco Restrictions Q2 2025
2. **[Campaign for Tobacco-Free Kids](https://www.tobaccofreekids.org)** - State Policy Database 2024
3. **[Tax Foundation](https://taxfoundation.org/data/all/state/vaping-taxes/)** - Vaping Taxes by State 2025
4. **[CDC STATE System](https://www.cdc.gov/statesystem)** - State Tobacco Activities Tracking and Evaluation
5. **[FDA](https://www.fda.gov/tobacco-products)** - Tobacco 21 Resources
6. **State Legislative Sources** - Direct review of statutes and regulations

**Data Currency**: December 2024/January 2025

---

## Usage

### Opening the Database

Simply open `State Vaping and Tobacco Policy Map.html` in any modern web browser. No installation or server required.

### Filtering Data

1. **By Policy Type**: Click filter buttons to view states with specific policies
   - Comprehensive Flavor Bans
   - Partial Restrictions
   - Menthol Bans
   - E-Cigarette Tax status

2. **By Search**: Type state name in search box for instant filtering

3. **By Column**: Click column headers to sort

### Viewing State Details

- Click any state row in the table
- Click "View Details" button
- View comprehensive policy information including:
  - Flavored e-cigarette restrictions
  - Menthol cigarette bans
  - E-cigarette taxation (rate, structure)
  - Indoor vaping bans
  - Age restrictions
  - Licensing requirements
  - Local restrictions
  - Recent policy changes
  - Data sources

---

## File Structure

```
state-vaping-tobacco-policy-map/
├── State Vaping and Tobacco Policy Map.html  # Interactive web database
├── state_policies.json                       # Complete policy data (JSON)
├── state_policies.py                         # Data compilation script
├── README.md                                 # This file
└── LICENSE                                   # MIT License
```

---

## Notable Policy Highlights

### States with Comprehensive Bans

- **California** (2022) - All flavored tobacco including menthol
- **Massachusetts** (2020) - All flavored tobacco including menthol (first state)
- **New Jersey** (2020) - Flavored e-cigarettes (tobacco only allowed)
- **New York** (2020) - Flavored e-cigarettes (tobacco only allowed)
- **Rhode Island** (2025) - Flavored e-cigarettes except tobacco and menthol
- **Utah** (2025) - Flavored e-cigarettes except tobacco and menthol
- **District of Columbia** - Comprehensive flavor restrictions

### Recent 2025 Policy Changes

- **California**: Expanded ban to internet sales, prohibited menthol-like cooling (Jan 1, 2025)
- **Rhode Island**: Made 2019 executive order flavor ban permanent (Jan 1, 2025)
- **Utah**: Flavor ban effective Jan 1, 2025; upheld by federal court March 2025
- **Ohio**: State flavor ban enacted 2025
- **Texas**: Flavor ban + China-made product ban enacted 2025
- **North Carolina**: FDA-authorized product requirement (July 1, 2025)
- **Wisconsin**: FDA-authorized product requirement scheduled (Sept 1, 2025)

### Tax Rate Extremes

**Highest Wholesale Taxes:**
- Minnesota: 95%
- Vermont: 92%
- D.C.: 96%

**Highest Volume Taxes:**
- Rhode Island: $0.50 per mL
- Connecticut: $0.40 per mL

**States Without E-Cig Tax:** 17 states (AL, AK, AZ, AR, FL, ID, IA, MI, MS, MO, MT, ND, OK, SC, SD, TN, TX)

---

## Methodology

### Data Collection

1. **Primary Sources**: Direct review of authoritative public health organizations and government databases
2. **Cross-Verification**: Multiple sources consulted for each data point
3. **Legislative Review**: Direct examination of state statutes where applicable
4. **Temporal Accuracy**: Focus on most recent data (Q4 2024 - Q1 2025)

### Data Categories

Each state entry includes:
- **Flavored E-Cigarette Ban Status**: Comprehensive / Partial / None
- **Menthol Cigarette Ban**: Yes / No
- **E-Cigarette Excise Tax**: Rate, structure, implementation details
- **Indoor Vaping Restrictions**: Comprehensive smoke-free law coverage
- **Minimum Age**: Federal T21 + state law status
- **Licensing Requirements**: Required / Not required + fees
- **Local Restrictions**: Notable city/county policies
- **Recent Changes**: 2024-2025 policy updates
- **Sources**: Specific citations for each state

### Limitations

- Local ordinances noted where significant but not comprehensively cataloged
- Enforcement practices may vary by jurisdiction
- Policies subject to legal challenges and change
- Tax rates reflect statutory rates; actual implementation may vary
- Data current as of December 2024; policies continue to evolve

---

## Updates & Maintenance

This database is designed to be updateable. To update state data:

1. Edit `state_policies.py` with new information
2. Run `python3 state_policies.py` to regenerate `state_policies.json`
3. Refresh the HTML page to see updated data

---

## Use Cases

### For State Attorneys General Offices
- Compare state policies for legislative planning
- Research legal precedents and implementation approaches
- Identify trends in tobacco control regulation
- Support policy development and enforcement strategies

### For Public Health Officials
- Track state-level tobacco control progress
- Identify gaps in regulation
- Support evidence-based policymaking
- Monitor policy implementation and effectiveness

### For Researchers
- Analyze policy landscape across jurisdictions
- Study correlations between policies and outcomes
- Track policy diffusion and adoption patterns
- Support academic research and publication

---

## Federal Context

### Tobacco 21 (T21)

Federal law prohibits the sale of tobacco products to anyone under 21 years of age nationwide (effective December 20, 2019). This applies to:
- Cigarettes
- Smokeless tobacco
- E-cigarettes and vaping products
- Cigars
- All nicotine-containing products

42 states have enacted their own T21 laws; federal law applies to all states regardless.

### FDA Menthol Rule

The FDA withdrew proposed federal menthol and flavored cigar bans in January 2025. State and local policies continue to vary independently.

---

## Citation

**Recommended Citation:**

State Vaping and Flavored Tobacco Policy Database (2024-2025). Data compiled from Truth Initiative, Campaign for Tobacco-Free Kids, Tax Foundation, CDC STATE System, FDA, and state legislative sources. Last updated December 24, 2024. Available at: [repository URL]

---

## License

MIT License - See LICENSE file for details

This database is provided for research, policy analysis, and public health purposes. While we strive for accuracy, users should consult primary sources for legal and regulatory decisions.

---

## Contact & Contributions

For corrections, updates, or questions:
- File an issue in this repository
- Consult primary sources listed in the database
- Contact relevant state health departments for official interpretations

---

## Acknowledgments

This database synthesizes publicly available data from:
- Truth Initiative
- Campaign for Tobacco-Free Kids
- Tax Foundation
- Centers for Disease Control and Prevention
- U.S. Food and Drug Administration
- State legislative and regulatory bodies

Special thanks to the tobacco control research community for their ongoing work in tracking and analyzing state policies.

---

**Last Updated**: December 24, 2024
**Data Version**: 1.0
**Coverage**: All 50 U.S. states + District of Columbia

---

*This is an independent research tool. It does not represent official policy positions of any government agency or organization.*
